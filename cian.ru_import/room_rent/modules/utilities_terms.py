#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko

class UtilitiesTerms (Base):
    
    def __init__(self):
        pass
    
    @property
    def price (self):
        return self.__Price
    
    @price.setter
    def price(self, value):
        self.__Price = value
    
    @property
    def included_in_price (self):
        return self.__IncludedInPrice
    
    @included_in_price.setter
    def included_in_price (self, value):
        self.__IncludedInPrice = value
        
    
        
    def as_xml (self):
        result = [            
            f'<Price>{self.price}</Price>',
            f'<IncludedInPrice>{self.included_in_price}</IncludedInPrice>'
            ]
        result = '\n      '.join(result)
        return f'<UtilitiesTerms>\n      {result}\n    </UtilitiesTrems>'   
