'''This module provides the message type object which manages the types of
   warnings and errors you can provide and how to print them to the user'''

from enum import Enum, unique

@unique
class Severity(Enum):
  ERROR = 0
  WARNING = 1
  SUGGESTION = 2
  HINT = 3
