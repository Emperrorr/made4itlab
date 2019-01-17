# -*- coding: utf-8 -*-

from modules.flat_sale import *


x = FlatSale()

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
x.photos.full_url= 'www.2.ru'
x.photos.is_default = 'false'
x.videos.url = 'www.2.ru'
x.jkschema.id = '234'
x.jkschema.name = ' kjanfkag'
x.building.name = 'dsfs'
x.building.floors_count = '23'
x.building.build_year = '19999'
x.building.material_type = 'cvwef'
x.building.series = '33'
x.building.ceiling_height = '44'
x.building.passenger_lifts_count = '3'
x.building.cargo_lifts_count = '9'
x.building.has_garbage_chute = 'true'
x.building.parking_type = 'rr'
x.bargain_terms.mortgage_allowed = 'true'
x.bargain_terms.sale_type = 'change'
x.bargain_terms.price = '43'
x.bargain_terms.currency = 'br'
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
x.coordinates.lat = '25'
x.coordinates.lng='34'
x.publish_terms.excluded_services.excluded_services = 'top3'
x.publish_terms.included_services.included_services = 'sale'
x.external_id='121313'
x.description='ljglawejefbq;okef'
x.address='dslkasdglma;oidghn'
x.cadastral_number='vjqlheult,bk'
x.category=';erjghlaebg'
x.room_type='wdwg'
x.flat_rooms_count='44'
x.is_apartments='true'
x.is_penthouse='true'
x.total_area='8752'
x.floor_number='7987'
x.all_rooms_area='666'
x.living_area='999'
x.kitchen_area='000'
x.loggias_count='33'
x.balconies_count='2'
x.windows_view_type='hell'
x.separate_wcs_count='1'
x.combined_wcs_count='1'
x.repair_type='none'
x.has_internet='21'
x.has_furniture='no'
x.has_phone='no'
x.has_kitchen_furniture='fff'
x.has_tv='false'
x.has_washer='false'
x.has_conditioner='false'
x.has_ramp='false'
x.has_bathtub='false'
x.is_in_hidden_base='false'
x.has_shower='false'
x.has_dishwasher='false'
x.pets_allowed='false'
x.has_fridge='false'
x.children_allowed='false'

s=x.as_xml()

print (s)
