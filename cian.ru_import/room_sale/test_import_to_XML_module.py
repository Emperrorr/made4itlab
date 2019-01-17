# -*- coding: utf-8 -*-

from modules.room_sale import *


x = RoomSale()


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

x.category='roomSale'
x.rooms_for_sale_count ='44'
x.room_type='wdwg'
x.rooms_count = '5'
x.room_area = '33'
x.total_area='8752'
x.floor_number='7987'
x.jkschema.id = '3'
x.jkschema.name = '44444'
x.kitchen_area='000'
x.loggias_count='33'
x.balconies_count='2'
x.separate_wcs_count='1'
x.combined_wcs_count='1'
x.repair_type='none'
x.has_ramp='false'
x.is_in_hidden_base='false'

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

x.bargain_terms.price = '43'
x.bargain_terms.currency = 'br'
x.bargain_terms.mortgage_allowed = 'trecc'
x.bargain_terms.sale_type = 'rfrf'
x.bargain_terms.agent_bonus.value = '222'
x.bargain_terms.agent_bonus.payment_type = '333'
x.bargain_terms.agent_bonus.currency = 'eer'

s=x.as_xml()

print (s)
