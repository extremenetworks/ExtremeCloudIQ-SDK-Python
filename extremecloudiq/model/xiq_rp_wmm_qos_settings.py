# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.2.0.123
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


class XiqRpWmmQosSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload of config for the radio profile
    """


    class MetaOapg:
        required = {
            "update_time",
            "create_time",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            access_category = schemas.StrSchema
            arbitration_interframe_space = schemas.Int32Schema
            min_contention_window = schemas.Int32Schema
            max_contention_window = schemas.Int32Schema
            transmission_opportunity_limit = schemas.Int32Schema
            enable_no_ack = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "access_category": access_category,
                "arbitration_interframe_space": arbitration_interframe_space,
                "min_contention_window": min_contention_window,
                "max_contention_window": max_contention_window,
                "transmission_opportunity_limit": transmission_opportunity_limit,
                "enable_no_ack": enable_no_ack,
            }
    
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_category"]) -> MetaOapg.properties.access_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arbitration_interframe_space"]) -> MetaOapg.properties.arbitration_interframe_space: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_contention_window"]) -> MetaOapg.properties.min_contention_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_contention_window"]) -> MetaOapg.properties.max_contention_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transmission_opportunity_limit"]) -> MetaOapg.properties.transmission_opportunity_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_no_ack"]) -> MetaOapg.properties.enable_no_ack: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "access_category", "arbitration_interframe_space", "min_contention_window", "max_contention_window", "transmission_opportunity_limit", "enable_no_ack", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_category"]) -> typing.Union[MetaOapg.properties.access_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arbitration_interframe_space"]) -> typing.Union[MetaOapg.properties.arbitration_interframe_space, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_contention_window"]) -> typing.Union[MetaOapg.properties.min_contention_window, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_contention_window"]) -> typing.Union[MetaOapg.properties.max_contention_window, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transmission_opportunity_limit"]) -> typing.Union[MetaOapg.properties.transmission_opportunity_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_no_ack"]) -> typing.Union[MetaOapg.properties.enable_no_ack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "access_category", "arbitration_interframe_space", "min_contention_window", "max_contention_window", "transmission_opportunity_limit", "enable_no_ack", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        access_category: typing.Union[MetaOapg.properties.access_category, str, schemas.Unset] = schemas.unset,
        arbitration_interframe_space: typing.Union[MetaOapg.properties.arbitration_interframe_space, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        min_contention_window: typing.Union[MetaOapg.properties.min_contention_window, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_contention_window: typing.Union[MetaOapg.properties.max_contention_window, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transmission_opportunity_limit: typing.Union[MetaOapg.properties.transmission_opportunity_limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_no_ack: typing.Union[MetaOapg.properties.enable_no_ack, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqRpWmmQosSettings':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            access_category=access_category,
            arbitration_interframe_space=arbitration_interframe_space,
            min_contention_window=min_contention_window,
            max_contention_window=max_contention_window,
            transmission_opportunity_limit=transmission_opportunity_limit,
            enable_no_ack=enable_no_ack,
            _configuration=_configuration,
            **kwargs,
        )
