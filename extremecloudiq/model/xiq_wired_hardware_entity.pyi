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


class XiqWiredHardwareEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ Connectivity Experience data
    """


    class MetaOapg:
        required = {
            "timestamp",
        }
        
        class properties:
            timestamp = schemas.Int64Schema
            quality_index = schemas.Int32Schema
            total_switches = schemas.Int32Schema
            affected_ratio = schemas.Int32Schema
            affected = schemas.Float64Schema
            __annotations__ = {
                "timestamp": timestamp,
                "quality_index": quality_index,
                "total_switches": total_switches,
                "affected_ratio": affected_ratio,
                "affected": affected,
            }
    
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quality_index"]) -> MetaOapg.properties.quality_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_switches"]) -> MetaOapg.properties.total_switches: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affected_ratio"]) -> MetaOapg.properties.affected_ratio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affected"]) -> MetaOapg.properties.affected: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "quality_index", "total_switches", "affected_ratio", "affected", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quality_index"]) -> typing.Union[MetaOapg.properties.quality_index, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_switches"]) -> typing.Union[MetaOapg.properties.total_switches, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affected_ratio"]) -> typing.Union[MetaOapg.properties.affected_ratio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affected"]) -> typing.Union[MetaOapg.properties.affected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "quality_index", "total_switches", "affected_ratio", "affected", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, ],
        quality_index: typing.Union[MetaOapg.properties.quality_index, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_switches: typing.Union[MetaOapg.properties.total_switches, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        affected_ratio: typing.Union[MetaOapg.properties.affected_ratio, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        affected: typing.Union[MetaOapg.properties.affected, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWiredHardwareEntity':
        return super().__new__(
            cls,
            *_args,
            timestamp=timestamp,
            quality_index=quality_index,
            total_switches=total_switches,
            affected_ratio=affected_ratio,
            affected=affected,
            _configuration=_configuration,
            **kwargs,
        )
