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


class XiqFloor(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Floor information on the floorplan.
    """


    class MetaOapg:
        required = {
            "environment",
            "unique_name",
            "update_time",
            "create_time",
            "installation_height",
            "parent_id",
            "db_attenuation",
            "name",
            "measurement_unit",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            parent_id = schemas.Int64Schema
            name = schemas.StrSchema
            unique_name = schemas.StrSchema
        
            @staticmethod
            def environment() -> typing.Type['XiqRfEnvironmentType']:
                return XiqRfEnvironmentType
            db_attenuation = schemas.Float64Schema
        
            @staticmethod
            def measurement_unit() -> typing.Type['XiqMeasurementUnit']:
                return XiqMeasurementUnit
            installation_height = schemas.Float64Schema
            org_id = schemas.Int64Schema
            map_size_width = schemas.Float64Schema
            map_size_height = schemas.Float64Schema
            map_name = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "parent_id": parent_id,
                "name": name,
                "unique_name": unique_name,
                "environment": environment,
                "db_attenuation": db_attenuation,
                "measurement_unit": measurement_unit,
                "installation_height": installation_height,
                "org_id": org_id,
                "map_size_width": map_size_width,
                "map_size_height": map_size_height,
                "map_name": map_name,
            }
    
    environment: 'XiqRfEnvironmentType'
    unique_name: MetaOapg.properties.unique_name
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    installation_height: MetaOapg.properties.installation_height
    parent_id: MetaOapg.properties.parent_id
    db_attenuation: MetaOapg.properties.db_attenuation
    name: MetaOapg.properties.name
    measurement_unit: 'XiqMeasurementUnit'
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unique_name"]) -> MetaOapg.properties.unique_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'XiqRfEnvironmentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["db_attenuation"]) -> MetaOapg.properties.db_attenuation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["measurement_unit"]) -> 'XiqMeasurementUnit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["installation_height"]) -> MetaOapg.properties.installation_height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_size_width"]) -> MetaOapg.properties.map_size_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_size_height"]) -> MetaOapg.properties.map_size_height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_name"]) -> MetaOapg.properties.map_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "parent_id", "name", "unique_name", "environment", "db_attenuation", "measurement_unit", "installation_height", "org_id", "map_size_width", "map_size_height", "map_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unique_name"]) -> MetaOapg.properties.unique_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'XiqRfEnvironmentType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["db_attenuation"]) -> MetaOapg.properties.db_attenuation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["measurement_unit"]) -> 'XiqMeasurementUnit': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["installation_height"]) -> MetaOapg.properties.installation_height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map_size_width"]) -> typing.Union[MetaOapg.properties.map_size_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map_size_height"]) -> typing.Union[MetaOapg.properties.map_size_height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map_name"]) -> typing.Union[MetaOapg.properties.map_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "parent_id", "name", "unique_name", "environment", "db_attenuation", "measurement_unit", "installation_height", "org_id", "map_size_width", "map_size_height", "map_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'XiqRfEnvironmentType',
        unique_name: typing.Union[MetaOapg.properties.unique_name, str, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        installation_height: typing.Union[MetaOapg.properties.installation_height, decimal.Decimal, int, float, ],
        parent_id: typing.Union[MetaOapg.properties.parent_id, decimal.Decimal, int, ],
        db_attenuation: typing.Union[MetaOapg.properties.db_attenuation, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        measurement_unit: 'XiqMeasurementUnit',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        map_size_width: typing.Union[MetaOapg.properties.map_size_width, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        map_size_height: typing.Union[MetaOapg.properties.map_size_height, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        map_name: typing.Union[MetaOapg.properties.map_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqFloor':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            unique_name=unique_name,
            update_time=update_time,
            create_time=create_time,
            installation_height=installation_height,
            parent_id=parent_id,
            db_attenuation=db_attenuation,
            name=name,
            measurement_unit=measurement_unit,
            id=id,
            org_id=org_id,
            map_size_width=map_size_width,
            map_size_height=map_size_height,
            map_name=map_name,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_measurement_unit import XiqMeasurementUnit
from extremecloudiq.model.xiq_rf_environment_type import XiqRfEnvironmentType
