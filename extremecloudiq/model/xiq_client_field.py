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


class XiqClientField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ID": "ID",
            "CREATE_TIME": "CREATE_TIME",
            "UPDATE_TIME": "UPDATE_TIME",
            "ORG_ID": "ORG_ID",
            "ORG_NAME": "ORG_NAME",
            "LOCATION_ID": "LOCATION_ID",
            "LOCATIONS": "LOCATIONS",
            "HOSTNAME": "HOSTNAME",
            "MAC_ADDRESS": "MAC_ADDRESS",
            "IP_ADDRESS": "IP_ADDRESS",
            "IPV6_ADDRESS": "IPV6_ADDRESS",
            "OS_TYPE": "OS_TYPE",
            "DEVICE_ID": "DEVICE_ID",
            "DEVICE_FUNCTION": "DEVICE_FUNCTION",
            "DEVICE_NAME": "DEVICE_NAME",
            "USERNAME": "USERNAME",
            "USER_PROFILE_NAME": "USER_PROFILE_NAME",
            "CONNECTED": "CONNECTED",
            "ONLINE_TIME": "ONLINE_TIME",
            "OFFLINE_TIME": "OFFLINE_TIME",
            "VLAN": "VLAN",
            "CONNECTION_TYPE": "CONNECTION_TYPE",
            "SSID": "SSID",
            "PORT": "PORT",
            "BSSID": "BSSID",
            "PORT_TYPE_NAME": "PORT_TYPE_NAME",
            "INTERFACE_NAME": "INTERFACE_NAME",
            "AUTH": "AUTH",
            "ENCRYPTION_METHOD": "ENCRYPTION_METHOD",
            "CHANNEL": "CHANNEL",
            "CLIENT_HEALTH": "CLIENT_HEALTH",
            "APPLICATION_HEALTH": "APPLICATION_HEALTH",
            "NETWORK_HEALTH": "NETWORK_HEALTH",
            "RADIO_HEALTH": "RADIO_HEALTH",
            "RSSI": "RSSI",
            "SNR": "SNR",
            "RADIO_TYPE": "RADIO_TYPE",
            "WING_AP": "WING_AP",
            "VENDOR": "VENDOR",
            "MOBILITY": "MOBILITY",
            "CATEGORY": "CATEGORY",
            "DESCRIPTION": "DESCRIPTION",
            "DEVICE_MAC_ADDRESS": "DEVICE_MAC_ADDRESS",
            "ALIAS": "ALIAS",
            "PRODUCT_TYPE": "PRODUCT_TYPE",
            "TH_RLOC16": "TH_RLOC16",
            "TH_CHILD_ID": "TH_CHILD_ID",
            "TH_TIMEOUT": "TH_TIMEOUT",
            "TH_SUPERVISION_INTERVAL": "TH_SUPERVISION_INTERVAL",
            "TH_NETDATA_VERSION": "TH_NETDATA_VERSION",
            "TH_CSL_SYNCED": "TH_CSL_SYNCED",
            "TH_IP_ADDRESSES": "TH_IP_ADDRESSES",
            "TH_ROUTER_LAST_REPORTED": "TH_ROUTER_LAST_REPORTED",
            "THREAD_CONNECTED": "THREAD_CONNECTED",
            "MAC_PROTOCOL": "MAC_PROTOCOL",
            "MAKE": "MAKE",
            "OS_VERSION": "OS_VERSION",
            "CONNECTED_TO": "CONNECTED_TO",
            "CONNECTION_DURATION": "CONNECTION_DURATION",
            "CAPTIVE_WEB_PORTAL": "CAPTIVE_WEB_PORTAL",
        }
    
    @schemas.classproperty
    def ID(cls):
        return cls("ID")
    
    @schemas.classproperty
    def CREATE_TIME(cls):
        return cls("CREATE_TIME")
    
    @schemas.classproperty
    def UPDATE_TIME(cls):
        return cls("UPDATE_TIME")
    
    @schemas.classproperty
    def ORG_ID(cls):
        return cls("ORG_ID")
    
    @schemas.classproperty
    def ORG_NAME(cls):
        return cls("ORG_NAME")
    
    @schemas.classproperty
    def LOCATION_ID(cls):
        return cls("LOCATION_ID")
    
    @schemas.classproperty
    def LOCATIONS(cls):
        return cls("LOCATIONS")
    
    @schemas.classproperty
    def HOSTNAME(cls):
        return cls("HOSTNAME")
    
    @schemas.classproperty
    def MAC_ADDRESS(cls):
        return cls("MAC_ADDRESS")
    
    @schemas.classproperty
    def IP_ADDRESS(cls):
        return cls("IP_ADDRESS")
    
    @schemas.classproperty
    def IPV6_ADDRESS(cls):
        return cls("IPV6_ADDRESS")
    
    @schemas.classproperty
    def OS_TYPE(cls):
        return cls("OS_TYPE")
    
    @schemas.classproperty
    def DEVICE_ID(cls):
        return cls("DEVICE_ID")
    
    @schemas.classproperty
    def DEVICE_FUNCTION(cls):
        return cls("DEVICE_FUNCTION")
    
    @schemas.classproperty
    def DEVICE_NAME(cls):
        return cls("DEVICE_NAME")
    
    @schemas.classproperty
    def USERNAME(cls):
        return cls("USERNAME")
    
    @schemas.classproperty
    def USER_PROFILE_NAME(cls):
        return cls("USER_PROFILE_NAME")
    
    @schemas.classproperty
    def CONNECTED(cls):
        return cls("CONNECTED")
    
    @schemas.classproperty
    def ONLINE_TIME(cls):
        return cls("ONLINE_TIME")
    
    @schemas.classproperty
    def OFFLINE_TIME(cls):
        return cls("OFFLINE_TIME")
    
    @schemas.classproperty
    def VLAN(cls):
        return cls("VLAN")
    
    @schemas.classproperty
    def CONNECTION_TYPE(cls):
        return cls("CONNECTION_TYPE")
    
    @schemas.classproperty
    def SSID(cls):
        return cls("SSID")
    
    @schemas.classproperty
    def PORT(cls):
        return cls("PORT")
    
    @schemas.classproperty
    def BSSID(cls):
        return cls("BSSID")
    
    @schemas.classproperty
    def PORT_TYPE_NAME(cls):
        return cls("PORT_TYPE_NAME")
    
    @schemas.classproperty
    def INTERFACE_NAME(cls):
        return cls("INTERFACE_NAME")
    
    @schemas.classproperty
    def AUTH(cls):
        return cls("AUTH")
    
    @schemas.classproperty
    def ENCRYPTION_METHOD(cls):
        return cls("ENCRYPTION_METHOD")
    
    @schemas.classproperty
    def CHANNEL(cls):
        return cls("CHANNEL")
    
    @schemas.classproperty
    def CLIENT_HEALTH(cls):
        return cls("CLIENT_HEALTH")
    
    @schemas.classproperty
    def APPLICATION_HEALTH(cls):
        return cls("APPLICATION_HEALTH")
    
    @schemas.classproperty
    def NETWORK_HEALTH(cls):
        return cls("NETWORK_HEALTH")
    
    @schemas.classproperty
    def RADIO_HEALTH(cls):
        return cls("RADIO_HEALTH")
    
    @schemas.classproperty
    def RSSI(cls):
        return cls("RSSI")
    
    @schemas.classproperty
    def SNR(cls):
        return cls("SNR")
    
    @schemas.classproperty
    def RADIO_TYPE(cls):
        return cls("RADIO_TYPE")
    
    @schemas.classproperty
    def WING_AP(cls):
        return cls("WING_AP")
    
    @schemas.classproperty
    def VENDOR(cls):
        return cls("VENDOR")
    
    @schemas.classproperty
    def MOBILITY(cls):
        return cls("MOBILITY")
    
    @schemas.classproperty
    def CATEGORY(cls):
        return cls("CATEGORY")
    
    @schemas.classproperty
    def DESCRIPTION(cls):
        return cls("DESCRIPTION")
    
    @schemas.classproperty
    def DEVICE_MAC_ADDRESS(cls):
        return cls("DEVICE_MAC_ADDRESS")
    
    @schemas.classproperty
    def ALIAS(cls):
        return cls("ALIAS")
    
    @schemas.classproperty
    def PRODUCT_TYPE(cls):
        return cls("PRODUCT_TYPE")
    
    @schemas.classproperty
    def TH_RLOC16(cls):
        return cls("TH_RLOC16")
    
    @schemas.classproperty
    def TH_CHILD_ID(cls):
        return cls("TH_CHILD_ID")
    
    @schemas.classproperty
    def TH_TIMEOUT(cls):
        return cls("TH_TIMEOUT")
    
    @schemas.classproperty
    def TH_SUPERVISION_INTERVAL(cls):
        return cls("TH_SUPERVISION_INTERVAL")
    
    @schemas.classproperty
    def TH_NETDATA_VERSION(cls):
        return cls("TH_NETDATA_VERSION")
    
    @schemas.classproperty
    def TH_CSL_SYNCED(cls):
        return cls("TH_CSL_SYNCED")
    
    @schemas.classproperty
    def TH_IP_ADDRESSES(cls):
        return cls("TH_IP_ADDRESSES")
    
    @schemas.classproperty
    def TH_ROUTER_LAST_REPORTED(cls):
        return cls("TH_ROUTER_LAST_REPORTED")
    
    @schemas.classproperty
    def THREAD_CONNECTED(cls):
        return cls("THREAD_CONNECTED")
    
    @schemas.classproperty
    def MAC_PROTOCOL(cls):
        return cls("MAC_PROTOCOL")
    
    @schemas.classproperty
    def MAKE(cls):
        return cls("MAKE")
    
    @schemas.classproperty
    def OS_VERSION(cls):
        return cls("OS_VERSION")
    
    @schemas.classproperty
    def CONNECTED_TO(cls):
        return cls("CONNECTED_TO")
    
    @schemas.classproperty
    def CONNECTION_DURATION(cls):
        return cls("CONNECTION_DURATION")
    
    @schemas.classproperty
    def CAPTIVE_WEB_PORTAL(cls):
        return cls("CAPTIVE_WEB_PORTAL")
