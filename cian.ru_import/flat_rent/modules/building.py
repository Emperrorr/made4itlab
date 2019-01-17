#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko



class Building (Base):
    
    def __init__ (self):
        pass
    
    @property
    def name (self):
        return self.__Name
    
    @name.setter
    def name (self, value):
        self.__Name = value
    
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
    def series (self):
        return self.__Series
    
    @series.setter
    def series (self, value):
        self.__Series = value
        
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
    def has_garbage_chute (self):
        return self.__HasGarbageChute
    
    @has_garbage_chute.setter
    def has_garbage_chute (self, value):
        self.__HasGarbageChute = value
        
    @property
    def parking_type (self):
        return self.__Type
    
    @parking_type.setter
    def parking_type (self, value):
        self.__Type = value
        
    
    def as_xml(self):
        result = [
            f'<Name>{self.name}</Name>',
            f'<FloorsCount>{self.floors_count}</FloorsCount>',
            f'<BuildYear>{self.build_year}</BuildYear>',
            f'<MaterialType>{self.material_type}</MaterialType>',
            f'<Series>{self.series}</Series>',
            f'<CeilingHeight>{self.ceiling_height}</CeilingHeight>',
            f'<PassengerLiftsCount>{self.passenger_lifts_count}</PassengerLiftsCount>',
            f'<CargoLiftsCount>{self.cargo_lifts_count}</CargoLiftsCount>',
            f'<HasGarbageChute>{self.has_garbage_chute}</HasGarbageChute>',
            f'<Parking>\n<Type>{self.parking_type}</Type></Parking>\n'
            ]
        result = '\n      '.join(result)
        return f'< Building >\n      {result}\n    </ Building >'   
