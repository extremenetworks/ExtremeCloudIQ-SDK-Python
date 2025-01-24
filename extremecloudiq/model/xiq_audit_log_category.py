# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.1.0.147
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


class XiqAuditLogCategory(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ADMIN": "ADMIN",
            "SYSTEM": "SYSTEM",
            "DEPLOYMENT": "DEPLOYMENT",
            "CONFIG": "CONFIG",
            "MONITOR": "MONITOR",
            "ALARM": "ALARM",
        }
    
    @schemas.classproperty
    def ADMIN(cls):
        return cls("ADMIN")
    
    @schemas.classproperty
    def SYSTEM(cls):
        return cls("SYSTEM")
    
    @schemas.classproperty
    def DEPLOYMENT(cls):
        return cls("DEPLOYMENT")
    
    @schemas.classproperty
    def CONFIG(cls):
        return cls("CONFIG")
    
    @schemas.classproperty
    def MONITOR(cls):
        return cls("MONITOR")
    
    @schemas.classproperty
    def ALARM(cls):
        return cls("ALARM")
