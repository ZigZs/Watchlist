class CommandNotFound(Exception):
    pass
class MovieNotFound(Exception):
    pass
# class AttributeNotFound(Exception):
#     pass
class MovieAlreadyExistError(Exception):
    pass
class WrongStatusError(Exception):
    pass
class CommentTooLong(Exception):
    pass
class WrongReviewError(Exception):
    pass
class EmptyListError(Exception):
    pass