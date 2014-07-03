'''
This module provides the abstract report interface
'''

class AbstractReport(object):
  def __init__(self, checkFile):
    self.checkFile = checkFile

  def asString(self):
    '''Makes the report as a string and returns it'''
    return 'Not Implemented'

  def toFile(self, fileName):
    '''Leverages asString to write out the report to a file'''
    with open(fileName, 'r') as f:
      f.write(self.asString())

  def __str__(self):
    return self.asString()
