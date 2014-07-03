
class Report(object):
  ERROR = 0
  WARNING = 1
  def __init__(self):
    self.files = {}

  def addError(self, file, line, col, msg):
    self.files[file] = (line, col, ERROR, msg)

  def addWarning(self, file, line, col, msg):
    self.files[file] = (line, col, WARNING, msg)
