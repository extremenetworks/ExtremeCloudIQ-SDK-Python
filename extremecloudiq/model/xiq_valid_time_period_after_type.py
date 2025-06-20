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


class XiqValidTimePeriodAfterType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The valid time period after Id creation or first login.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ID_CREATION": "ID_CREATION",
            "FIRST_LOGIN": "FIRST_LOGIN",
        }
    
    @schemas.classproperty
    def ID_CREATION(cls):
        return cls("ID_CREATION")
    
    @schemas.classproperty
    def FIRST_LOGIN(cls):
        return cls("FIRST_LOGIN")
