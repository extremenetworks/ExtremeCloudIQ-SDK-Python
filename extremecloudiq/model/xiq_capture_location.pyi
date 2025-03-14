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


class XiqCaptureLocation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This represents the options for location packet capture.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def direction() -> typing.Type['XiqCaptureDirectionSelection']:
                return XiqCaptureDirectionSelection
        
            @staticmethod
            def radio() -> typing.Type['XiqCaptureRadioSelection']:
                return XiqCaptureRadioSelection
        
            @staticmethod
            def wired_interface() -> typing.Type['XiqCaptureWiredSelection']:
                return XiqCaptureWiredSelection
        
            @staticmethod
            def wireless_band() -> typing.Type['XiqCaptureBandSelection']:
                return XiqCaptureBandSelection
            
            
            class wired_filters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqWiredFilterType']:
                        return XiqWiredFilterType
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqWiredFilterType'], typing.List['XiqWiredFilterType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wired_filters':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqWiredFilterType':
                    return super().__getitem__(i)
            
            
            class wireless_filters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqWirelessFilterType']:
                        return XiqWirelessFilterType
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqWirelessFilterType'], typing.List['XiqWirelessFilterType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wireless_filters':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqWirelessFilterType':
                    return super().__getitem__(i)
            __annotations__ = {
                "direction": direction,
                "radio": radio,
                "wired_interface": wired_interface,
                "wireless_band": wireless_band,
                "wired_filters": wired_filters,
                "wireless_filters": wireless_filters,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> 'XiqCaptureDirectionSelection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio"]) -> 'XiqCaptureRadioSelection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wired_interface"]) -> 'XiqCaptureWiredSelection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wireless_band"]) -> 'XiqCaptureBandSelection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wired_filters"]) -> MetaOapg.properties.wired_filters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wireless_filters"]) -> MetaOapg.properties.wireless_filters: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["direction", "radio", "wired_interface", "wireless_band", "wired_filters", "wireless_filters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union['XiqCaptureDirectionSelection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio"]) -> typing.Union['XiqCaptureRadioSelection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wired_interface"]) -> typing.Union['XiqCaptureWiredSelection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wireless_band"]) -> typing.Union['XiqCaptureBandSelection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wired_filters"]) -> typing.Union[MetaOapg.properties.wired_filters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wireless_filters"]) -> typing.Union[MetaOapg.properties.wireless_filters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["direction", "radio", "wired_interface", "wireless_band", "wired_filters", "wireless_filters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        direction: typing.Union['XiqCaptureDirectionSelection', schemas.Unset] = schemas.unset,
        radio: typing.Union['XiqCaptureRadioSelection', schemas.Unset] = schemas.unset,
        wired_interface: typing.Union['XiqCaptureWiredSelection', schemas.Unset] = schemas.unset,
        wireless_band: typing.Union['XiqCaptureBandSelection', schemas.Unset] = schemas.unset,
        wired_filters: typing.Union[MetaOapg.properties.wired_filters, list, tuple, schemas.Unset] = schemas.unset,
        wireless_filters: typing.Union[MetaOapg.properties.wireless_filters, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCaptureLocation':
        return super().__new__(
            cls,
            *_args,
            direction=direction,
            radio=radio,
            wired_interface=wired_interface,
            wireless_band=wireless_band,
            wired_filters=wired_filters,
            wireless_filters=wireless_filters,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_capture_band_selection import XiqCaptureBandSelection
from extremecloudiq.model.xiq_capture_direction_selection import XiqCaptureDirectionSelection
from extremecloudiq.model.xiq_capture_radio_selection import XiqCaptureRadioSelection
from extremecloudiq.model.xiq_capture_wired_selection import XiqCaptureWiredSelection
from extremecloudiq.model.xiq_wired_filter_type import XiqWiredFilterType
from extremecloudiq.model.xiq_wireless_filter_type import XiqWirelessFilterType
