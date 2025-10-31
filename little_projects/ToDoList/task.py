import logging

log = logging.getLogger(__name__)

class Task():
	def __init__(self, name, desciption, status = "To-Do"):
		self.name = name
		self.desciption = desciption
		self.status = status