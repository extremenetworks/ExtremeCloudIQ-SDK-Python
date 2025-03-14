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


class XiqLicenseMode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The license mode
    """


    class MetaOapg:
        enum_value_to_name = {
            "BUY": "BUY",
            "PLANNER": "PLANNER",
            "EVAL": "EVAL",
            "MSP": "MSP",
            "UNKNOWN": "UNKNOWN",
        }
    
    @schemas.classproperty
    def BUY(cls):
        return cls("BUY")
    
    @schemas.classproperty
    def PLANNER(cls):
        return cls("PLANNER")
    
    @schemas.classproperty
    def EVAL(cls):
        return cls("EVAL")
    
    @schemas.classproperty
    def MSP(cls):
        return cls("MSP")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
