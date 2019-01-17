#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko

from modules.deadline import *


class Building (Base):
    
    def __init__ (self):
        self.__deadline = Deadline ()
        
    @property
    def deadline (self):
        return self.__deadline
    
    @property
    def floors_count (self):
        return self.__FloorsCount
    
    @floors_count.setter
    def floors_count (self, value):
        self.__FloorsCount = value
        
    @property
    def material_type (self):
        return self.__MaterialType
    
    @material_type.setter
    def material_type (self, value):
        self.__MaterialType = value
        
    @property
    def ceiling_height (self):
        return self.__CeilingHeight
    
    @ceiling_height.setter
    def ceiling_height (self, value):
        self.__CeilingHeight = value
        
    @property
    def passenger_lifts_count (self):
        return self.__PassengerLiftsCount
    
    @passenger_lifts_count.setter
    def passenger_lifts_count (self, value):
        self.__PassengerLiftsCount = value
        
    @property
    def cargo_lifts_count (self):
        return self.__CargoLiftsCount
    
    @cargo_lifts_count.setter
    def cargo_lifts_count (self, value):
        self.__CargoLiftsCount = value
    
    @property
    def parking_type (self):
        return self.__Type
    
    @parking_type.setter
    def parking_type (self, value):
        self.__Type = value
    
    def as_xml(self):
        result = [
            f'<FloorsCount>{self.floors_count}</FloorsCount>',
            f'<MaterialType>{self.material_type}</MaterialType>',
            f'<CeilingHeight>{self.ceiling_height}</CeilingHeight>',
            f'<PassengerLiftsCount>{self.passenger_lifts_count}</PassengerLiftsCount>',
            f'<CargoLiftsCount>{self.cargo_lifts_count}</CargoLiftsCount>',
            f'<Parking>\n      <Type>{self.parking_type}</Type>\n      </Parking>',
            self.deadline.as_xml()
            ]
        result = '\n      '.join(result)
        return f'< Building >\n      {result}\n    </ Building >'   
