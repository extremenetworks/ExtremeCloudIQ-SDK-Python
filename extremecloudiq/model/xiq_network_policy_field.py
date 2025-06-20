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


class XiqNetworkPolicyField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ID": "ID",
            "CREATE_TIME": "CREATE_TIME",
            "UPDATE_TIME": "UPDATE_TIME",
            "ORG_ID": "ORG_ID",
            "NAME": "NAME",
            "DESCRIPTION": "DESCRIPTION",
            "TYPE": "TYPE",
            "PREDEFINED": "PREDEFINED",
        }
    
    @schemas.classproperty
    def ID(cls):
        return cls("ID")
    
    @schemas.classproperty
    def CREATE_TIME(cls):
        return cls("CREATE_TIME")
    
    @schemas.classproperty
    def UPDATE_TIME(cls):
        return cls("UPDATE_TIME")
    
    @schemas.classproperty
    def ORG_ID(cls):
        return cls("ORG_ID")
    
    @schemas.classproperty
    def NAME(cls):
        return cls("NAME")
    
    @schemas.classproperty
    def DESCRIPTION(cls):
        return cls("DESCRIPTION")
    
    @schemas.classproperty
    def TYPE(cls):
        return cls("TYPE")
    
    @schemas.classproperty
    def PREDEFINED(cls):
        return cls("PREDEFINED")
