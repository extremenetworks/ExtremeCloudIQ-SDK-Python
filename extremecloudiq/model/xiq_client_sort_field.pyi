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


class XiqClientSortField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def AUTH_METHOD(cls):
        return cls("AUTH_METHOD")
    
    @schemas.classproperty
    def CHANNEL(cls):
        return cls("CHANNEL")
    
    @schemas.classproperty
    def CONNECTED_VIA(cls):
        return cls("CONNECTED_VIA")
    
    @schemas.classproperty
    def CONNECTION_TYPE(cls):
        return cls("CONNECTION_TYPE")
    
    @schemas.classproperty
    def DEVICE_NAME(cls):
        return cls("DEVICE_NAME")
    
    @schemas.classproperty
    def HOST_NAME(cls):
        return cls("HOST_NAME")
    
    @schemas.classproperty
    def IPV4(cls):
        return cls("IPV4")
    
    @schemas.classproperty
    def IPV6(cls):
        return cls("IPV6")
    
    @schemas.classproperty
    def MAC(cls):
        return cls("MAC")
    
    @schemas.classproperty
    def NAC_DETAILS(cls):
        return cls("NAC_DETAILS")
    
    @schemas.classproperty
    def NAC_PROFILE(cls):
        return cls("NAC_PROFILE")
    
    @schemas.classproperty
    def OS_TYPE(cls):
        return cls("OS_TYPE")
    
    @schemas.classproperty
    def REPORTED_BY(cls):
        return cls("REPORTED_BY")
    
    @schemas.classproperty
    def START_TIME(cls):
        return cls("START_TIME")
    
    @schemas.classproperty
    def USER_NAME(cls):
        return cls("USER_NAME")
    
    @schemas.classproperty
    def USER_PROFILE(cls):
        return cls("USER_PROFILE")
    
    @schemas.classproperty
    def VLAN(cls):
        return cls("VLAN")
    
    @schemas.classproperty
    def TH_RLOC16(cls):
        return cls("TH_RLOC16")
    
    @schemas.classproperty
    def CLIENT_MAC(cls):
        return cls("CLIENT_MAC")
    
    @schemas.classproperty
    def RSSI(cls):
        return cls("RSSI")
    
    @schemas.classproperty
    def DEVICE_MAC(cls):
        return cls("DEVICE_MAC")
