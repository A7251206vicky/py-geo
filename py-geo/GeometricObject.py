class GeometricObject:
    def __intit__(self,color="white",filled=False):
        self.__color=color
        self.__filled=filled
    def getColor(self):
        return self.__color
    def setColor(self,nc):
        self.__color=nc
    def isFilled(self):
        return self.filled
    def setFilled(self,nf):
        self.__filled=nf
    def __str__(self):
        return "color: " +self.__color+\
            " and filled: "+str(self.__filled)