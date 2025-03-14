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


class XiqSsidAccessSecurityType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The SSID access security type
    """


    class MetaOapg:
        enum_value_to_name = {
            "OPEN": "OPEN",
            "ENHANCED_OPEN": "ENHANCED_OPEN",
            "PPSK": "PPSK",
            "PSK": "PSK",
            "WEP": "WEP",
            "TYPE_802DOT1X": "TYPE_802DOT1X",
        }
    
    @schemas.classproperty
    def OPEN(cls):
        return cls("OPEN")
    
    @schemas.classproperty
    def ENHANCED_OPEN(cls):
        return cls("ENHANCED_OPEN")
    
    @schemas.classproperty
    def PPSK(cls):
        return cls("PPSK")
    
    @schemas.classproperty
    def PSK(cls):
        return cls("PSK")
    
    @schemas.classproperty
    def WEP(cls):
        return cls("WEP")
    
    @schemas.classproperty
    def TYPE_802DOT1X(cls):
        return cls("TYPE_802DOT1X")
