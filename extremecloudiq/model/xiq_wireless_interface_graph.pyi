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


class XiqWirelessInterfaceGraph(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            timestamp = schemas.Int64Schema
            channel_utilization = schemas.Int64Schema
            connected_clients = schemas.Int64Schema
            __annotations__ = {
                "timestamp": timestamp,
                "channel_utilization": channel_utilization,
                "connected_clients": connected_clients,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_utilization"]) -> MetaOapg.properties.channel_utilization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connected_clients"]) -> MetaOapg.properties.connected_clients: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "channel_utilization", "connected_clients", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_utilization"]) -> typing.Union[MetaOapg.properties.channel_utilization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connected_clients"]) -> typing.Union[MetaOapg.properties.connected_clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "channel_utilization", "connected_clients", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        channel_utilization: typing.Union[MetaOapg.properties.channel_utilization, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        connected_clients: typing.Union[MetaOapg.properties.connected_clients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWirelessInterfaceGraph':
        return super().__new__(
            cls,
            *_args,
            timestamp=timestamp,
            channel_utilization=channel_utilization,
            connected_clients=connected_clients,
            _configuration=_configuration,
            **kwargs,
        )
