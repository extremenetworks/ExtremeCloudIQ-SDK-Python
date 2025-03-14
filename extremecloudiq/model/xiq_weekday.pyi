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


class XiqWeekday(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The OS object name.
    """
    
    @schemas.classproperty
    def MONDAY(cls):
        return cls("MONDAY")
    
    @schemas.classproperty
    def TUESDAY(cls):
        return cls("TUESDAY")
    
    @schemas.classproperty
    def WEDNESDAY(cls):
        return cls("WEDNESDAY")
    
    @schemas.classproperty
    def THURSDAY(cls):
        return cls("THURSDAY")
    
    @schemas.classproperty
    def FRIDAY(cls):
        return cls("FRIDAY")
    
    @schemas.classproperty
    def SATURDAY(cls):
        return cls("SATURDAY")
    
    @schemas.classproperty
    def SUNDAY(cls):
        return cls("SUNDAY")
