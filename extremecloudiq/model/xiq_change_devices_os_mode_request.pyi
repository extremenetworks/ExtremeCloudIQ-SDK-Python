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


class XiqChangeDevicesOsModeRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The request for change the device(s) OS mode.
    """


    class MetaOapg:
        required = {
            "target_os",
            "device_ids",
        }
        
        class properties:
            
            
            class device_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'device_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            target_os = schemas.StrSchema
            __annotations__ = {
                "device_ids": device_ids,
                "target_os": target_os,
            }
    
    target_os: MetaOapg.properties.target_os
    device_ids: MetaOapg.properties.device_ids
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_ids"]) -> MetaOapg.properties.device_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_os"]) -> MetaOapg.properties.target_os: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_ids", "target_os", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_ids"]) -> MetaOapg.properties.device_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_os"]) -> MetaOapg.properties.target_os: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_ids", "target_os", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        target_os: typing.Union[MetaOapg.properties.target_os, str, ],
        device_ids: typing.Union[MetaOapg.properties.device_ids, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqChangeDevicesOsModeRequest':
        return super().__new__(
            cls,
            *_args,
            target_os=target_os,
            device_ids=device_ids,
            _configuration=_configuration,
            **kwargs,
        )
