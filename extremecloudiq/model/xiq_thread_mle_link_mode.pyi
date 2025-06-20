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


class XiqThreadMleLinkMode(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The thread MLE Link Mode configuration
    """


    class MetaOapg:
        
        class properties:
            rx_on_when_idle = schemas.BoolSchema
            full_thread_device = schemas.BoolSchema
            full_network_data = schemas.BoolSchema
            __annotations__ = {
                "rx_on_when_idle": rx_on_when_idle,
                "full_thread_device": full_thread_device,
                "full_network_data": full_network_data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rx_on_when_idle"]) -> MetaOapg.properties.rx_on_when_idle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_thread_device"]) -> MetaOapg.properties.full_thread_device: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_network_data"]) -> MetaOapg.properties.full_network_data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rx_on_when_idle", "full_thread_device", "full_network_data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rx_on_when_idle"]) -> typing.Union[MetaOapg.properties.rx_on_when_idle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_thread_device"]) -> typing.Union[MetaOapg.properties.full_thread_device, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_network_data"]) -> typing.Union[MetaOapg.properties.full_network_data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rx_on_when_idle", "full_thread_device", "full_network_data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        rx_on_when_idle: typing.Union[MetaOapg.properties.rx_on_when_idle, bool, schemas.Unset] = schemas.unset,
        full_thread_device: typing.Union[MetaOapg.properties.full_thread_device, bool, schemas.Unset] = schemas.unset,
        full_network_data: typing.Union[MetaOapg.properties.full_network_data, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqThreadMleLinkMode':
        return super().__new__(
            cls,
            *_args,
            rx_on_when_idle=rx_on_when_idle,
            full_thread_device=full_thread_device,
            full_network_data=full_network_data,
            _configuration=_configuration,
            **kwargs,
        )
