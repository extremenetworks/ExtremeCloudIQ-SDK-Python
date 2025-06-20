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


class XiqDeviceView(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The logic collections of device fields<br/><br/>BASIC: ID, ORG_ID, SERIAL_NUMBER, SERVICE_TAG, MAC_ADDRESS, SIMULATED, DEVICE_FUNCTION, PRODUCT_TYPE, HOSTNAME, IP_ADDRESS, SOFTWARE_VERSION, DEVICE_ADMIN_STATE, CONNECTED, CONFIG_MISMATCH<br>FULL: All fields<br/>STATUS: ID, DEVICE_ADMIN_STATE, CONNECTED<br/>LOCATION: ID, LOCATION_ID, LOCATIONS<br>CLIENT: ID, ACTIVE_CLIENTS<br/>DETAIL: ID, ORG_ID, CREATE_TIME, UPDATE_TIME, SERIAL_NUMBER, SERVICE_TAG, MAC_ADDRESS,SIMULATED, DEVICE_FUNCTION, PRODUCT_TYPE, HOSTNAME, IP_ADDRESS, SOFTWARE_VERSION, DEVICE_ADMIN_STATE, CONNECTED, LAST_CONNECT_TIME, DNS_SERVER_ADDRESS, SUBNET_MASK, DEFAULT_GATEWAY, IPV6_ADDRESS, IPV6_NETMASK, DISPLAY_VERSION ,CONFIG_MISMATCH, THREAD_EUI64, THREAD_EXT_MAC, IMAGES_NAMES, MGT_VLAN, VISIBLE
    """


    class MetaOapg:
        enum_value_to_name = {
            "BASIC": "BASIC",
            "FULL": "FULL",
            "STATUS": "STATUS",
            "LOCATION": "LOCATION",
            "CLIENT": "CLIENT",
            "DETAIL": "DETAIL",
        }
    
    @schemas.classproperty
    def BASIC(cls):
        return cls("BASIC")
    
    @schemas.classproperty
    def FULL(cls):
        return cls("FULL")
    
    @schemas.classproperty
    def STATUS(cls):
        return cls("STATUS")
    
    @schemas.classproperty
    def LOCATION(cls):
        return cls("LOCATION")
    
    @schemas.classproperty
    def CLIENT(cls):
        return cls("CLIENT")
    
    @schemas.classproperty
    def DETAIL(cls):
        return cls("DETAIL")
