#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Building (Base):
    
    def __init__ (self):
        pass
    
    
    @property
    def floors_count (self):
        return self.__FloorsCount
    
    @floors_count.setter
    def floors_count (self, value):
        self.__FloorsCount = value
        
    @property
    def build_year (self):
        return self.__BuildYear
    
    @build_year.setter
    def build_year (self, value):
        self.__BuildYear = value
        
    @property
    def material_type (self):
        return self.__MaterialType
    
    @material_type.setter
    def material_type (self, value):
        self.__MaterialType = value
        
    @property
    def heating_type (self):
        return self.__HeatingType
    
    @heating_type.setter
    def heating_type (self, value):
        self.__HeatingType = value

        
    
    def as_xml(self):
        result = [
            f'<FloorsCount>{self.floors_count}</FloorsCount>',
            f'<BuildYear>{self.build_year}</BuildYear>',
            f'<MaterialType>{self.material_type}</MaterialType>',
            f'<HeatingType>{self.heating_type}</HeatingType>'
            ]
        result = '\n      '.join(result)
        return f'< Building >\n      {result}\n    </ Building >'   
