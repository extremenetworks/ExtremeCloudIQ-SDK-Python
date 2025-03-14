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


class XiqAlertEmailSubscription(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The alert email subscription data model
    """


    class MetaOapg:
        required = {
            "is_enabled",
            "update_time",
            "create_time",
            "is_email_verified",
            "id",
            "is_subscribe_all",
            "email",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            email = schemas.StrSchema
            is_enabled = schemas.BoolSchema
            is_email_verified = schemas.BoolSchema
            is_subscribe_all = schemas.BoolSchema
            
            
            class alert_policy_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'alert_policy_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "email": email,
                "is_enabled": is_enabled,
                "is_email_verified": is_email_verified,
                "is_subscribe_all": is_subscribe_all,
                "alert_policy_ids": alert_policy_ids,
            }
    
    is_enabled: MetaOapg.properties.is_enabled
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    is_email_verified: MetaOapg.properties.is_email_verified
    id: MetaOapg.properties.id
    is_subscribe_all: MetaOapg.properties.is_subscribe_all
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_email_verified"]) -> MetaOapg.properties.is_email_verified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_subscribe_all"]) -> MetaOapg.properties.is_subscribe_all: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alert_policy_ids"]) -> MetaOapg.properties.alert_policy_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "email", "is_enabled", "is_email_verified", "is_subscribe_all", "alert_policy_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_email_verified"]) -> MetaOapg.properties.is_email_verified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_subscribe_all"]) -> MetaOapg.properties.is_subscribe_all: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alert_policy_ids"]) -> typing.Union[MetaOapg.properties.alert_policy_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "email", "is_enabled", "is_email_verified", "is_subscribe_all", "alert_policy_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        is_email_verified: typing.Union[MetaOapg.properties.is_email_verified, bool, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        is_subscribe_all: typing.Union[MetaOapg.properties.is_subscribe_all, bool, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        alert_policy_ids: typing.Union[MetaOapg.properties.alert_policy_ids, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAlertEmailSubscription':
        return super().__new__(
            cls,
            *_args,
            is_enabled=is_enabled,
            update_time=update_time,
            create_time=create_time,
            is_email_verified=is_email_verified,
            id=id,
            is_subscribe_all=is_subscribe_all,
            email=email,
            alert_policy_ids=alert_policy_ids,
            _configuration=_configuration,
            **kwargs,
        )
