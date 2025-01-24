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


class XiqPasswordCharacterType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Password generation using letters, numbers, and/or special characters
    """


    class MetaOapg:
        enum_value_to_name = {
            "INCLUDE_ALL_CHARACTER_TYPE_ENABLED": "ALL_CHARACTER_TYPE_ENABLED",
            "INCLUDE_ANY_CHARACTER_TYPES_ENABLED": "ANY_CHARACTER_TYPES_ENABLED",
            "INCLUDE_ONLY_ONE_CHARACTER_TYPE_ENABLED": "ONLY_ONE_CHARACTER_TYPE_ENABLED",
        }
    
    @schemas.classproperty
    def ALL_CHARACTER_TYPE_ENABLED(cls):
        return cls("INCLUDE_ALL_CHARACTER_TYPE_ENABLED")
    
    @schemas.classproperty
    def ANY_CHARACTER_TYPES_ENABLED(cls):
        return cls("INCLUDE_ANY_CHARACTER_TYPES_ENABLED")
    
    @schemas.classproperty
    def ONLY_ONE_CHARACTER_TYPE_ENABLED(cls):
        return cls("INCLUDE_ONLY_ONE_CHARACTER_TYPE_ENABLED")
