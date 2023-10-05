"""
exectimer.py file

This file contains the implementation of the ExecutionTimer that is used in
the request modules.
"""


from asyncio import sleep
from time import perf_counter


__all__ = (
    'ExecutionTimer',
)


class ExecutionTimer:
    """
    Execution timer class that manages the delay between each request to
    avoid getting rate limited

    This class needs to be called in the asynchronous context manager.

    Attributes:
        _min_time (float):
            the minimum time in seconds the timer should prevent from exiting
            the context manager
    """

    def __init__(self, min_time=0):
        """
        Initialisation method of the execution timer

        Args:
            min_time (float):
                the minimum time in seconds the timer should prevent from
                exiting the context manager
        """
        self._min_time = min_time
        return

    async def __aenter__(self):
        """
        Asynchronous context manager (enter)

        Returns:
            ExecutionTimer: returns itself
        """
        self._start = perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Asynchronous context manager (exit)

        Args:
            exc_type:   exception type
            exc_val:    exception value
            exc_tb:     exception traceback
        """
        end = perf_counter()
        if (diff := end - self._start) < self._min_time:
            await sleep(diff)
        return


