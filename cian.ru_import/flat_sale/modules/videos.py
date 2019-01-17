#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Videos (Base):
    
    def __init__ (self):
        pass
    
    @property
    def url (self):
        return self.__Url
    
    @url.setter
    def url (self, value):
        self.__Url = value
        
    
    def as_xml(self):
        result = [
            f'<VideoSchema>',
            f'<Url>{self.url}</Url>',
            f'</VideoSchema>'
            ]
        result = '\n  '.join(result)
        return f'<Videos>\n  {result}\n</Videos>'
