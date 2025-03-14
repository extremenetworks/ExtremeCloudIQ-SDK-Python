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


class XiqSetSsidModeWepRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The request for setting the SSID to be WEP mode.
    """


    class MetaOapg:
        required = {
            "key_management",
            "encryption_method",
        }
        
        class properties:
        
            @staticmethod
            def key_management() -> typing.Type['XiqSsidWepKeyManagement']:
                return XiqSsidWepKeyManagement
        
            @staticmethod
            def encryption_method() -> typing.Type['XiqSsidWepEncryptionMethod']:
                return XiqSsidWepEncryptionMethod
        
            @staticmethod
            def authentication_method() -> typing.Type['XiqSsidWepAuthenticationMethod']:
                return XiqSsidWepAuthenticationMethod
        
            @staticmethod
            def default_key() -> typing.Type['XiqSsidWepDefaultKey']:
                return XiqSsidWepDefaultKey
        
            @staticmethod
            def key_type() -> typing.Type['XiqSsidKeyType']:
                return XiqSsidKeyType
            
            
            class key_value(
                schemas.StrSchema
            ):
                pass
            
            
            class key_value2(
                schemas.StrSchema
            ):
                pass
            
            
            class key_value3(
                schemas.StrSchema
            ):
                pass
            
            
            class key_value4(
                schemas.StrSchema
            ):
                pass
            radius_server_group_id = schemas.Int64Schema
            __annotations__ = {
                "key_management": key_management,
                "encryption_method": encryption_method,
                "authentication_method": authentication_method,
                "default_key": default_key,
                "key_type": key_type,
                "key_value": key_value,
                "key_value2": key_value2,
                "key_value3": key_value3,
                "key_value4": key_value4,
                "radius_server_group_id": radius_server_group_id,
            }
    
    key_management: 'XiqSsidWepKeyManagement'
    encryption_method: 'XiqSsidWepEncryptionMethod'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_management"]) -> 'XiqSsidWepKeyManagement': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encryption_method"]) -> 'XiqSsidWepEncryptionMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication_method"]) -> 'XiqSsidWepAuthenticationMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_key"]) -> 'XiqSsidWepDefaultKey': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_type"]) -> 'XiqSsidKeyType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_value"]) -> MetaOapg.properties.key_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_value2"]) -> MetaOapg.properties.key_value2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_value3"]) -> MetaOapg.properties.key_value3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_value4"]) -> MetaOapg.properties.key_value4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radius_server_group_id"]) -> MetaOapg.properties.radius_server_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key_management", "encryption_method", "authentication_method", "default_key", "key_type", "key_value", "key_value2", "key_value3", "key_value4", "radius_server_group_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_management"]) -> 'XiqSsidWepKeyManagement': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encryption_method"]) -> 'XiqSsidWepEncryptionMethod': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication_method"]) -> typing.Union['XiqSsidWepAuthenticationMethod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_key"]) -> typing.Union['XiqSsidWepDefaultKey', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_type"]) -> typing.Union['XiqSsidKeyType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_value"]) -> typing.Union[MetaOapg.properties.key_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_value2"]) -> typing.Union[MetaOapg.properties.key_value2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_value3"]) -> typing.Union[MetaOapg.properties.key_value3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_value4"]) -> typing.Union[MetaOapg.properties.key_value4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radius_server_group_id"]) -> typing.Union[MetaOapg.properties.radius_server_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key_management", "encryption_method", "authentication_method", "default_key", "key_type", "key_value", "key_value2", "key_value3", "key_value4", "radius_server_group_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        key_management: 'XiqSsidWepKeyManagement',
        encryption_method: 'XiqSsidWepEncryptionMethod',
        authentication_method: typing.Union['XiqSsidWepAuthenticationMethod', schemas.Unset] = schemas.unset,
        default_key: typing.Union['XiqSsidWepDefaultKey', schemas.Unset] = schemas.unset,
        key_type: typing.Union['XiqSsidKeyType', schemas.Unset] = schemas.unset,
        key_value: typing.Union[MetaOapg.properties.key_value, str, schemas.Unset] = schemas.unset,
        key_value2: typing.Union[MetaOapg.properties.key_value2, str, schemas.Unset] = schemas.unset,
        key_value3: typing.Union[MetaOapg.properties.key_value3, str, schemas.Unset] = schemas.unset,
        key_value4: typing.Union[MetaOapg.properties.key_value4, str, schemas.Unset] = schemas.unset,
        radius_server_group_id: typing.Union[MetaOapg.properties.radius_server_group_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqSetSsidModeWepRequest':
        return super().__new__(
            cls,
            *_args,
            key_management=key_management,
            encryption_method=encryption_method,
            authentication_method=authentication_method,
            default_key=default_key,
            key_type=key_type,
            key_value=key_value,
            key_value2=key_value2,
            key_value3=key_value3,
            key_value4=key_value4,
            radius_server_group_id=radius_server_group_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_ssid_key_type import XiqSsidKeyType
from extremecloudiq.model.xiq_ssid_wep_authentication_method import XiqSsidWepAuthenticationMethod
from extremecloudiq.model.xiq_ssid_wep_default_key import XiqSsidWepDefaultKey
from extremecloudiq.model.xiq_ssid_wep_encryption_method import XiqSsidWepEncryptionMethod
from extremecloudiq.model.xiq_ssid_wep_key_management import XiqSsidWepKeyManagement
