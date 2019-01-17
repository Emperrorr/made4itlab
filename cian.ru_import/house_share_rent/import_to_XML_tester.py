# -*- coding: utf-8 -*-

from modules.house_share_rent import *

x = HouseShareRent ()

x.external_id='121313'
x.description='ljglawejefbq;okef'
x.address='dslkasdglma;oidghn'
x.coordinates.lat = '25'
x.coordinates.lng='34'
x.cadastral_number='vjqlheult,bk'
x.phones.country_code = '+49'
x.phones.number = '1235678'
x.highway.id = '245'
x.highway.distance = 'nowhere'
x.undergrounds.transport_type = 'walk'
x.undergrounds.time = '40'
x.undergrounds.id = '456'
x.subagent.email = '01@2345.ru'
x.subagent.phone = '+79991234567'
x.subagent.first_name = 'agent001'
x.subagent.last_name = 'Bond'
x.layout_photo.full_url= 'www.1.ru'
x.layout_photo.is_default = 'true'
x.photos.full_url= 'www.1.ru'
x.photos.is_default = 'true'
x.photos.full_url= 'www.1.ru'
x.photos.is_default = 'false'
x.videos.url = 'www.2.ru'
x.publish_terms.included_services.included_services = '2563'
x.publish_terms.excluded_services.excluded_services = '2563333'

x.category='house_share_rent'
x.settlement_name = 'dali-dalekie'
x.total_area='8752'
x.share_amouunt = '55555'
x.bedrooms_count = '33'
x.wc_location_type = 'out'
x.repair_type='none'
x.has_internet='21'
x.has_furniture='no'
x.has_phone='no'
x.has_kitchen_furniture='fff'
x.has_tv='false'
x.has_washer='false'
x.has_conditioner='false'
x.has_bathtub='false'
x.is_in_hidden_base='false'
x.has_shower='false'
x.has_bathhouse = 'true'
x.has_garage = 'false'
x.has_pool = '22'
x.has_dishwasher='false'
x.pets_allowed='false'
x.has_fridge='false'
x.children_allowed='false'

x.building.floors_count = '23'
x.building.build_year = '19999'
x.building.material_type = 'cvwef'
x.building.heating_type = 'gaz'

x.land.area = '112'
x.land.area_unit_type = 'gha'

x.bargain_terms.price = '43'
x.bargain_terms.currency = 'br'
x.bargain_terms.utilities_terms.price = '345'
x.bargain_terms.utilities_terms.included_in_price = 'false'
x.bargain_terms.payment_period = '55'
x.bargain_terms.bargain_allowed = 'trecc'
x.bargain_terms.bargain_price = '44'
x.bargain_terms.bargain_conditions = 'rtyui'
x.bargain_terms.lease_term_type = 'logg'
x.bargain_terms.prepay_months = '90'
x.bargain_terms.deposit = '09'
x.bargain_terms.client_fee = 'iu'
x.bargain_terms.agent_fee = 'rfrf'
x.bargain_terms.agent_bonus.value = '222'
x.bargain_terms.agent_bonus.payment_type = '333'
x.bargain_terms.agent_bonus.currency = 'eer'


s=x.as_xml()

print (s)


























