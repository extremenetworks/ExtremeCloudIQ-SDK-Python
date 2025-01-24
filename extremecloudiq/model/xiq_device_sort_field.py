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


class XiqDeviceSortField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    All available device sort fields<br/><br/>MAC = Device MAC Address<br/>SN = Device Serial Number
    """


    class MetaOapg:
        enum_value_to_name = {
            "MAC": "MAC",
            "SN": "SN",
        }
    
    @schemas.classproperty
    def MAC(cls):
        return cls("MAC")
    
    @schemas.classproperty
    def SN(cls):
        return cls("SN")
