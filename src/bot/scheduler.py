from apscheduler.schedulers.blocking import BlockingScheduler


def build_scheduler(timezone: str = "Europe/Istanbul") -> BlockingScheduler:
    return BlockingScheduler(timezone=timezone)
