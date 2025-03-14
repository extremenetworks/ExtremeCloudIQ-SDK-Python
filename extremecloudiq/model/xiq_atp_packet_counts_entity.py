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


class XiqAtpPacketCountsEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ Data Point
    """


    class MetaOapg:
        required = {
            "timestamp",
        }
        
        class properties:
            timestamp = schemas.Int64Schema
            unicast_tx = schemas.NumberSchema
            unicast_rx = schemas.NumberSchema
            multicast_tx = schemas.NumberSchema
            multicast_rx = schemas.NumberSchema
            broadcast_tx = schemas.NumberSchema
            broadcast_rx = schemas.NumberSchema
            __annotations__ = {
                "timestamp": timestamp,
                "unicast_tx": unicast_tx,
                "unicast_rx": unicast_rx,
                "multicast_tx": multicast_tx,
                "multicast_rx": multicast_rx,
                "broadcast_tx": broadcast_tx,
                "broadcast_rx": broadcast_rx,
            }
    
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unicast_tx"]) -> MetaOapg.properties.unicast_tx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unicast_rx"]) -> MetaOapg.properties.unicast_rx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multicast_tx"]) -> MetaOapg.properties.multicast_tx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multicast_rx"]) -> MetaOapg.properties.multicast_rx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["broadcast_tx"]) -> MetaOapg.properties.broadcast_tx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["broadcast_rx"]) -> MetaOapg.properties.broadcast_rx: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "unicast_tx", "unicast_rx", "multicast_tx", "multicast_rx", "broadcast_tx", "broadcast_rx", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unicast_tx"]) -> typing.Union[MetaOapg.properties.unicast_tx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unicast_rx"]) -> typing.Union[MetaOapg.properties.unicast_rx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multicast_tx"]) -> typing.Union[MetaOapg.properties.multicast_tx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multicast_rx"]) -> typing.Union[MetaOapg.properties.multicast_rx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["broadcast_tx"]) -> typing.Union[MetaOapg.properties.broadcast_tx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["broadcast_rx"]) -> typing.Union[MetaOapg.properties.broadcast_rx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "unicast_tx", "unicast_rx", "multicast_tx", "multicast_rx", "broadcast_tx", "broadcast_rx", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, ],
        unicast_tx: typing.Union[MetaOapg.properties.unicast_tx, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        unicast_rx: typing.Union[MetaOapg.properties.unicast_rx, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        multicast_tx: typing.Union[MetaOapg.properties.multicast_tx, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        multicast_rx: typing.Union[MetaOapg.properties.multicast_rx, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        broadcast_tx: typing.Union[MetaOapg.properties.broadcast_tx, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        broadcast_rx: typing.Union[MetaOapg.properties.broadcast_rx, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAtpPacketCountsEntity':
        return super().__new__(
            cls,
            *_args,
            timestamp=timestamp,
            unicast_tx=unicast_tx,
            unicast_rx=unicast_rx,
            multicast_tx=multicast_tx,
            multicast_rx=multicast_rx,
            broadcast_tx=broadcast_tx,
            broadcast_rx=broadcast_rx,
            _configuration=_configuration,
            **kwargs,
        )
