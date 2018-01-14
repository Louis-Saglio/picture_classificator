class PictureClassificatorException(BaseException):
    pass


class EndProgramSignal(PictureClassificatorException):
    pass


class InvalidSignalError(PictureClassificatorException):
    pass
