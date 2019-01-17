#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko




class Highway (Base):
    
    def __init__ (self):
        pass
    
    @property
    def id (self):
        return self.__Id
    
    @id.setter
    def id (self, value):
        self.__Id = value
        
    @property
    def distance (self):
        return self.__Distance
    
    @distance.setter
    def distance (self, value):
        self.__Distance = value
    
    
    def as_xml(self):
        result = [
            f'<Id>{self.id}</Id>',
            f'<Distance>{self.distance}</Distance>'
            ]
        result = '\n  '.join(result)
        return f'<Highway>\n  {result}\n</Highway>'    
