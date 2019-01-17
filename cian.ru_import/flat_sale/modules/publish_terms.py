#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


from modules.included_services import *
from modules.excluded_services import *

class PublishTerms (Base):
    
    def __init__ (self):
        self.__excluded_services = ExcludedServices()
        self.__included_services = IncludedServices()
        
    @property
    def excluded_services (self):
        return self.__excluded_services
    
    @ property
    def included_services (self):
        return self.__included_services
    
    def as_xml(self):
        result =[
            self.included_services.as_xml(),
            self.excluded_services.as_xml()
            ]
        result = '\n  '.join(result)
        return f'<PublishTerms>\n <Terms> \n <PublishTermSchema>\n  {result}\</PublishTermSchema> \n </Terms> \n </PublishTerms>'