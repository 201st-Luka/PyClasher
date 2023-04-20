class After:
    """
    Holds the after string
    """

    def __init__(self, after: str):
        self.__response = after
        return

    @property
    def value(self) -> str:
        return self.__response

    def __repr__(self) -> str:
        return "After()"

    def __str__(self) -> str:
        return f"After(value={self.value})"


class Before:
    """
    Holds the before string
    """

    def __init__(self, before: str):
        self.__response = before
        return

    @property
    def value(self) -> str:
        return self.__response

    def __repr__(self) -> str:
        return "Before()"

    def __str__(self) -> str:
        return f"Before(value={self.value})"


class Cursor:
    """
    Holds information about the cursor on the war log pages
    """

    def __init__(self, cursor: dict) -> None:
        self.__response = cursor
        return

    @property
    def after(self) -> After | None:
        return After(self.__response['after']) if 'after' in self.__response else None

    @property
    def before(self) -> Before | None:
        return Before(self.__response['before']) if 'before' in self.__response else None

    def __repr__(self) -> str:
        return "Cursor"

    def __str__(self) -> str:
        return f"Cursor({self.after}, {self.before})"


class Paging:
    """
    Holds information about the paging of the clan war log
    """

    def __init__(self, paging: dict) -> None:
        self.__response = paging
        return

    @property
    def cursor(self) -> Cursor:
        return Cursor(self.__response['cursors'])

    def __repr__(self) -> str:
        return "Paging()"

    def __str__(self) -> str:
        return f"Paging({self.cursor})"

