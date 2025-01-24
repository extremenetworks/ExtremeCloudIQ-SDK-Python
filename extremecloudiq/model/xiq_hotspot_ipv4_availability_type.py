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


class XiqHotspotIpv4AvailabilityType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The IPv4 address availability type.
    """


    class MetaOapg:
        enum_value_to_name = {
            "NOT_AVAILABLE": "NOT_AVAILABLE",
            "PUBLIC": "PUBLIC",
            "PORT_RESTRICTED": "PORT_RESTRICTED",
            "SINGLE_NAT": "SINGLE_NAT",
            "DOUBLE_NAT": "DOUBLE_NAT",
            "PORT_RESTRICTED_SINGLE_NAT": "PORT_RESTRICTED_SINGLE_NAT",
            "PORT_RESTRICTED_DOUBLE_NAT": "PORT_RESTRICTED_DOUBLE_NAT",
            "UNKNOWN": "UNKNOWN",
        }
    
    @schemas.classproperty
    def NOT_AVAILABLE(cls):
        return cls("NOT_AVAILABLE")
    
    @schemas.classproperty
    def PUBLIC(cls):
        return cls("PUBLIC")
    
    @schemas.classproperty
    def PORT_RESTRICTED(cls):
        return cls("PORT_RESTRICTED")
    
    @schemas.classproperty
    def SINGLE_NAT(cls):
        return cls("SINGLE_NAT")
    
    @schemas.classproperty
    def DOUBLE_NAT(cls):
        return cls("DOUBLE_NAT")
    
    @schemas.classproperty
    def PORT_RESTRICTED_SINGLE_NAT(cls):
        return cls("PORT_RESTRICTED_SINGLE_NAT")
    
    @schemas.classproperty
    def PORT_RESTRICTED_DOUBLE_NAT(cls):
        return cls("PORT_RESTRICTED_DOUBLE_NAT")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
