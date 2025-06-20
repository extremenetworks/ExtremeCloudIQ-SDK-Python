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


class XiqHardwareHealthStatsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Hardware Health Stats
    """


    class MetaOapg:
        
        class properties:
            
            
            class hd_device_stats_entities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqHardwareHealthDeviceStatsEntity']:
                        return XiqHardwareHealthDeviceStatsEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqHardwareHealthDeviceStatsEntity'], typing.List['XiqHardwareHealthDeviceStatsEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hd_device_stats_entities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqHardwareHealthDeviceStatsEntity':
                    return super().__getitem__(i)
            
            
            class hd_packet_counts_entities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqHardwareHealthPacketCountsEntity']:
                        return XiqHardwareHealthPacketCountsEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqHardwareHealthPacketCountsEntity'], typing.List['XiqHardwareHealthPacketCountsEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hd_packet_counts_entities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqHardwareHealthPacketCountsEntity':
                    return super().__getitem__(i)
            
            
            class hd_reboot_stats_entities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqHardwareHealthRebootStatsEntity']:
                        return XiqHardwareHealthRebootStatsEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqHardwareHealthRebootStatsEntity'], typing.List['XiqHardwareHealthRebootStatsEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hd_reboot_stats_entities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqHardwareHealthRebootStatsEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "hd_device_stats_entities": hd_device_stats_entities,
                "hd_packet_counts_entities": hd_packet_counts_entities,
                "hd_reboot_stats_entities": hd_reboot_stats_entities,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hd_device_stats_entities"]) -> MetaOapg.properties.hd_device_stats_entities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hd_packet_counts_entities"]) -> MetaOapg.properties.hd_packet_counts_entities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hd_reboot_stats_entities"]) -> MetaOapg.properties.hd_reboot_stats_entities: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hd_device_stats_entities", "hd_packet_counts_entities", "hd_reboot_stats_entities", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hd_device_stats_entities"]) -> typing.Union[MetaOapg.properties.hd_device_stats_entities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hd_packet_counts_entities"]) -> typing.Union[MetaOapg.properties.hd_packet_counts_entities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hd_reboot_stats_entities"]) -> typing.Union[MetaOapg.properties.hd_reboot_stats_entities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hd_device_stats_entities", "hd_packet_counts_entities", "hd_reboot_stats_entities", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        hd_device_stats_entities: typing.Union[MetaOapg.properties.hd_device_stats_entities, list, tuple, schemas.Unset] = schemas.unset,
        hd_packet_counts_entities: typing.Union[MetaOapg.properties.hd_packet_counts_entities, list, tuple, schemas.Unset] = schemas.unset,
        hd_reboot_stats_entities: typing.Union[MetaOapg.properties.hd_reboot_stats_entities, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHardwareHealthStatsResponse':
        return super().__new__(
            cls,
            *_args,
            hd_device_stats_entities=hd_device_stats_entities,
            hd_packet_counts_entities=hd_packet_counts_entities,
            hd_reboot_stats_entities=hd_reboot_stats_entities,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_hardware_health_device_stats_entity import XiqHardwareHealthDeviceStatsEntity
from extremecloudiq.model.xiq_hardware_health_packet_counts_entity import XiqHardwareHealthPacketCountsEntity
from extremecloudiq.model.xiq_hardware_health_reboot_stats_entity import XiqHardwareHealthRebootStatsEntity
