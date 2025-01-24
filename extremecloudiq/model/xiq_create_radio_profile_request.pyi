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


class XiqCreateRadioProfileRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class transmission_power(
                schemas.Int32Schema
            ):
                pass
            
            
            class max_transmit_power(
                schemas.Int32Schema
            ):
                pass
            
            
            class transmission_power_floor(
                schemas.Int32Schema
            ):
                pass
            
            
            class transmission_power_max_drop(
                schemas.Int32Schema
            ):
                pass
            
            
            class max_clients(
                schemas.Int32Schema
            ):
                pass
            enable_client_transmission_power = schemas.BoolSchema
            
            
            class client_transmission_power(
                schemas.Int32Schema
            ):
                pass
        
            @staticmethod
            def radio_mode() -> typing.Type['XiqRadioMode']:
                return XiqRadioMode
            enable_ofdma = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "description": description,
                "transmission_power": transmission_power,
                "max_transmit_power": max_transmit_power,
                "transmission_power_floor": transmission_power_floor,
                "transmission_power_max_drop": transmission_power_max_drop,
                "max_clients": max_clients,
                "enable_client_transmission_power": enable_client_transmission_power,
                "client_transmission_power": client_transmission_power,
                "radio_mode": radio_mode,
                "enable_ofdma": enable_ofdma,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transmission_power"]) -> MetaOapg.properties.transmission_power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_transmit_power"]) -> MetaOapg.properties.max_transmit_power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transmission_power_floor"]) -> MetaOapg.properties.transmission_power_floor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transmission_power_max_drop"]) -> MetaOapg.properties.transmission_power_max_drop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_clients"]) -> MetaOapg.properties.max_clients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_client_transmission_power"]) -> MetaOapg.properties.enable_client_transmission_power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_transmission_power"]) -> MetaOapg.properties.client_transmission_power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio_mode"]) -> 'XiqRadioMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_ofdma"]) -> MetaOapg.properties.enable_ofdma: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "transmission_power", "max_transmit_power", "transmission_power_floor", "transmission_power_max_drop", "max_clients", "enable_client_transmission_power", "client_transmission_power", "radio_mode", "enable_ofdma", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transmission_power"]) -> typing.Union[MetaOapg.properties.transmission_power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_transmit_power"]) -> typing.Union[MetaOapg.properties.max_transmit_power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transmission_power_floor"]) -> typing.Union[MetaOapg.properties.transmission_power_floor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transmission_power_max_drop"]) -> typing.Union[MetaOapg.properties.transmission_power_max_drop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_clients"]) -> typing.Union[MetaOapg.properties.max_clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_client_transmission_power"]) -> typing.Union[MetaOapg.properties.enable_client_transmission_power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_transmission_power"]) -> typing.Union[MetaOapg.properties.client_transmission_power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio_mode"]) -> typing.Union['XiqRadioMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_ofdma"]) -> typing.Union[MetaOapg.properties.enable_ofdma, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "transmission_power", "max_transmit_power", "transmission_power_floor", "transmission_power_max_drop", "max_clients", "enable_client_transmission_power", "client_transmission_power", "radio_mode", "enable_ofdma", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        transmission_power: typing.Union[MetaOapg.properties.transmission_power, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_transmit_power: typing.Union[MetaOapg.properties.max_transmit_power, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transmission_power_floor: typing.Union[MetaOapg.properties.transmission_power_floor, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transmission_power_max_drop: typing.Union[MetaOapg.properties.transmission_power_max_drop, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_clients: typing.Union[MetaOapg.properties.max_clients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_client_transmission_power: typing.Union[MetaOapg.properties.enable_client_transmission_power, bool, schemas.Unset] = schemas.unset,
        client_transmission_power: typing.Union[MetaOapg.properties.client_transmission_power, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        radio_mode: typing.Union['XiqRadioMode', schemas.Unset] = schemas.unset,
        enable_ofdma: typing.Union[MetaOapg.properties.enable_ofdma, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCreateRadioProfileRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            transmission_power=transmission_power,
            max_transmit_power=max_transmit_power,
            transmission_power_floor=transmission_power_floor,
            transmission_power_max_drop=transmission_power_max_drop,
            max_clients=max_clients,
            enable_client_transmission_power=enable_client_transmission_power,
            client_transmission_power=client_transmission_power,
            radio_mode=radio_mode,
            enable_ofdma=enable_ofdma,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_radio_mode import XiqRadioMode
