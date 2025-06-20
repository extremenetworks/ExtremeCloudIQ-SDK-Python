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


class XiqFtmSettingsRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "wgs84_override",
            "zsubelement_override",
            "civic_address_override",
        }
        
        class properties:
            wgs84_override = schemas.BoolSchema
            zsubelement_override = schemas.BoolSchema
            civic_address_override = schemas.BoolSchema
        
            @staticmethod
            def wgs84() -> typing.Type['XiqWgs84']:
                return XiqWgs84
        
            @staticmethod
            def zsubelement() -> typing.Type['XiqZsubelement']:
                return XiqZsubelement
            civic_address = schemas.StrSchema
            __annotations__ = {
                "wgs84_override": wgs84_override,
                "zsubelement_override": zsubelement_override,
                "civic_address_override": civic_address_override,
                "wgs84": wgs84,
                "zsubelement": zsubelement,
                "civic_address": civic_address,
            }
    
    wgs84_override: MetaOapg.properties.wgs84_override
    zsubelement_override: MetaOapg.properties.zsubelement_override
    civic_address_override: MetaOapg.properties.civic_address_override
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wgs84_override"]) -> MetaOapg.properties.wgs84_override: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zsubelement_override"]) -> MetaOapg.properties.zsubelement_override: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["civic_address_override"]) -> MetaOapg.properties.civic_address_override: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wgs84"]) -> 'XiqWgs84': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zsubelement"]) -> 'XiqZsubelement': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["civic_address"]) -> MetaOapg.properties.civic_address: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["wgs84_override", "zsubelement_override", "civic_address_override", "wgs84", "zsubelement", "civic_address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wgs84_override"]) -> MetaOapg.properties.wgs84_override: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zsubelement_override"]) -> MetaOapg.properties.zsubelement_override: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["civic_address_override"]) -> MetaOapg.properties.civic_address_override: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wgs84"]) -> typing.Union['XiqWgs84', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zsubelement"]) -> typing.Union['XiqZsubelement', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["civic_address"]) -> typing.Union[MetaOapg.properties.civic_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["wgs84_override", "zsubelement_override", "civic_address_override", "wgs84", "zsubelement", "civic_address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        wgs84_override: typing.Union[MetaOapg.properties.wgs84_override, bool, ],
        zsubelement_override: typing.Union[MetaOapg.properties.zsubelement_override, bool, ],
        civic_address_override: typing.Union[MetaOapg.properties.civic_address_override, bool, ],
        wgs84: typing.Union['XiqWgs84', schemas.Unset] = schemas.unset,
        zsubelement: typing.Union['XiqZsubelement', schemas.Unset] = schemas.unset,
        civic_address: typing.Union[MetaOapg.properties.civic_address, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqFtmSettingsRequest':
        return super().__new__(
            cls,
            *_args,
            wgs84_override=wgs84_override,
            zsubelement_override=zsubelement_override,
            civic_address_override=civic_address_override,
            wgs84=wgs84,
            zsubelement=zsubelement,
            civic_address=civic_address,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_wgs84 import XiqWgs84
from extremecloudiq.model.xiq_zsubelement import XiqZsubelement
