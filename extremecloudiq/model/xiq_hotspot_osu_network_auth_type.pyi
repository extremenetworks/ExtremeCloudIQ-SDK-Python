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


class XiqHotspotOsuNetworkAuthType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Network Authentication type for Hotspot profiles.
    """
    
    @schemas.classproperty
    def ACCEPTANCE_TERMS(cls):
        return cls("ACCEPTANCE_TERMS")
    
    @schemas.classproperty
    def ONLINE_SIGN_UP(cls):
        return cls("ONLINE_SIGN_UP")
    
    @schemas.classproperty
    def CWP(cls):
        return cls("CWP")
