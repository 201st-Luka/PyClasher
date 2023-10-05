"""
exectimer.pyi file

This file contains the type hints of the ExecutionTimer that is used in
the request modules.
"""


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

    def __init__(self, min_time: float = 0) -> None:
        """
        Initialisation method of the execution timer

        Args:
            min_time (float):
                the minimum time in seconds the timer should prevent from
                exiting the context manager
        """
        self._min_time = min_time
        ...

    async def __aenter__(self) -> ExecutionTimer:
        """
        Asynchronous context manager (enter)

        Returns:
            ExecutionTimer: returns itself
        """
        self._start: float = ...
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Asynchronous context manager (exit)

        Args:
            exc_type:   exception type
            exc_val:    exception value
            exc_tb:     exception traceback
        """
        ...
