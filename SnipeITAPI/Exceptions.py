class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class SnipeITErrorHandler(object):
    """Handles SnipeIT Exceptions"""
    def __init__(self,request):
        self.fault=request.json()
        if isinstance(self.fault,dict) and self.fault.get('fault'):
            pass
        elif isinstance(self.fault,dict) and self.fault.get('error'):
            pass
        elif isinstance(self.fault,dict) and self.fault.get('message'):
            pass
        elif self.fault.status_code == 400:
            raise BadRequestError()
        else:
            raise IWasNotProgramedForThisError()

class BadRequestError(Error):
    """Exception raised for Bad Request Errors."""

class UndefinedFaultStringError(Error):
    """Exception raised for unhandled errors."""

    def __init__(self,expression, message):
        self.message = message
        self.expression = expression

class IWasNotProgramedForThisError():
    """Exception raised when the passed exception cannot be handled"""