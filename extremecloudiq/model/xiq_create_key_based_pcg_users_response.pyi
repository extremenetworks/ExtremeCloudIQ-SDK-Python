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


class XiqCreateKeyBasedPcgUsersResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The response of add Key-based Private Client Group users request
    """


    class MetaOapg:
        required = {
            "policy_id",
            "status",
        }
        
        class properties:
            policy_id = schemas.Int64Schema
            status = schemas.StrSchema
            
            
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
                "policy_id": policy_id,
                "status": status,
                "users": users,
            }
    
    policy_id: MetaOapg.properties.policy_id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policy_id"]) -> MetaOapg.properties.policy_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["policy_id", "status", "users", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policy_id"]) -> MetaOapg.properties.policy_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union[MetaOapg.properties.users, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["policy_id", "status", "users", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        policy_id: typing.Union[MetaOapg.properties.policy_id, decimal.Decimal, int, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        users: typing.Union[MetaOapg.properties.users, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCreateKeyBasedPcgUsersResponse':
        return super().__new__(
            cls,
            *_args,
            policy_id=policy_id,
            status=status,
            users=users,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_key_based_pcg_user import XiqKeyBasedPcgUser
