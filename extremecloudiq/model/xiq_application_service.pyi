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


class XiqApplicationService(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Application service
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def application() -> typing.Type['XiqApplication']:
                return XiqApplication
            
            
            class service_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NETWORK(cls):
                    return cls("NETWORK")
                
                @schemas.classproperty
                def APPLICATION(cls):
                    return cls("APPLICATION")
            __annotations__ = {
                "application": application,
                "service_type": service_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["application"]) -> 'XiqApplication': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service_type"]) -> MetaOapg.properties.service_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["application", "service_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["application"]) -> typing.Union['XiqApplication', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service_type"]) -> typing.Union[MetaOapg.properties.service_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["application", "service_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        application: typing.Union['XiqApplication', schemas.Unset] = schemas.unset,
        service_type: typing.Union[MetaOapg.properties.service_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqApplicationService':
        return super().__new__(
            cls,
            *_args,
            application=application,
            service_type=service_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_application import XiqApplication
