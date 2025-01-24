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


class XiqDeviceLocationAssignment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Device location assignment
    """


    class MetaOapg:
        required = {
            "location_id",
        }
        
        class properties:
            location_id = schemas.Int64Schema
            x = schemas.Float64Schema
            y = schemas.Float64Schema
            latitude = schemas.Float64Schema
            longitude = schemas.Float64Schema
            __annotations__ = {
                "location_id": location_id,
                "x": x,
                "y": y,
                "latitude": latitude,
                "longitude": longitude,
            }
    
    location_id: MetaOapg.properties.location_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["location_id", "x", "y", "latitude", "longitude", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> typing.Union[MetaOapg.properties.x, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> typing.Union[MetaOapg.properties.y, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> typing.Union[MetaOapg.properties.latitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> typing.Union[MetaOapg.properties.longitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["location_id", "x", "y", "latitude", "longitude", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        latitude: typing.Union[MetaOapg.properties.latitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        longitude: typing.Union[MetaOapg.properties.longitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeviceLocationAssignment':
        return super().__new__(
            cls,
            *_args,
            location_id=location_id,
            x=x,
            y=y,
            latitude=latitude,
            longitude=longitude,
            _configuration=_configuration,
            **kwargs,
        )
