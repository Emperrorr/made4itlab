#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


class Flat (Base):
    
    def __init__ (self):
        pass
    
    @property
    def flat_number (self):
        return self.__FlatNumber
    
    @flat_number.setter
    def flat_number (self, value):
        self.__FlatNumber = value
        
    @property
    def section_number (self):
        return self.__SectionNumber
    
    @section_number.setter
    def section_number (self, value):
        self.__SectionNumber = value
        
    @property
    def flat_type (self):
        return self.__FlatType
    
    @flat_type.setter
    def flat_type (self, value):
        self.__FlatType = value
    
    
    def as_xml(self):
        result = [
            f'<FlatNumber>{self.flat_number}</FlatNumber>',
            f'<SectionNumber>{self.section_number}</SectionNumber>',
            f'<FlatType>{self.flat_type}</FlatType>'
            ]
        result = '\n  '.join(result)
        return f'<Flat>\n  {result}\n</Flat>'
