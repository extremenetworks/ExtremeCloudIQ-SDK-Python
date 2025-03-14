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


class XiqCaptureBandSelection(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The wireless band to capture. Set to ALL for all bands.
    """
    
    @schemas.classproperty
    def ALL(cls):
        return cls("ALL")
    
    @schemas.classproperty
    def _4GHZ(cls):
        return cls("2.4GHZ")
    
    @schemas.classproperty
    def GHZ(cls):
        return cls("5GHZ")
    
    @schemas.classproperty
    def GHZ(cls):
        return cls("6GHZ")
