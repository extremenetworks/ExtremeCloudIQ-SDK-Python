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


class XiqValidTimePeriodAfterIdCreation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The settings for the valid time period after ID Creation option or null for the other option
    """


    class MetaOapg:
        required = {
            "valid_time_period",
            "valid_time_period_unit",
        }
        
        class properties:
            valid_time_period = schemas.Int32Schema
        
            @staticmethod
            def valid_time_period_unit() -> typing.Type['XiqDateTimeUnitType']:
                return XiqDateTimeUnitType
            __annotations__ = {
                "valid_time_period": valid_time_period,
                "valid_time_period_unit": valid_time_period_unit,
            }
    
    valid_time_period: MetaOapg.properties.valid_time_period
    valid_time_period_unit: 'XiqDateTimeUnitType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valid_time_period"]) -> MetaOapg.properties.valid_time_period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valid_time_period_unit"]) -> 'XiqDateTimeUnitType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["valid_time_period", "valid_time_period_unit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valid_time_period"]) -> MetaOapg.properties.valid_time_period: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valid_time_period_unit"]) -> 'XiqDateTimeUnitType': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["valid_time_period", "valid_time_period_unit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        valid_time_period: typing.Union[MetaOapg.properties.valid_time_period, decimal.Decimal, int, ],
        valid_time_period_unit: 'XiqDateTimeUnitType',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqValidTimePeriodAfterIdCreation':
        return super().__new__(
            cls,
            *_args,
            valid_time_period=valid_time_period,
            valid_time_period_unit=valid_time_period_unit,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_date_time_unit_type import XiqDateTimeUnitType
