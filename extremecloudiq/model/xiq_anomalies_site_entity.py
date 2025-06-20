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


class XiqAnomaliesSiteEntity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Anomalies By Site
    """


    class MetaOapg:
        
        class properties:
            building_id = schemas.Int64Schema
            location_name = schemas.StrSchema
            anomalies_count_by_location = schemas.Int32Schema
            __annotations__ = {
                "building_id": building_id,
                "location_name": location_name,
                "anomalies_count_by_location": anomalies_count_by_location,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["building_id"]) -> MetaOapg.properties.building_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_name"]) -> MetaOapg.properties.location_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomalies_count_by_location"]) -> MetaOapg.properties.anomalies_count_by_location: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["building_id", "location_name", "anomalies_count_by_location", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["building_id"]) -> typing.Union[MetaOapg.properties.building_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_name"]) -> typing.Union[MetaOapg.properties.location_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomalies_count_by_location"]) -> typing.Union[MetaOapg.properties.anomalies_count_by_location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building_id", "location_name", "anomalies_count_by_location", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        building_id: typing.Union[MetaOapg.properties.building_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        location_name: typing.Union[MetaOapg.properties.location_name, str, schemas.Unset] = schemas.unset,
        anomalies_count_by_location: typing.Union[MetaOapg.properties.anomalies_count_by_location, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAnomaliesSiteEntity':
        return super().__new__(
            cls,
            *_args,
            building_id=building_id,
            location_name=location_name,
            anomalies_count_by_location=anomalies_count_by_location,
            _configuration=_configuration,
            **kwargs,
        )
