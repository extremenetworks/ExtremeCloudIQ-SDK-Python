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


class XiqAnomalyDeviceEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Anomaly Device data
    """


    class MetaOapg:
        
        class properties:
            device_id = schemas.Int64Schema
            device_name = schemas.StrSchema
            pinned = schemas.BoolSchema
            wired = schemas.BoolSchema
            anomaly_id = schemas.StrSchema
        
            @staticmethod
            def severity() -> typing.Type['XiqAnomalySeverity']:
                return XiqAnomalySeverity
            summary = schemas.StrSchema
            last_detected_time = schemas.Int64Schema
            recommended_action = schemas.StrSchema
            anomaly_subtypes = schemas.StrSchema
            interface_name = schemas.StrSchema
            channel_mode = schemas.StrSchema
            channel = schemas.Int32Schema
            frequency = schemas.StrSchema
            location_id = schemas.Int64Schema
            __annotations__ = {
                "device_id": device_id,
                "device_name": device_name,
                "pinned": pinned,
                "wired": wired,
                "anomaly_id": anomaly_id,
                "severity": severity,
                "summary": summary,
                "last_detected_time": last_detected_time,
                "recommended_action": recommended_action,
                "anomaly_subtypes": anomaly_subtypes,
                "interface_name": interface_name,
                "channel_mode": channel_mode,
                "channel": channel,
                "frequency": frequency,
                "location_id": location_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pinned"]) -> MetaOapg.properties.pinned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wired"]) -> MetaOapg.properties.wired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomaly_id"]) -> MetaOapg.properties.anomaly_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity"]) -> 'XiqAnomalySeverity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_detected_time"]) -> MetaOapg.properties.last_detected_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommended_action"]) -> MetaOapg.properties.recommended_action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomaly_subtypes"]) -> MetaOapg.properties.anomaly_subtypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interface_name"]) -> MetaOapg.properties.interface_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_mode"]) -> MetaOapg.properties.channel_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "device_name", "pinned", "wired", "anomaly_id", "severity", "summary", "last_detected_time", "recommended_action", "anomaly_subtypes", "interface_name", "channel_mode", "channel", "frequency", "location_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> typing.Union[MetaOapg.properties.device_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pinned"]) -> typing.Union[MetaOapg.properties.pinned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wired"]) -> typing.Union[MetaOapg.properties.wired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomaly_id"]) -> typing.Union[MetaOapg.properties.anomaly_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union['XiqAnomalySeverity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_detected_time"]) -> typing.Union[MetaOapg.properties.last_detected_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommended_action"]) -> typing.Union[MetaOapg.properties.recommended_action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomaly_subtypes"]) -> typing.Union[MetaOapg.properties.anomaly_subtypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interface_name"]) -> typing.Union[MetaOapg.properties.interface_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_mode"]) -> typing.Union[MetaOapg.properties.channel_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "device_name", "pinned", "wired", "anomaly_id", "severity", "summary", "last_detected_time", "recommended_action", "anomaly_subtypes", "interface_name", "channel_mode", "channel", "frequency", "location_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        device_id: typing.Union[MetaOapg.properties.device_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        device_name: typing.Union[MetaOapg.properties.device_name, str, schemas.Unset] = schemas.unset,
        pinned: typing.Union[MetaOapg.properties.pinned, bool, schemas.Unset] = schemas.unset,
        wired: typing.Union[MetaOapg.properties.wired, bool, schemas.Unset] = schemas.unset,
        anomaly_id: typing.Union[MetaOapg.properties.anomaly_id, str, schemas.Unset] = schemas.unset,
        severity: typing.Union['XiqAnomalySeverity', schemas.Unset] = schemas.unset,
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        last_detected_time: typing.Union[MetaOapg.properties.last_detected_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        recommended_action: typing.Union[MetaOapg.properties.recommended_action, str, schemas.Unset] = schemas.unset,
        anomaly_subtypes: typing.Union[MetaOapg.properties.anomaly_subtypes, str, schemas.Unset] = schemas.unset,
        interface_name: typing.Union[MetaOapg.properties.interface_name, str, schemas.Unset] = schemas.unset,
        channel_mode: typing.Union[MetaOapg.properties.channel_mode, str, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, str, schemas.Unset] = schemas.unset,
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAnomalyDeviceEntity':
        return super().__new__(
            cls,
            *_args,
            device_id=device_id,
            device_name=device_name,
            pinned=pinned,
            wired=wired,
            anomaly_id=anomaly_id,
            severity=severity,
            summary=summary,
            last_detected_time=last_detected_time,
            recommended_action=recommended_action,
            anomaly_subtypes=anomaly_subtypes,
            interface_name=interface_name,
            channel_mode=channel_mode,
            channel=channel,
            frequency=frequency,
            location_id=location_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_anomaly_severity import XiqAnomalySeverity
