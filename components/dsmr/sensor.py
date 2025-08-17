import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    ICON_EMPTY,
    
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_NONE,
    UNIT_AMPERE,
    UNIT_EMPTY,
    UNIT_VOLT,
    UNIT_WATT_HOURS,
    UNIT_WATT,
)
from . import DSMR, CONF_DSMR_ID

AUTO_LOAD = ["dsmr"]


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_DSMR_ID): cv.use_id(DSMR),

        cv.Optional("energy_delivered_lux"): sensor.sensor_schema(
            unit_of_measurement="kWh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("energy_delivered_tariff1"): sensor.sensor_schema(
            unit_of_measurement="kWh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("energy_delivered_tariff2"): sensor.sensor_schema(
            unit_of_measurement="kWh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("energy_returned_lux"): sensor.sensor_schema(
            unit_of_measurement="kWh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("energy_returned_tariff1"): sensor.sensor_schema(
            unit_of_measurement="kWh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("energy_returned_tariff2"): sensor.sensor_schema(
            unit_of_measurement="kWh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("total_imported_energy"): sensor.sensor_schema(
            unit_of_measurement="kvarh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("total_exported_energy"): sensor.sensor_schema(
            unit_of_measurement="kvarh",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("power_delivered"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered"): sensor.sensor_schema(
            unit_of_measurement="kvar",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("reactive_power_returned"): sensor.sensor_schema(
            unit_of_measurement="kvar",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("electricity_threshold"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_switch_position"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_failures"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_long_failures"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_sags_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_sags_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("electricity_sags_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_swells_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("electricity_swells_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("electricity_swells_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("current_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_EMPTY,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("current_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_EMPTY,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("current_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_EMPTY,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_delivered_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_delivered_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_delivered_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_returned_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_returned_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_returned_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("voltage_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_EMPTY,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("voltage_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_EMPTY,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("voltage_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_EMPTY,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_NONE,
        ),
        cv.Optional("gas_delivered"): sensor.sensor_schema(
            unit_of_measurement="m³",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("gas_delivered_be"): sensor.sensor_schema(
            unit_of_measurement="m³",
            icon=ICON_EMPTY,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_EMPTY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
    }
).extend(cv.COMPONENT_SCHEMA)



def to_code(config):
    hub = yield cg.get_variable(config[CONF_DSMR_ID])

    sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == sensor.Sensor:
            s = yield sensor.new_sensor(conf)
            cg.add(getattr(hub, f"set_{key}")(s))
            sensors.append(f"F({key})")

    cg.add_define("DSMR_SENSOR_LIST(F, sep)", cg.RawExpression(" sep ".join(sensors)))
