/**
 * Arduino DSMR parser.
 *
 * This software is licensed under the MIT License.
 *
 * Copyright (c) 2015 Matthijs Kooijman <matthijs@stdin.nl>
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 * Field parsing functions
 */

#include "fields.h"

using namespace dsmr;
using namespace dsmr::fields;

// Since C++11 it is possible to define the initial values for static
// const members in the class declaration, but if their address is
// taken, they still need a normal definition somewhere (to allocate
// storage).
const char units::none[];
const char units::kWh[];
const char units::Wh[];
const char units::kW[];
const char units::W[];
const char units::V[];
const char units::mV[];
const char units::A[];
const char units::mA[];
const char units::m3[];
const char units::dm3[];
const char units::GJ[];
const char units::MJ[];
const char units::kvar[];
const char units::kvarh[];

const ObisId identification::id;
const char identification::name_progmem[];
const const __FlashStringHelper *identification::name;

const ObisId p1_version::id;
const char p1_version::name_progmem[];
const const __FlashStringHelper *p1_version::name;

/* extra field for Belgium */
const ObisId p1_version_be::id;
const char p1_version_be::name_progmem[];
const const __FlashStringHelper *p1_version_be::name;

const ObisId timestamp::id;
const char timestamp::name_progmem[];
const const __FlashStringHelper *timestamp::name;

const ObisId equipment_id::id;
const char equipment_id::name_progmem[];
const const __FlashStringHelper *equipment_id::name;

/* extra for Lux */
const ObisId energy_delivered_lux::id;
const char energy_delivered_lux::name_progmem[];
const const __FlashStringHelper *energy_delivered_lux::name;

const ObisId energy_delivered_tariff1::id;
const char energy_delivered_tariff1::name_progmem[];
const const __FlashStringHelper *energy_delivered_tariff1::name;

const ObisId energy_delivered_tariff2::id;
const char energy_delivered_tariff2::name_progmem[];
const const __FlashStringHelper *energy_delivered_tariff2::name;

/* extra for Lux */
const ObisId energy_returned_lux::id;
const char energy_returned_lux::name_progmem[];
const const __FlashStringHelper *energy_returned_lux::name;

const ObisId energy_returned_tariff1::id;
const char energy_returned_tariff1::name_progmem[];
const const __FlashStringHelper *energy_returned_tariff1::name;

const ObisId energy_returned_tariff2::id;
const char energy_returned_tariff2::name_progmem[];
const const __FlashStringHelper *energy_returned_tariff2::name;

/* extra for Lux */
const ObisId total_imported_energy::id;
const char total_imported_energy::name_progmem[];
const const __FlashStringHelper *total_imported_energy::name;

/* extra for Lux */
const ObisId total_exported_energy::id;
const char total_exported_energy::name_progmem[];
const const __FlashStringHelper *total_exported_energy::name;

/* extra for Lux */
const ObisId reactive_power_delivered::id;
const char reactive_power_delivered::name_progmem[];
const const __FlashStringHelper *reactive_power_delivered::name;

/* extra for Lux */
const ObisId reactive_power_returned::id;
const char reactive_power_returned::name_progmem[];
const const __FlashStringHelper *reactive_power_returned::name;

const ObisId electricity_tariff::id;
const char electricity_tariff::name_progmem[];
const const __FlashStringHelper *electricity_tariff::name;

const ObisId power_delivered::id;
const char power_delivered::name_progmem[];
const const __FlashStringHelper *power_delivered::name;

const ObisId power_returned::id;
const char power_returned::name_progmem[];
const const __FlashStringHelper *power_returned::name;

const ObisId electricity_threshold::id;
const char electricity_threshold::name_progmem[];
const const __FlashStringHelper *electricity_threshold::name;

const ObisId electricity_switch_position::id;
const char electricity_switch_position::name_progmem[];
const const __FlashStringHelper *electricity_switch_position::name;

const ObisId electricity_failures::id;
const char electricity_failures::name_progmem[];
const const __FlashStringHelper *electricity_failures::name;

const ObisId electricity_long_failures::id;
const char electricity_long_failures::name_progmem[];
const const __FlashStringHelper *electricity_long_failures::name;

const ObisId electricity_failure_log::id;
const char electricity_failure_log::name_progmem[];
const const __FlashStringHelper *electricity_failure_log::name;

const ObisId electricity_sags_l1::id;
const char electricity_sags_l1::name_progmem[];
const const __FlashStringHelper *electricity_sags_l1::name;

const ObisId electricity_sags_l2::id;
const char electricity_sags_l2::name_progmem[];
const const __FlashStringHelper *electricity_sags_l2::name;

const ObisId electricity_sags_l3::id;
const char electricity_sags_l3::name_progmem[];
const const __FlashStringHelper *electricity_sags_l3::name;

const ObisId electricity_swells_l1::id;
const char electricity_swells_l1::name_progmem[];
const const __FlashStringHelper *electricity_swells_l1::name;

const ObisId electricity_swells_l2::id;
const char electricity_swells_l2::name_progmem[];
const const __FlashStringHelper *electricity_swells_l2::name;

const ObisId electricity_swells_l3::id;
const char electricity_swells_l3::name_progmem[];
const const __FlashStringHelper *electricity_swells_l3::name;

const ObisId message_short::id;
const char message_short::name_progmem[];
const const __FlashStringHelper *message_short::name;

const ObisId message_long::id;
const char message_long::name_progmem[];
const const __FlashStringHelper *message_long::name;

