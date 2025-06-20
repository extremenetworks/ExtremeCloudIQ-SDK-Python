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


class XiqApiAccessToken(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

     The API Access Token 
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
            application = schemas.StrSchema
            access_token = schemas.StrSchema
            grantor = schemas.StrSchema
            generated_on = schemas.DateTimeSchema
            expiration = schemas.Int64Schema
            refresh_token = schemas.StrSchema
            client_id = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "application": application,
                "access_token": access_token,
                "grantor": grantor,
                "generated_on": generated_on,
                "expiration": expiration,
                "refresh_token": refresh_token,
                "client_id": client_id,
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
    def __getitem__(self, name: typing_extensions.Literal["application"]) -> MetaOapg.properties.application: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantor"]) -> MetaOapg.properties.grantor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["generated_on"]) -> MetaOapg.properties.generated_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token"]) -> MetaOapg.properties.refresh_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "application", "access_token", "grantor", "generated_on", "expiration", "refresh_token", "client_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["application"]) -> typing.Union[MetaOapg.properties.application, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> typing.Union[MetaOapg.properties.access_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantor"]) -> typing.Union[MetaOapg.properties.grantor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["generated_on"]) -> typing.Union[MetaOapg.properties.generated_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration"]) -> typing.Union[MetaOapg.properties.expiration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token"]) -> typing.Union[MetaOapg.properties.refresh_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "application", "access_token", "grantor", "generated_on", "expiration", "refresh_token", "client_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        application: typing.Union[MetaOapg.properties.application, str, schemas.Unset] = schemas.unset,
        access_token: typing.Union[MetaOapg.properties.access_token, str, schemas.Unset] = schemas.unset,
        grantor: typing.Union[MetaOapg.properties.grantor, str, schemas.Unset] = schemas.unset,
        generated_on: typing.Union[MetaOapg.properties.generated_on, str, datetime, schemas.Unset] = schemas.unset,
        expiration: typing.Union[MetaOapg.properties.expiration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        refresh_token: typing.Union[MetaOapg.properties.refresh_token, str, schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqApiAccessToken':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            application=application,
            access_token=access_token,
            grantor=grantor,
            generated_on=generated_on,
            expiration=expiration,
            refresh_token=refresh_token,
            client_id=client_id,
            _configuration=_configuration,
            **kwargs,
        )
