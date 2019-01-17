#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


from modules.utilities_terms import *
from modules.agent_bonus import *


class BargainTerms (Base):
    
    def __init__ (self):
        self.__agent_bonus = AgentBonus()
        self.__utilities_terms = UtilitiesTerms()
        
    @property
    def utilities_terms (self):
        return self.__utilities_terms
    
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
    def payment_period (self):
        return self.__PaymentPeriod
    
    @payment_period.setter
    def payment_period (self, value):
        self.__PaymentPeriod = value
    
    @property
    def bargain_allowed (self):
        return self.__BargainAllowed
    
    @bargain_allowed.setter
    def bargain_allowed (self, value):
        self.__BargainAllowed = value
    
    @property
    def bargain_price (self):
        return self.__BargainPrice
    
    @bargain_price.setter
    def bargain_price (self, value):
        self.__BargainPrice = value
    
    @property
    def bargain_conditions (self):
        return self.__BargainConditions
    
    @bargain_conditions.setter
    def bargain_conditions (self, value):
        self.__BargainConditions = value
    
    @property
    def lease_term_type (self):
        return self.__LeaseTermType 
    
    @lease_term_type.setter
    def lease_term_type (self, value):
        self.__LeaseTermType = value
    
    @property
    def prepay_months (self):
        return self.__PrepayMonths 
    
    @prepay_months.setter
    def prepay_months (self, value):
        self.__PrepayMonths = value
    
    @property
    def deposit (self):
        return self.__Deposit 
    
    @deposit.setter
    def deposit (self, value):
        self.__Deposit = value
        
    @property
    def client_fee (self):
        return self.__ClientFee 
    
    @client_fee.setter
    def client_fee (self, value):
        self.__ClientFee = value
    
    @property
    def agent_fee (self):
        return self.__AgentFee 
    
    @agent_fee.setter
    def agent_fee (self, value):
        self.__AgentFee = value
    
    
    def as_xml(self):
        result = [
            f'<Price>{self.price}</Price>',
            self.utilities_terms.as_xml(),
            f'<Currency>{self.currency}</Currency>',
            f'<PaymentPeriod>{self.payment_period}</PaymentPeriod>',
            f'<BargainAllowed>{self.bargain_allowed}</BargainAllowed>',
            f'<BargainPrice>{self.bargain_price}</BargainPrice>',
            f'<BargainConditions>{self.bargain_conditions}</BargainConditions>',
            f'<LeaseTermType>{self.lease_term_type}</LeaseTermType>',
            f'<PrepayMonths>{self.prepay_months}</PrepayMonths>',
            f'<Deposit>{self.deposit}</Deposit>',
            f'<ClientFee>{self.client_fee}</ClientFee>',
            f'<AgentFee>{self.agent_fee}</AgentFee>',
            self.agent_bonus.as_xml(),
            ]
        result = '\n    '.join(result)
        return f'<BargainTerms>\n   {result}\n  </BargainTerms>'
        
