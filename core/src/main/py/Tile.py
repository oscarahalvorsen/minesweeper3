# !/usr/bin/python3
# coding=utf-8

class Tile:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.type=0
        self.covered=True
        self.flag=False
        self.tempUncovered=False
        self.__areCoordinatesValid

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getType(self):
        return self.type

    def isAir(self):
        return self.type==0

    def isBomb(self):
        return self.type==9
    
    def setNumber(self, n):
        self.isNumberValid
        self.type=n

    def setBomb(self):
        self.type=9

    def isCovered(self):
        return self.covered

    def uncover(self):
        self.covered=False

    def isFlag(self):
        return self.flag
    
    def toggleFlag(self):
        self.flag= False if self.isFlag() else True

    def __isTempUncovered(self):
        return self.tempUncovered

    def toggleTempUncovered(self):
        self.tempUncovered = False if self.__isTempUncovered else True
    
    def __areCoordinatesValid(x, y):
        if (not isinstance(x, int) or not isinstance(y, int)):
            raise TypeError("Coordinates must be integers.")
        if (x<0 or y<0):
            raise ValueError("Coordinates must be possitive integers.")
    

    def isNumberValid(self, type):
        if (not isinstance(type, int)):
            raise TypeError("Tile number must be integer.")
        if (type<0 or type>9):
            raise ValueError("Tile number cannot be less that 0 or more than 9.")
    
    def __str__(self):
        return "T:" + str(self.getType()) + " F:" + str(self.isFlag()) + " C:" + str(self.isCovered())
    