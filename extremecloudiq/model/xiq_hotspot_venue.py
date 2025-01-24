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


class XiqHotspotVenue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Venue information helps client devices understand the type and nature of the location where the Wi-Fi network is deployed.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def venue_group() -> typing.Type['XiqHotspotVenueGroup']:
                return XiqHotspotVenueGroup
        
            @staticmethod
            def venue_type() -> typing.Type['XiqHotspotVenueType']:
                return XiqHotspotVenueType
            
            
            class names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqHotspotLocalizedName']:
                        return XiqHotspotLocalizedName
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqHotspotLocalizedName'], typing.List['XiqHotspotLocalizedName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'names':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqHotspotLocalizedName':
                    return super().__getitem__(i)
            __annotations__ = {
                "venue_group": venue_group,
                "venue_type": venue_type,
                "names": names,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["venue_group"]) -> 'XiqHotspotVenueGroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["venue_type"]) -> 'XiqHotspotVenueType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["names"]) -> MetaOapg.properties.names: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["venue_group", "venue_type", "names", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["venue_group"]) -> typing.Union['XiqHotspotVenueGroup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["venue_type"]) -> typing.Union['XiqHotspotVenueType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["names"]) -> typing.Union[MetaOapg.properties.names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["venue_group", "venue_type", "names", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        venue_group: typing.Union['XiqHotspotVenueGroup', schemas.Unset] = schemas.unset,
        venue_type: typing.Union['XiqHotspotVenueType', schemas.Unset] = schemas.unset,
        names: typing.Union[MetaOapg.properties.names, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHotspotVenue':
        return super().__new__(
            cls,
            *_args,
            venue_group=venue_group,
            venue_type=venue_type,
            names=names,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_hotspot_localized_name import XiqHotspotLocalizedName
from extremecloudiq.model.xiq_hotspot_venue_group import XiqHotspotVenueGroup
from extremecloudiq.model.xiq_hotspot_venue_type import XiqHotspotVenueType
