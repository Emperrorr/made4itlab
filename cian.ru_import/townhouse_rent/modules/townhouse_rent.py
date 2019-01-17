#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko

###### general terms import
from modules.coordinates import *
from modules.phones import *
from modules.highway import *
from modules.undergrounds import *
from modules.subagent import *
from modules.layout_photo import *
from modules.photos import *
from modules.videos import *
from modules.publish_terms import *

###### townhouse rent terms import
from modules.building import *
from modules.land import *
from modules.bargain_terms import *


class TownhouseRent (Base):
    
    def __init__ (self):
        self.__coordinates = Coordinates()
        self.__phones = Phones()
        self.__highway = Highway()
        self.__undergrounds = Undergrounds()
        self.__subagent = SubAgent()
        self.__layout_photo = LayoutPhoto()
        self.__photos = Photos()
        self.__videos = Videos()
        self.__publish_terms = PublishTerms()
        self.__building = Building()
        self.__land = Land()
        self.__bargain_terms = BargainTerms()
        
    @property
    def bargain_terms (self):
        return self.__bargain_terms
        
    @property
    def land (self):
        return self.__land
        
    @property
    def building (self):
        return self.__building
    
    @property
    def publish_terms (self):
        return self.__publish_terms
    
    @property
    def videos (self):
        return self.__videos
    
    @property
    def photos (self):
        return self.__photos
    
    @property
    def layout_photo (self):
        return self.__layout_photo
    
    @property
    def subagent (self):
        return self.__subagent
    
    @property
    def undergrounds (self):
        return self.__undergrounds
    
    @property
    def highway (self):
        return self.__highway
    
    @property
    def phones (self):
        return self.__phones
    
    @property
    def coordinates (self):
        return self.__coordinates


#######   GENERAL ADVERTISMENT DETAILS

    @property
    def external_id (self):
        return self.__ExternalId
    
    @external_id.setter
    def external_id (self, value):
        self.__ExternalId = value
    
    @property
    def description (self):
        return self.__Description
    
    @description.setter
    def description (self, value):
        self.__Description = value
    
    @property
    def address (self):
        return self.__Address

    @address.setter
    def address (self, value):
        self.__Address = value
    
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
    
    @property
    def cadastral_number (self):
        return self.__CadastralNumber
    
    @cadastral_number.setter
    def cadastral_number (self, value):
        self.__CadastralNumber = value


######## COTTAGE RENT ADVERTISMENT DETAILS

    @property
    def category (self):
        return self.__Category
        
    @category.setter
    def category(self, value):
        self.__Category = value
        
    @property
    def settlement_name (self):
        return self.__SettlementName
   
    @settlement_name.setter
    def settlement_name (self, value):
        self.__SettlementName = value
        
    @property
    def total_area (self):
        return self.__TotalArea
    
    @total_area.setter
    def total_area (self, value):
        self.__TotalArea = value
   
    @property
    def bedrooms_count (self):
        return self.__BedroomsCount
    
    @bedrooms_count.setter
    def bedrooms_count (self, value):
        self.__BedroomsCount = value
    
    @property
    def wc_location_type (self):
        return self.__WcLocationType
    
    @wc_location_type.setter
    def wc_location_type (self, value):
        self.__WcLocationType = value
          
    @property
    def repair_type (self):
        return self.__RepairType
    
    @repair_type.setter
    def repair_type (self, value):
        self.__RepairType = value
    
    @property
    def has_internet(self):
        return self.__HasInternet
    
    @has_internet.setter
    def has_internet (self, value):
        self.__HasInternet = value
        
    @property
    def has_furniture (self):
        return self.__HasFurniture
    
    @has_furniture.setter
    def has_furniture (self, value):
        self.__HasFurniture = value
        
    @property
    def has_phone (self):
        return self.__HasPhone

    @has_phone.setter
    def has_phone (self, value):
        self.__HasPhone = value
    
    @property
    def has_kitchen_furniture (self):
        return self.__HasKitchenFurniture
    
    @has_kitchen_furniture.setter
    def has_kitchen_furniture (self, value):
        self.__HasKitchenFurniture = value
    
    @property
    def has_tv (self):
        return self.__HasTv
    
    @has_tv.setter
    def has_tv (self, value):
        self.__HasTv = value
        
    @property
    def has_washer (self):
        return self.__HasWasher
    
    @has_washer.setter
    def has_washer (self, value):
        self.__HasWasher = value
        
    @property
    def has_conditioner (self):
        return self.__HasConditioner
    
    @has_conditioner.setter
    def has_conditioner (self,value):
        self.__HasConditioner = value
    
    @property
    def has_bathtub (self):
        return self.__HasBathtub
    
    @has_bathtub.setter
    def has_bathtub (self, value):
        self.__HasBathtub = value
    
    @property
    def is_in_hidden_base (self):
        return self.__IsInHiddenBase
    
    @is_in_hidden_base.setter
    def is_in_hidden_base (self, value):
        self.__IsInHiddenBase = value
        
    @property
    def has_shower (self):
        return self.__HasShower
    
    @has_shower.setter
    def has_shower (self, value):
        self.__HasShower = value
        
    @property
    def has_bathhouse (self):
        return self.__HasBathhouse
    
    @has_bathhouse.setter
    def has_bathhouse (self, value):
        self.__HasBathhouse = value
    
    @property
    def has_garage (self):
        return self.__HasGarage
    
    @has_garage.setter
    def has_garage (self, value):
        self.__HasGarage = value
    
    @property
    def has_pool (self):
        return self.__HasPool
    
    @has_pool.setter
    def has_pool (self, value):
        self.__HasPool = value  
    
    @property
    def has_dishwasher (self):
        return self.__HasDishwasher
            
    @has_dishwasher.setter
    def has_dishwasher (self, value):
        self.__HasDishwasher = value
        
    @property
    def pets_allowed (self):
        return self.__PetsAllowed
    
    @pets_allowed.setter
    def pets_allowed (self, value):
        self.__PetsAllowed = value
        
    @property
    def has_fridge (self):
        return self.__HasFridge
    
    @has_fridge.setter
    def has_fridge (self, value):
        self.__HasFridge = value
    
    @property
    def children_allowed (self):
        return self.__ChildrenAllowed
    
    @children_allowed.setter
    def children_allowed (self, value):
        self.__ChildrenAllowed = value
        
        

