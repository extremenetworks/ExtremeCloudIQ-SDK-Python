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


class XiqClientDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Client Details Info
    """


    class MetaOapg:
        
        class properties:
            device_connected = schemas.BoolSchema
            device_id = schemas.Int64Schema
            os_type = schemas.StrSchema
            ip_address = schemas.StrSchema
            mac_address = schemas.StrSchema
            device_location_names = schemas.StrSchema
            device_location_id = schemas.Int64Schema
            alias = schemas.StrSchema
            user = schemas.StrSchema
            connection_to = schemas.StrSchema
            connection_time = schemas.Int64Schema
            vlan = schemas.Int32Schema
            cwp_used = schemas.Int32Schema
            user_profile = schemas.StrSchema
            ssid = schemas.StrSchema
            radio = schemas.StrSchema
            wifi_protocol = schemas.StrSchema
            channel = schemas.Int32Schema
            client_hostname = schemas.StrSchema
            __annotations__ = {
                "device_connected": device_connected,
                "device_id": device_id,
                "os_type": os_type,
                "ip_address": ip_address,
                "mac_address": mac_address,
                "device_location_names": device_location_names,
                "device_location_id": device_location_id,
                "alias": alias,
                "user": user,
                "connection_to": connection_to,
                "connection_time": connection_time,
                "vlan": vlan,
                "cwp_used": cwp_used,
                "user_profile": user_profile,
                "ssid": ssid,
                "radio": radio,
                "wifi_protocol": wifi_protocol,
                "channel": channel,
                "client_hostname": client_hostname,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_connected"]) -> MetaOapg.properties.device_connected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_type"]) -> MetaOapg.properties.os_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip_address"]) -> MetaOapg.properties.ip_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_location_names"]) -> MetaOapg.properties.device_location_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_location_id"]) -> MetaOapg.properties.device_location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alias"]) -> MetaOapg.properties.alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connection_to"]) -> MetaOapg.properties.connection_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connection_time"]) -> MetaOapg.properties.connection_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vlan"]) -> MetaOapg.properties.vlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cwp_used"]) -> MetaOapg.properties.cwp_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_profile"]) -> MetaOapg.properties.user_profile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssid"]) -> MetaOapg.properties.ssid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio"]) -> MetaOapg.properties.radio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi_protocol"]) -> MetaOapg.properties.wifi_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_hostname"]) -> MetaOapg.properties.client_hostname: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_connected", "device_id", "os_type", "ip_address", "mac_address", "device_location_names", "device_location_id", "alias", "user", "connection_to", "connection_time", "vlan", "cwp_used", "user_profile", "ssid", "radio", "wifi_protocol", "channel", "client_hostname", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_connected"]) -> typing.Union[MetaOapg.properties.device_connected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_type"]) -> typing.Union[MetaOapg.properties.os_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip_address"]) -> typing.Union[MetaOapg.properties.ip_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> typing.Union[MetaOapg.properties.mac_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_location_names"]) -> typing.Union[MetaOapg.properties.device_location_names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_location_id"]) -> typing.Union[MetaOapg.properties.device_location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alias"]) -> typing.Union[MetaOapg.properties.alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connection_to"]) -> typing.Union[MetaOapg.properties.connection_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connection_time"]) -> typing.Union[MetaOapg.properties.connection_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vlan"]) -> typing.Union[MetaOapg.properties.vlan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cwp_used"]) -> typing.Union[MetaOapg.properties.cwp_used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_profile"]) -> typing.Union[MetaOapg.properties.user_profile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssid"]) -> typing.Union[MetaOapg.properties.ssid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio"]) -> typing.Union[MetaOapg.properties.radio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi_protocol"]) -> typing.Union[MetaOapg.properties.wifi_protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_hostname"]) -> typing.Union[MetaOapg.properties.client_hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_connected", "device_id", "os_type", "ip_address", "mac_address", "device_location_names", "device_location_id", "alias", "user", "connection_to", "connection_time", "vlan", "cwp_used", "user_profile", "ssid", "radio", "wifi_protocol", "channel", "client_hostname", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        device_connected: typing.Union[MetaOapg.properties.device_connected, bool, schemas.Unset] = schemas.unset,
        device_id: typing.Union[MetaOapg.properties.device_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        os_type: typing.Union[MetaOapg.properties.os_type, str, schemas.Unset] = schemas.unset,
        ip_address: typing.Union[MetaOapg.properties.ip_address, str, schemas.Unset] = schemas.unset,
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, schemas.Unset] = schemas.unset,
        device_location_names: typing.Union[MetaOapg.properties.device_location_names, str, schemas.Unset] = schemas.unset,
        device_location_id: typing.Union[MetaOapg.properties.device_location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        alias: typing.Union[MetaOapg.properties.alias, str, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        connection_to: typing.Union[MetaOapg.properties.connection_to, str, schemas.Unset] = schemas.unset,
        connection_time: typing.Union[MetaOapg.properties.connection_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        vlan: typing.Union[MetaOapg.properties.vlan, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cwp_used: typing.Union[MetaOapg.properties.cwp_used, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_profile: typing.Union[MetaOapg.properties.user_profile, str, schemas.Unset] = schemas.unset,
        ssid: typing.Union[MetaOapg.properties.ssid, str, schemas.Unset] = schemas.unset,
        radio: typing.Union[MetaOapg.properties.radio, str, schemas.Unset] = schemas.unset,
        wifi_protocol: typing.Union[MetaOapg.properties.wifi_protocol, str, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        client_hostname: typing.Union[MetaOapg.properties.client_hostname, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqClientDetail':
        return super().__new__(
            cls,
            *_args,
            device_connected=device_connected,
            device_id=device_id,
            os_type=os_type,
            ip_address=ip_address,
            mac_address=mac_address,
            device_location_names=device_location_names,
            device_location_id=device_location_id,
            alias=alias,
            user=user,
            connection_to=connection_to,
            connection_time=connection_time,
            vlan=vlan,
            cwp_used=cwp_used,
            user_profile=user_profile,
            ssid=ssid,
            radio=radio,
            wifi_protocol=wifi_protocol,
            channel=channel,
            client_hostname=client_hostname,
            _configuration=_configuration,
            **kwargs,
        )
