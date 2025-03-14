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


class XiqIpFirewallRuleRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of IP Firewall Rules.....
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def action() -> typing.Type['XiqIpFirewallAction']:
                return XiqIpFirewallAction
            service_id = schemas.Int64Schema
            source_ip_id = schemas.Int64Schema
            destination_ip_id = schemas.Int64Schema
        
            @staticmethod
            def logging_type() -> typing.Type['XiqLoggingType']:
                return XiqLoggingType
            __annotations__ = {
                "action": action,
                "service_id": service_id,
                "source_ip_id": source_ip_id,
                "destination_ip_id": destination_ip_id,
                "logging_type": logging_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> 'XiqIpFirewallAction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service_id"]) -> MetaOapg.properties.service_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_ip_id"]) -> MetaOapg.properties.source_ip_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination_ip_id"]) -> MetaOapg.properties.destination_ip_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logging_type"]) -> 'XiqLoggingType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["action", "service_id", "source_ip_id", "destination_ip_id", "logging_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union['XiqIpFirewallAction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service_id"]) -> typing.Union[MetaOapg.properties.service_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_ip_id"]) -> typing.Union[MetaOapg.properties.source_ip_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination_ip_id"]) -> typing.Union[MetaOapg.properties.destination_ip_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logging_type"]) -> typing.Union['XiqLoggingType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["action", "service_id", "source_ip_id", "destination_ip_id", "logging_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union['XiqIpFirewallAction', schemas.Unset] = schemas.unset,
        service_id: typing.Union[MetaOapg.properties.service_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        source_ip_id: typing.Union[MetaOapg.properties.source_ip_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        destination_ip_id: typing.Union[MetaOapg.properties.destination_ip_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        logging_type: typing.Union['XiqLoggingType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqIpFirewallRuleRequest':
        return super().__new__(
            cls,
            *_args,
            action=action,
            service_id=service_id,
            source_ip_id=source_ip_id,
            destination_ip_id=destination_ip_id,
            logging_type=logging_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_ip_firewall_action import XiqIpFirewallAction
from extremecloudiq.model.xiq_logging_type import XiqLoggingType
