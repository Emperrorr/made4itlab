#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Developer(Base):
    
            
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
            f'<Name>{self.name}</Name>'
            ]
        result = '\n  '.join(result)
        return f'<Developer>\n  {result}\n</Developer>'
