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


class XiqClientHealthSortField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "OPERATING_SYSTEM": "OPERATING_SYSTEM",
            "FREQUENCY": "FREQUENCY",
            "SSID": "SSID",
            "CONNECTION_STATUS": "CONNECTION_STATUS",
            "ALIAS": "ALIAS",
            "CLIENT_MAC": "CLIENT_MAC",
            "CATEGORY_ASSIGNMENT": "CATEGORY_ASSIGNMENT",
            "USER_PROFILE": "USER_PROFILE",
            "CLIENT_IP": "CLIENT_IP",
            "CONNECTED_DEVICE_MAC": "CONNECTED_DEVICE_MAC",
            "ENCRYPTION": "ENCRYPTION",
            "IPV4": "IPV4",
            "IPV6": "IPV6",
            "VLAN": "VLAN",
            "RSSI": "RSSI",
            "SNR": "SNR",
            "AIR_TIME": "AIR_TIME",
            "CLIENT_DEVICE_ID": "CLIENT_DEVICE_ID",
            "RX_CLIENT_RETIRES": "RX_CLIENT_RETIRES",
            "TX_CLIENT_RETIRES": "TX_CLIENT_RETIRES",
            "AUTHENTICATION": "AUTHENTICATION",
        }
    
    @schemas.classproperty
    def OPERATING_SYSTEM(cls):
        return cls("OPERATING_SYSTEM")
    
    @schemas.classproperty
    def FREQUENCY(cls):
        return cls("FREQUENCY")
    
    @schemas.classproperty
    def SSID(cls):
        return cls("SSID")
    
    @schemas.classproperty
    def CONNECTION_STATUS(cls):
        return cls("CONNECTION_STATUS")
    
    @schemas.classproperty
    def ALIAS(cls):
        return cls("ALIAS")
    
    @schemas.classproperty
    def CLIENT_MAC(cls):
        return cls("CLIENT_MAC")
    
    @schemas.classproperty
    def CATEGORY_ASSIGNMENT(cls):
        return cls("CATEGORY_ASSIGNMENT")
    
    @schemas.classproperty
    def USER_PROFILE(cls):
        return cls("USER_PROFILE")
    
    @schemas.classproperty
    def CLIENT_IP(cls):
        return cls("CLIENT_IP")
    
    @schemas.classproperty
    def CONNECTED_DEVICE_MAC(cls):
        return cls("CONNECTED_DEVICE_MAC")
    
    @schemas.classproperty
    def ENCRYPTION(cls):
        return cls("ENCRYPTION")
    
    @schemas.classproperty
    def IPV4(cls):
        return cls("IPV4")
    
    @schemas.classproperty
    def IPV6(cls):
        return cls("IPV6")
    
    @schemas.classproperty
    def VLAN(cls):
        return cls("VLAN")
    
    @schemas.classproperty
    def RSSI(cls):
        return cls("RSSI")
    
    @schemas.classproperty
    def SNR(cls):
        return cls("SNR")
    
    @schemas.classproperty
    def AIR_TIME(cls):
        return cls("AIR_TIME")
    
    @schemas.classproperty
    def CLIENT_DEVICE_ID(cls):
        return cls("CLIENT_DEVICE_ID")
    
    @schemas.classproperty
    def RX_CLIENT_RETIRES(cls):
        return cls("RX_CLIENT_RETIRES")
    
    @schemas.classproperty
    def TX_CLIENT_RETIRES(cls):
        return cls("TX_CLIENT_RETIRES")
    
    @schemas.classproperty
    def AUTHENTICATION(cls):
        return cls("AUTHENTICATION")
