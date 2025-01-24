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


class XiqUserGroup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "password_settings",
            "ssids",
            "update_time",
            "create_time",
            "password_type",
            "user_count",
            "name",
            "expiration_settings",
            "password_db_location",
            "id",
            "predefined",
            "delivery_settings",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            name = schemas.StrSchema
            predefined = schemas.BoolSchema
        
            @staticmethod
            def password_db_location() -> typing.Type['XiqPasswordDbLocation']:
                return XiqPasswordDbLocation
        
            @staticmethod
            def password_type() -> typing.Type['XiqPasswordType']:
                return XiqPasswordType
        
            @staticmethod
            def password_settings() -> typing.Type['XiqPasswordSettings']:
                return XiqPasswordSettings
        
            @staticmethod
            def expiration_settings() -> typing.Type['XiqExpirationSettings']:
                return XiqExpirationSettings
        
            @staticmethod
            def delivery_settings() -> typing.Type['XiqDeliverySettings']:
                return XiqDeliverySettings
            user_count = schemas.Int32Schema
            
            
            class ssids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            org_id = schemas.Int64Schema
            description = schemas.StrSchema
            pcg_use_only = schemas.BoolSchema
        
            @staticmethod
            def pcg_type() -> typing.Type['XiqPcgType']:
                return XiqPcgType
            ppsk_use_only = schemas.BoolSchema
            enable_cwp_reg = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "name": name,
                "predefined": predefined,
                "password_db_location": password_db_location,
                "password_type": password_type,
                "password_settings": password_settings,
                "expiration_settings": expiration_settings,
                "delivery_settings": delivery_settings,
                "user_count": user_count,
                "ssids": ssids,
                "org_id": org_id,
                "description": description,
                "pcg_use_only": pcg_use_only,
                "pcg_type": pcg_type,
                "ppsk_use_only": ppsk_use_only,
                "enable_cwp_reg": enable_cwp_reg,
            }
    
    password_settings: 'XiqPasswordSettings'
    ssids: MetaOapg.properties.ssids
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    password_type: 'XiqPasswordType'
    user_count: MetaOapg.properties.user_count
    name: MetaOapg.properties.name
    expiration_settings: 'XiqExpirationSettings'
    password_db_location: 'XiqPasswordDbLocation'
    id: MetaOapg.properties.id
    predefined: MetaOapg.properties.predefined
    delivery_settings: 'XiqDeliverySettings'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predefined"]) -> MetaOapg.properties.predefined: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_db_location"]) -> 'XiqPasswordDbLocation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_type"]) -> 'XiqPasswordType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_settings"]) -> 'XiqPasswordSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration_settings"]) -> 'XiqExpirationSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery_settings"]) -> 'XiqDeliverySettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_count"]) -> MetaOapg.properties.user_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssids"]) -> MetaOapg.properties.ssids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pcg_use_only"]) -> MetaOapg.properties.pcg_use_only: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pcg_type"]) -> 'XiqPcgType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ppsk_use_only"]) -> MetaOapg.properties.ppsk_use_only: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_cwp_reg"]) -> MetaOapg.properties.enable_cwp_reg: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "predefined", "password_db_location", "password_type", "password_settings", "expiration_settings", "delivery_settings", "user_count", "ssids", "org_id", "description", "pcg_use_only", "pcg_type", "ppsk_use_only", "enable_cwp_reg", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["predefined"]) -> MetaOapg.properties.predefined: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_db_location"]) -> 'XiqPasswordDbLocation': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_type"]) -> 'XiqPasswordType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_settings"]) -> 'XiqPasswordSettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration_settings"]) -> 'XiqExpirationSettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery_settings"]) -> 'XiqDeliverySettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_count"]) -> MetaOapg.properties.user_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssids"]) -> MetaOapg.properties.ssids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pcg_use_only"]) -> typing.Union[MetaOapg.properties.pcg_use_only, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pcg_type"]) -> typing.Union['XiqPcgType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ppsk_use_only"]) -> typing.Union[MetaOapg.properties.ppsk_use_only, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_cwp_reg"]) -> typing.Union[MetaOapg.properties.enable_cwp_reg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "predefined", "password_db_location", "password_type", "password_settings", "expiration_settings", "delivery_settings", "user_count", "ssids", "org_id", "description", "pcg_use_only", "pcg_type", "ppsk_use_only", "enable_cwp_reg", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        password_settings: 'XiqPasswordSettings',
        ssids: typing.Union[MetaOapg.properties.ssids, list, tuple, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        password_type: 'XiqPasswordType',
        user_count: typing.Union[MetaOapg.properties.user_count, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        expiration_settings: 'XiqExpirationSettings',
        password_db_location: 'XiqPasswordDbLocation',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        predefined: typing.Union[MetaOapg.properties.predefined, bool, ],
        delivery_settings: 'XiqDeliverySettings',
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        pcg_use_only: typing.Union[MetaOapg.properties.pcg_use_only, bool, schemas.Unset] = schemas.unset,
        pcg_type: typing.Union['XiqPcgType', schemas.Unset] = schemas.unset,
        ppsk_use_only: typing.Union[MetaOapg.properties.ppsk_use_only, bool, schemas.Unset] = schemas.unset,
        enable_cwp_reg: typing.Union[MetaOapg.properties.enable_cwp_reg, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUserGroup':
        return super().__new__(
            cls,
            *_args,
            password_settings=password_settings,
            ssids=ssids,
            update_time=update_time,
            create_time=create_time,
            password_type=password_type,
            user_count=user_count,
            name=name,
            expiration_settings=expiration_settings,
            password_db_location=password_db_location,
            id=id,
            predefined=predefined,
            delivery_settings=delivery_settings,
            org_id=org_id,
            description=description,
            pcg_use_only=pcg_use_only,
            pcg_type=pcg_type,
            ppsk_use_only=ppsk_use_only,
            enable_cwp_reg=enable_cwp_reg,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_delivery_settings import XiqDeliverySettings
from extremecloudiq.model.xiq_expiration_settings import XiqExpirationSettings
from extremecloudiq.model.xiq_password_db_location import XiqPasswordDbLocation
from extremecloudiq.model.xiq_password_settings import XiqPasswordSettings
from extremecloudiq.model.xiq_password_type import XiqPasswordType
from extremecloudiq.model.xiq_pcg_type import XiqPcgType
