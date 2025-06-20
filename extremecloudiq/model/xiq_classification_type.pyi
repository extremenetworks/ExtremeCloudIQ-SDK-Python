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


class XiqClassificationType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Classification type
    """
    
    @schemas.classproperty
    def LOCATION(cls):
        return cls("LOCATION")
    
    @schemas.classproperty
    def CLOUD_CONFIG_GROUP(cls):
        return cls("CLOUD_CONFIG_GROUP")
    
    @schemas.classproperty
    def IP_ADDRESS(cls):
        return cls("IP_ADDRESS")
    
    @schemas.classproperty
    def IP_SUBNET(cls):
        return cls("IP_SUBNET")
    
    @schemas.classproperty
    def IP_RANGE(cls):
        return cls("IP_RANGE")
