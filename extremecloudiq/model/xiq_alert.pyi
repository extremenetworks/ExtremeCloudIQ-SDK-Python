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


class XiqAlert(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Alert Model
    """


    class MetaOapg:
        required = {
            "id",
            "tags",
            "timestamp",
        }
        
        class properties:
            id = schemas.StrSchema
            timestamp = schemas.DateTimeSchema
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqAlertTag']:
                        return XiqAlertTag
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqAlertTag'], typing.List['XiqAlertTag']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqAlertTag':
                    return super().__getitem__(i)
            owner_id = schemas.Int64Schema
            org_id = schemas.Int64Schema
            message_metadata_id = schemas.Int64Schema
            message_metadata_type = schemas.StrSchema
            message_metadata_name = schemas.StrSchema
            summary = schemas.StrSchema
            severity_name = schemas.StrSchema
            category_name = schemas.StrSchema
            severity_id = schemas.Int64Schema
            category_id = schemas.Int64Schema
        
            @staticmethod
            def source() -> typing.Type['XiqAlertSource']:
                return XiqAlertSource
            acknowledged = schemas.BoolSchema
            site_id = schemas.Int64Schema
            site_name = schemas.StrSchema
            alert_policy_id = schemas.Int64Schema
            alert_policy_name = schemas.StrSchema
            alert_rule_id = schemas.Int64Schema
            acknowledged_username = schemas.StrSchema
            floor_id = schemas.Int64Schema
            floor_name = schemas.StrSchema
            building_id = schemas.Int64Schema
            building_name = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "timestamp": timestamp,
                "tags": tags,
                "owner_id": owner_id,
                "org_id": org_id,
                "message_metadata_id": message_metadata_id,
                "message_metadata_type": message_metadata_type,
                "message_metadata_name": message_metadata_name,
                "summary": summary,
                "severity_name": severity_name,
                "category_name": category_name,
                "severity_id": severity_id,
                "category_id": category_id,
                "source": source,
                "acknowledged": acknowledged,
                "site_id": site_id,
                "site_name": site_name,
                "alert_policy_id": alert_policy_id,
                "alert_policy_name": alert_policy_name,
                "alert_rule_id": alert_rule_id,
                "acknowledged_username": acknowledged_username,
                "floor_id": floor_id,
                "floor_name": floor_name,
                "building_id": building_id,
                "building_name": building_name,
            }
    
    id: MetaOapg.properties.id
    tags: MetaOapg.properties.tags
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_metadata_id"]) -> MetaOapg.properties.message_metadata_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_metadata_type"]) -> MetaOapg.properties.message_metadata_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_metadata_name"]) -> MetaOapg.properties.message_metadata_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity_name"]) -> MetaOapg.properties.severity_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_name"]) -> MetaOapg.properties.category_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity_id"]) -> MetaOapg.properties.severity_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_id"]) -> MetaOapg.properties.category_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'XiqAlertSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acknowledged"]) -> MetaOapg.properties.acknowledged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_id"]) -> MetaOapg.properties.site_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_name"]) -> MetaOapg.properties.site_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alert_policy_id"]) -> MetaOapg.properties.alert_policy_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alert_policy_name"]) -> MetaOapg.properties.alert_policy_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alert_rule_id"]) -> MetaOapg.properties.alert_rule_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acknowledged_username"]) -> MetaOapg.properties.acknowledged_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floor_id"]) -> MetaOapg.properties.floor_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floor_name"]) -> MetaOapg.properties.floor_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["building_id"]) -> MetaOapg.properties.building_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["building_name"]) -> MetaOapg.properties.building_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "timestamp", "tags", "owner_id", "org_id", "message_metadata_id", "message_metadata_type", "message_metadata_name", "summary", "severity_name", "category_name", "severity_id", "category_id", "source", "acknowledged", "site_id", "site_name", "alert_policy_id", "alert_policy_name", "alert_rule_id", "acknowledged_username", "floor_id", "floor_name", "building_id", "building_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_id"]) -> typing.Union[MetaOapg.properties.owner_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_metadata_id"]) -> typing.Union[MetaOapg.properties.message_metadata_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_metadata_type"]) -> typing.Union[MetaOapg.properties.message_metadata_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_metadata_name"]) -> typing.Union[MetaOapg.properties.message_metadata_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity_name"]) -> typing.Union[MetaOapg.properties.severity_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_name"]) -> typing.Union[MetaOapg.properties.category_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity_id"]) -> typing.Union[MetaOapg.properties.severity_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_id"]) -> typing.Union[MetaOapg.properties.category_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union['XiqAlertSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acknowledged"]) -> typing.Union[MetaOapg.properties.acknowledged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_id"]) -> typing.Union[MetaOapg.properties.site_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_name"]) -> typing.Union[MetaOapg.properties.site_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alert_policy_id"]) -> typing.Union[MetaOapg.properties.alert_policy_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alert_policy_name"]) -> typing.Union[MetaOapg.properties.alert_policy_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alert_rule_id"]) -> typing.Union[MetaOapg.properties.alert_rule_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acknowledged_username"]) -> typing.Union[MetaOapg.properties.acknowledged_username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floor_id"]) -> typing.Union[MetaOapg.properties.floor_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floor_name"]) -> typing.Union[MetaOapg.properties.floor_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["building_id"]) -> typing.Union[MetaOapg.properties.building_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["building_name"]) -> typing.Union[MetaOapg.properties.building_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "timestamp", "tags", "owner_id", "org_id", "message_metadata_id", "message_metadata_type", "message_metadata_name", "summary", "severity_name", "category_name", "severity_id", "category_id", "source", "acknowledged", "site_id", "site_name", "alert_policy_id", "alert_policy_name", "alert_rule_id", "acknowledged_username", "floor_id", "floor_name", "building_id", "building_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        owner_id: typing.Union[MetaOapg.properties.owner_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        message_metadata_id: typing.Union[MetaOapg.properties.message_metadata_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        message_metadata_type: typing.Union[MetaOapg.properties.message_metadata_type, str, schemas.Unset] = schemas.unset,
        message_metadata_name: typing.Union[MetaOapg.properties.message_metadata_name, str, schemas.Unset] = schemas.unset,
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        severity_name: typing.Union[MetaOapg.properties.severity_name, str, schemas.Unset] = schemas.unset,
        category_name: typing.Union[MetaOapg.properties.category_name, str, schemas.Unset] = schemas.unset,
        severity_id: typing.Union[MetaOapg.properties.severity_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        category_id: typing.Union[MetaOapg.properties.category_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        source: typing.Union['XiqAlertSource', schemas.Unset] = schemas.unset,
        acknowledged: typing.Union[MetaOapg.properties.acknowledged, bool, schemas.Unset] = schemas.unset,
        site_id: typing.Union[MetaOapg.properties.site_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        site_name: typing.Union[MetaOapg.properties.site_name, str, schemas.Unset] = schemas.unset,
        alert_policy_id: typing.Union[MetaOapg.properties.alert_policy_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        alert_policy_name: typing.Union[MetaOapg.properties.alert_policy_name, str, schemas.Unset] = schemas.unset,
        alert_rule_id: typing.Union[MetaOapg.properties.alert_rule_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        acknowledged_username: typing.Union[MetaOapg.properties.acknowledged_username, str, schemas.Unset] = schemas.unset,
        floor_id: typing.Union[MetaOapg.properties.floor_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        floor_name: typing.Union[MetaOapg.properties.floor_name, str, schemas.Unset] = schemas.unset,
        building_id: typing.Union[MetaOapg.properties.building_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        building_name: typing.Union[MetaOapg.properties.building_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAlert':
        return super().__new__(
            cls,
            *_args,
            id=id,
            tags=tags,
            timestamp=timestamp,
            owner_id=owner_id,
            org_id=org_id,
            message_metadata_id=message_metadata_id,
            message_metadata_type=message_metadata_type,
            message_metadata_name=message_metadata_name,
            summary=summary,
            severity_name=severity_name,
            category_name=category_name,
            severity_id=severity_id,
            category_id=category_id,
            source=source,
            acknowledged=acknowledged,
            site_id=site_id,
            site_name=site_name,
            alert_policy_id=alert_policy_id,
            alert_policy_name=alert_policy_name,
            alert_rule_id=alert_rule_id,
            acknowledged_username=acknowledged_username,
            floor_id=floor_id,
            floor_name=floor_name,
            building_id=building_id,
            building_name=building_name,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_alert_source import XiqAlertSource
from extremecloudiq.model.xiq_alert_tag import XiqAlertTag
