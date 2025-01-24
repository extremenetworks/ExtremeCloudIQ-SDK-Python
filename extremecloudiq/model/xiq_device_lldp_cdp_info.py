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


class XiqDeviceLldpCdpInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The LLDP/CDP information
    """


    class MetaOapg:
        
        class properties:
            port_id = schemas.StrSchema
            system_id = schemas.StrSchema
            system_name = schemas.StrSchema
            interface_name = schemas.StrSchema
            management_ip = schemas.StrSchema
            port_description = schemas.StrSchema
            __annotations__ = {
                "port_id": port_id,
                "system_id": system_id,
                "system_name": system_name,
                "interface_name": interface_name,
                "management_ip": management_ip,
                "port_description": port_description,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port_id"]) -> MetaOapg.properties.port_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system_id"]) -> MetaOapg.properties.system_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system_name"]) -> MetaOapg.properties.system_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interface_name"]) -> MetaOapg.properties.interface_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["management_ip"]) -> MetaOapg.properties.management_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port_description"]) -> MetaOapg.properties.port_description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["port_id", "system_id", "system_name", "interface_name", "management_ip", "port_description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port_id"]) -> typing.Union[MetaOapg.properties.port_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system_id"]) -> typing.Union[MetaOapg.properties.system_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system_name"]) -> typing.Union[MetaOapg.properties.system_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interface_name"]) -> typing.Union[MetaOapg.properties.interface_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["management_ip"]) -> typing.Union[MetaOapg.properties.management_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port_description"]) -> typing.Union[MetaOapg.properties.port_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["port_id", "system_id", "system_name", "interface_name", "management_ip", "port_description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        port_id: typing.Union[MetaOapg.properties.port_id, str, schemas.Unset] = schemas.unset,
        system_id: typing.Union[MetaOapg.properties.system_id, str, schemas.Unset] = schemas.unset,
        system_name: typing.Union[MetaOapg.properties.system_name, str, schemas.Unset] = schemas.unset,
        interface_name: typing.Union[MetaOapg.properties.interface_name, str, schemas.Unset] = schemas.unset,
        management_ip: typing.Union[MetaOapg.properties.management_ip, str, schemas.Unset] = schemas.unset,
        port_description: typing.Union[MetaOapg.properties.port_description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeviceLldpCdpInfo':
        return super().__new__(
            cls,
            *_args,
            port_id=port_id,
            system_id=system_id,
            system_name=system_name,
            interface_name=interface_name,
            management_ip=management_ip,
            port_description=port_description,
            _configuration=_configuration,
            **kwargs,
        )
