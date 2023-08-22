class BaseMiningError(Exception):
    pass


class StructuredFormatError(BaseMiningError):
    pass


class TokenLimitError(BaseMiningError):
    pass


class ContextError(BaseMiningError):
    pass
