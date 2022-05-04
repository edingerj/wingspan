import time


sleep_enabled = False


def sleep(seconds: float) -> None:
    if sleep_enabled:
        time.sleep(seconds)
