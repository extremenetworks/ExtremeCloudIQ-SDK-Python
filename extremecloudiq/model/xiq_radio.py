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


class XiqRadio(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ Radio Information associated to a device
    """


    class MetaOapg:
        required = {
            "mode",
            "name",
            "channel_width",
        }
        
        class properties:
            name = schemas.StrSchema
            channel_width = schemas.StrSchema
            mode = schemas.StrSchema
            channel_number = schemas.Int32Schema
            mac_address = schemas.StrSchema
            power = schemas.Int32Schema
            frequency = schemas.StrSchema
            
            
            class clients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqWirelessClient']:
                        return XiqWirelessClient
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqWirelessClient'], typing.List['XiqWirelessClient']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clients':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqWirelessClient':
                    return super().__getitem__(i)
            
            
            class wlans(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqWirelessWlan']:
                        return XiqWirelessWlan
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqWirelessWlan'], typing.List['XiqWirelessWlan']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wlans':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqWirelessWlan':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "channel_width": channel_width,
                "mode": mode,
                "channel_number": channel_number,
                "mac_address": mac_address,
                "power": power,
                "frequency": frequency,
                "clients": clients,
                "wlans": wlans,
            }
    
    mode: MetaOapg.properties.mode
    name: MetaOapg.properties.name
    channel_width: MetaOapg.properties.channel_width
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_width"]) -> MetaOapg.properties.channel_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_number"]) -> MetaOapg.properties.channel_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["power"]) -> MetaOapg.properties.power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clients"]) -> MetaOapg.properties.clients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wlans"]) -> MetaOapg.properties.wlans: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "channel_width", "mode", "channel_number", "mac_address", "power", "frequency", "clients", "wlans", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_width"]) -> MetaOapg.properties.channel_width: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_number"]) -> typing.Union[MetaOapg.properties.channel_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> typing.Union[MetaOapg.properties.mac_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["power"]) -> typing.Union[MetaOapg.properties.power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clients"]) -> typing.Union[MetaOapg.properties.clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wlans"]) -> typing.Union[MetaOapg.properties.wlans, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "channel_width", "mode", "channel_number", "mac_address", "power", "frequency", "clients", "wlans", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mode: typing.Union[MetaOapg.properties.mode, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        channel_width: typing.Union[MetaOapg.properties.channel_width, str, ],
        channel_number: typing.Union[MetaOapg.properties.channel_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, schemas.Unset] = schemas.unset,
        power: typing.Union[MetaOapg.properties.power, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, str, schemas.Unset] = schemas.unset,
        clients: typing.Union[MetaOapg.properties.clients, list, tuple, schemas.Unset] = schemas.unset,
        wlans: typing.Union[MetaOapg.properties.wlans, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqRadio':
        return super().__new__(
            cls,
            *_args,
            mode=mode,
            name=name,
            channel_width=channel_width,
            channel_number=channel_number,
            mac_address=mac_address,
            power=power,
            frequency=frequency,
            clients=clients,
            wlans=wlans,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_wireless_client import XiqWirelessClient
from extremecloudiq.model.xiq_wireless_wlan import XiqWirelessWlan
