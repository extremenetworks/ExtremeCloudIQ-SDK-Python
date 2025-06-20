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


class XiqViqTaskProgress(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            task_name = schemas.StrSchema
            finish_percentage = schemas.Int64Schema
            detail = schemas.StrSchema
            status = schemas.StrSchema
            __annotations__ = {
                "task_name": task_name,
                "finish_percentage": finish_percentage,
                "detail": detail,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task_name"]) -> MetaOapg.properties.task_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finish_percentage"]) -> MetaOapg.properties.finish_percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["task_name", "finish_percentage", "detail", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task_name"]) -> typing.Union[MetaOapg.properties.task_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finish_percentage"]) -> typing.Union[MetaOapg.properties.finish_percentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> typing.Union[MetaOapg.properties.detail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["task_name", "finish_percentage", "detail", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        task_name: typing.Union[MetaOapg.properties.task_name, str, schemas.Unset] = schemas.unset,
        finish_percentage: typing.Union[MetaOapg.properties.finish_percentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        detail: typing.Union[MetaOapg.properties.detail, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqViqTaskProgress':
        return super().__new__(
            cls,
            *_args,
            task_name=task_name,
            finish_percentage=finish_percentage,
            detail=detail,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
