# BIST Uyarı Botu (Signal + Rapor + Shadow Portfolio)

> **Yatırım tavsiyesi değildir.**
> Bu proje **otomatik emir vermez**, yalnızca sinyal üretir, raporlar ve simülasyon yapar.
> Veri gecikmesi ve veri hataları olabilir.

## Özellikler
- BIST (.IS) sembollerinde günlük/intraday tarama (MVP: yfinance)
- CompositeScore hesaplama, regime çarpanı, RS20/RS5 katkısı
- Anomali korumaları, smoothing + hysteresis + delta threshold
- Haftalık odak: Pazartesi giriş adayları, Cuma exit bias
- Shadow portfolio simülasyonu: risk bazlı sizing, stop/trailing/TP/time stop, fee+slippage
- SQLite state: score_state, symbol_state, report_hash, portfolio_state
- Telegram bildirim altyapısı (stub-safe)

## Kurulum
```bash
poetry install
cp .env.example .env
python -m bot.main run
```

## CLI
```bash
python -m bot.main run
python -m bot.main scan --mode daily
python -m bot.main scan --mode friday
python -m bot.main backtest --weeks 156
python -m bot.main portfolio-backtest --start 2020-01-01 --end 2025-12-31 --timeframe 1d
python -m bot.main universe --print --source csv
```

## Docker
```bash
docker compose up --build
```

## Telegram kurulumu
1. @BotFather ile bot oluştur.
2. Token değerini `.env` içine `TELEGRAM_BOT_TOKEN` olarak koy.
3. Chat id alıp `TELEGRAM_CHAT_ID` olarak ekle.
4. Uygulama gönderimi `notifications/telegram.py` üstünden yapar.

## BIST sembol formatı
- Loader `THYAO -> THYAO.IS` normalize eder.
- `USE_IS_SUFFIX=false` ile suffix kaldırılabilir.

## Cuma agresif mod
- Cuma 14:00-17:00 arası sık tarama ve exit pressure özeti.
- 17:20 final exit raporu (WEEKLY_FLAT=true ise kapatma eğilimi).

## Shadow trading açıklaması
- Bu mod tamamen simülasyondur; gerçek emir gönderilmez.
- Amaç pozisyon yönetimi kurallarını ve risk/maliyet etkisini görmek.

## Strateji ekleme (5 adım)
1. `src/bot/strategies/` altına dosya oluştur.
2. Giriş/çıkış sinyal fonksiyonu yaz.
3. `main.py` veya scheduler pipeline'ına bağla.
4. Score/filter katmanına gerekli katkıyı ekle.
5. Test dosyası ekle (`tests/`).
