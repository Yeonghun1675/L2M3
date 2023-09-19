class BaseMiningError(Exception):
    pass


class StructuredFormatError(BaseMiningError):
    pass


class TokenLimitError(BaseMiningError):
    pass


class ContextError(BaseMiningError):
    pass


class LangchainError(BaseMiningError):
    pass


class ReaderError(BaseMiningError):
    pass


class ParserError(BaseMiningError):
    pass
