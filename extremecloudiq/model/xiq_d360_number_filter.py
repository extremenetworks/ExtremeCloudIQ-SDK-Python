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


class XiqD360NumberFilter(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Number Filter
    """


    class MetaOapg:
        
        class properties:
            column_name = schemas.StrSchema
        
            @staticmethod
            def filter_type() -> typing.Type['XiqD360FilterType']:
                return XiqD360FilterType
            value = schemas.Int64Schema
            min = schemas.Int64Schema
            max = schemas.Int64Schema
            __annotations__ = {
                "column_name": column_name,
                "filter_type": filter_type,
                "value": value,
                "min": min,
                "max": max,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["column_name"]) -> MetaOapg.properties.column_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter_type"]) -> 'XiqD360FilterType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["column_name", "filter_type", "value", "min", "max", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["column_name"]) -> typing.Union[MetaOapg.properties.column_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter_type"]) -> typing.Union['XiqD360FilterType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> typing.Union[MetaOapg.properties.max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["column_name", "filter_type", "value", "min", "max", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        column_name: typing.Union[MetaOapg.properties.column_name, str, schemas.Unset] = schemas.unset,
        filter_type: typing.Union['XiqD360FilterType', schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max: typing.Union[MetaOapg.properties.max, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqD360NumberFilter':
        return super().__new__(
            cls,
            *_args,
            column_name=column_name,
            filter_type=filter_type,
            value=value,
            min=min,
            max=max,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_d360_filter_type import XiqD360FilterType
