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


class XiqSubscriptionDataType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The webhook subscription data type.
    """
    
    @schemas.classproperty
    def LOCATION(cls):
        return cls("LOCATION")
    
    @schemas.classproperty
    def AUDIT_LOG(cls):
        return cls("AUDIT_LOG")
    
    @schemas.classproperty
    def GDPR_LOG(cls):
        return cls("GDPR_LOG")
    
    @schemas.classproperty
    def CREDENTIAL_LOG(cls):
        return cls("CREDENTIAL_LOG")
    
    @schemas.classproperty
    def ACCOUNTING_LOG(cls):
        return cls("ACCOUNTING_LOG")
    
    @schemas.classproperty
    def AUTHENTICATION_LOG(cls):
        return cls("AUTHENTICATION_LOG")
    
    @schemas.classproperty
    def EMAIL_LOG(cls):
        return cls("EMAIL_LOG")
    
    @schemas.classproperty
    def SMS_LOG(cls):
        return cls("SMS_LOG")
