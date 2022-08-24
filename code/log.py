class Log():

  

    def __init__(self) -> None:
        self.isDebug = True

    def writeLog(self, type, text):
        if self.isDebug:
            print("{}: {}".format(type, text))