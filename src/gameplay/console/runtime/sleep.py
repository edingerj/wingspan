import time

from gameplay import runtime_flags


def sleep(seconds: float) -> None:
    if not getattr(runtime_flags.get(), 'no_sleep', False):
        time.sleep(seconds)
