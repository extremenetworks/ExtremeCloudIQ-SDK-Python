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


class XiqSsidEncryptionMethod(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The SSID encryption method.
    """
    
    @schemas.classproperty
    def CCMP(cls):
        return cls("CCMP")
    
    @schemas.classproperty
    def TKIP(cls):
        return cls("TKIP")
    
    @schemas.classproperty
    def AUTO_TKIP_CCMP(cls):
        return cls("AUTO_TKIP_CCMP")
    
    @schemas.classproperty
    def WEP40(cls):
        return cls("WEP40")
    
    @schemas.classproperty
    def WEP104(cls):
        return cls("WEP104")
    
    @schemas.classproperty
    def AES192(cls):
        return cls("AES192")
