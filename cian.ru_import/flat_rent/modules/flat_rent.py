#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Shevchenko


from modules.coordinates import *
from modules.phones import *
from modules.highway import *
from modules.undergrounds import *
from modules.subagent import *
from modules.layout_photo import *
from modules.photos import *
from modules.videos import *
from modules.jkschema import *
from modules.building import *
from modules.bargain_terms import *
from modules.utilities_terms import *
from modules.agent_bonus import *
from modules.publish_terms import *


class FlatRent (Base):
    
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
        self.__jkschema = JKSchema()
        self.__building = Building()
        self.__bargain_terms = BargainTerms ()
        self.__utilities_terms = UtilitiesTerms()
        self.__agent_bonus = AgentBonus ()
    
    @property
    def agent_bonus (self):
        return self.__agent_bonus
    
    @property
    def utilities_terms (self):
        return self.__utilities_terms
    
    @property
    def bargain_terms (self):
        return self.__bargain_terms
    
    @property
    def building (self):
        return self.__building
    
    @property
    def jkschema (self):
        return self.__jkschema
    
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


######## FLAT RENT ADVERTISMENT DETAILS

    @property
    def category (self):
        return self.__Category
        
    @category.setter
    def category(self, value):
        self.__Category = value
        
    @property
    def room_type (self):
        return self.__RoomType
   
    @room_type.setter
    def room_type (self, value):
        self.__RoomType = value
   
    @property
    def flat_rooms_count (self):
        return self.__FlatRoomsCount
    
    @flat_rooms_count.setter
    def flat_rooms_count (self, value):
        self.__FlatRoomsCount = value
    
    @property
    def is_apartment (self):
        return self.__IsApartments
    
    @is_apartment.setter
    def is_apartment (self, value):
        self.__IsApartments = value
    
    @property
    def is_penthouse (self):
        return self.__IsPenthouse
    
    @is_penthouse.setter
    def is_penthouse (self, value):
        self.__IsPenthouse  = value
    
    @property
    def total_area (self):
        return self.__TotalArea
    
    @total_area.setter
    def total_area (self, value):
        self.__TotalArea  = value
    
    @property
    def floor_number (self):
        return self.__FloorNumber
    
    @floor_number.setter
    def floor_number (self, value):
        self.__FloorNumber  = value
        
    @property
    def all_rooms_area (self):
        return self.__AllRoomsArea
    
    @all_rooms_area.setter
    def all_rooms_area (self, value):
        self.__AllRoomsArea = value
        
    @property
    def living_area (self):
        return self.__LivingArea
    
    @living_area.setter
    def living_area (self, value):
        self.__LivingArea = value
        
    @property
    def kitchen_area (self):
        return self.__KitchenArea
    
    @kitchen_area.setter
    def kitchen_area (self, value):
        self.__KitchenArea = value
        
    @property
    def loggias_count (self):
        return self.__LoggiasCount

    @loggias_count.setter
    def loggias_count (self, value):
        self.__LoggiasCount = value
    
    @property
    def balconies_count (self):
        return self.__BalconiesCount
    
    @balconies_count.setter
    def balconies_count (self, value):
        self.__BalconiesCount = value
        
    @property
    def windows_view_type (self):
        return self.__WindowsViewType
    
    @windows_view_type.setter
    def windows_view_type (self, value):
        self.__WindowsViewType = value
        
    @property
    def separate_wcs_count (self):
        return self.__SeparateWcsCount
    
    @separate_wcs_count.setter
    def separate_wcs_count (self, value):
        self.__SeparateWcsCount = value
        
    @property
    def combined_wcs_count (self):
        return self.__CombinedWcsCount
    
    @combined_wcs_count.setter
    def combined_wcs_count (self, value):
        self.__CombinedWcsCount = value
        
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
    def has_ramp (self):
        return self.__HasRamp
    
    @has_ramp.setter
    def has_ramp (self, value):
        self.__HasRamp = value
    
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
            f'<Categorym>{self.category}</Category>',
            f'<RoomType>{self.room_type}</RoomType>',
            f'<FlatRoomsCount>{self.flat_rooms_count}</FlatRoomsCount>',
            f'<IsApartments>{self.is_apartments}</IsApartments>',
            f'<IsPenthouse>{self.is_penthouse}</IsPenthouse>',
            f'<TotalArea>{self.total_area}</TotalArea>',
            f'<FloorNumber>{self.floor_number}</FloorNumber>',
            self.jkschema.as_xml(),
            f'<AllRoomsArea>{self.all_rooms_area}</AllRoomsArea>',
            f'<LivingArea>"{self.living_area}</LivingArea>',
            f'<KitchenArea>{self.kitchen_area}</KitchenArea>',
            f'<LoggiasCount>self.loggias_count</LoggiasCount>',
            f'<BalconiesCount>{self.balconies_count}</BalconiesCount>',
            f'<WindowsViewType>{self.windows_view_type}<WindowsViewType>',
            f'<SeparateWcsCount>{self.separate_wcs_count}</SeparateWcsCount>',
            f'<CombinedWcsCount>{self.combined_wcs_count}</CombinedWcsCount>',
            f'<RepairType>{self.repair_type}</RepairType>',
            f'<HasInternet>{self.has_internet}</HasInternet>',
            f'<HasFurniture>{self.has_furniture}</HasFurniture>',
            f'<HasPhone>{self.has_phone}</HasPhone>',
            f'<HasKitchenFurniture>{self.has_kitchen_furniture}</HasKitchenFurniture>',
            f'<HasTv>{self.has_tv}</HasTv>',
            f'<HasWasher>{self.has_washer}</HasWasher>',
            f'<HasConditioner>{self.has_conditioner}</HasConditioner>',
            f'<HasRamp>{self.has_ramp}</HasRamp>',
            f'<HasBathtub>{self.has_bathtub}</HasBathtub>',
            f'<IsInHiddenBase>{self.is_in_hidden_base}</IsInHiddenBase>',
            f'<HasShower>{self.has_shower}</HasShower>',
            f'<HasDishwasher>{self.has_dishwasher}</HasDishwasher>',
            self.building.as_xml(),
            self.bargain_terms.as_xml(),
            f'<PetsAllowed>{self.pets_allowed}</PetsAllowed>',
            f'<HasFridge>{self.has_fridge}</HasFridge>',
            f'<ChildrenAllowed>{self.children_allowed}</ChildrenAllowed>',
            ]
        result = '\n  '.join(result)
        return f'<object>\n  {result}\n</object>'
            

