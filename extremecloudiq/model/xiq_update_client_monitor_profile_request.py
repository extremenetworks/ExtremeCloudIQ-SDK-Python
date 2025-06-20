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


class XiqUpdateClientMonitorProfileRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
                    min_length = 1
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 0
        
            @staticmethod
            def association() -> typing.Type['XiqClientMonitorParameters']:
                return XiqClientMonitorParameters
        
            @staticmethod
            def authentication() -> typing.Type['XiqClientMonitorParameters']:
                return XiqClientMonitorParameters
        
            @staticmethod
            def networking() -> typing.Type['XiqClientMonitorParameters']:
                return XiqClientMonitorParameters
            __annotations__ = {
                "name": name,
                "description": description,
                "association": association,
                "authentication": authentication,
                "networking": networking,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["association"]) -> 'XiqClientMonitorParameters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication"]) -> 'XiqClientMonitorParameters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networking"]) -> 'XiqClientMonitorParameters': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "association", "authentication", "networking", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["association"]) -> typing.Union['XiqClientMonitorParameters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication"]) -> typing.Union['XiqClientMonitorParameters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networking"]) -> typing.Union['XiqClientMonitorParameters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "association", "authentication", "networking", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        association: typing.Union['XiqClientMonitorParameters', schemas.Unset] = schemas.unset,
        authentication: typing.Union['XiqClientMonitorParameters', schemas.Unset] = schemas.unset,
        networking: typing.Union['XiqClientMonitorParameters', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUpdateClientMonitorProfileRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            association=association,
            authentication=authentication,
            networking=networking,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_client_monitor_parameters import XiqClientMonitorParameters
