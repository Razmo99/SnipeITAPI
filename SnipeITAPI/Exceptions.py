class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class SnipeITErrorHandler(object):
    """Handles SnipeIT Exceptions"""
    def __init__(self,request):
        self.fault=request.json()
        print(self.fault)
        if self.fault.get('status')=='error':
            if self.fault.get('messages') == 'Unauthorised.':
                raise UnauthorisedError()
            elif self.fault.get('messages')== 'You cannot add a maintenance for that asset':
                raise CannotAddMaintenanceError()
            else:
                raise UndefinedFaultStringError(request,self.fault)
        elif request.status_code == 400:
            raise BadRequestError()
        else:
            raise IWasNotProgramedForThisError(request)

class CannotAddMaintenanceError(Error):
    """Exception raised when maintenance cannot be added for a asset"""

class BadRequestError(Error):
    """Exception raised for Bad Request"""
class UnauthorisedError(Error):
    """Exception raised for Unauthorised Requests"""

class UndefinedFaultStringError(Error):
    """Exception raised for unhandled errors."""

    def __init__(self,request, message):
        self.message = message
        self.request = request

class IWasNotProgramedForThisError(Error):
    """Exception raised when the passed exception cannot be handled"""
        
    def __init__(self,request):
        self.request = request