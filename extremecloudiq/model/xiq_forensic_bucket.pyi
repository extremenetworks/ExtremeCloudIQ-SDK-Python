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


class XiqForensicBucket(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def TWENTY_FOUR_HOURS(cls):
        return cls("TWENTY_FOUR_HOURS")
    
    @schemas.classproperty
    def ONE_HOUR(cls):
        return cls("ONE_HOUR")
    
    @schemas.classproperty
    def TODAY(cls):
        return cls("TODAY")
    
    @schemas.classproperty
    def ONE_WEEK(cls):
        return cls("ONE_WEEK")
    
    @schemas.classproperty
    def SEVEN_DAYS(cls):
        return cls("SEVEN_DAYS")
    
    @schemas.classproperty
    def THIRTY_DAYS(cls):
        return cls("THIRTY_DAYS")
    
    @schemas.classproperty
    def NINETY_DAYS(cls):
        return cls("NINETY_DAYS")
