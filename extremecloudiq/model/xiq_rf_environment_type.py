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


class XiqRfEnvironmentType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The floor RF environment
    """


    class MetaOapg:
        enum_value_to_name = {
            "AUTO_ESTIMATE": "AUTO_ESTIMATE",
            "OFFICE": "OFFICE",
            "OUTDOOR_FREE_SPACE": "OUTDOOR_FREE_SPACE",
            "OBSTRUCTED_IN_BUILDING": "OBSTRUCTED_IN_BUILDING",
            "OUTDOOR_SUBURBAN": "OUTDOOR_SUBURBAN",
            "WAREHOUSE": "WAREHOUSE",
            "OUTDOOR_DENSE_URBAN": "OUTDOOR_DENSE_URBAN",
        }
    
    @schemas.classproperty
    def AUTO_ESTIMATE(cls):
        return cls("AUTO_ESTIMATE")
    
    @schemas.classproperty
    def OFFICE(cls):
        return cls("OFFICE")
    
    @schemas.classproperty
    def OUTDOOR_FREE_SPACE(cls):
        return cls("OUTDOOR_FREE_SPACE")
    
    @schemas.classproperty
    def OBSTRUCTED_IN_BUILDING(cls):
        return cls("OBSTRUCTED_IN_BUILDING")
    
    @schemas.classproperty
    def OUTDOOR_SUBURBAN(cls):
        return cls("OUTDOOR_SUBURBAN")
    
    @schemas.classproperty
    def WAREHOUSE(cls):
        return cls("WAREHOUSE")
    
    @schemas.classproperty
    def OUTDOOR_DENSE_URBAN(cls):
        return cls("OUTDOOR_DENSE_URBAN")
