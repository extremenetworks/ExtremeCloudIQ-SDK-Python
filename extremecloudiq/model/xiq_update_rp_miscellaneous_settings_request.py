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


class XiqUpdateRpMiscellaneousSettingsRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            sla_throughput_level = schemas.StrSchema
            
            
            class radio_range(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 10000
                    inclusive_minimum = 300
            __annotations__ = {
                "sla_throughput_level": sla_throughput_level,
                "radio_range": radio_range,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sla_throughput_level"]) -> MetaOapg.properties.sla_throughput_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio_range"]) -> MetaOapg.properties.radio_range: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sla_throughput_level", "radio_range", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sla_throughput_level"]) -> typing.Union[MetaOapg.properties.sla_throughput_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio_range"]) -> typing.Union[MetaOapg.properties.radio_range, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sla_throughput_level", "radio_range", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        sla_throughput_level: typing.Union[MetaOapg.properties.sla_throughput_level, str, schemas.Unset] = schemas.unset,
        radio_range: typing.Union[MetaOapg.properties.radio_range, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUpdateRpMiscellaneousSettingsRequest':
        return super().__new__(
            cls,
            *_args,
            sla_throughput_level=sla_throughput_level,
            radio_range=radio_range,
            _configuration=_configuration,
            **kwargs,
        )
