#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


class SubAgent (Base):
    
    def __init__ (self):
        pass
    
    @property
    def email (self):
        return self.__Email
    
    @email.setter
    def email (self, value):
        self.__Email = value
        
    @property
    def phone (self):
        return self.__Phone
    
    @phone.setter
    def phone (self, value):
        self.__Phone = value
    
    @property
    def first_name (self):
        return self.__FirstName
    
    @first_name.setter
    def first_name (self, value):
        self.__FirstName = value
        
    @property
    def last_name (self):
        return self.__LastName
    
    @last_name.setter
    def last_name (self, value):
        self.__LastName = value
        
    def as_xml(self):
        result = [
            f'<Email>{self.email}</Email>',
            f'<Phone>{self.phone}</Phone>',
            f'<FirstName>{self.first_name}</FirstName>',
            f'<LastName>{self.last_name}</LastName>'
            ]
        result = '\n  '.join(result)
        return f'<SubAgent>\n  {result}\n</SubAgent>'
        


