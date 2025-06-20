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


class XiqAfcStatusSummary(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            total_available = schemas.Int32Schema
            total_pending = schemas.Int32Schema
            total_grace_period = schemas.Int32Schema
            __annotations__ = {
                "total_available": total_available,
                "total_pending": total_pending,
                "total_grace_period": total_grace_period,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_available"]) -> MetaOapg.properties.total_available: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pending"]) -> MetaOapg.properties.total_pending: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_grace_period"]) -> MetaOapg.properties.total_grace_period: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_available", "total_pending", "total_grace_period", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_available"]) -> typing.Union[MetaOapg.properties.total_available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pending"]) -> typing.Union[MetaOapg.properties.total_pending, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_grace_period"]) -> typing.Union[MetaOapg.properties.total_grace_period, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_available", "total_pending", "total_grace_period", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        total_available: typing.Union[MetaOapg.properties.total_available, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_pending: typing.Union[MetaOapg.properties.total_pending, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_grace_period: typing.Union[MetaOapg.properties.total_grace_period, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAfcStatusSummary':
        return super().__new__(
            cls,
            *_args,
            total_available=total_available,
            total_pending=total_pending,
            total_grace_period=total_grace_period,
            _configuration=_configuration,
            **kwargs,
        )
