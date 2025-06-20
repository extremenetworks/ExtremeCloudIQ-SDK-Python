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


class XiqEndUser(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "update_time",
            "email_address",
            "create_time",
            "approval_type",
            "user_name",
            "name",
            "expired_time",
            "phone_number",
            "id",
            "user_group_name",
            "user_group_id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            name = schemas.StrSchema
            email_address = schemas.StrSchema
            phone_number = schemas.StrSchema
            user_name = schemas.StrSchema
            user_group_id = schemas.Int64Schema
            user_group_name = schemas.StrSchema
            approval_type = schemas.StrSchema
            expired_time = schemas.Int64Schema
            org_id = schemas.Int64Schema
            description = schemas.StrSchema
            password = schemas.StrSchema
            organization = schemas.StrSchema
            visit_purpose = schemas.StrSchema
            email_password_delivery = schemas.StrSchema
            sms_password_delivery = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "name": name,
                "email_address": email_address,
                "phone_number": phone_number,
                "user_name": user_name,
                "user_group_id": user_group_id,
                "user_group_name": user_group_name,
                "approval_type": approval_type,
                "expired_time": expired_time,
                "org_id": org_id,
                "description": description,
                "password": password,
                "organization": organization,
                "visit_purpose": visit_purpose,
                "email_password_delivery": email_password_delivery,
                "sms_password_delivery": sms_password_delivery,
            }
    
    update_time: MetaOapg.properties.update_time
    email_address: MetaOapg.properties.email_address
    create_time: MetaOapg.properties.create_time
    approval_type: MetaOapg.properties.approval_type
    user_name: MetaOapg.properties.user_name
    name: MetaOapg.properties.name
    expired_time: MetaOapg.properties.expired_time
    phone_number: MetaOapg.properties.phone_number
    id: MetaOapg.properties.id
    user_group_name: MetaOapg.properties.user_group_name
    user_group_id: MetaOapg.properties.user_group_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> MetaOapg.properties.email_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_group_id"]) -> MetaOapg.properties.user_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_group_name"]) -> MetaOapg.properties.user_group_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval_type"]) -> MetaOapg.properties.approval_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expired_time"]) -> MetaOapg.properties.expired_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visit_purpose"]) -> MetaOapg.properties.visit_purpose: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_password_delivery"]) -> MetaOapg.properties.email_password_delivery: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sms_password_delivery"]) -> MetaOapg.properties.sms_password_delivery: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "email_address", "phone_number", "user_name", "user_group_id", "user_group_name", "approval_type", "expired_time", "org_id", "description", "password", "organization", "visit_purpose", "email_password_delivery", "sms_password_delivery", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> MetaOapg.properties.email_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_group_id"]) -> MetaOapg.properties.user_group_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_group_name"]) -> MetaOapg.properties.user_group_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval_type"]) -> MetaOapg.properties.approval_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expired_time"]) -> MetaOapg.properties.expired_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union[MetaOapg.properties.organization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visit_purpose"]) -> typing.Union[MetaOapg.properties.visit_purpose, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_password_delivery"]) -> typing.Union[MetaOapg.properties.email_password_delivery, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sms_password_delivery"]) -> typing.Union[MetaOapg.properties.sms_password_delivery, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "email_address", "phone_number", "user_name", "user_group_id", "user_group_name", "approval_type", "expired_time", "org_id", "description", "password", "organization", "visit_purpose", "email_password_delivery", "sms_password_delivery", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        email_address: typing.Union[MetaOapg.properties.email_address, str, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        approval_type: typing.Union[MetaOapg.properties.approval_type, str, ],
        user_name: typing.Union[MetaOapg.properties.user_name, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        expired_time: typing.Union[MetaOapg.properties.expired_time, decimal.Decimal, int, ],
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        user_group_name: typing.Union[MetaOapg.properties.user_group_name, str, ],
        user_group_id: typing.Union[MetaOapg.properties.user_group_id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        organization: typing.Union[MetaOapg.properties.organization, str, schemas.Unset] = schemas.unset,
        visit_purpose: typing.Union[MetaOapg.properties.visit_purpose, str, schemas.Unset] = schemas.unset,
        email_password_delivery: typing.Union[MetaOapg.properties.email_password_delivery, str, schemas.Unset] = schemas.unset,
        sms_password_delivery: typing.Union[MetaOapg.properties.sms_password_delivery, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqEndUser':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            email_address=email_address,
            create_time=create_time,
            approval_type=approval_type,
            user_name=user_name,
            name=name,
            expired_time=expired_time,
            phone_number=phone_number,
            id=id,
            user_group_name=user_group_name,
            user_group_id=user_group_id,
            org_id=org_id,
            description=description,
            password=password,
            organization=organization,
            visit_purpose=visit_purpose,
            email_password_delivery=email_password_delivery,
            sms_password_delivery=sms_password_delivery,
            _configuration=_configuration,
            **kwargs,
        )
