class graphNode:
    def __init__(self,v,e=None):
        self.v = v
        self.e = e
    
    def getVertices(self):
        return self.e
        
    def getValue(self):
        return self.v
