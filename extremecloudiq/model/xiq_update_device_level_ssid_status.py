# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.2.0.123
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


class XiqUpdateDeviceLevelSsidStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The request for disable/enable device level ssid.
    """


    class MetaOapg:
        required = {
            "if_names",
            "ssid_ids",
            "enabled",
        }
        
        class properties:
            
            
            class ssid_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssid_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class if_names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqWirelessIfName']:
                        return XiqWirelessIfName
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqWirelessIfName'], typing.List['XiqWirelessIfName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'if_names':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqWirelessIfName':
                    return super().__getitem__(i)
            enabled = schemas.BoolSchema
            __annotations__ = {
                "ssid_ids": ssid_ids,
                "if_names": if_names,
                "enabled": enabled,
            }
    
    if_names: MetaOapg.properties.if_names
    ssid_ids: MetaOapg.properties.ssid_ids
    enabled: MetaOapg.properties.enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid_ids"]) -> MetaOapg.properties.ssid_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["if_names"]) -> MetaOapg.properties.if_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ssid_ids", "if_names", "enabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid_ids"]) -> MetaOapg.properties.ssid_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["if_names"]) -> MetaOapg.properties.if_names: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ssid_ids", "if_names", "enabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        if_names: typing.Union[MetaOapg.properties.if_names, list, tuple, ],
        ssid_ids: typing.Union[MetaOapg.properties.ssid_ids, list, tuple, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUpdateDeviceLevelSsidStatus':
        return super().__new__(
            cls,
            *_args,
            if_names=if_names,
            ssid_ids=ssid_ids,
            enabled=enabled,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_wireless_if_name import XiqWirelessIfName
