#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Deadline(Base):
    
            
    @property
    def quater (self):
        return self.__Quater
    
    @quater.setter
    def quater (self, value):
        self.__Quater = value
        
    @property
    def year (self):
        return self.__Year
    
    @year.setter
    def year (self, value):
        self.__Year = value
    
    @property
    def is_complete (self):
        return self.__IsComplete
    
    @is_complete.setter
    def is_complete (self, value):
        self.__IsComplete = value    
    
    def as_xml(self):
        result = [
            f'<Quarter>{self.quater}</Quarter>',
            f'<Year>{self.year}</Year>',
            f'<IsComplete>{self.is_complete}</IsComplete>'
            ]
        result = '\n    '.join(result)
        return f'<Deadline>\n    {result}\n    </Deadline>'
