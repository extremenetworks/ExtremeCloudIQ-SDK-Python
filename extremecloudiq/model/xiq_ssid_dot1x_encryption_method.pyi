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


class XiqSsidDot1xEncryptionMethod(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The encryption method: for WPA_8021X, WPA2_8021X, please use CCMP or TKIP, for AUTO_8021X, please use AUTO_TKIP_CCMP, for WPA3_8021X, please use AES192
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
    def AES192(cls):
        return cls("AES192")
