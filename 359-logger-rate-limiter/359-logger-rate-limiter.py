class Logger(object):

    def __init__(self):
        
        self.d={}
        #self.t = timestamp
        #self.message = message

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        #for i in timestamp:
        #print(timestamp,message)
        #print(self.d)
        try:
            
            Flag = (self.d[message][-1] <= timestamp )
            if Flag:
                
                self.d[message].append(timestamp+10)
        except:
            self.d[message]=[timestamp+10]
            return True
            
        
        return Flag
        #print(self.d[message][-1])
        
        #return self.d[message][-1] >= timestamp
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)