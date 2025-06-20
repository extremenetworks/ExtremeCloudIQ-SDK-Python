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


class XiqWiredDeviceHealthFanStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The fan status
    """


    class MetaOapg:
        
        class properties:
            fan_description = schemas.StrSchema
            fan_status = schemas.StrSchema
            __annotations__ = {
                "fan_description": fan_description,
                "fan_status": fan_status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fan_description"]) -> MetaOapg.properties.fan_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fan_status"]) -> MetaOapg.properties.fan_status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fan_description", "fan_status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fan_description"]) -> typing.Union[MetaOapg.properties.fan_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fan_status"]) -> typing.Union[MetaOapg.properties.fan_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fan_description", "fan_status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        fan_description: typing.Union[MetaOapg.properties.fan_description, str, schemas.Unset] = schemas.unset,
        fan_status: typing.Union[MetaOapg.properties.fan_status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWiredDeviceHealthFanStatus':
        return super().__new__(
            cls,
            *_args,
            fan_description=fan_description,
            fan_status=fan_status,
            _configuration=_configuration,
            **kwargs,
        )
