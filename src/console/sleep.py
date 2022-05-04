import time

sleep_enabled: bool = True


def sleep(seconds: float) -> None:
    if sleep_enabled:
        time.sleep(seconds)
