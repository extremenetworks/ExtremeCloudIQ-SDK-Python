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


class XiqPasswordSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The password settings ID
    """


    class MetaOapg:
        required = {
            "psk_generation_method",
            "password_character_types",
            "password_length",
        }
        
        class properties:
        
            @staticmethod
            def psk_generation_method() -> typing.Type['XiqPskGenerationMethod']:
                return XiqPskGenerationMethod
        
            @staticmethod
            def password_character_types() -> typing.Type['XiqPasswordCharacterType']:
                return XiqPasswordCharacterType
            password_length = schemas.Int32Schema
            enable_letters = schemas.BoolSchema
            enable_numbers = schemas.BoolSchema
            enable_special_characters = schemas.BoolSchema
            password_concat_string = schemas.StrSchema
            __annotations__ = {
                "psk_generation_method": psk_generation_method,
                "password_character_types": password_character_types,
                "password_length": password_length,
                "enable_letters": enable_letters,
                "enable_numbers": enable_numbers,
                "enable_special_characters": enable_special_characters,
                "password_concat_string": password_concat_string,
            }
    
    psk_generation_method: 'XiqPskGenerationMethod'
    password_character_types: 'XiqPasswordCharacterType'
    password_length: MetaOapg.properties.password_length
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["psk_generation_method"]) -> 'XiqPskGenerationMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_character_types"]) -> 'XiqPasswordCharacterType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_length"]) -> MetaOapg.properties.password_length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_letters"]) -> MetaOapg.properties.enable_letters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_numbers"]) -> MetaOapg.properties.enable_numbers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_special_characters"]) -> MetaOapg.properties.enable_special_characters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password_concat_string"]) -> MetaOapg.properties.password_concat_string: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["psk_generation_method", "password_character_types", "password_length", "enable_letters", "enable_numbers", "enable_special_characters", "password_concat_string", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["psk_generation_method"]) -> 'XiqPskGenerationMethod': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_character_types"]) -> 'XiqPasswordCharacterType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_length"]) -> MetaOapg.properties.password_length: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_letters"]) -> typing.Union[MetaOapg.properties.enable_letters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_numbers"]) -> typing.Union[MetaOapg.properties.enable_numbers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_special_characters"]) -> typing.Union[MetaOapg.properties.enable_special_characters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password_concat_string"]) -> typing.Union[MetaOapg.properties.password_concat_string, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["psk_generation_method", "password_character_types", "password_length", "enable_letters", "enable_numbers", "enable_special_characters", "password_concat_string", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        psk_generation_method: 'XiqPskGenerationMethod',
        password_character_types: 'XiqPasswordCharacterType',
        password_length: typing.Union[MetaOapg.properties.password_length, decimal.Decimal, int, ],
        enable_letters: typing.Union[MetaOapg.properties.enable_letters, bool, schemas.Unset] = schemas.unset,
        enable_numbers: typing.Union[MetaOapg.properties.enable_numbers, bool, schemas.Unset] = schemas.unset,
        enable_special_characters: typing.Union[MetaOapg.properties.enable_special_characters, bool, schemas.Unset] = schemas.unset,
        password_concat_string: typing.Union[MetaOapg.properties.password_concat_string, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqPasswordSettings':
        return super().__new__(
            cls,
            *_args,
            psk_generation_method=psk_generation_method,
            password_character_types=password_character_types,
            password_length=password_length,
            enable_letters=enable_letters,
            enable_numbers=enable_numbers,
            enable_special_characters=enable_special_characters,
            password_concat_string=password_concat_string,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_password_character_type import XiqPasswordCharacterType
from extremecloudiq.model.xiq_psk_generation_method import XiqPskGenerationMethod
