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


class XiqIotpTgWhiteListEntry(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "pskd",
            "long_eui",
        }
        
        class properties:
            
            
            class long_eui(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^([*]|[0-9a-fA-F]{16})$',  # noqa: E501
                    }]
            
            
            class pskd(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
                    min_length = 6
                    regex=[{
                        'pattern': r'^[0-9ABCDEFGHJKLMNPRSTUVWXY]+$',  # noqa: E501
                    }]
            __annotations__ = {
                "long_eui": long_eui,
                "pskd": pskd,
            }
    
    pskd: MetaOapg.properties.pskd
    long_eui: MetaOapg.properties.long_eui
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["long_eui"]) -> MetaOapg.properties.long_eui: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pskd"]) -> MetaOapg.properties.pskd: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["long_eui", "pskd", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["long_eui"]) -> MetaOapg.properties.long_eui: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pskd"]) -> MetaOapg.properties.pskd: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["long_eui", "pskd", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pskd: typing.Union[MetaOapg.properties.pskd, str, ],
        long_eui: typing.Union[MetaOapg.properties.long_eui, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqIotpTgWhiteListEntry':
        return super().__new__(
            cls,
            *_args,
            pskd=pskd,
            long_eui=long_eui,
            _configuration=_configuration,
            **kwargs,
        )
