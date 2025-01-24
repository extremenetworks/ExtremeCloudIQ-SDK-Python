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


class XiqOperationMetadata(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The metadata of Long Running Operation (LRO)
    """


    class MetaOapg:
        required = {
            "update_time",
            "cancelable",
            "create_time",
            "expires_in",
            "status",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['XiqOperationStatus']:
                return XiqOperationStatus
            cancelable = schemas.BoolSchema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            expires_in = schemas.Int64Schema
            
            
            class percentage(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            step = schemas.StrSchema
            start_time = schemas.DateTimeSchema
            end_time = schemas.DateTimeSchema
            __annotations__ = {
                "status": status,
                "cancelable": cancelable,
                "create_time": create_time,
                "update_time": update_time,
                "expires_in": expires_in,
                "percentage": percentage,
                "step": step,
                "start_time": start_time,
                "end_time": end_time,
            }
    
    update_time: MetaOapg.properties.update_time
    cancelable: MetaOapg.properties.cancelable
    create_time: MetaOapg.properties.create_time
    expires_in: MetaOapg.properties.expires_in
    status: 'XiqOperationStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'XiqOperationStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancelable"]) -> MetaOapg.properties.cancelable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percentage"]) -> MetaOapg.properties.percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["step"]) -> MetaOapg.properties.step: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "cancelable", "create_time", "update_time", "expires_in", "percentage", "step", "start_time", "end_time", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'XiqOperationStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancelable"]) -> MetaOapg.properties.cancelable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percentage"]) -> typing.Union[MetaOapg.properties.percentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["step"]) -> typing.Union[MetaOapg.properties.step, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> typing.Union[MetaOapg.properties.end_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "cancelable", "create_time", "update_time", "expires_in", "percentage", "step", "start_time", "end_time", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        cancelable: typing.Union[MetaOapg.properties.cancelable, bool, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, ],
        status: 'XiqOperationStatus',
        percentage: typing.Union[MetaOapg.properties.percentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        step: typing.Union[MetaOapg.properties.step, str, schemas.Unset] = schemas.unset,
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        end_time: typing.Union[MetaOapg.properties.end_time, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqOperationMetadata':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            cancelable=cancelable,
            create_time=create_time,
            expires_in=expires_in,
            status=status,
            percentage=percentage,
            step=step,
            start_time=start_time,
            end_time=end_time,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_operation_status import XiqOperationStatus
