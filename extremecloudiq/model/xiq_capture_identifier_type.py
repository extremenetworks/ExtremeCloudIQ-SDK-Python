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


class XiqCaptureIdentifierType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The capture identifier type for selecting the APs. Depending on the type, one of "ap_serial_number", "device_ids" and "location_id" must be provided.
    """


    class MetaOapg:
        enum_value_to_name = {
            "AP_SERIAL_NUMBER": "AP_SERIAL_NUMBER",
            "DEVICE_IDS": "DEVICE_IDS",
            "LOCATION": "LOCATION",
        }
    
    @schemas.classproperty
    def AP_SERIAL_NUMBER(cls):
        return cls("AP_SERIAL_NUMBER")
    
    @schemas.classproperty
    def DEVICE_IDS(cls):
        return cls("DEVICE_IDS")
    
    @schemas.classproperty
    def LOCATION(cls):
        return cls("LOCATION")
