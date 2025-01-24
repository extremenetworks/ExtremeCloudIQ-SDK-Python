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


class WifiHealth(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            overall_score = schemas.Int32Schema
            snr_score = schemas.Int32Schema
            channel_utilization_score = schemas.Int32Schema
            association_per_radio_score = schemas.Int32Schema
            __annotations__ = {
                "overall_score": overall_score,
                "snr_score": snr_score,
                "channel_utilization_score": channel_utilization_score,
                "association_per_radio_score": association_per_radio_score,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overall_score"]) -> MetaOapg.properties.overall_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snr_score"]) -> MetaOapg.properties.snr_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_utilization_score"]) -> MetaOapg.properties.channel_utilization_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["association_per_radio_score"]) -> MetaOapg.properties.association_per_radio_score: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["overall_score", "snr_score", "channel_utilization_score", "association_per_radio_score", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overall_score"]) -> typing.Union[MetaOapg.properties.overall_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snr_score"]) -> typing.Union[MetaOapg.properties.snr_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_utilization_score"]) -> typing.Union[MetaOapg.properties.channel_utilization_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["association_per_radio_score"]) -> typing.Union[MetaOapg.properties.association_per_radio_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["overall_score", "snr_score", "channel_utilization_score", "association_per_radio_score", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        overall_score: typing.Union[MetaOapg.properties.overall_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        snr_score: typing.Union[MetaOapg.properties.snr_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        channel_utilization_score: typing.Union[MetaOapg.properties.channel_utilization_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        association_per_radio_score: typing.Union[MetaOapg.properties.association_per_radio_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WifiHealth':
        return super().__new__(
            cls,
            *_args,
            overall_score=overall_score,
            snr_score=snr_score,
            channel_utilization_score=channel_utilization_score,
            association_per_radio_score=association_per_radio_score,
            _configuration=_configuration,
            **kwargs,
        )
