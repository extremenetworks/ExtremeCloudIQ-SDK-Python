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


class XiqCreateUserRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "user_role",
            "login_name",
            "idle_timeout",
            "display_name",
        }
        
        class properties:
            login_name = schemas.StrSchema
            display_name = schemas.StrSchema
            idle_timeout = schemas.Int32Schema
        
            @staticmethod
            def user_role() -> typing.Type['XiqUserRole']:
                return XiqUserRole
            
            
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
            __annotations__ = {
                "login_name": login_name,
                "display_name": display_name,
                "idle_timeout": idle_timeout,
                "user_role": user_role,
                "location_ids": location_ids,
            }
    
    user_role: 'XiqUserRole'
    login_name: MetaOapg.properties.login_name
    idle_timeout: MetaOapg.properties.idle_timeout
    display_name: MetaOapg.properties.display_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_name"]) -> MetaOapg.properties.login_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idle_timeout"]) -> MetaOapg.properties.idle_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_role"]) -> 'XiqUserRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_ids"]) -> MetaOapg.properties.location_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["login_name", "display_name", "idle_timeout", "user_role", "location_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_name"]) -> MetaOapg.properties.login_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idle_timeout"]) -> MetaOapg.properties.idle_timeout: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_role"]) -> 'XiqUserRole': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_ids"]) -> typing.Union[MetaOapg.properties.location_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["login_name", "display_name", "idle_timeout", "user_role", "location_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_role: 'XiqUserRole',
        login_name: typing.Union[MetaOapg.properties.login_name, str, ],
        idle_timeout: typing.Union[MetaOapg.properties.idle_timeout, decimal.Decimal, int, ],
        display_name: typing.Union[MetaOapg.properties.display_name, str, ],
        location_ids: typing.Union[MetaOapg.properties.location_ids, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCreateUserRequest':
        return super().__new__(
            cls,
            *_args,
            user_role=user_role,
            login_name=login_name,
            idle_timeout=idle_timeout,
            display_name=display_name,
            location_ids=location_ids,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_user_role import XiqUserRole
