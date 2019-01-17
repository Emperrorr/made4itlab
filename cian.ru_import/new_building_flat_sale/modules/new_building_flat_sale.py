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

###### flat terms import
from modules.jkschema import *
from modules.building import *
from modules.bargain_terms import *
from modules.agent_bonus import *



class NewBuildingFlatSale (object):
    
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


######## FLAT_SHARE SALE ADVERTISMENT DETAILS

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
    def decoration (self):
        return self.__Decoration
    
    @decoration.setter
    def decoration (self, value):
        self.__Decoration = value
    
    @property
    def project_declaration_url (self):
        return self.__ProjectDeclarationUrl
    
    @project_declaration_url.setter
    def project_declaration_url (self, value):
        self.__ProjectDeclarationUrl = value
        
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
    def has_ramp (self):
        return self.__HasRamp
    
    @has_ramp.setter
    def has_ramp (self, value):
        self.__HasRamp = value
    
    @property
    def is_in_hidden_base (self):
        return self.__IsInHiddenBase
    
    @is_in_hidden_base.setter
    def is_in_hidden_base (self, value):
        self.__IsInHiddenBase = value
        
            
        

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
            f'<RoomType>{self.room_type}</RoomType>'
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
            f'<Decoration>{self.decoration}</Decoration>',
            f'<ProjectDeclarationUrl>{self.project_declaration_url}</ProjectDeclarationUrl>',
            f'<WindowsViewType>{self.windows_view_type}<WindowsViewType>',
            f'<SeparateWcsCount>{self.separate_wcs_count}</SeparateWcsCount>',
            f'<CombinedWcsCount>{self.combined_wcs_count}</CombinedWcsCount>',
            f'<HasRamp>{self.has_ramp}</HasRamp>',
            f'<IsInHiddenBase>{self.is_in_hidden_base}</IsInHiddenBase>',
            self.building.as_xml(),
            self.bargain_terms.as_xml()
            ]
        result = '\n  '.join(result)
        return f'<object>\n  {result}\n</object>'
            

