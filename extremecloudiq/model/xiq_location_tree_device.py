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


class XiqLocationTreeDevice(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The device on the location hierarchy.
    """


    class MetaOapg:
        required = {
            "device_name",
            "mac_address",
        }
        
        class properties:
            device_name = schemas.StrSchema
            mac_address = schemas.StrSchema
            serial_number = schemas.StrSchema
            device_function = schemas.StrSchema
            product_type = schemas.StrSchema
            ip_address = schemas.StrSchema
            location_id = schemas.Int64Schema
            map_name = schemas.StrSchema
            x = schemas.Float64Schema
            y = schemas.Float64Schema
            scale_x = schemas.Float64Schema
            scale_y = schemas.Float64Schema
            __annotations__ = {
                "device_name": device_name,
                "mac_address": mac_address,
                "serial_number": serial_number,
                "device_function": device_function,
                "product_type": product_type,
                "ip_address": ip_address,
                "location_id": location_id,
                "map_name": map_name,
                "x": x,
                "y": y,
                "scale_x": scale_x,
                "scale_y": scale_y,
            }
    
    device_name: MetaOapg.properties.device_name
    mac_address: MetaOapg.properties.mac_address
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serial_number"]) -> MetaOapg.properties.serial_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_function"]) -> MetaOapg.properties.device_function: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product_type"]) -> MetaOapg.properties.product_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip_address"]) -> MetaOapg.properties.ip_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_name"]) -> MetaOapg.properties.map_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale_x"]) -> MetaOapg.properties.scale_x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale_y"]) -> MetaOapg.properties.scale_y: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_name", "mac_address", "serial_number", "device_function", "product_type", "ip_address", "location_id", "map_name", "x", "y", "scale_x", "scale_y", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial_number"]) -> typing.Union[MetaOapg.properties.serial_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_function"]) -> typing.Union[MetaOapg.properties.device_function, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product_type"]) -> typing.Union[MetaOapg.properties.product_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip_address"]) -> typing.Union[MetaOapg.properties.ip_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map_name"]) -> typing.Union[MetaOapg.properties.map_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> typing.Union[MetaOapg.properties.x, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> typing.Union[MetaOapg.properties.y, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale_x"]) -> typing.Union[MetaOapg.properties.scale_x, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale_y"]) -> typing.Union[MetaOapg.properties.scale_y, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_name", "mac_address", "serial_number", "device_function", "product_type", "ip_address", "location_id", "map_name", "x", "y", "scale_x", "scale_y", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        device_name: typing.Union[MetaOapg.properties.device_name, str, ],
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, ],
        serial_number: typing.Union[MetaOapg.properties.serial_number, str, schemas.Unset] = schemas.unset,
        device_function: typing.Union[MetaOapg.properties.device_function, str, schemas.Unset] = schemas.unset,
        product_type: typing.Union[MetaOapg.properties.product_type, str, schemas.Unset] = schemas.unset,
        ip_address: typing.Union[MetaOapg.properties.ip_address, str, schemas.Unset] = schemas.unset,
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        map_name: typing.Union[MetaOapg.properties.map_name, str, schemas.Unset] = schemas.unset,
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scale_x: typing.Union[MetaOapg.properties.scale_x, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scale_y: typing.Union[MetaOapg.properties.scale_y, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqLocationTreeDevice':
        return super().__new__(
            cls,
            *_args,
            device_name=device_name,
            mac_address=mac_address,
            serial_number=serial_number,
            device_function=device_function,
            product_type=product_type,
            ip_address=ip_address,
            location_id=location_id,
            map_name=map_name,
            x=x,
            y=y,
            scale_x=scale_x,
            scale_y=scale_y,
            _configuration=_configuration,
            **kwargs,
        )
