import hashlib
import sqlite3
from pathlib import Path


class StateStore:
    def __init__(self, db_path: str | Path):
        self.conn = sqlite3.connect(db_path)
        self._init()

    def _init(self):
        cur = self.conn.cursor()
        cur.execute("create table if not exists score_state(symbol text primary key, prev_smoothed real)")
        cur.execute("create table if not exists report_hash(report_key text primary key, hash text)")
        cur.execute("create table if not exists symbol_state(symbol text primary key, last_signal_ts text)")
        cur.execute("create table if not exists portfolio_state(k text primary key, v text)")
        self.conn.commit()

    def get_prev_smoothed(self, symbol: str):
        cur = self.conn.cursor()
        row = cur.execute("select prev_smoothed from score_state where symbol=?", (symbol,)).fetchone()
        return None if not row else row[0]

    def set_prev_smoothed(self, symbol: str, value: float):
        self.conn.execute("insert into score_state(symbol, prev_smoothed) values(?, ?) on conflict(symbol) do update set prev_smoothed=excluded.prev_smoothed", (symbol, value))
        self.conn.commit()

    def report_changed(self, report_key: str, content: str) -> bool:
        h = hashlib.sha256(content.encode()).hexdigest()
        cur = self.conn.cursor()
        row = cur.execute("select hash from report_hash where report_key=?", (report_key,)).fetchone()
        if row and row[0] == h:
            return False
        self.conn.execute("insert into report_hash(report_key, hash) values(?, ?) on conflict(report_key) do update set hash=excluded.hash", (report_key, h))
        self.conn.commit()
        return True
