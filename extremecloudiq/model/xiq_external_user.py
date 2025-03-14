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


class XiqExternalUser(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "user_role",
            "update_time",
            "login_name",
            "create_time",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            login_name = schemas.StrSchema
        
            @staticmethod
            def user_role() -> typing.Type['XiqUserRole']:
                return XiqUserRole
            org_id = schemas.Int64Schema
            
            
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
            grantee_id = schemas.Int64Schema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "login_name": login_name,
                "user_role": user_role,
                "org_id": org_id,
                "location_ids": location_ids,
                "grantee_id": grantee_id,
            }
    
    user_role: 'XiqUserRole'
    update_time: MetaOapg.properties.update_time
    login_name: MetaOapg.properties.login_name
    create_time: MetaOapg.properties.create_time
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_name"]) -> MetaOapg.properties.login_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_role"]) -> 'XiqUserRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_ids"]) -> MetaOapg.properties.location_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantee_id"]) -> MetaOapg.properties.grantee_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "login_name", "user_role", "org_id", "location_ids", "grantee_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_name"]) -> MetaOapg.properties.login_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_role"]) -> 'XiqUserRole': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_ids"]) -> typing.Union[MetaOapg.properties.location_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantee_id"]) -> typing.Union[MetaOapg.properties.grantee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "login_name", "user_role", "org_id", "location_ids", "grantee_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_role: 'XiqUserRole',
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        login_name: typing.Union[MetaOapg.properties.login_name, str, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        location_ids: typing.Union[MetaOapg.properties.location_ids, list, tuple, schemas.Unset] = schemas.unset,
        grantee_id: typing.Union[MetaOapg.properties.grantee_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqExternalUser':
        return super().__new__(
            cls,
            *_args,
            user_role=user_role,
            update_time=update_time,
            login_name=login_name,
            create_time=create_time,
            id=id,
            org_id=org_id,
            location_ids=location_ids,
            grantee_id=grantee_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_user_role import XiqUserRole
