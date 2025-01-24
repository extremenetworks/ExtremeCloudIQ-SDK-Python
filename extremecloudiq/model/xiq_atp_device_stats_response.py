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


class XiqAtpDeviceStatsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Atp Device Stats
    """


    class MetaOapg:
        
        class properties:
            summary = schemas.StrSchema
            
            
            class atp_device_stats_entities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqAtpDeviceStatsEntity']:
                        return XiqAtpDeviceStatsEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqAtpDeviceStatsEntity'], typing.List['XiqAtpDeviceStatsEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'atp_device_stats_entities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqAtpDeviceStatsEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "summary": summary,
                "atp_device_stats_entities": atp_device_stats_entities,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["atp_device_stats_entities"]) -> MetaOapg.properties.atp_device_stats_entities: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "atp_device_stats_entities", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["atp_device_stats_entities"]) -> typing.Union[MetaOapg.properties.atp_device_stats_entities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "atp_device_stats_entities", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        atp_device_stats_entities: typing.Union[MetaOapg.properties.atp_device_stats_entities, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAtpDeviceStatsResponse':
        return super().__new__(
            cls,
            *_args,
            summary=summary,
            atp_device_stats_entities=atp_device_stats_entities,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_atp_device_stats_entity import XiqAtpDeviceStatsEntity
