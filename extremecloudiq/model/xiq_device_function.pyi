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


class XiqDeviceFunction(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The device function, such as AP, Router, Switch, etc.
    """
    
    @schemas.classproperty
    def AP(cls):
        return cls("AP")
    
    @schemas.classproperty
    def ROUTER(cls):
        return cls("ROUTER")
    
    @schemas.classproperty
    def ROUTER_AS_L2_VPN_GATEWAY(cls):
        return cls("ROUTER_AS_L2_VPN_GATEWAY")
    
    @schemas.classproperty
    def ROUTER_AS_L3_VPN_GATEWAY(cls):
        return cls("ROUTER_AS_L3_VPN_GATEWAY")
    
    @schemas.classproperty
    def SWITCH(cls):
        return cls("SWITCH")
    
    @schemas.classproperty
    def SWITCH_HAC(cls):
        return cls("SWITCH_HAC")
    
    @schemas.classproperty
    def SWITCH_DELL(cls):
        return cls("SWITCH_DELL")
    
    @schemas.classproperty
    def L2_VPN_GATEWAY(cls):
        return cls("L2_VPN_GATEWAY")
    
    @schemas.classproperty
    def L3_VPN_GATEWAY(cls):
        return cls("L3_VPN_GATEWAY")
