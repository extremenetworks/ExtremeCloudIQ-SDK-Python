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


class XiqSendCliRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The request for sending CLIs to devices
    """


    class MetaOapg:
        required = {
            "devices",
            "clis",
        }
        
        class properties:
        
            @staticmethod
            def devices() -> typing.Type['XiqDeviceFilter']:
                return XiqDeviceFilter
            
            
            class clis(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clis':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "devices": devices,
                "clis": clis,
            }
    
    devices: 'XiqDeviceFilter'
    clis: MetaOapg.properties.clis
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devices"]) -> 'XiqDeviceFilter': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clis"]) -> MetaOapg.properties.clis: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["devices", "clis", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devices"]) -> 'XiqDeviceFilter': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clis"]) -> MetaOapg.properties.clis: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["devices", "clis", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        devices: 'XiqDeviceFilter',
        clis: typing.Union[MetaOapg.properties.clis, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqSendCliRequest':
        return super().__new__(
            cls,
            *_args,
            devices=devices,
            clis=clis,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_device_filter import XiqDeviceFilter
