__all__ = (
    'ExecutionTimer',
)


class ExecutionTimer:
    def __init__(self, min_time: float = 0) -> None:
        self._min_time = min_time
        ...

    async def __aenter__(self) -> ExecutionTimer:
        self._start: float = ...
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        ...
