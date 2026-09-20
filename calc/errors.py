"""Domain errors for calc."""


class InvalidLine(ValueError):
    """An invoice line that cannot be represented, such as a zero quantity."""
