import json

class  ContentValues():
    __data=[]

    def put(self,keyObject,valueObject):
        self.__data.append({keyObject:valueObject})

    
    def getAll(self):
        return self.__data

    

        

