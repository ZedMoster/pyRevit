# General Exceptions
class PyRevitException(Exception):
    """Base class for all pyRevit Exceptions.
    Parameters args and message are derived from Exception class.
    """
    pass


class PyRevitUnknownAssemblyError(PyRevitException):
    pass


class PyRevitUnknownFormatError(PyRevitException):
    pass


class PyRevitLoaderNotFoundError(PyRevitException):
    pass


class PyRevitNoScriptFileError(PyRevitException):
    pass


class PyRevitScriptDependencyError(PyRevitException):
    pass


# Cache-Specific Exceptions
class PyRevitCacheError(PyRevitException):
    pass


class PyRevitCacheReadError(PyRevitCacheError):
    pass


class PyRevitCacheWriteError(PyRevitCacheError):
    pass


class PyRevitCacheExpiredError(PyRevitCacheError):
    pass


# Config file parsing exeptions
class ConfigFileError(PyRevitException):
    pass
