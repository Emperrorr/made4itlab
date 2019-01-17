#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko




class AgentBonus (Base):
    
    def __init__ (self):
        pass
    
    @property
    def value (self):
        return self.__Value
    
    @value.setter
    def value (self, value):
        self.__Value = value
        
    @property
    def payment_type (self):
        return self.__PaymentType
    
    @payment_type.setter
    def payment_type (self, value):
        self.__PaymentType = value
    
    @property
    def currency (self):
        return self.__Currency
    
    @currency.setter
    def currency (self, value):
        self.__Currency = value
    
    def as_xml(self):
        result = [
            f'<Value>{self.value}</Value>',
            f'<PaymentType>{self.payment_type}</PaymentType>',
            f'<Currency>{self.currency}</Currency>'
            ]
        result = '\n    '.join(result)
        return f'<AgentBonus>\n    {result}\n  </AgentBonus>'    
