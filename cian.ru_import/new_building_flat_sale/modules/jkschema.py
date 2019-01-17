#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


from modules.house import *
from modules.developer import *


class JKSchema (Base):
    
    def __init__ (self):
        self.__flat = Flat()
        self.__house = House ()
        self.__developer = Developer ()
        
    @property
    def flat (self):
        return self.__flat
    
    @property
    def house (self):
        return self.__house
    
    @property
    def developer(self):
        return self.__developer
    
    @property
    def id (self):
        return self.__Id
    
    @id.setter
    def id (self, value):
        self.__Id = value
        
    @property
    def name (self):
        return self.__Name
    
    @name.setter
    def name (self, value):
        self.__Name = value
    
    
    def as_xml(self):
        result = [
            f'<Id>{self.id}</Id>',
            f'<Name>{self.name}</Name>',
            self.house.as_xml(),
            self.developer.as_xml()
            ]
        result = '\n  '.join(result)
        return f'<JKSchema>\n  {result}\n</JKSchema>'
