from asyncio import sleep
from time import perf_counter


__all__ = (
    'ExecutionTimer',
)


class ExecutionTimer:
    def __init__(self, min_time=0):
        self._min_time = min_time
        return

    async def __aenter__(self):
        self._start = perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        end = perf_counter()
        if (diff := end - self._start) < self._min_time:
            await sleep(diff)
        return


