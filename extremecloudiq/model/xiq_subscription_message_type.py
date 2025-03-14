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


class XiqSubscriptionMessageType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The subscription message type.
    """


    class MetaOapg:
        enum_value_to_name = {
            "LOCATION_AP_CENTRIC": "LOCATION_AP_CENTRIC",
            "LOCATION_CLIENT_CENTRIC": "LOCATION_CLIENT_CENTRIC",
            "AUDIT_LOG_ALL": "AUDIT_LOG_ALL",
            "GDPR_LOG_ALL": "GDPR_LOG_ALL",
            "CREDENTIAL_LOG_ALL": "CREDENTIAL_LOG_ALL",
            "ACCOUNTING_LOG_ALL": "ACCOUNTING_LOG_ALL",
            "AUTHENTICATION_LOG_ALL": "AUTHENTICATION_LOG_ALL",
            "EMAIL_LOG_ALL": "EMAIL_LOG_ALL",
            "SMS_LOG_ALL": "SMS_LOG_ALL",
        }
    
    @schemas.classproperty
    def LOCATION_AP_CENTRIC(cls):
        return cls("LOCATION_AP_CENTRIC")
    
    @schemas.classproperty
    def LOCATION_CLIENT_CENTRIC(cls):
        return cls("LOCATION_CLIENT_CENTRIC")
    
    @schemas.classproperty
    def AUDIT_LOG_ALL(cls):
        return cls("AUDIT_LOG_ALL")
    
    @schemas.classproperty
    def GDPR_LOG_ALL(cls):
        return cls("GDPR_LOG_ALL")
    
    @schemas.classproperty
    def CREDENTIAL_LOG_ALL(cls):
        return cls("CREDENTIAL_LOG_ALL")
    
    @schemas.classproperty
    def ACCOUNTING_LOG_ALL(cls):
        return cls("ACCOUNTING_LOG_ALL")
    
    @schemas.classproperty
    def AUTHENTICATION_LOG_ALL(cls):
        return cls("AUTHENTICATION_LOG_ALL")
    
    @schemas.classproperty
    def EMAIL_LOG_ALL(cls):
        return cls("EMAIL_LOG_ALL")
    
    @schemas.classproperty
    def SMS_LOG_ALL(cls):
        return cls("SMS_LOG_ALL")
