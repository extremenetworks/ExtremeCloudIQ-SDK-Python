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


class XiqHotspotOnlineSignup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Hotspot profile Online Signup settings.
    """


    class MetaOapg:
        required = {
            "network_auth_type",
        }
        
        class properties:
        
            @staticmethod
            def network_auth_type() -> typing.Type['XiqHotspotOsuNetworkAuthType']:
                return XiqHotspotOsuNetworkAuthType
            
            
            class redirection_url(
                schemas.StrSchema
            ):
                pass
            ssid_id = schemas.Int64Schema
            __annotations__ = {
                "network_auth_type": network_auth_type,
                "redirection_url": redirection_url,
                "ssid_id": ssid_id,
            }
    
    network_auth_type: 'XiqHotspotOsuNetworkAuthType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_auth_type"]) -> 'XiqHotspotOsuNetworkAuthType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirection_url"]) -> MetaOapg.properties.redirection_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid_id"]) -> MetaOapg.properties.ssid_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["network_auth_type", "redirection_url", "ssid_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_auth_type"]) -> 'XiqHotspotOsuNetworkAuthType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirection_url"]) -> typing.Union[MetaOapg.properties.redirection_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid_id"]) -> typing.Union[MetaOapg.properties.ssid_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["network_auth_type", "redirection_url", "ssid_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        network_auth_type: 'XiqHotspotOsuNetworkAuthType',
        redirection_url: typing.Union[MetaOapg.properties.redirection_url, str, schemas.Unset] = schemas.unset,
        ssid_id: typing.Union[MetaOapg.properties.ssid_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHotspotOnlineSignup':
        return super().__new__(
            cls,
            *_args,
            network_auth_type=network_auth_type,
            redirection_url=redirection_url,
            ssid_id=ssid_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_hotspot_osu_network_auth_type import XiqHotspotOsuNetworkAuthType
