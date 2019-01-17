#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Phones (Base):
    
    def __init__ (self):
        pass
    
    @property
    def country_code (self):
        return self.__CountryCode
    
    @country_code.setter
    def country_code (self, value):
        self.__CountryCode = value
        
    @property
    def number (self):
        return self.__Number
    
    @number.setter
    def number (self, value):
        self.__Number = value
    
    
    def as_xml(self):
        result = [
            f'<PhoneSchema>',
            f'<CountryCode>{self.country_code}</CountryCode>',
            f'<Number>{self.number}</Number>',
            f'</PhoneSchema>'
            ]
        result = '\n  '.join(result)
        return f'<Phones>\n  {result}\n</Phones>'
        
