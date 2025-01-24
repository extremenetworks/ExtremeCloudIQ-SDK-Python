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


class XiqPacketCaptureStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of the packet capture result
    """
    
    @schemas.classproperty
    def INITIAL(cls):
        return cls("INITIAL")
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("ACTIVE")
    
    @schemas.classproperty
    def SUCCESS(cls):
        return cls("SUCCESS")
    
    @schemas.classproperty
    def PARTIAL_SUCCESS(cls):
        return cls("PARTIAL_SUCCESS")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
