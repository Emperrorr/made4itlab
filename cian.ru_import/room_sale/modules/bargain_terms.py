#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


from modules.agent_bonus import *


class BargainTerms (Base):
    
    def __init__ (self):
        self.__agent_bonus = AgentBonus()
              
    
    @property
    def agent_bonus (self):
        return self.__agent_bonus
    
        
    @property
    def price (self):
        return self.__Price
    
    @price.setter
    def price (self, value):
        self.__Price = value
    
    @property
    def currency (self):
        return self.__Currency
    
    @currency.setter
    def currency (self, value):
        self.__Currency = value
    
    @property
    def mortgage_allowed (self):
        return self.__MortgageAllowed
    
    @mortgage_allowed.setter
    def mortgage_allowed (self, value):
        self.__MortgageAllowed = value
    
    @property
    def sale_type (self):
        return self.__SaleType
    
    @sale_type.setter
    def sale_type (self, value):
        self.__SaleType = value
    
    
    
    def as_xml(self):
        result = [
            f'<Price>{self.price}</Price>',
            f'<Currency>{self.currency}</Currency>',
            f'<MortgageAllowed>{self.mortgage_allowed}</MortgageAllowed>',
            f'<SaleType>{self.sale_type}</SaleType>',
            self.agent_bonus.as_xml(),
            ]
        result = '\n    '.join(result)
        return f'<BargainTerms>\n   {result}\n  </BargainTerms>'
        
