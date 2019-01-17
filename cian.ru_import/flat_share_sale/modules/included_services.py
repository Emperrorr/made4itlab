#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


class IncludedServices (Base):
    
    def __init__ (self):
        pass
    
    @property
    def included_services (self):
        return self.__Services
    
    @included_services.setter
    def included_services (self, value):
        self.__Services = value
        
        
    def as_xml(self):
        result = [
            f'<ServicesEnum>{self.included_services}</ServicesEnum>',
            ]
        result = '\n  '.join(result)
        return f'<Services>\n  {result}\n  </Services>'    
