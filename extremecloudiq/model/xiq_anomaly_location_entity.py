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


class XiqAnomalyLocationEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Anomaly Locations data
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def location_type() -> typing.Type['XiqLocationType']:
                return XiqLocationType
            
            
            class location_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'location_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            building_id = schemas.Int64Schema
            location_name = schemas.StrSchema
            pinned = schemas.BoolSchema
            muted = schemas.BoolSchema
        
            @staticmethod
            def severity() -> typing.Type['XiqAnomalySeverity']:
                return XiqAnomalySeverity
            severity_id = schemas.Int32Schema
            summary = schemas.StrSchema
            affected_device_count = schemas.Int32Schema
            last_detected_time = schemas.Int64Schema
        
            @staticmethod
            def anomaly_type() -> typing.Type['XiqAnomalyType']:
                return XiqAnomalyType
            __annotations__ = {
                "location_type": location_type,
                "location_ids": location_ids,
                "building_id": building_id,
                "location_name": location_name,
                "pinned": pinned,
                "muted": muted,
                "severity": severity,
                "severity_id": severity_id,
                "summary": summary,
                "affected_device_count": affected_device_count,
                "last_detected_time": last_detected_time,
                "anomaly_type": anomaly_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_type"]) -> 'XiqLocationType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_ids"]) -> MetaOapg.properties.location_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["building_id"]) -> MetaOapg.properties.building_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_name"]) -> MetaOapg.properties.location_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pinned"]) -> MetaOapg.properties.pinned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["muted"]) -> MetaOapg.properties.muted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity"]) -> 'XiqAnomalySeverity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity_id"]) -> MetaOapg.properties.severity_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affected_device_count"]) -> MetaOapg.properties.affected_device_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_detected_time"]) -> MetaOapg.properties.last_detected_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomaly_type"]) -> 'XiqAnomalyType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["location_type", "location_ids", "building_id", "location_name", "pinned", "muted", "severity", "severity_id", "summary", "affected_device_count", "last_detected_time", "anomaly_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_type"]) -> typing.Union['XiqLocationType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_ids"]) -> typing.Union[MetaOapg.properties.location_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["building_id"]) -> typing.Union[MetaOapg.properties.building_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_name"]) -> typing.Union[MetaOapg.properties.location_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pinned"]) -> typing.Union[MetaOapg.properties.pinned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["muted"]) -> typing.Union[MetaOapg.properties.muted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union['XiqAnomalySeverity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity_id"]) -> typing.Union[MetaOapg.properties.severity_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affected_device_count"]) -> typing.Union[MetaOapg.properties.affected_device_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_detected_time"]) -> typing.Union[MetaOapg.properties.last_detected_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomaly_type"]) -> typing.Union['XiqAnomalyType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["location_type", "location_ids", "building_id", "location_name", "pinned", "muted", "severity", "severity_id", "summary", "affected_device_count", "last_detected_time", "anomaly_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        location_type: typing.Union['XiqLocationType', schemas.Unset] = schemas.unset,
        location_ids: typing.Union[MetaOapg.properties.location_ids, list, tuple, schemas.Unset] = schemas.unset,
        building_id: typing.Union[MetaOapg.properties.building_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        location_name: typing.Union[MetaOapg.properties.location_name, str, schemas.Unset] = schemas.unset,
        pinned: typing.Union[MetaOapg.properties.pinned, bool, schemas.Unset] = schemas.unset,
        muted: typing.Union[MetaOapg.properties.muted, bool, schemas.Unset] = schemas.unset,
        severity: typing.Union['XiqAnomalySeverity', schemas.Unset] = schemas.unset,
        severity_id: typing.Union[MetaOapg.properties.severity_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        affected_device_count: typing.Union[MetaOapg.properties.affected_device_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_detected_time: typing.Union[MetaOapg.properties.last_detected_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        anomaly_type: typing.Union['XiqAnomalyType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAnomalyLocationEntity':
        return super().__new__(
            cls,
            *_args,
            location_type=location_type,
            location_ids=location_ids,
            building_id=building_id,
            location_name=location_name,
            pinned=pinned,
            muted=muted,
            severity=severity,
            severity_id=severity_id,
            summary=summary,
            affected_device_count=affected_device_count,
            last_detected_time=last_detected_time,
            anomaly_type=anomaly_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_anomaly_severity import XiqAnomalySeverity
from extremecloudiq.model.xiq_anomaly_type import XiqAnomalyType
from extremecloudiq.model.xiq_location_type import XiqLocationType
