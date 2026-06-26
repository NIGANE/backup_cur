
class MyError(BaseException):
    """Base exception for project-specific errors.

    This exception serves as the root of the project's custom exception
    hierarchy. It can be subclassed to represent specific error conditions
    encountered during constrained decoding, grammar processing, or LLM
    interactions.
    """
    pass
