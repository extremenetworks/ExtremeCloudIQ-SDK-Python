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


class XiqClientMonitorParameters(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This represents the client monitor parameters for a problem type
    """


    class MetaOapg:
        
        class properties:
            
            
            class trigger_times(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 10
                    inclusive_minimum = 1
            
            
            class report_interval(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 3600
                    inclusive_minimum = 30
            __annotations__ = {
                "trigger_times": trigger_times,
                "report_interval": report_interval,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger_times"]) -> MetaOapg.properties.trigger_times: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_interval"]) -> MetaOapg.properties.report_interval: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["trigger_times", "report_interval", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger_times"]) -> typing.Union[MetaOapg.properties.trigger_times, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_interval"]) -> typing.Union[MetaOapg.properties.report_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trigger_times", "report_interval", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        trigger_times: typing.Union[MetaOapg.properties.trigger_times, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        report_interval: typing.Union[MetaOapg.properties.report_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqClientMonitorParameters':
        return super().__new__(
            cls,
            *_args,
            trigger_times=trigger_times,
            report_interval=report_interval,
            _configuration=_configuration,
            **kwargs,
        )
