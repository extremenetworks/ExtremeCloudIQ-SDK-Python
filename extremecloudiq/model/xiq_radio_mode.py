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


class XiqRadioMode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The supported radio modes.
    """


    class MetaOapg:
        enum_value_to_name = {
            "B_G": "B_G",
            "G_N": "G_N",
            "A": "A",
            "A_N": "A_N",
            "AC": "AC",
            "AX_2_4_GHZ": "AX_2_4_GHZ",
            "AX_5_GHZ": "AX_5_GHZ",
            "AX_6_GHZ": "AX_6_GHZ",
            "BE_2_4_GHZ": "BE_2_4_GHZ",
            "BE_5_GHZ": "BE_5_GHZ",
            "BE_6_GHZ": "BE_6_GHZ",
        }
    
    @schemas.classproperty
    def B_G(cls):
        return cls("B_G")
    
    @schemas.classproperty
    def G_N(cls):
        return cls("G_N")
    
    @schemas.classproperty
    def A(cls):
        return cls("A")
    
    @schemas.classproperty
    def A_N(cls):
        return cls("A_N")
    
    @schemas.classproperty
    def AC(cls):
        return cls("AC")
    
    @schemas.classproperty
    def AX_2_4_GHZ(cls):
        return cls("AX_2_4_GHZ")
    
    @schemas.classproperty
    def AX_5_GHZ(cls):
        return cls("AX_5_GHZ")
    
    @schemas.classproperty
    def AX_6_GHZ(cls):
        return cls("AX_6_GHZ")
    
    @schemas.classproperty
    def BE_2_4_GHZ(cls):
        return cls("BE_2_4_GHZ")
    
    @schemas.classproperty
    def BE_5_GHZ(cls):
        return cls("BE_5_GHZ")
    
    @schemas.classproperty
    def BE_6_GHZ(cls):
        return cls("BE_6_GHZ")
