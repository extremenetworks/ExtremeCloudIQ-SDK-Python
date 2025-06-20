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


class XiqMissingVlanInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Missing Vlan Info
    """


    class MetaOapg:
        
        class properties:
            lldp_enabled = schemas.BoolSchema
            upstream_switch_name = schemas.StrSchema
            floor_name = schemas.StrSchema
            
            
            class affected_device_entity(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqMissingVlanAffectedDeviceEntity']:
                        return XiqMissingVlanAffectedDeviceEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqMissingVlanAffectedDeviceEntity'], typing.List['XiqMissingVlanAffectedDeviceEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'affected_device_entity':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqMissingVlanAffectedDeviceEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "lldp_enabled": lldp_enabled,
                "upstream_switch_name": upstream_switch_name,
                "floor_name": floor_name,
                "affected_device_entity": affected_device_entity,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lldp_enabled"]) -> MetaOapg.properties.lldp_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upstream_switch_name"]) -> MetaOapg.properties.upstream_switch_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floor_name"]) -> MetaOapg.properties.floor_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affected_device_entity"]) -> MetaOapg.properties.affected_device_entity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lldp_enabled", "upstream_switch_name", "floor_name", "affected_device_entity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lldp_enabled"]) -> typing.Union[MetaOapg.properties.lldp_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upstream_switch_name"]) -> typing.Union[MetaOapg.properties.upstream_switch_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floor_name"]) -> typing.Union[MetaOapg.properties.floor_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affected_device_entity"]) -> typing.Union[MetaOapg.properties.affected_device_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lldp_enabled", "upstream_switch_name", "floor_name", "affected_device_entity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        lldp_enabled: typing.Union[MetaOapg.properties.lldp_enabled, bool, schemas.Unset] = schemas.unset,
        upstream_switch_name: typing.Union[MetaOapg.properties.upstream_switch_name, str, schemas.Unset] = schemas.unset,
        floor_name: typing.Union[MetaOapg.properties.floor_name, str, schemas.Unset] = schemas.unset,
        affected_device_entity: typing.Union[MetaOapg.properties.affected_device_entity, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqMissingVlanInfo':
        return super().__new__(
            cls,
            *_args,
            lldp_enabled=lldp_enabled,
            upstream_switch_name=upstream_switch_name,
            floor_name=floor_name,
            affected_device_entity=affected_device_entity,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_missing_vlan_affected_device_entity import XiqMissingVlanAffectedDeviceEntity
