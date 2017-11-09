
class EmptyItemsError(Exception):
    """
    Raised when items is empty
	used for peek() and get() variations
    """

class WrongTypeException(Exception):
	"""
	Raised when wrong type is encountered for data
	structure implementation
	"""


class MethodNotAvailable(Exception):
	"""
	Raised when user tries to use method that is 
	not available to current structure
	"""


class ItemNotInList(Exception):
	"""
	Raised when user tries to retrieve item that doesn't exist (for list)
	"""		