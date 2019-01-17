#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko




class Coordinates (Base):
    
    def __init__ (self):
        pass
    
    @property
    def lat (self):
        return self.__Lat
    
    @lat.setter
    def lat (self, value):
        self.__Lat = value
        
    @property
    def lng (self):
        return self.__Lng
    
    @lng.setter
    def lng (self, value):
        self.__Lng = value
    
    
    def as_xml(self):
        result = [
            f'<Lat>{self.lat}</Lat>',
            f'<Lng>{self.lng}</Lng>'
            ]
        result = '\n  '.join(result)
        return f'<Coordinates>\n  {result}\n  </Coordinates>'    
