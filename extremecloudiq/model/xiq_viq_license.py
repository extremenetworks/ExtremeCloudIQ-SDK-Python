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


class XiqViqLicense(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The license list
    """


    class MetaOapg:
        required = {
            "update_time",
            "create_time",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
        
            @staticmethod
            def status() -> typing.Type['XiqLicenseStatus']:
                return XiqLicenseStatus
            active_date = schemas.DateTimeSchema
            expire_date = schemas.DateTimeSchema
            entitlement_key = schemas.StrSchema
        
            @staticmethod
            def entitlement_type() -> typing.Type['XiqEntitlementType']:
                return XiqEntitlementType
        
            @staticmethod
            def mode() -> typing.Type['XiqLicenseMode']:
                return XiqLicenseMode
            devices = schemas.Int32Schema
            activated = schemas.Int32Schema
            available = schemas.Int32Schema
            license_type = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "status": status,
                "active_date": active_date,
                "expire_date": expire_date,
                "entitlement_key": entitlement_key,
                "entitlement_type": entitlement_type,
                "mode": mode,
                "devices": devices,
                "activated": activated,
                "available": available,
                "license_type": license_type,
            }
    
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'XiqLicenseStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_date"]) -> MetaOapg.properties.active_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expire_date"]) -> MetaOapg.properties.expire_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entitlement_key"]) -> MetaOapg.properties.entitlement_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entitlement_type"]) -> 'XiqEntitlementType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> 'XiqLicenseMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devices"]) -> MetaOapg.properties.devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activated"]) -> MetaOapg.properties.activated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available"]) -> MetaOapg.properties.available: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license_type"]) -> MetaOapg.properties.license_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "status", "active_date", "expire_date", "entitlement_key", "entitlement_type", "mode", "devices", "activated", "available", "license_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['XiqLicenseStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_date"]) -> typing.Union[MetaOapg.properties.active_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expire_date"]) -> typing.Union[MetaOapg.properties.expire_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entitlement_key"]) -> typing.Union[MetaOapg.properties.entitlement_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entitlement_type"]) -> typing.Union['XiqEntitlementType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union['XiqLicenseMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devices"]) -> typing.Union[MetaOapg.properties.devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activated"]) -> typing.Union[MetaOapg.properties.activated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available"]) -> typing.Union[MetaOapg.properties.available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license_type"]) -> typing.Union[MetaOapg.properties.license_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "status", "active_date", "expire_date", "entitlement_key", "entitlement_type", "mode", "devices", "activated", "available", "license_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        status: typing.Union['XiqLicenseStatus', schemas.Unset] = schemas.unset,
        active_date: typing.Union[MetaOapg.properties.active_date, str, datetime, schemas.Unset] = schemas.unset,
        expire_date: typing.Union[MetaOapg.properties.expire_date, str, datetime, schemas.Unset] = schemas.unset,
        entitlement_key: typing.Union[MetaOapg.properties.entitlement_key, str, schemas.Unset] = schemas.unset,
        entitlement_type: typing.Union['XiqEntitlementType', schemas.Unset] = schemas.unset,
        mode: typing.Union['XiqLicenseMode', schemas.Unset] = schemas.unset,
        devices: typing.Union[MetaOapg.properties.devices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activated: typing.Union[MetaOapg.properties.activated, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        available: typing.Union[MetaOapg.properties.available, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        license_type: typing.Union[MetaOapg.properties.license_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqViqLicense':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            status=status,
            active_date=active_date,
            expire_date=expire_date,
            entitlement_key=entitlement_key,
            entitlement_type=entitlement_type,
            mode=mode,
            devices=devices,
            activated=activated,
            available=available,
            license_type=license_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_entitlement_type import XiqEntitlementType
from extremecloudiq.model.xiq_license_mode import XiqLicenseMode
from extremecloudiq.model.xiq_license_status import XiqLicenseStatus
