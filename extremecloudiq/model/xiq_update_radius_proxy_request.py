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


class XiqUpdateRadiusProxyRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload to update RADIUS proxy
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
        
            @staticmethod
            def format_type() -> typing.Type['XiqRadiusProxyFormatType']:
                return XiqRadiusProxyFormatType
            retry_count = schemas.Int32Schema
            retry_delay = schemas.Int32Schema
            dead_time = schemas.Int32Schema
            enable_inject_operator_name_attribute = schemas.BoolSchema
            
            
            class clients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqUpdateRadiusClient']:
                        return XiqUpdateRadiusClient
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqUpdateRadiusClient'], typing.List['XiqUpdateRadiusClient']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clients':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqUpdateRadiusClient':
                    return super().__getitem__(i)
            
            
            class realms(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 2147483647
                    min_items = 2
                    
                    @staticmethod
                    def items() -> typing.Type['XiqUpdateRadiusProxyRealm']:
                        return XiqUpdateRadiusProxyRealm
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqUpdateRadiusProxyRealm'], typing.List['XiqUpdateRadiusProxyRealm']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'realms':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqUpdateRadiusProxyRealm':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "description": description,
                "format_type": format_type,
                "retry_count": retry_count,
                "retry_delay": retry_delay,
                "dead_time": dead_time,
                "enable_inject_operator_name_attribute": enable_inject_operator_name_attribute,
                "clients": clients,
                "realms": realms,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format_type"]) -> 'XiqRadiusProxyFormatType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retry_count"]) -> MetaOapg.properties.retry_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retry_delay"]) -> MetaOapg.properties.retry_delay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dead_time"]) -> MetaOapg.properties.dead_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_inject_operator_name_attribute"]) -> MetaOapg.properties.enable_inject_operator_name_attribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clients"]) -> MetaOapg.properties.clients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realms"]) -> MetaOapg.properties.realms: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "format_type", "retry_count", "retry_delay", "dead_time", "enable_inject_operator_name_attribute", "clients", "realms", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format_type"]) -> typing.Union['XiqRadiusProxyFormatType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retry_count"]) -> typing.Union[MetaOapg.properties.retry_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retry_delay"]) -> typing.Union[MetaOapg.properties.retry_delay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dead_time"]) -> typing.Union[MetaOapg.properties.dead_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_inject_operator_name_attribute"]) -> typing.Union[MetaOapg.properties.enable_inject_operator_name_attribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clients"]) -> typing.Union[MetaOapg.properties.clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realms"]) -> typing.Union[MetaOapg.properties.realms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "format_type", "retry_count", "retry_delay", "dead_time", "enable_inject_operator_name_attribute", "clients", "realms", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        format_type: typing.Union['XiqRadiusProxyFormatType', schemas.Unset] = schemas.unset,
        retry_count: typing.Union[MetaOapg.properties.retry_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        retry_delay: typing.Union[MetaOapg.properties.retry_delay, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dead_time: typing.Union[MetaOapg.properties.dead_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_inject_operator_name_attribute: typing.Union[MetaOapg.properties.enable_inject_operator_name_attribute, bool, schemas.Unset] = schemas.unset,
        clients: typing.Union[MetaOapg.properties.clients, list, tuple, schemas.Unset] = schemas.unset,
        realms: typing.Union[MetaOapg.properties.realms, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUpdateRadiusProxyRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            format_type=format_type,
            retry_count=retry_count,
            retry_delay=retry_delay,
            dead_time=dead_time,
            enable_inject_operator_name_attribute=enable_inject_operator_name_attribute,
            clients=clients,
            realms=realms,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_radius_proxy_format_type import XiqRadiusProxyFormatType
from extremecloudiq.model.xiq_update_radius_client import XiqUpdateRadiusClient
from extremecloudiq.model.xiq_update_radius_proxy_realm import XiqUpdateRadiusProxyRealm
