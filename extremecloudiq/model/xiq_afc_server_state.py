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


class XiqAfcServerState(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "CONNECTED": "CONNECTED",
            "DNS_ERROR": "DNS_ERROR",
            "UNREACHABLE": "UNREACHABLE",
            "CONNECTION_REFUSED": "CONNECTION_REFUSED",
            "INVALID_CERT": "INVALID_CERT",
            "REVOKED_CERT": "REVOKED_CERT",
            "NOT_FOUND": "NOT_FOUND",
            "HTTP_ERROR": "HTTP_ERROR",
            "INVALID_RESPONSE": "INVALID_RESPONSE",
            "CONNECTION_RESET": "CONNECTION_RESET",
            "READ_TIMEOUT": "READ_TIMEOUT",
            "UNKNOWN_ERROR": "UNKNOWN_ERROR",
        }
    
    @schemas.classproperty
    def CONNECTED(cls):
        return cls("CONNECTED")
    
    @schemas.classproperty
    def DNS_ERROR(cls):
        return cls("DNS_ERROR")
    
    @schemas.classproperty
    def UNREACHABLE(cls):
        return cls("UNREACHABLE")
    
    @schemas.classproperty
    def CONNECTION_REFUSED(cls):
        return cls("CONNECTION_REFUSED")
    
    @schemas.classproperty
    def INVALID_CERT(cls):
        return cls("INVALID_CERT")
    
    @schemas.classproperty
    def REVOKED_CERT(cls):
        return cls("REVOKED_CERT")
    
    @schemas.classproperty
    def NOT_FOUND(cls):
        return cls("NOT_FOUND")
    
    @schemas.classproperty
    def HTTP_ERROR(cls):
        return cls("HTTP_ERROR")
    
    @schemas.classproperty
    def INVALID_RESPONSE(cls):
        return cls("INVALID_RESPONSE")
    
    @schemas.classproperty
    def CONNECTION_RESET(cls):
        return cls("CONNECTION_RESET")
    
    @schemas.classproperty
    def READ_TIMEOUT(cls):
        return cls("READ_TIMEOUT")
    
    @schemas.classproperty
    def UNKNOWN_ERROR(cls):
        return cls("UNKNOWN_ERROR")
