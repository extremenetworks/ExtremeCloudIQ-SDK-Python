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


class XiqHotspotServiceProviderIconFile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The list of localized icon files for the service provider.
    """


    class MetaOapg:
        required = {
            "file",
            "file_directory_name",
        }
        
        class properties:
            
            
            class file_directory_name(
                schemas.StrSchema
            ):
                pass
            
            
            class file(
                schemas.StrSchema
            ):
                pass
            
            
            class language(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "file_directory_name": file_directory_name,
                "file": file,
                "language": language,
            }
    
    file: MetaOapg.properties.file
    file_directory_name: MetaOapg.properties.file_directory_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_directory_name"]) -> MetaOapg.properties.file_directory_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file_directory_name", "file", "language", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_directory_name"]) -> MetaOapg.properties.file_directory_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file_directory_name", "file", "language", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        file: typing.Union[MetaOapg.properties.file, str, ],
        file_directory_name: typing.Union[MetaOapg.properties.file_directory_name, str, ],
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHotspotServiceProviderIconFile':
        return super().__new__(
            cls,
            *_args,
            file=file,
            file_directory_name=file_directory_name,
            language=language,
            _configuration=_configuration,
            **kwargs,
        )
