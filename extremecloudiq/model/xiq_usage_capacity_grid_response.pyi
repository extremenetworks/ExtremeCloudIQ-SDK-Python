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


class XiqUsageCapacityGridResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The usage & capacity grid of wireless devices
    """


    class MetaOapg:
        
        class properties:
            hostname = schemas.StrSchema
            device_ip = schemas.StrSchema
            site = schemas.StrSchema
            building = schemas.StrSchema
            floor = schemas.StrSchema
            mac_address = schemas.StrSchema
            wifi0_retry_score = schemas.Int64Schema
            wifi1_retry_score = schemas.Int64Schema
            wifi2_retry_score = schemas.Int64Schema
            wifi0_packet_loss = schemas.Int64Schema
            wifi1_packet_loss = schemas.Int64Schema
            wifi2_packet_loss = schemas.Int64Schema
            eth0_unicast_score = schemas.Int64Schema
            eth0_broadcast_score = schemas.Int64Schema
            eth0_multicast_score = schemas.Int64Schema
            eth1_unicast_score = schemas.Int64Schema
            eth1_broadcast_score = schemas.Int64Schema
            eth1_multicast_score = schemas.Int64Schema
            wifi0_interference_score = schemas.Int64Schema
            wifi1_interference_score = schemas.Int64Schema
            wifi2_interference_score = schemas.Int64Schema
            wifi0_noise = schemas.Int64Schema
            wifi1_noise = schemas.Int64Schema
            wifi2_noise = schemas.Int64Schema
            device_id = schemas.Int64Schema
            packet_loss = schemas.Int64Schema
            link_error2_dot4_g = schemas.Int64Schema
            link_error5g = schemas.Int64Schema
            link_error6g = schemas.Int64Schema
            healthy_clients = schemas.Int32Schema
            unhealthy_clients = schemas.Int32Schema
            has_usage_capacity_issue = schemas.BoolSchema
            radio_2dot4g_utilization_score = schemas.Int64Schema
            radio_5g_utilization_score = schemas.Int64Schema
            radio_6g_utilization_score = schemas.Int64Schema
            __annotations__ = {
                "hostname": hostname,
                "device_ip": device_ip,
                "site": site,
                "building": building,
                "floor": floor,
                "mac_address": mac_address,
                "wifi0_retry_score": wifi0_retry_score,
                "wifi1_retry_score": wifi1_retry_score,
                "wifi2_retry_score": wifi2_retry_score,
                "wifi0_packet_loss": wifi0_packet_loss,
                "wifi1_packet_loss": wifi1_packet_loss,
                "wifi2_packet_loss": wifi2_packet_loss,
                "eth0_unicast_score": eth0_unicast_score,
                "eth0_broadcast_score": eth0_broadcast_score,
                "eth0_multicast_score": eth0_multicast_score,
                "eth1_unicast_score": eth1_unicast_score,
                "eth1_broadcast_score": eth1_broadcast_score,
                "eth1_multicast_score": eth1_multicast_score,
                "wifi0_interference_score": wifi0_interference_score,
                "wifi1_interference_score": wifi1_interference_score,
                "wifi2_interference_score": wifi2_interference_score,
                "wifi0_noise": wifi0_noise,
                "wifi1_noise": wifi1_noise,
                "wifi2_noise": wifi2_noise,
                "device_id": device_id,
                "packet_loss": packet_loss,
                "link_error2_dot4_g": link_error2_dot4_g,
                "link_error5g": link_error5g,
                "link_error6g": link_error6g,
                "healthy_clients": healthy_clients,
                "unhealthy_clients": unhealthy_clients,
                "has_usage_capacity_issue": has_usage_capacity_issue,
                "radio_2dot4g_utilization_score": radio_2dot4g_utilization_score,
                "radio_5g_utilization_score": radio_5g_utilization_score,
                "radio_6g_utilization_score": radio_6g_utilization_score,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_ip"]) -> MetaOapg.properties.device_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site"]) -> MetaOapg.properties.site: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["building"]) -> MetaOapg.properties.building: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floor"]) -> MetaOapg.properties.floor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi0_retry_score"]) -> MetaOapg.properties.wifi0_retry_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi1_retry_score"]) -> MetaOapg.properties.wifi1_retry_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi2_retry_score"]) -> MetaOapg.properties.wifi2_retry_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi0_packet_loss"]) -> MetaOapg.properties.wifi0_packet_loss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi1_packet_loss"]) -> MetaOapg.properties.wifi1_packet_loss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi2_packet_loss"]) -> MetaOapg.properties.wifi2_packet_loss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth0_unicast_score"]) -> MetaOapg.properties.eth0_unicast_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth0_broadcast_score"]) -> MetaOapg.properties.eth0_broadcast_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth0_multicast_score"]) -> MetaOapg.properties.eth0_multicast_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth1_unicast_score"]) -> MetaOapg.properties.eth1_unicast_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth1_broadcast_score"]) -> MetaOapg.properties.eth1_broadcast_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth1_multicast_score"]) -> MetaOapg.properties.eth1_multicast_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi0_interference_score"]) -> MetaOapg.properties.wifi0_interference_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi1_interference_score"]) -> MetaOapg.properties.wifi1_interference_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi2_interference_score"]) -> MetaOapg.properties.wifi2_interference_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi0_noise"]) -> MetaOapg.properties.wifi0_noise: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi1_noise"]) -> MetaOapg.properties.wifi1_noise: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi2_noise"]) -> MetaOapg.properties.wifi2_noise: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["packet_loss"]) -> MetaOapg.properties.packet_loss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_error2_dot4_g"]) -> MetaOapg.properties.link_error2_dot4_g: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_error5g"]) -> MetaOapg.properties.link_error5g: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_error6g"]) -> MetaOapg.properties.link_error6g: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["healthy_clients"]) -> MetaOapg.properties.healthy_clients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unhealthy_clients"]) -> MetaOapg.properties.unhealthy_clients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_usage_capacity_issue"]) -> MetaOapg.properties.has_usage_capacity_issue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio_2dot4g_utilization_score"]) -> MetaOapg.properties.radio_2dot4g_utilization_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio_5g_utilization_score"]) -> MetaOapg.properties.radio_5g_utilization_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio_6g_utilization_score"]) -> MetaOapg.properties.radio_6g_utilization_score: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hostname", "device_ip", "site", "building", "floor", "mac_address", "wifi0_retry_score", "wifi1_retry_score", "wifi2_retry_score", "wifi0_packet_loss", "wifi1_packet_loss", "wifi2_packet_loss", "eth0_unicast_score", "eth0_broadcast_score", "eth0_multicast_score", "eth1_unicast_score", "eth1_broadcast_score", "eth1_multicast_score", "wifi0_interference_score", "wifi1_interference_score", "wifi2_interference_score", "wifi0_noise", "wifi1_noise", "wifi2_noise", "device_id", "packet_loss", "link_error2_dot4_g", "link_error5g", "link_error6g", "healthy_clients", "unhealthy_clients", "has_usage_capacity_issue", "radio_2dot4g_utilization_score", "radio_5g_utilization_score", "radio_6g_utilization_score", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_ip"]) -> typing.Union[MetaOapg.properties.device_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site"]) -> typing.Union[MetaOapg.properties.site, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["building"]) -> typing.Union[MetaOapg.properties.building, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floor"]) -> typing.Union[MetaOapg.properties.floor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> typing.Union[MetaOapg.properties.mac_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi0_retry_score"]) -> typing.Union[MetaOapg.properties.wifi0_retry_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi1_retry_score"]) -> typing.Union[MetaOapg.properties.wifi1_retry_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi2_retry_score"]) -> typing.Union[MetaOapg.properties.wifi2_retry_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi0_packet_loss"]) -> typing.Union[MetaOapg.properties.wifi0_packet_loss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi1_packet_loss"]) -> typing.Union[MetaOapg.properties.wifi1_packet_loss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi2_packet_loss"]) -> typing.Union[MetaOapg.properties.wifi2_packet_loss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth0_unicast_score"]) -> typing.Union[MetaOapg.properties.eth0_unicast_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth0_broadcast_score"]) -> typing.Union[MetaOapg.properties.eth0_broadcast_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth0_multicast_score"]) -> typing.Union[MetaOapg.properties.eth0_multicast_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth1_unicast_score"]) -> typing.Union[MetaOapg.properties.eth1_unicast_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth1_broadcast_score"]) -> typing.Union[MetaOapg.properties.eth1_broadcast_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth1_multicast_score"]) -> typing.Union[MetaOapg.properties.eth1_multicast_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi0_interference_score"]) -> typing.Union[MetaOapg.properties.wifi0_interference_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi1_interference_score"]) -> typing.Union[MetaOapg.properties.wifi1_interference_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi2_interference_score"]) -> typing.Union[MetaOapg.properties.wifi2_interference_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi0_noise"]) -> typing.Union[MetaOapg.properties.wifi0_noise, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi1_noise"]) -> typing.Union[MetaOapg.properties.wifi1_noise, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi2_noise"]) -> typing.Union[MetaOapg.properties.wifi2_noise, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["packet_loss"]) -> typing.Union[MetaOapg.properties.packet_loss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_error2_dot4_g"]) -> typing.Union[MetaOapg.properties.link_error2_dot4_g, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_error5g"]) -> typing.Union[MetaOapg.properties.link_error5g, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_error6g"]) -> typing.Union[MetaOapg.properties.link_error6g, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["healthy_clients"]) -> typing.Union[MetaOapg.properties.healthy_clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unhealthy_clients"]) -> typing.Union[MetaOapg.properties.unhealthy_clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_usage_capacity_issue"]) -> typing.Union[MetaOapg.properties.has_usage_capacity_issue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio_2dot4g_utilization_score"]) -> typing.Union[MetaOapg.properties.radio_2dot4g_utilization_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio_5g_utilization_score"]) -> typing.Union[MetaOapg.properties.radio_5g_utilization_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio_6g_utilization_score"]) -> typing.Union[MetaOapg.properties.radio_6g_utilization_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hostname", "device_ip", "site", "building", "floor", "mac_address", "wifi0_retry_score", "wifi1_retry_score", "wifi2_retry_score", "wifi0_packet_loss", "wifi1_packet_loss", "wifi2_packet_loss", "eth0_unicast_score", "eth0_broadcast_score", "eth0_multicast_score", "eth1_unicast_score", "eth1_broadcast_score", "eth1_multicast_score", "wifi0_interference_score", "wifi1_interference_score", "wifi2_interference_score", "wifi0_noise", "wifi1_noise", "wifi2_noise", "device_id", "packet_loss", "link_error2_dot4_g", "link_error5g", "link_error6g", "healthy_clients", "unhealthy_clients", "has_usage_capacity_issue", "radio_2dot4g_utilization_score", "radio_5g_utilization_score", "radio_6g_utilization_score", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        device_ip: typing.Union[MetaOapg.properties.device_ip, str, schemas.Unset] = schemas.unset,
        site: typing.Union[MetaOapg.properties.site, str, schemas.Unset] = schemas.unset,
        building: typing.Union[MetaOapg.properties.building, str, schemas.Unset] = schemas.unset,
        floor: typing.Union[MetaOapg.properties.floor, str, schemas.Unset] = schemas.unset,
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, schemas.Unset] = schemas.unset,
        wifi0_retry_score: typing.Union[MetaOapg.properties.wifi0_retry_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi1_retry_score: typing.Union[MetaOapg.properties.wifi1_retry_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi2_retry_score: typing.Union[MetaOapg.properties.wifi2_retry_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi0_packet_loss: typing.Union[MetaOapg.properties.wifi0_packet_loss, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi1_packet_loss: typing.Union[MetaOapg.properties.wifi1_packet_loss, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi2_packet_loss: typing.Union[MetaOapg.properties.wifi2_packet_loss, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth0_unicast_score: typing.Union[MetaOapg.properties.eth0_unicast_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth0_broadcast_score: typing.Union[MetaOapg.properties.eth0_broadcast_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth0_multicast_score: typing.Union[MetaOapg.properties.eth0_multicast_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth1_unicast_score: typing.Union[MetaOapg.properties.eth1_unicast_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth1_broadcast_score: typing.Union[MetaOapg.properties.eth1_broadcast_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        eth1_multicast_score: typing.Union[MetaOapg.properties.eth1_multicast_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi0_interference_score: typing.Union[MetaOapg.properties.wifi0_interference_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi1_interference_score: typing.Union[MetaOapg.properties.wifi1_interference_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi2_interference_score: typing.Union[MetaOapg.properties.wifi2_interference_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi0_noise: typing.Union[MetaOapg.properties.wifi0_noise, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi1_noise: typing.Union[MetaOapg.properties.wifi1_noise, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wifi2_noise: typing.Union[MetaOapg.properties.wifi2_noise, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        device_id: typing.Union[MetaOapg.properties.device_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        packet_loss: typing.Union[MetaOapg.properties.packet_loss, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        link_error2_dot4_g: typing.Union[MetaOapg.properties.link_error2_dot4_g, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        link_error5g: typing.Union[MetaOapg.properties.link_error5g, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        link_error6g: typing.Union[MetaOapg.properties.link_error6g, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        healthy_clients: typing.Union[MetaOapg.properties.healthy_clients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        unhealthy_clients: typing.Union[MetaOapg.properties.unhealthy_clients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        has_usage_capacity_issue: typing.Union[MetaOapg.properties.has_usage_capacity_issue, bool, schemas.Unset] = schemas.unset,
        radio_2dot4g_utilization_score: typing.Union[MetaOapg.properties.radio_2dot4g_utilization_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        radio_5g_utilization_score: typing.Union[MetaOapg.properties.radio_5g_utilization_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        radio_6g_utilization_score: typing.Union[MetaOapg.properties.radio_6g_utilization_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUsageCapacityGridResponse':
        return super().__new__(
            cls,
            *_args,
            hostname=hostname,
            device_ip=device_ip,
            site=site,
            building=building,
            floor=floor,
            mac_address=mac_address,
            wifi0_retry_score=wifi0_retry_score,
            wifi1_retry_score=wifi1_retry_score,
            wifi2_retry_score=wifi2_retry_score,
            wifi0_packet_loss=wifi0_packet_loss,
            wifi1_packet_loss=wifi1_packet_loss,
            wifi2_packet_loss=wifi2_packet_loss,
            eth0_unicast_score=eth0_unicast_score,
            eth0_broadcast_score=eth0_broadcast_score,
            eth0_multicast_score=eth0_multicast_score,
            eth1_unicast_score=eth1_unicast_score,
            eth1_broadcast_score=eth1_broadcast_score,
            eth1_multicast_score=eth1_multicast_score,
            wifi0_interference_score=wifi0_interference_score,
            wifi1_interference_score=wifi1_interference_score,
            wifi2_interference_score=wifi2_interference_score,
            wifi0_noise=wifi0_noise,
            wifi1_noise=wifi1_noise,
            wifi2_noise=wifi2_noise,
            device_id=device_id,
            packet_loss=packet_loss,
            link_error2_dot4_g=link_error2_dot4_g,
            link_error5g=link_error5g,
            link_error6g=link_error6g,
            healthy_clients=healthy_clients,
            unhealthy_clients=unhealthy_clients,
            has_usage_capacity_issue=has_usage_capacity_issue,
            radio_2dot4g_utilization_score=radio_2dot4g_utilization_score,
            radio_5g_utilization_score=radio_5g_utilization_score,
            radio_6g_utilization_score=radio_6g_utilization_score,
            _configuration=_configuration,
            **kwargs,
        )