const ObisId voltage_l1::id;
const char voltage_l1::name_progmem[];
const const __FlashStringHelper *voltage_l1::name;

const ObisId voltage_l2::id;
const char voltage_l2::name_progmem[];
const const __FlashStringHelper *voltage_l2::name;

const ObisId voltage_l3::id;
const char voltage_l3::name_progmem[];
const const __FlashStringHelper *voltage_l3::name;

const ObisId current_l1::id;
const char current_l1::name_progmem[];
const const __FlashStringHelper *current_l1::name;

const ObisId current_l2::id;
const char current_l2::name_progmem[];
const const __FlashStringHelper *current_l2::name;

const ObisId current_l3::id;
const char current_l3::name_progmem[];
const const __FlashStringHelper *current_l3::name;

const ObisId power_delivered_l1::id;
const char power_delivered_l1::name_progmem[];
const const __FlashStringHelper *power_delivered_l1::name;

const ObisId power_delivered_l2::id;
const char power_delivered_l2::name_progmem[];
const const __FlashStringHelper *power_delivered_l2::name;

const ObisId power_delivered_l3::id;
const char power_delivered_l3::name_progmem[];
const const __FlashStringHelper *power_delivered_l3::name;

const ObisId power_returned_l1::id;
const char power_returned_l1::name_progmem[];
const const __FlashStringHelper *power_returned_l1::name;

const ObisId power_returned_l2::id;
const char power_returned_l2::name_progmem[];
const const __FlashStringHelper *power_returned_l2::name;

const ObisId power_returned_l3::id;
const char power_returned_l3::name_progmem[];
const const __FlashStringHelper *power_returned_l3::name;

/* LUX */
const ObisId reactive_power_delivered_l1::id;
const char reactive_power_delivered_l1::name_progmem[];
const const __FlashStringHelper *reactive_power_delivered_l1::name;

/* LUX */
const ObisId reactive_power_delivered_l2::id;
const char reactive_power_delivered_l2::name_progmem[];
const const __FlashStringHelper *reactive_power_delivered_l2::name;

/* LUX */
const ObisId reactive_power_delivered_l3::id;
const char reactive_power_delivered_l3::name_progmem[];
const const __FlashStringHelper *reactive_power_delivered_l3::name;

/* LUX */
const ObisId reactive_power_returned_l1::id;
const char reactive_power_returned_l1::name_progmem[];
const const __FlashStringHelper *reactive_power_returned_l1::name;

/* LUX */
const ObisId reactive_power_returned_l2::id;
const char reactive_power_returned_l2::name_progmem[];
const const __FlashStringHelper *reactive_power_returned_l2::name;

/* LUX */
const ObisId reactive_power_returned_l3::id;
const char reactive_power_returned_l3::name_progmem[];
const const __FlashStringHelper *reactive_power_returned_l3::name;

const ObisId gas_device_type::id;
const char gas_device_type::name_progmem[];
const const __FlashStringHelper *gas_device_type::name;

const ObisId gas_equipment_id::id;
const char gas_equipment_id::name_progmem[];
const const __FlashStringHelper *gas_equipment_id::name;

const ObisId gas_valve_position::id;
const char gas_valve_position::name_progmem[];
const const __FlashStringHelper *gas_valve_position::name;

/* _NL */
const ObisId gas_delivered::id;
const char gas_delivered::name_progmem[];
const const __FlashStringHelper *gas_delivered::name;

/* _BE */
const ObisId gas_delivered_be::id;
const char gas_delivered_be::name_progmem[];
const const __FlashStringHelper *gas_delivered_be::name;

const ObisId thermal_device_type::id;
const char thermal_device_type::name_progmem[];
const const __FlashStringHelper *thermal_device_type::name;

const ObisId thermal_equipment_id::id;
const char thermal_equipment_id::name_progmem[];
const const __FlashStringHelper *thermal_equipment_id::name;

const ObisId thermal_valve_position::id;
const char thermal_valve_position::name_progmem[];
const const __FlashStringHelper *thermal_valve_position::name;

const ObisId thermal_delivered::id;
const char thermal_delivered::name_progmem[];
const const __FlashStringHelper *thermal_delivered::name;

const ObisId water_device_type::id;
const char water_device_type::name_progmem[];
const const __FlashStringHelper *water_device_type::name;

const ObisId water_equipment_id::id;
const char water_equipment_id::name_progmem[];
const const __FlashStringHelper *water_equipment_id::name;

const ObisId water_valve_position::id;
const char water_valve_position::name_progmem[];
const const __FlashStringHelper *water_valve_position::name;

const ObisId water_delivered::id;
const char water_delivered::name_progmem[];
const const __FlashStringHelper *water_delivered::name;

const ObisId water_delivered_2::id;
const char water_delivered_2::name_progmem[];
const const __FlashStringHelper *water_delivered_2::name;

const ObisId slave_device_type::id;
const char slave_device_type::name_progmem[];
const const __FlashStringHelper *slave_device_type::name;

const ObisId slave_equipment_id::id;
const char slave_equipment_id::name_progmem[];
const const __FlashStringHelper *slave_equipment_id::name;

const ObisId slave_valve_position::id;
const char slave_valve_position::name_progmem[];
const const __FlashStringHelper *slave_valve_position::name;

const ObisId slave_delivered::id;
const char slave_delivered::name_progmem[];
const const __FlashStringHelper *slave_delivered::name;

