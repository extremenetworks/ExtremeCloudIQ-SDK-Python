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


class XiqCopilotMissingVlanSiteDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The list of excluded vlan's site details
    """


    class MetaOapg:
        
        class properties:
            site_id = schemas.Int64Schema
            site_name = schemas.StrSchema
            __annotations__ = {
                "site_id": site_id,
                "site_name": site_name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_id"]) -> MetaOapg.properties.site_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site_name"]) -> MetaOapg.properties.site_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["site_id", "site_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_id"]) -> typing.Union[MetaOapg.properties.site_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site_name"]) -> typing.Union[MetaOapg.properties.site_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["site_id", "site_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        site_id: typing.Union[MetaOapg.properties.site_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        site_name: typing.Union[MetaOapg.properties.site_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCopilotMissingVlanSiteDetails':
        return super().__new__(
            cls,
            *_args,
            site_id=site_id,
            site_name=site_name,
            _configuration=_configuration,
            **kwargs,
        )
