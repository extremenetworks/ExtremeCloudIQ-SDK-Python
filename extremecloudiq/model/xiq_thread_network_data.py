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


class XiqThreadNetworkData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The thread network data
    """


    class MetaOapg:
        
        class properties:
            length = schemas.Int32Schema
            max_length = schemas.Int32Schema
            
            
            class net_data_on_mesh_prefixes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqThreadNetDataPrefix']:
                        return XiqThreadNetDataPrefix
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqThreadNetDataPrefix'], typing.List['XiqThreadNetDataPrefix']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'net_data_on_mesh_prefixes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqThreadNetDataPrefix':
                    return super().__getitem__(i)
            
            
            class net_data_routes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqThreadNetDataRoute']:
                        return XiqThreadNetDataRoute
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqThreadNetDataRoute'], typing.List['XiqThreadNetDataRoute']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'net_data_routes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqThreadNetDataRoute':
                    return super().__getitem__(i)
            
            
            class net_data_services(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqThreadNetDataService']:
                        return XiqThreadNetDataService
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqThreadNetDataService'], typing.List['XiqThreadNetDataService']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'net_data_services':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqThreadNetDataService':
                    return super().__getitem__(i)
            __annotations__ = {
                "length": length,
                "max_length": max_length,
                "net_data_on_mesh_prefixes": net_data_on_mesh_prefixes,
                "net_data_routes": net_data_routes,
                "net_data_services": net_data_services,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_length"]) -> MetaOapg.properties.max_length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_data_on_mesh_prefixes"]) -> MetaOapg.properties.net_data_on_mesh_prefixes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_data_routes"]) -> MetaOapg.properties.net_data_routes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_data_services"]) -> MetaOapg.properties.net_data_services: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["length", "max_length", "net_data_on_mesh_prefixes", "net_data_routes", "net_data_services", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> typing.Union[MetaOapg.properties.length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_length"]) -> typing.Union[MetaOapg.properties.max_length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_data_on_mesh_prefixes"]) -> typing.Union[MetaOapg.properties.net_data_on_mesh_prefixes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_data_routes"]) -> typing.Union[MetaOapg.properties.net_data_routes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_data_services"]) -> typing.Union[MetaOapg.properties.net_data_services, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["length", "max_length", "net_data_on_mesh_prefixes", "net_data_routes", "net_data_services", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_length: typing.Union[MetaOapg.properties.max_length, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        net_data_on_mesh_prefixes: typing.Union[MetaOapg.properties.net_data_on_mesh_prefixes, list, tuple, schemas.Unset] = schemas.unset,
        net_data_routes: typing.Union[MetaOapg.properties.net_data_routes, list, tuple, schemas.Unset] = schemas.unset,
        net_data_services: typing.Union[MetaOapg.properties.net_data_services, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqThreadNetworkData':
        return super().__new__(
            cls,
            *_args,
            length=length,
            max_length=max_length,
            net_data_on_mesh_prefixes=net_data_on_mesh_prefixes,
            net_data_routes=net_data_routes,
            net_data_services=net_data_services,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_thread_net_data_prefix import XiqThreadNetDataPrefix
from extremecloudiq.model.xiq_thread_net_data_route import XiqThreadNetDataRoute
from extremecloudiq.model.xiq_thread_net_data_service import XiqThreadNetDataService
