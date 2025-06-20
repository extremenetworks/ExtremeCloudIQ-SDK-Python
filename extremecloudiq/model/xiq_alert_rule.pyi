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


class XiqAlertRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The state for a configured alert rule
    """


    class MetaOapg:
        required = {
            "is_enabled",
            "trigger_type",
            "id",
            "severity_id",
            "message_metadata_id",
        }
        
        class properties:
            id = schemas.Int64Schema
            message_metadata_id = schemas.Int64Schema
            severity_id = schemas.Int64Schema
            is_enabled = schemas.BoolSchema
            trigger_type = schemas.StrSchema
            message_metadata_name = schemas.StrSchema
            message_metadata_type = schemas.StrSchema
            description = schemas.StrSchema
            severity_name = schemas.StrSchema
            duration = schemas.Int32Schema
            time_window = schemas.Int32Schema
            count = schemas.Int32Schema
            threshold = schemas.Float64Schema
            unit = schemas.StrSchema
            operator = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "message_metadata_id": message_metadata_id,
                "severity_id": severity_id,
                "is_enabled": is_enabled,
                "trigger_type": trigger_type,
                "message_metadata_name": message_metadata_name,
                "message_metadata_type": message_metadata_type,
                "description": description,
                "severity_name": severity_name,
                "duration": duration,
                "time_window": time_window,
                "count": count,
                "threshold": threshold,
                "unit": unit,
                "operator": operator,
            }
    
    is_enabled: MetaOapg.properties.is_enabled
    trigger_type: MetaOapg.properties.trigger_type
    id: MetaOapg.properties.id
    severity_id: MetaOapg.properties.severity_id
    message_metadata_id: MetaOapg.properties.message_metadata_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_metadata_id"]) -> MetaOapg.properties.message_metadata_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity_id"]) -> MetaOapg.properties.severity_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger_type"]) -> MetaOapg.properties.trigger_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_metadata_name"]) -> MetaOapg.properties.message_metadata_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_metadata_type"]) -> MetaOapg.properties.message_metadata_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity_name"]) -> MetaOapg.properties.severity_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_window"]) -> MetaOapg.properties.time_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["threshold"]) -> MetaOapg.properties.threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "message_metadata_id", "severity_id", "is_enabled", "trigger_type", "message_metadata_name", "message_metadata_type", "description", "severity_name", "duration", "time_window", "count", "threshold", "unit", "operator", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_metadata_id"]) -> MetaOapg.properties.message_metadata_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity_id"]) -> MetaOapg.properties.severity_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger_type"]) -> MetaOapg.properties.trigger_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_metadata_name"]) -> typing.Union[MetaOapg.properties.message_metadata_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_metadata_type"]) -> typing.Union[MetaOapg.properties.message_metadata_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity_name"]) -> typing.Union[MetaOapg.properties.severity_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_window"]) -> typing.Union[MetaOapg.properties.time_window, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["threshold"]) -> typing.Union[MetaOapg.properties.threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> typing.Union[MetaOapg.properties.unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "message_metadata_id", "severity_id", "is_enabled", "trigger_type", "message_metadata_name", "message_metadata_type", "description", "severity_name", "duration", "time_window", "count", "threshold", "unit", "operator", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, ],
        trigger_type: typing.Union[MetaOapg.properties.trigger_type, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        severity_id: typing.Union[MetaOapg.properties.severity_id, decimal.Decimal, int, ],
        message_metadata_id: typing.Union[MetaOapg.properties.message_metadata_id, decimal.Decimal, int, ],
        message_metadata_name: typing.Union[MetaOapg.properties.message_metadata_name, str, schemas.Unset] = schemas.unset,
        message_metadata_type: typing.Union[MetaOapg.properties.message_metadata_type, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        severity_name: typing.Union[MetaOapg.properties.severity_name, str, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        time_window: typing.Union[MetaOapg.properties.time_window, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        threshold: typing.Union[MetaOapg.properties.threshold, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        unit: typing.Union[MetaOapg.properties.unit, str, schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAlertRule':
        return super().__new__(
            cls,
            *_args,
            is_enabled=is_enabled,
            trigger_type=trigger_type,
            id=id,
            severity_id=severity_id,
            message_metadata_id=message_metadata_id,
            message_metadata_name=message_metadata_name,
            message_metadata_type=message_metadata_type,
            description=description,
            severity_name=severity_name,
            duration=duration,
            time_window=time_window,
            count=count,
            threshold=threshold,
            unit=unit,
            operator=operator,
            _configuration=_configuration,
            **kwargs,
        )
