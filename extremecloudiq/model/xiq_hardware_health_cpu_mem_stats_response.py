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


class XiqHardwareHealthCpuMemStatsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Hardware Health Cpu Memory Stats
    """


    class MetaOapg:
        
        class properties:
            
            
            class cpu_mem_stats(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqHhCpuMemStatsEntity']:
                        return XiqHhCpuMemStatsEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqHhCpuMemStatsEntity'], typing.List['XiqHhCpuMemStatsEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cpu_mem_stats':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqHhCpuMemStatsEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "cpu_mem_stats": cpu_mem_stats,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_mem_stats"]) -> MetaOapg.properties.cpu_mem_stats: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cpu_mem_stats", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_mem_stats"]) -> typing.Union[MetaOapg.properties.cpu_mem_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cpu_mem_stats", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cpu_mem_stats: typing.Union[MetaOapg.properties.cpu_mem_stats, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHardwareHealthCpuMemStatsResponse':
        return super().__new__(
            cls,
            *_args,
            cpu_mem_stats=cpu_mem_stats,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_hh_cpu_mem_stats_entity import XiqHhCpuMemStatsEntity
