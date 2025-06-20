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


class XiqAssetDashboard(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The asset diagnostic data for total, offline, wired, and wireless offline devices.
    """


    class MetaOapg:
        
        class properties:
            total_devices = schemas.Int64Schema
            total_offline_devices = schemas.Int64Schema
            wired_offline_devices = schemas.Int64Schema
            wireless_offline_devices = schemas.Int64Schema
            __annotations__ = {
                "total_devices": total_devices,
                "total_offline_devices": total_offline_devices,
                "wired_offline_devices": wired_offline_devices,
                "wireless_offline_devices": wireless_offline_devices,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_devices"]) -> MetaOapg.properties.total_devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_offline_devices"]) -> MetaOapg.properties.total_offline_devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wired_offline_devices"]) -> MetaOapg.properties.wired_offline_devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wireless_offline_devices"]) -> MetaOapg.properties.wireless_offline_devices: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_devices", "total_offline_devices", "wired_offline_devices", "wireless_offline_devices", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_devices"]) -> typing.Union[MetaOapg.properties.total_devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_offline_devices"]) -> typing.Union[MetaOapg.properties.total_offline_devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wired_offline_devices"]) -> typing.Union[MetaOapg.properties.wired_offline_devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wireless_offline_devices"]) -> typing.Union[MetaOapg.properties.wireless_offline_devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_devices", "total_offline_devices", "wired_offline_devices", "wireless_offline_devices", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        total_devices: typing.Union[MetaOapg.properties.total_devices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_offline_devices: typing.Union[MetaOapg.properties.total_offline_devices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wired_offline_devices: typing.Union[MetaOapg.properties.wired_offline_devices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wireless_offline_devices: typing.Union[MetaOapg.properties.wireless_offline_devices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAssetDashboard':
        return super().__new__(
            cls,
            *_args,
            total_devices=total_devices,
            total_offline_devices=total_offline_devices,
            wired_offline_devices=wired_offline_devices,
            wireless_offline_devices=wireless_offline_devices,
            _configuration=_configuration,
            **kwargs,
        )
