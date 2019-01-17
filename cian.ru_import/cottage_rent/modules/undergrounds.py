#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Undergrounds (Base):
    
    def __init__ (self):
        pass
    
    @property
    def transport_type (self):
        return self.__TransportType
    
    @transport_type.setter
    def transport_type (self, value):
        self.__TransportType = value
        
    @property
    def time (self):
        return self.__Time
    
    @time.setter
    def time (self, value):
        self.__Time = value
    
    @property
    def id (self):
        return self.__Id
    
    @id.setter
    def id (self, value):
        self.__Id = value
    
    def as_xml(self):
        result = [
            f'<UndergroundInfoSchema>',
            f'< TransportType >{self.transport_type}</ TransportType >',
            f'<Time>{self.time}</Time>',
            f'<Id>{self.id}</Id>',
            f'</UndergroundInfoSchema>'
            ]
        result = '\n  '.join(result)
        return f'<Undergrounds>\n  {result}\n</Undergrounds>'
        

