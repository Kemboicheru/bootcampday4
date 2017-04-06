class BinarySearch(list):
    ourarray = []
    length = 0
    interval = 0
    
    def __init__(self,a,b):
        self.length = a
        self.interval = b
        value = b
        for item in range(self.length):
            self.ourarray.append(value)
            value += self.interval

    def search(self,searchitem):
        returnvalue = {}
        count = 0

        firstitem = 0
        lastitem = self.length -1
        foundict = {}
        found = False
        
        while firstitem <= lastitem and found == False:
            count += 1
            middleitem = (firstitem + lastitem)//2
            if self.ourarray[middleitem] == searchitem:
                foundict['count'] = count
                foundict['index'] = middleitem
                found = True
                return foundict
            elif searchitem < self.ourarray[middleitem]:
                lastitem = middleitem - 1
            else:
                firstitem = middleitem + 1
                
bina = BinarySearch(10,3)

print bina.search(4) 
            
        
