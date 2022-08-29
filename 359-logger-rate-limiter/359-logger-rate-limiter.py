class Logger(object):

    def __init__(self):
        
        self.d={}


    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        try:
            
            Flag = (self.d[message][-1] <= timestamp )
            if Flag:
                self.d[message].append(timestamp+10)
        except:
            self.d[message]=[timestamp+10]
            return True
            
        
        return Flag
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)