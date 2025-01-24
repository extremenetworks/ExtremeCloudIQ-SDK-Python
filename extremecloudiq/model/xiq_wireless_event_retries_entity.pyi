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


class XiqWirelessEventRetriesEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ Connectivity Experience Wireless Events Retries Details
    """


    class MetaOapg:
        
        class properties:
            avg_rx_retry = schemas.Float64Schema
            max_rx_retry = schemas.Float64Schema
            avg_tx_retry = schemas.Float64Schema
            max_tx_retry = schemas.Float64Schema
            rx_retry_threshold = schemas.Float64Schema
            tx_retry_threshold = schemas.Float64Schema
            __annotations__ = {
                "avg_rx_retry": avg_rx_retry,
                "max_rx_retry": max_rx_retry,
                "avg_tx_retry": avg_tx_retry,
                "max_tx_retry": max_tx_retry,
                "rx_retry_threshold": rx_retry_threshold,
                "tx_retry_threshold": tx_retry_threshold,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avg_rx_retry"]) -> MetaOapg.properties.avg_rx_retry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_rx_retry"]) -> MetaOapg.properties.max_rx_retry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avg_tx_retry"]) -> MetaOapg.properties.avg_tx_retry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_tx_retry"]) -> MetaOapg.properties.max_tx_retry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rx_retry_threshold"]) -> MetaOapg.properties.rx_retry_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tx_retry_threshold"]) -> MetaOapg.properties.tx_retry_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["avg_rx_retry", "max_rx_retry", "avg_tx_retry", "max_tx_retry", "rx_retry_threshold", "tx_retry_threshold", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avg_rx_retry"]) -> typing.Union[MetaOapg.properties.avg_rx_retry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_rx_retry"]) -> typing.Union[MetaOapg.properties.max_rx_retry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avg_tx_retry"]) -> typing.Union[MetaOapg.properties.avg_tx_retry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_tx_retry"]) -> typing.Union[MetaOapg.properties.max_tx_retry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rx_retry_threshold"]) -> typing.Union[MetaOapg.properties.rx_retry_threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tx_retry_threshold"]) -> typing.Union[MetaOapg.properties.tx_retry_threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avg_rx_retry", "max_rx_retry", "avg_tx_retry", "max_tx_retry", "rx_retry_threshold", "tx_retry_threshold", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        avg_rx_retry: typing.Union[MetaOapg.properties.avg_rx_retry, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        max_rx_retry: typing.Union[MetaOapg.properties.max_rx_retry, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        avg_tx_retry: typing.Union[MetaOapg.properties.avg_tx_retry, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        max_tx_retry: typing.Union[MetaOapg.properties.max_tx_retry, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        rx_retry_threshold: typing.Union[MetaOapg.properties.rx_retry_threshold, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tx_retry_threshold: typing.Union[MetaOapg.properties.tx_retry_threshold, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWirelessEventRetriesEntity':
        return super().__new__(
            cls,
            *_args,
            avg_rx_retry=avg_rx_retry,
            max_rx_retry=max_rx_retry,
            avg_tx_retry=avg_tx_retry,
            max_tx_retry=max_tx_retry,
            rx_retry_threshold=rx_retry_threshold,
            tx_retry_threshold=tx_retry_threshold,
            _configuration=_configuration,
            **kwargs,
        )
