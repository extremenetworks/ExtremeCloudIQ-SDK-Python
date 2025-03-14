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


class XiqRpMiscellaneousSettings(
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
            sla_throughput_level = schemas.StrSchema
            radio_range = schemas.Int32Schema
            
            
            class wmm_qos_settings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqRpWmmQosSettings']:
                        return XiqRpWmmQosSettings
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqRpWmmQosSettings'], typing.List['XiqRpWmmQosSettings']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wmm_qos_settings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqRpWmmQosSettings':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "sla_throughput_level": sla_throughput_level,
                "radio_range": radio_range,
                "wmm_qos_settings": wmm_qos_settings,
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
    def __getitem__(self, name: typing_extensions.Literal["sla_throughput_level"]) -> MetaOapg.properties.sla_throughput_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio_range"]) -> MetaOapg.properties.radio_range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wmm_qos_settings"]) -> MetaOapg.properties.wmm_qos_settings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "sla_throughput_level", "radio_range", "wmm_qos_settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sla_throughput_level"]) -> typing.Union[MetaOapg.properties.sla_throughput_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio_range"]) -> typing.Union[MetaOapg.properties.radio_range, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wmm_qos_settings"]) -> typing.Union[MetaOapg.properties.wmm_qos_settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "sla_throughput_level", "radio_range", "wmm_qos_settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        sla_throughput_level: typing.Union[MetaOapg.properties.sla_throughput_level, str, schemas.Unset] = schemas.unset,
        radio_range: typing.Union[MetaOapg.properties.radio_range, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wmm_qos_settings: typing.Union[MetaOapg.properties.wmm_qos_settings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqRpMiscellaneousSettings':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            sla_throughput_level=sla_throughput_level,
            radio_range=radio_range,
            wmm_qos_settings=wmm_qos_settings,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_rp_wmm_qos_settings import XiqRpWmmQosSettings
