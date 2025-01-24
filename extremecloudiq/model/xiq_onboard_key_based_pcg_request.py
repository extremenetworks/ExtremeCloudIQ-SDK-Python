# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.1.0.147
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


class XiqOnboardKeyBasedPcgRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload to create Key Based PCG data(from exist network policy and SSID)
    """


    class MetaOapg:
        required = {
            "user_ids",
            "ssid_name",
            "enabled",
        }
        
        class properties:
            ssid_name = schemas.StrSchema
            enabled = schemas.BoolSchema
            
            
            class user_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'user_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "ssid_name": ssid_name,
                "enabled": enabled,
                "user_ids": user_ids,
            }
    
    user_ids: MetaOapg.properties.user_ids
    ssid_name: MetaOapg.properties.ssid_name
    enabled: MetaOapg.properties.enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid_name"]) -> MetaOapg.properties.ssid_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_ids"]) -> MetaOapg.properties.user_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ssid_name", "enabled", "user_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid_name"]) -> MetaOapg.properties.ssid_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_ids"]) -> MetaOapg.properties.user_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ssid_name", "enabled", "user_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_ids: typing.Union[MetaOapg.properties.user_ids, list, tuple, ],
        ssid_name: typing.Union[MetaOapg.properties.ssid_name, str, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqOnboardKeyBasedPcgRequest':
        return super().__new__(
            cls,
            *_args,
            user_ids=user_ids,
            ssid_name=ssid_name,
            enabled=enabled,
            _configuration=_configuration,
            **kwargs,
        )
