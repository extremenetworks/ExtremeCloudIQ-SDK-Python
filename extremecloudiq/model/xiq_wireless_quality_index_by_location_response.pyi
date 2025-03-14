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


class XiqWirelessQualityIndexByLocationResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Wireless Quality Index By Location Response
    """


    class MetaOapg:
        
        class properties:
            time_to_connect_score = schemas.Int32Schema
            quality_index = schemas.Int32Schema
            performance_score = schemas.Int32Schema
            total_clients = schemas.Int32Schema
            __annotations__ = {
                "time_to_connect_score": time_to_connect_score,
                "quality_index": quality_index,
                "performance_score": performance_score,
                "total_clients": total_clients,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_to_connect_score"]) -> MetaOapg.properties.time_to_connect_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quality_index"]) -> MetaOapg.properties.quality_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["performance_score"]) -> MetaOapg.properties.performance_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_clients"]) -> MetaOapg.properties.total_clients: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["time_to_connect_score", "quality_index", "performance_score", "total_clients", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_to_connect_score"]) -> typing.Union[MetaOapg.properties.time_to_connect_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quality_index"]) -> typing.Union[MetaOapg.properties.quality_index, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["performance_score"]) -> typing.Union[MetaOapg.properties.performance_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_clients"]) -> typing.Union[MetaOapg.properties.total_clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["time_to_connect_score", "quality_index", "performance_score", "total_clients", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        time_to_connect_score: typing.Union[MetaOapg.properties.time_to_connect_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        quality_index: typing.Union[MetaOapg.properties.quality_index, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        performance_score: typing.Union[MetaOapg.properties.performance_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_clients: typing.Union[MetaOapg.properties.total_clients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWirelessQualityIndexByLocationResponse':
        return super().__new__(
            cls,
            *_args,
            time_to_connect_score=time_to_connect_score,
            quality_index=quality_index,
            performance_score=performance_score,
            total_clients=total_clients,
            _configuration=_configuration,
            **kwargs,
        )
