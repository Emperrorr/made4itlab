#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Land (object):
    
    def __init__ (self):
        pass
    
    
    @property
    def area (self):
        return self.__Area
    
    @area.setter
    def area (self, value):
        self.__Area = value
        
    @property
    def area_unit_type (self):
        return self.__AreaUnitType
    
    @area_unit_type.setter
    def area_unit_type (self, value):
        self.__AreaUnitType = value
        
           
    
    def as_xml(self):
        result = [
            f'<Area>{self.area}</Area>',
            f'<AreaUnitType>{self.area_unit_type}</AreaUnitType>'
            ]
        result = '\n      '.join(result)
        return f'< Land >\n      {result}\n    </ Land >'   
