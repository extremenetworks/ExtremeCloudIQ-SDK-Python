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


class XiqWirelessClient(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ExtremeCloud IQ BSS and Network Data
    """


    class MetaOapg:
        
        class properties:
            network_policy_name = schemas.StrSchema
            ssid = schemas.StrSchema
        
            @staticmethod
            def ssid_status() -> typing.Type['XiqSsidStatus']:
                return XiqSsidStatus
        
            @staticmethod
            def ssid_security_type() -> typing.Type['XiqSsidAccessSecurityType']:
                return XiqSsidAccessSecurityType
            __annotations__ = {
                "network_policy_name": network_policy_name,
                "ssid": ssid,
                "ssid_status": ssid_status,
                "ssid_security_type": ssid_security_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_policy_name"]) -> MetaOapg.properties.network_policy_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid"]) -> MetaOapg.properties.ssid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid_status"]) -> 'XiqSsidStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid_security_type"]) -> 'XiqSsidAccessSecurityType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["network_policy_name", "ssid", "ssid_status", "ssid_security_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_policy_name"]) -> typing.Union[MetaOapg.properties.network_policy_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid"]) -> typing.Union[MetaOapg.properties.ssid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid_status"]) -> typing.Union['XiqSsidStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid_security_type"]) -> typing.Union['XiqSsidAccessSecurityType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["network_policy_name", "ssid", "ssid_status", "ssid_security_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        network_policy_name: typing.Union[MetaOapg.properties.network_policy_name, str, schemas.Unset] = schemas.unset,
        ssid: typing.Union[MetaOapg.properties.ssid, str, schemas.Unset] = schemas.unset,
        ssid_status: typing.Union['XiqSsidStatus', schemas.Unset] = schemas.unset,
        ssid_security_type: typing.Union['XiqSsidAccessSecurityType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWirelessClient':
        return super().__new__(
            cls,
            *_args,
            network_policy_name=network_policy_name,
            ssid=ssid,
            ssid_status=ssid_status,
            ssid_security_type=ssid_security_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_ssid_access_security_type import XiqSsidAccessSecurityType
from extremecloudiq.model.xiq_ssid_status import XiqSsidStatus
