#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class ExcludedServices (Base):
    
    def __init__ (self):
        pass
    
    @property
    def excluded_services (self):
        return self.__ExcludedServices
    
    @excluded_services.setter
    def excluded_services (self, value):
        self.__ExcludedServices = value
        
        
    def as_xml(self):
        result = [
            f'<ExcludedServicesEnum>{self.excluded_services}</ExcludedServicesEnum>',
            ]
        result = '\n  '.join(result)
        return f'<ExcludedServices>\n  {result}\n  </ExcludedServices>'    
