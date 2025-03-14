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


class XiqDigitalTwinDevice(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Digital Twin device to onboard.
    """


    class MetaOapg:
        required = {
            "os_version",
            "model",
            "make",
        }
        
        class properties:
        
            @staticmethod
            def make() -> typing.Type['XiqDigitalTwinMake']:
                return XiqDigitalTwinMake
        
            @staticmethod
            def model() -> typing.Type['XiqDigitalTwinModel']:
                return XiqDigitalTwinModel
            os_version = schemas.StrSchema
            os_type = schemas.StrSchema
            
            
            class vim_modules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqDigitalTwinVimModule']:
                        return XiqDigitalTwinVimModule
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqDigitalTwinVimModule'], typing.List['XiqDigitalTwinVimModule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vim_modules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqDigitalTwinVimModule':
                    return super().__getitem__(i)
            
            
            class feat_licenses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqDigitalTwinFeatLicense']:
                        return XiqDigitalTwinFeatLicense
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqDigitalTwinFeatLicense'], typing.List['XiqDigitalTwinFeatLicense']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'feat_licenses':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqDigitalTwinFeatLicense':
                    return super().__getitem__(i)
            __annotations__ = {
                "make": make,
                "model": model,
                "os_version": os_version,
                "os_type": os_type,
                "vim_modules": vim_modules,
                "feat_licenses": feat_licenses,
            }
    
    os_version: MetaOapg.properties.os_version
    model: 'XiqDigitalTwinModel'
    make: 'XiqDigitalTwinMake'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["make"]) -> 'XiqDigitalTwinMake': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> 'XiqDigitalTwinModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_version"]) -> MetaOapg.properties.os_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_type"]) -> MetaOapg.properties.os_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vim_modules"]) -> MetaOapg.properties.vim_modules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feat_licenses"]) -> MetaOapg.properties.feat_licenses: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["make", "model", "os_version", "os_type", "vim_modules", "feat_licenses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["make"]) -> 'XiqDigitalTwinMake': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> 'XiqDigitalTwinModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_version"]) -> MetaOapg.properties.os_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_type"]) -> typing.Union[MetaOapg.properties.os_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vim_modules"]) -> typing.Union[MetaOapg.properties.vim_modules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feat_licenses"]) -> typing.Union[MetaOapg.properties.feat_licenses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["make", "model", "os_version", "os_type", "vim_modules", "feat_licenses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        os_version: typing.Union[MetaOapg.properties.os_version, str, ],
        model: 'XiqDigitalTwinModel',
        make: 'XiqDigitalTwinMake',
        os_type: typing.Union[MetaOapg.properties.os_type, str, schemas.Unset] = schemas.unset,
        vim_modules: typing.Union[MetaOapg.properties.vim_modules, list, tuple, schemas.Unset] = schemas.unset,
        feat_licenses: typing.Union[MetaOapg.properties.feat_licenses, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDigitalTwinDevice':
        return super().__new__(
            cls,
            *_args,
            os_version=os_version,
            model=model,
            make=make,
            os_type=os_type,
            vim_modules=vim_modules,
            feat_licenses=feat_licenses,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_digital_twin_feat_license import XiqDigitalTwinFeatLicense
from extremecloudiq.model.xiq_digital_twin_make import XiqDigitalTwinMake
from extremecloudiq.model.xiq_digital_twin_model import XiqDigitalTwinModel
from extremecloudiq.model.xiq_digital_twin_vim_module import XiqDigitalTwinVimModule
