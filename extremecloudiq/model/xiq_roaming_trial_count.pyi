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


class XiqRoamingTrialCount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Get roaming trial counts
    """


    class MetaOapg:
        
        class properties:
            roam_completed = schemas.Int64Schema
            roam_failed = schemas.Int64Schema
            __annotations__ = {
                "roam_completed": roam_completed,
                "roam_failed": roam_failed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roam_completed"]) -> MetaOapg.properties.roam_completed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roam_failed"]) -> MetaOapg.properties.roam_failed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["roam_completed", "roam_failed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roam_completed"]) -> typing.Union[MetaOapg.properties.roam_completed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roam_failed"]) -> typing.Union[MetaOapg.properties.roam_failed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["roam_completed", "roam_failed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        roam_completed: typing.Union[MetaOapg.properties.roam_completed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        roam_failed: typing.Union[MetaOapg.properties.roam_failed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqRoamingTrialCount':
        return super().__new__(
            cls,
            *_args,
            roam_completed=roam_completed,
            roam_failed=roam_failed,
            _configuration=_configuration,
            **kwargs,
        )
