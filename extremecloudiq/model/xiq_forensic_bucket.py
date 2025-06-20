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


class XiqForensicBucket(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "TWENTY_FOUR_HOURS": "TWENTY_FOUR_HOURS",
            "ONE_HOUR": "ONE_HOUR",
            "TODAY": "TODAY",
            "ONE_WEEK": "ONE_WEEK",
            "SEVEN_DAYS": "SEVEN_DAYS",
            "THIRTY_DAYS": "THIRTY_DAYS",
            "NINETY_DAYS": "NINETY_DAYS",
        }
    
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
