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


class XiqEkahauFloorToOutdoorSiteAssociation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Association between an Ekahau floor and XIQ outdoor site
    """


    class MetaOapg:
        required = {
            "parentSiteGroupId",
            "countryCode",
            "floorName",
        }
        
        class properties:
            floorName = schemas.StrSchema
            parentSiteGroupId = schemas.Int64Schema
            countryCode = schemas.Int32Schema
            __annotations__ = {
                "floorName": floorName,
                "parentSiteGroupId": parentSiteGroupId,
                "countryCode": countryCode,
            }
    
    parentSiteGroupId: MetaOapg.properties.parentSiteGroupId
    countryCode: MetaOapg.properties.countryCode
    floorName: MetaOapg.properties.floorName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floorName"]) -> MetaOapg.properties.floorName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentSiteGroupId"]) -> MetaOapg.properties.parentSiteGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["floorName", "parentSiteGroupId", "countryCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floorName"]) -> MetaOapg.properties.floorName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentSiteGroupId"]) -> MetaOapg.properties.parentSiteGroupId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["floorName", "parentSiteGroupId", "countryCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        parentSiteGroupId: typing.Union[MetaOapg.properties.parentSiteGroupId, decimal.Decimal, int, ],
        countryCode: typing.Union[MetaOapg.properties.countryCode, decimal.Decimal, int, ],
        floorName: typing.Union[MetaOapg.properties.floorName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqEkahauFloorToOutdoorSiteAssociation':
        return super().__new__(
            cls,
            *_args,
            parentSiteGroupId=parentSiteGroupId,
            countryCode=countryCode,
            floorName=floorName,
            _configuration=_configuration,
            **kwargs,
        )