#######  EXPORT TO .XML FORMAT



    def as_xml(self):
        result = [
            f'<ExternalId>{self.external_id}</ExternalId>',
            f'<Description>{self.description}</Description>',
            f'<Address>{self.address}</Address>',
            self.coordinates.as_xml(),
            f'<CadastralNumber>"{self.cadastral_number}"</CadastralNumber>',
            self.phones.as_xml(),
            self.highway.as_xml(),
            self.undergrounds.as_xml(),
            self.subagent.as_xml(),
            self.layout_photo.as_xml(),
            self.photos.as_xml(),
            self.videos.as_xml(),
            self.publish_terms.as_xml(),
            f'<Category>{self.category}</Category>',
            f'<SettlementName>{self.settlement_name}</SettlementName>',
            f'<TotalArea>{self.total_area}</TotalArea>',
            f'<BedroomsCount>{self.bedrooms_count}</BedroomsCount>',
            f'<WcLocationType>{self.wc_location_type}</WcLocationType>',
            f'<RepairType>{self.repair_type}</RepairType>',
            f'<HasInternet>{self.has_internet}</HasInternet>',
            f'<HasFurniture>{self.has_furniture}</HasFurniture>',
            f'<HasPhone>{self.has_phone}</HasPhone>',
            f'<HasKitchenFurniture>{self.has_kitchen_furniture}</HasKitchenFurniture>',
            f'<HasTv>{self.has_tv}</HasTv>',
            f'<HasWasher>{self.has_washer}</HasWasher>',
            f'<HasConditioner>{self.has_conditioner}</HasConditioner>',
            f'<HasBathtub>{self.has_bathtub}</HasBathtub>',
            f'<IsInHiddenBase>{self.is_in_hidden_base}</IsInHiddenBase>',
            f'<HasShower>{self.has_shower}</HasShower>',
            f'<HasBathhouse>{self.has_bathhouse}</HasBathhouse>',
            f'<HasGarage>{self.has_garage}</HasGarage>',
            f'<HasPool>{self.has_pool}</HasPool>',
            f'<HasDishwasher>{self.has_dishwasher}</HasDishwasher>',
            f'<PetsAllowed>{self.pets_allowed}</PetsAllowed>',
            f'<HasFridge>{self.has_fridge}</HasFridge>',
            f'<ChildrenAllowed>{self.children_allowed}</ChildrenAllowed>',
            self.building.as_xml(),
            self.land.as_xml(),
            self.bargain_terms.as_xml()
            ]
        result = '\n  '.join(result)
        return f'<object>\n  {result}\n</object>'
            

