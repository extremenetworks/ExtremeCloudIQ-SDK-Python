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


class XiqDeviceField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
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
    def SERIAL_NUMBER(cls):
        return cls("SERIAL_NUMBER")
    
    @schemas.classproperty
    def SERVICE_TAG(cls):
        return cls("SERVICE_TAG")
    
    @schemas.classproperty
    def MAC_ADDRESS(cls):
        return cls("MAC_ADDRESS")
    
    @schemas.classproperty
    def DEVICE_FUNCTION(cls):
        return cls("DEVICE_FUNCTION")
    
    @schemas.classproperty
    def PRODUCT_TYPE(cls):
        return cls("PRODUCT_TYPE")
    
    @schemas.classproperty
    def HOSTNAME(cls):
        return cls("HOSTNAME")
    
    @schemas.classproperty
    def IP_ADDRESS(cls):
        return cls("IP_ADDRESS")
    
    @schemas.classproperty
    def SOFTWARE_VERSION(cls):
        return cls("SOFTWARE_VERSION")
    
    @schemas.classproperty
    def DEVICE_ADMIN_STATE(cls):
        return cls("DEVICE_ADMIN_STATE")
    
    @schemas.classproperty
    def CONNECTED(cls):
        return cls("CONNECTED")
    
    @schemas.classproperty
    def LAST_CONNECT_TIME(cls):
        return cls("LAST_CONNECT_TIME")
    
    @schemas.classproperty
    def NETWORK_POLICY_NAME(cls):
        return cls("NETWORK_POLICY_NAME")
    
    @schemas.classproperty
    def NETWORK_POLICY_ID(cls):
        return cls("NETWORK_POLICY_ID")
    
    @schemas.classproperty
    def NTP_SERVER_ADDRESS(cls):
        return cls("NTP_SERVER_ADDRESS")
    
    @schemas.classproperty
    def DNS_SERVER_ADDRESS(cls):
        return cls("DNS_SERVER_ADDRESS")
    
    @schemas.classproperty
    def SUBNET_MASK(cls):
        return cls("SUBNET_MASK")
    
    @schemas.classproperty
    def DEFAULT_GATEWAY(cls):
        return cls("DEFAULT_GATEWAY")
    
    @schemas.classproperty
    def IPV6_ADDRESS(cls):
        return cls("IPV6_ADDRESS")
    
    @schemas.classproperty
    def IPV6_NETMASK(cls):
        return cls("IPV6_NETMASK")
    
    @schemas.classproperty
    def SIMULATED(cls):
        return cls("SIMULATED")
    
    @schemas.classproperty
    def DISPLAY_VERSION(cls):
        return cls("DISPLAY_VERSION")
    
    @schemas.classproperty
    def ACTIVE_CLIENTS(cls):
        return cls("ACTIVE_CLIENTS")
    
    @schemas.classproperty
    def LOCATION_ID(cls):
        return cls("LOCATION_ID")
    
    @schemas.classproperty
    def LOCATIONS(cls):
        return cls("LOCATIONS")
    
    @schemas.classproperty
    def DESCRIPTION(cls):
        return cls("DESCRIPTION")
    
    @schemas.classproperty
    def COUNTRY_CODE(cls):
        return cls("COUNTRY_CODE")
    
    @schemas.classproperty
    def LLDP_CDP_INFO(cls):
        return cls("LLDP_CDP_INFO")
    
    @schemas.classproperty
    def SYSTEM_UP_TIME(cls):
        return cls("SYSTEM_UP_TIME")
    
    @schemas.classproperty
    def CONFIG_MISMATCH(cls):
        return cls("CONFIG_MISMATCH")
    
    @schemas.classproperty
    def MANAGED_BY(cls):
        return cls("MANAGED_BY")
    
    @schemas.classproperty
    def THREAD_EUI64(cls):
        return cls("THREAD_EUI64")
    
    @schemas.classproperty
    def THREAD_EXT_MAC(cls):
        return cls("THREAD_EXT_MAC")
