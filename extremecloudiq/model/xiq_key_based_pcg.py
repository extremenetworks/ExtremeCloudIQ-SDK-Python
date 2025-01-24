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


class XiqKeyBasedPcg(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The response of key based PCG data
    """


    class MetaOapg:
        required = {
            "update_time",
            "create_time",
            "policy_id",
            "policy_name",
            "ssid_name",
            "id",
            "enabled",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            policy_id = schemas.Int64Schema
            policy_name = schemas.StrSchema
            ssid_name = schemas.StrSchema
            enabled = schemas.BoolSchema
            org_id = schemas.Int64Schema
            
            
            class users(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqKeyBasedPcgUser']:
                        return XiqKeyBasedPcgUser
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqKeyBasedPcgUser'], typing.List['XiqKeyBasedPcgUser']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'users':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqKeyBasedPcgUser':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "policy_id": policy_id,
                "policy_name": policy_name,
                "ssid_name": ssid_name,
                "enabled": enabled,
                "org_id": org_id,
                "users": users,
            }
    
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    policy_id: MetaOapg.properties.policy_id
    policy_name: MetaOapg.properties.policy_name
    ssid_name: MetaOapg.properties.ssid_name
    id: MetaOapg.properties.id
    enabled: MetaOapg.properties.enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policy_id"]) -> MetaOapg.properties.policy_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policy_name"]) -> MetaOapg.properties.policy_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid_name"]) -> MetaOapg.properties.ssid_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "policy_id", "policy_name", "ssid_name", "enabled", "org_id", "users", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policy_id"]) -> MetaOapg.properties.policy_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policy_name"]) -> MetaOapg.properties.policy_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid_name"]) -> MetaOapg.properties.ssid_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union[MetaOapg.properties.users, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "policy_id", "policy_name", "ssid_name", "enabled", "org_id", "users", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        policy_id: typing.Union[MetaOapg.properties.policy_id, decimal.Decimal, int, ],
        policy_name: typing.Union[MetaOapg.properties.policy_name, str, ],
        ssid_name: typing.Union[MetaOapg.properties.ssid_name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        users: typing.Union[MetaOapg.properties.users, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqKeyBasedPcg':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            policy_id=policy_id,
            policy_name=policy_name,
            ssid_name=ssid_name,
            id=id,
            enabled=enabled,
            org_id=org_id,
            users=users,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_key_based_pcg_user import XiqKeyBasedPcgUser
