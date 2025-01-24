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


class XiqDuplexDataRateEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ Duplex DataRate
    """


    class MetaOapg:
        required = {
            "timestamp",
        }
        
        class properties:
            timestamp = schemas.Int64Schema
            duplex_mode = schemas.Int32Schema
            datarate_mode = schemas.Int32Schema
            __annotations__ = {
                "timestamp": timestamp,
                "duplex_mode": duplex_mode,
                "datarate_mode": datarate_mode,
            }
    
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duplex_mode"]) -> MetaOapg.properties.duplex_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datarate_mode"]) -> MetaOapg.properties.datarate_mode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "duplex_mode", "datarate_mode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duplex_mode"]) -> typing.Union[MetaOapg.properties.duplex_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datarate_mode"]) -> typing.Union[MetaOapg.properties.datarate_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "duplex_mode", "datarate_mode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, ],
        duplex_mode: typing.Union[MetaOapg.properties.duplex_mode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        datarate_mode: typing.Union[MetaOapg.properties.datarate_mode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDuplexDataRateEntity':
        return super().__new__(
            cls,
            *_args,
            timestamp=timestamp,
            duplex_mode=duplex_mode,
            datarate_mode=datarate_mode,
            _configuration=_configuration,
            **kwargs,
        )
