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


class XiqApiTokenInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "role",
            "user_id",
            "owner_id",
            "user_name",
            "data_center",
            "scopes",
            "issued_at",
        }
        
        class properties:
            user_name = schemas.StrSchema
            user_id = schemas.Int64Schema
            role = schemas.StrSchema
            owner_id = schemas.Int64Schema
            data_center = schemas.StrSchema
            
            
            class scopes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scopes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            issued_at = schemas.DateTimeSchema
            expiration_time = schemas.DateTimeSchema
            expires_in = schemas.Int64Schema
            __annotations__ = {
                "user_name": user_name,
                "user_id": user_id,
                "role": role,
                "owner_id": owner_id,
                "data_center": data_center,
                "scopes": scopes,
                "issued_at": issued_at,
                "expiration_time": expiration_time,
                "expires_in": expires_in,
            }
    
    role: MetaOapg.properties.role
    user_id: MetaOapg.properties.user_id
    owner_id: MetaOapg.properties.owner_id
    user_name: MetaOapg.properties.user_name
    data_center: MetaOapg.properties.data_center
    scopes: MetaOapg.properties.scopes
    issued_at: MetaOapg.properties.issued_at
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_center"]) -> MetaOapg.properties.data_center: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issued_at"]) -> MetaOapg.properties.issued_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration_time"]) -> MetaOapg.properties.expiration_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_name", "user_id", "role", "owner_id", "data_center", "scopes", "issued_at", "expiration_time", "expires_in", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_center"]) -> MetaOapg.properties.data_center: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issued_at"]) -> MetaOapg.properties.issued_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration_time"]) -> typing.Union[MetaOapg.properties.expiration_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union[MetaOapg.properties.expires_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_name", "user_id", "role", "owner_id", "data_center", "scopes", "issued_at", "expiration_time", "expires_in", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        role: typing.Union[MetaOapg.properties.role, str, ],
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, ],
        owner_id: typing.Union[MetaOapg.properties.owner_id, decimal.Decimal, int, ],
        user_name: typing.Union[MetaOapg.properties.user_name, str, ],
        data_center: typing.Union[MetaOapg.properties.data_center, str, ],
        scopes: typing.Union[MetaOapg.properties.scopes, list, tuple, ],
        issued_at: typing.Union[MetaOapg.properties.issued_at, str, datetime, ],
        expiration_time: typing.Union[MetaOapg.properties.expiration_time, str, datetime, schemas.Unset] = schemas.unset,
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqApiTokenInfo':
        return super().__new__(
            cls,
            *_args,
            role=role,
            user_id=user_id,
            owner_id=owner_id,
            user_name=user_name,
            data_center=data_center,
            scopes=scopes,
            issued_at=issued_at,
            expiration_time=expiration_time,
            expires_in=expires_in,
            _configuration=_configuration,
            **kwargs,
        )
