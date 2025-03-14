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


class XiqHttpServer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The BLE Scan destination HTTP server URL.
    """


    class MetaOapg:
        
        class properties:
            
            
            class url(
                schemas.StrSchema
            ):
                pass
            
            
            class interval(
                schemas.Int32Schema
            ):
                pass
            enable_deduplication = schemas.BoolSchema
            __annotations__ = {
                "url": url,
                "interval": interval,
                "enable_deduplication": enable_deduplication,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_deduplication"]) -> MetaOapg.properties.enable_deduplication: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "interval", "enable_deduplication", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> typing.Union[MetaOapg.properties.interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_deduplication"]) -> typing.Union[MetaOapg.properties.enable_deduplication, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "interval", "enable_deduplication", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        interval: typing.Union[MetaOapg.properties.interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_deduplication: typing.Union[MetaOapg.properties.enable_deduplication, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHttpServer':
        return super().__new__(
            cls,
            *_args,
            url=url,
            interval=interval,
            enable_deduplication=enable_deduplication,
            _configuration=_configuration,
            **kwargs,
        )
