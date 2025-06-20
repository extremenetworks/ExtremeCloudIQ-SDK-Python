# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from extremecloudiq import schemas  # noqa: F401


class XiqPowerSourceEquipment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot LLdp-Cdp Info For Anomalous Access Points
    """


    class MetaOapg:
        
        class properties:
            is_lldp_cdp_enabled = schemas.BoolSchema
            uplink_switch_system_name = schemas.StrSchema
            uplink_switch_system_id = schemas.StrSchema
            location_name = schemas.StrSchema
            floor_name = schemas.StrSchema
            
            
            class affected_downlink_devices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqAffectedDownlinkDevice']:
                        return XiqAffectedDownlinkDevice
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqAffectedDownlinkDevice'], typing.List['XiqAffectedDownlinkDevice']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'affected_downlink_devices':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqAffectedDownlinkDevice':
                    return super().__getitem__(i)
            
            
            class unaffected_downlink_devices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqUnaffectedDownlinkDevice']:
                        return XiqUnaffectedDownlinkDevice
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqUnaffectedDownlinkDevice'], typing.List['XiqUnaffectedDownlinkDevice']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unaffected_downlink_devices':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqUnaffectedDownlinkDevice':
                    return super().__getitem__(i)
            uplink_switch_device_id = schemas.Int64Schema
            __annotations__ = {
                "is_lldp_cdp_enabled": is_lldp_cdp_enabled,
                "uplink_switch_system_name": uplink_switch_system_name,
                "uplink_switch_system_id": uplink_switch_system_id,
                "location_name": location_name,
                "floor_name": floor_name,
                "affected_downlink_devices": affected_downlink_devices,
                "unaffected_downlink_devices": unaffected_downlink_devices,
                "uplink_switch_device_id": uplink_switch_device_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_lldp_cdp_enabled"]) -> MetaOapg.properties.is_lldp_cdp_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uplink_switch_system_name"]) -> MetaOapg.properties.uplink_switch_system_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uplink_switch_system_id"]) -> MetaOapg.properties.uplink_switch_system_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_name"]) -> MetaOapg.properties.location_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floor_name"]) -> MetaOapg.properties.floor_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affected_downlink_devices"]) -> MetaOapg.properties.affected_downlink_devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unaffected_downlink_devices"]) -> MetaOapg.properties.unaffected_downlink_devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uplink_switch_device_id"]) -> MetaOapg.properties.uplink_switch_device_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_lldp_cdp_enabled", "uplink_switch_system_name", "uplink_switch_system_id", "location_name", "floor_name", "affected_downlink_devices", "unaffected_downlink_devices", "uplink_switch_device_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_lldp_cdp_enabled"]) -> typing.Union[MetaOapg.properties.is_lldp_cdp_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uplink_switch_system_name"]) -> typing.Union[MetaOapg.properties.uplink_switch_system_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uplink_switch_system_id"]) -> typing.Union[MetaOapg.properties.uplink_switch_system_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_name"]) -> typing.Union[MetaOapg.properties.location_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floor_name"]) -> typing.Union[MetaOapg.properties.floor_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affected_downlink_devices"]) -> typing.Union[MetaOapg.properties.affected_downlink_devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unaffected_downlink_devices"]) -> typing.Union[MetaOapg.properties.unaffected_downlink_devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uplink_switch_device_id"]) -> typing.Union[MetaOapg.properties.uplink_switch_device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_lldp_cdp_enabled", "uplink_switch_system_name", "uplink_switch_system_id", "location_name", "floor_name", "affected_downlink_devices", "unaffected_downlink_devices", "uplink_switch_device_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_lldp_cdp_enabled: typing.Union[MetaOapg.properties.is_lldp_cdp_enabled, bool, schemas.Unset] = schemas.unset,
        uplink_switch_system_name: typing.Union[MetaOapg.properties.uplink_switch_system_name, str, schemas.Unset] = schemas.unset,
        uplink_switch_system_id: typing.Union[MetaOapg.properties.uplink_switch_system_id, str, schemas.Unset] = schemas.unset,
        location_name: typing.Union[MetaOapg.properties.location_name, str, schemas.Unset] = schemas.unset,
        floor_name: typing.Union[MetaOapg.properties.floor_name, str, schemas.Unset] = schemas.unset,
        affected_downlink_devices: typing.Union[MetaOapg.properties.affected_downlink_devices, list, tuple, schemas.Unset] = schemas.unset,
        unaffected_downlink_devices: typing.Union[MetaOapg.properties.unaffected_downlink_devices, list, tuple, schemas.Unset] = schemas.unset,
        uplink_switch_device_id: typing.Union[MetaOapg.properties.uplink_switch_device_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqPowerSourceEquipment':
        return super().__new__(
            cls,
            *_args,
            is_lldp_cdp_enabled=is_lldp_cdp_enabled,
            uplink_switch_system_name=uplink_switch_system_name,
            uplink_switch_system_id=uplink_switch_system_id,
            location_name=location_name,
            floor_name=floor_name,
            affected_downlink_devices=affected_downlink_devices,
            unaffected_downlink_devices=unaffected_downlink_devices,
            uplink_switch_device_id=uplink_switch_device_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_affected_downlink_device import XiqAffectedDownlinkDevice
from extremecloudiq.model.xiq_unaffected_downlink_device import XiqUnaffectedDownlinkDevice
