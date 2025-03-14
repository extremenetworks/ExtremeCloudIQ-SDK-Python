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


class XiqD360FilterType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The filter type
    """
    
    @schemas.classproperty
    def GT(cls):
        return cls("GT")
    
    @schemas.classproperty
    def GTE(cls):
        return cls("GTE")
    
    @schemas.classproperty
    def LT(cls):
        return cls("LT")
    
    @schemas.classproperty
    def LTE(cls):
        return cls("LTE")
    
    @schemas.classproperty
    def EQ(cls):
        return cls("EQ")
    
    @schemas.classproperty
    def NEQ(cls):
        return cls("NEQ")
    
    @schemas.classproperty
    def BTW(cls):
        return cls("BTW")
    
    @schemas.classproperty
    def BLANK(cls):
        return cls("BLANK")
    
    @schemas.classproperty
    def NOT_BLANK(cls):
        return cls("NOT_BLANK")
