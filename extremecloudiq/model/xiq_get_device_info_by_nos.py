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


class XiqGetDeviceInfoByNos(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "status_message",
            "status_code",
        }
        
        class properties:
            status_code = schemas.Int32Schema
            status_message = schemas.StrSchema
            body = schemas.StrSchema
            __annotations__ = {
                "status_code": status_code,
                "status_message": status_message,
                "body": body,
            }
    
    status_message: MetaOapg.properties.status_message
    status_code: MetaOapg.properties.status_code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_code"]) -> MetaOapg.properties.status_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_message"]) -> MetaOapg.properties.status_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status_code", "status_message", "body", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_code"]) -> MetaOapg.properties.status_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_message"]) -> MetaOapg.properties.status_message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status_code", "status_message", "body", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        status_message: typing.Union[MetaOapg.properties.status_message, str, ],
        status_code: typing.Union[MetaOapg.properties.status_code, decimal.Decimal, int, ],
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqGetDeviceInfoByNos':
        return super().__new__(
            cls,
            *_args,
            status_message=status_message,
            status_code=status_code,
            body=body,
            _configuration=_configuration,
            **kwargs,
        )
