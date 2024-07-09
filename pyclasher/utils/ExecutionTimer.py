"""
``ExecutionTimer`` class
"""


from asyncio import sleep
from time import perf_counter


class ExecutionTimer:
    """
    This class is an execution timer that makes the code waiting for a specific time if the end of the context is
    reached before the time is reached.

    Attributes:
        _min_time (float):
            The minimum time the context must take
    """

    def __init__(self, min_time: float = 0):
        """
        Args:
            min_time (float):
                The minimum time the context must take
        """
        self._min_time = min_time
        return

    async def __aenter__(self) -> 'ExecutionTimer':
        self._start = perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        end = perf_counter()
        if (diff := end - self._start) < self._min_time:
            await sleep(diff)
        return


