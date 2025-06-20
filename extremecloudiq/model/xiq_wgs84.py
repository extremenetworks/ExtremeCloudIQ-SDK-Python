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


class XiqWgs84(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload of WGS84 Settings
    """


    class MetaOapg:
        required = {
            "altitude",
            "latitude",
            "longitude",
        }
        
        class properties:
            latitude = schemas.Float64Schema
            longitude = schemas.Float64Schema
            altitude = schemas.Float64Schema
            __annotations__ = {
                "latitude": latitude,
                "longitude": longitude,
                "altitude": altitude,
            }
    
    altitude: MetaOapg.properties.altitude
    latitude: MetaOapg.properties.latitude
    longitude: MetaOapg.properties.longitude
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["altitude"]) -> MetaOapg.properties.altitude: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["latitude", "longitude", "altitude", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["altitude"]) -> MetaOapg.properties.altitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["latitude", "longitude", "altitude", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        altitude: typing.Union[MetaOapg.properties.altitude, decimal.Decimal, int, float, ],
        latitude: typing.Union[MetaOapg.properties.latitude, decimal.Decimal, int, float, ],
        longitude: typing.Union[MetaOapg.properties.longitude, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWgs84':
        return super().__new__(
            cls,
            *_args,
            altitude=altitude,
            latitude=latitude,
            longitude=longitude,
            _configuration=_configuration,
            **kwargs,
        )
