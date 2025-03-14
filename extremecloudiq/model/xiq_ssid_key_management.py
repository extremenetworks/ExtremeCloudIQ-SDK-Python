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


class XiqSsidKeyManagement(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The SSID key management value.
    """


    class MetaOapg:
        enum_value_to_name = {
            "WPA_PSK": "WPA_PSK",
            "WPA2_PSK": "WPA2_PSK",
            "WPA3_PSK": "WPA3_PSK",
            "AUTO_PSK": "AUTO_PSK",
            "WPA_8021X": "WPA_8021X",
            "WPA2_8021X": "WPA2_8021X",
            "WPA3_8021X": "WPA3_8021X",
            "AUTO_8021X": "AUTO_8021X",
            "WEP": "WEP",
            "WEP_8021": "WEP_8021",
        }
    
    @schemas.classproperty
    def WPA_PSK(cls):
        return cls("WPA_PSK")
    
    @schemas.classproperty
    def WPA2_PSK(cls):
        return cls("WPA2_PSK")
    
    @schemas.classproperty
    def WPA3_PSK(cls):
        return cls("WPA3_PSK")
    
    @schemas.classproperty
    def AUTO_PSK(cls):
        return cls("AUTO_PSK")
    
    @schemas.classproperty
    def WPA_8021X(cls):
        return cls("WPA_8021X")
    
    @schemas.classproperty
    def WPA2_8021X(cls):
        return cls("WPA2_8021X")
    
    @schemas.classproperty
    def WPA3_8021X(cls):
        return cls("WPA3_8021X")
    
    @schemas.classproperty
    def AUTO_8021X(cls):
        return cls("AUTO_8021X")
    
    @schemas.classproperty
    def WEP(cls):
        return cls("WEP")
    
    @schemas.classproperty
    def WEP_8021(cls):
        return cls("WEP_8021")
