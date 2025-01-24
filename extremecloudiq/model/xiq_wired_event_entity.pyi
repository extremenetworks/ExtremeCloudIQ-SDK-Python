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


class XiqWiredEventEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ Connectivity Experience data
    """


    class MetaOapg:
        
        class properties:
            device_id = schemas.StrSchema
            hostname = schemas.StrSchema
            interface_errors = schemas.Float64Schema
            maximum_errors = schemas.Float64Schema
            mgmt_ip = schemas.StrSchema
            port = schemas.StrSchema
            serial_number = schemas.StrSchema
            __annotations__ = {
                "device_id": device_id,
                "hostname": hostname,
                "interface_errors": interface_errors,
                "maximum_errors": maximum_errors,
                "mgmt_ip": mgmt_ip,
                "port": port,
                "serial_number": serial_number,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interface_errors"]) -> MetaOapg.properties.interface_errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximum_errors"]) -> MetaOapg.properties.maximum_errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mgmt_ip"]) -> MetaOapg.properties.mgmt_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serial_number"]) -> MetaOapg.properties.serial_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "hostname", "interface_errors", "maximum_errors", "mgmt_ip", "port", "serial_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interface_errors"]) -> typing.Union[MetaOapg.properties.interface_errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximum_errors"]) -> typing.Union[MetaOapg.properties.maximum_errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mgmt_ip"]) -> typing.Union[MetaOapg.properties.mgmt_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial_number"]) -> typing.Union[MetaOapg.properties.serial_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "hostname", "interface_errors", "maximum_errors", "mgmt_ip", "port", "serial_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        device_id: typing.Union[MetaOapg.properties.device_id, str, schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        interface_errors: typing.Union[MetaOapg.properties.interface_errors, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maximum_errors: typing.Union[MetaOapg.properties.maximum_errors, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        mgmt_ip: typing.Union[MetaOapg.properties.mgmt_ip, str, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, str, schemas.Unset] = schemas.unset,
        serial_number: typing.Union[MetaOapg.properties.serial_number, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWiredEventEntity':
        return super().__new__(
            cls,
            *_args,
            device_id=device_id,
            hostname=hostname,
            interface_errors=interface_errors,
            maximum_errors=maximum_errors,
            mgmt_ip=mgmt_ip,
            port=port,
            serial_number=serial_number,
            _configuration=_configuration,
            **kwargs,
        )
