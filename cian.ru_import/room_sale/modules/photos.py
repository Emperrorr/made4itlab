#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko




class Photos (Base):
    
    def __init__ (self):
        pass
    
    @property
    def full_url (self):
        return self.__FullUrl
    
    @full_url.setter
    def full_url (self, value):
        self.__FullUrl = value
        
    @property
    def is_default (self):
        return self.__IsDefault
    
    @is_default.setter
    def is_default (self, value):
        self.__IsDefault = value
    
    
    def as_xml(self):
        result = [
            f'<PhotoSchema>',
            f'<FullUrl>{self.full_url}</FullUrl>',
            f'<IsDefault>{self.is_default}</IsDefault>',
            f'</PhotoSchema>'
            ]
        result = '\n  '.join(result)
        return f'<Photos>\n  {result}\n</Photos>'
