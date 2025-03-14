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


class XiqUserRole(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The user administrative role
    """
    
    @schemas.classproperty
    def ADMINISTRATOR(cls):
        return cls("ADMINISTRATOR")
    
    @schemas.classproperty
    def OPERATOR(cls):
        return cls("OPERATOR")
    
    @schemas.classproperty
    def MONITOR(cls):
        return cls("MONITOR")
    
    @schemas.classproperty
    def HELP_DESK(cls):
        return cls("HELP_DESK")
    
    @schemas.classproperty
    def GUEST_MANAGEMENT(cls):
        return cls("GUEST_MANAGEMENT")
    
    @schemas.classproperty
    def OBSERVER(cls):
        return cls("OBSERVER")
    
    @schemas.classproperty
    def INSTALLER(cls):
        return cls("INSTALLER")
    
    @schemas.classproperty
    def APPLICATION_OPERATOR(cls):
        return cls("APPLICATION_OPERATOR")
