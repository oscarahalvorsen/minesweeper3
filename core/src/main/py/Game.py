# !/usr/bin/python3
# coding=utf-8

import Tile
import random

class Game:
    def __init__(self, height, width, bombNr):
        self.height=height
        self.width=width
        self.bombNr=bombNr
        self.__areProportionsValid(height, width)
        self.__isBombNrValid(height, width, bombNr)

        self.board=[[0 for i in range(self.width)] for j in range(self.height)]
        self.__createBoard()
        self.__placeBombs()
        self.__placeNumbers()
    
    #Create baord
    def __createBoard(self):
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                self.board[y][x]= Tile.Tile(x, y)

    def __placeBombs(self):
        i=0;
        while i<self.bombNr:
            randomX=random.randint(0, self.getWidth()-1)
            randomY=random.randint(0,self.getHeight()-1)
            tile = self.getTile(randomX, randomY)
            if (not tile.isBomb()):
                tile.setBomb()
                i+=1
    
    def __placeNumbers(self):
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                if (not self.getTile(x, y).isBomb()):
                    tileNumber=0
                    for j in range(-1, 2, 1):
                        for i in range(-1, 2, 1):
                            if (self.__isTileValid(x+i, y+j)):
                                if (self.getTile(x+i, y+j).isBomb()):
                                    tileNumber+=1
                    self.getTile(x,y).setNumber(tileNumber)

    #Game methods
    def toggleFlag(self, x, y):
        tile = self.getTile(x, y)
        if (tile.isCovered()):
            tile.toggleFlag()

    def uncover(self, x, y):
        tile = self.getTile(x,y)
        if (tile.isCovered() and not tile.isFlag()):
            tile.uncover()
            if (tile.isBomb()):
                return
            if (tile.isAir()):
                for j in range(-1, 2, 1):
                    for i in range(-1, 2, 1):
                        if (self.__isTileValid(x+i, y+j)):
                            if (not self.getTile(x+i, y+j).isBomb()):
                                self.uncover(x+i, y+j)

    def uncoverNearbyTiles(self, x, y):
        nearbyFlagCount=0
        tile = self.getTile(x, y)
        if (not tile.isCovered()):
            for j in range(-1, 2, 1):
                    for i in range(-1, 2, 1):
                            if (self.__isTileValid(x+i,y+j)):
                                if (tile.isFlag()):
                                    nearbyFlagCount+=1
            for j in range(-1, 2, 1):
                    for i in range(-1, 2, 1):
                        if (i!=0 or j!=0):
                            if (self.__isTileValid(x+i,y+j)):
                                if (not tile.isFlag()):
                                    if (nearbyFlagCount==tile.getType()):
                                        self.uncover(x+i, y+j)

    #Getters and setters
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getBombNr(self):
        return self.bombNr
    
    def getBoard(self):
        return self.board

    def getTile(self, x, y):
        if (not self.__isTileValid(x, y)):
            raise ValueError("Coordinates must be at least 0 and less than max.")
        return self.board[x][y]
    
    #Helping methods
    def __areProportionsValid(self, width, height):
        if (not isinstance(width, int) or not isinstance(height, int)):
            raise TypeError("Tile number must be integer.")  
        if (width<1 or height<1):
            raise ValueError("Width and height must be possitive integers.")
        
    def __isTileValid(self, x, y):
        if (not isinstance(x, int) or not isinstance(y, int)):
            raise TypeError("Coordinates must be integers.")
        return x >= 0 and x<self.getWidth() and y>=0 and y<self.getHeight()

    def __isBombNrValid(self, bombNr, height, width):
        if (bombNr<0 or bombNr>height*width):
            raise ValueError("BombNr must be positive integer lower than width*height")

    def __str__(self):
        string = ""
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                tile = self.getTile(x, y)
                string += tile.__str__() + "     "
            string+="\n"
        return string

game = Game(3,3,1)
game.uncover(0,0)
print(game)