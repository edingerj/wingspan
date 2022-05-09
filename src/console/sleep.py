import time

from game import runtime_flags


def sleep(seconds: float) -> None:
    if not runtime_flags.get().no_sleep:
        time.sleep(seconds)
