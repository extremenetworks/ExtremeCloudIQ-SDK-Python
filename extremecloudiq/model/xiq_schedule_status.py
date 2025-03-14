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


class XiqScheduleStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The schedule status
    """


    class MetaOapg:
        enum_value_to_name = {
            "SCHEDULED": "SCHEDULED",
            "IN_PROGRESS": "IN_PROGRESS",
            "ABORTED": "ABORTED",
            "COMPLETED": "COMPLETED",
            "FAILED": "FAILED",
            "TIME_OUT": "TIME_OUT",
        }
    
    @schemas.classproperty
    def SCHEDULED(cls):
        return cls("SCHEDULED")
    
    @schemas.classproperty
    def IN_PROGRESS(cls):
        return cls("IN_PROGRESS")
    
    @schemas.classproperty
    def ABORTED(cls):
        return cls("ABORTED")
    
    @schemas.classproperty
    def COMPLETED(cls):
        return cls("COMPLETED")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
    
    @schemas.classproperty
    def TIME_OUT(cls):
        return cls("TIME_OUT")
