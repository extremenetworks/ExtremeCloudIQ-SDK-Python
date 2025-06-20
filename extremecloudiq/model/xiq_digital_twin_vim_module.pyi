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


class XiqDigitalTwinVimModule(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Digital Twin VIM modules.
    """
    
    @schemas.classproperty
    def DIGIT_FIVE_520_VIM_4X(cls):
        return cls("DT_5520_VIM_4X")
    
    @schemas.classproperty
    def DIGIT_FIVE_520_VIM_4XE(cls):
        return cls("DT_5520_VIM_4XE")
    
    @schemas.classproperty
    def DIGIT_FIVE_520_VIM_4YE(cls):
        return cls("DT_5520_VIM_4YE")
    
    @schemas.classproperty
    def DIGIT_FIVE_720_VIM_2CE(cls):
        return cls("DT_5720_VIM_2CE")
    
    @schemas.classproperty
    def DIGIT_FIVE_720_VIM_6YE(cls):
        return cls("DT_5720_VIM_6YE")
