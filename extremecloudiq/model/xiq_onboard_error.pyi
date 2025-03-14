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


class XiqOnboardError(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The onboard error code
    """
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
    
    @schemas.classproperty
    def SUCCEED(cls):
        return cls("SUCCEED")
    
    @schemas.classproperty
    def EXIST_IN_REDIRECT(cls):
        return cls("EXIST_IN_REDIRECT")
    
    @schemas.classproperty
    def FAILED_IN_DB(cls):
        return cls("FAILED_IN_DB")
    
    @schemas.classproperty
    def FAILED_STORE_IN_REDIRECT(cls):
        return cls("FAILED_STORE_IN_REDIRECT")
    
    @schemas.classproperty
    def SN_IS_NOT_RIGHT(cls):
        return cls("SN_IS_NOT_RIGHT")
    
    @schemas.classproperty
    def PRODUCT_TYPE_NOT_EXIST(cls):
        return cls("PRODUCT_TYPE_NOT_EXIST")
    
    @schemas.classproperty
    def REACH_MAX_SIZE(cls):
        return cls("REACH_MAX_SIZE")
    
    @schemas.classproperty
    def NOT_SUPPORT_DEVICE(cls):
        return cls("NOT_SUPPORT_DEVICE")
    
    @schemas.classproperty
    def SN_EXISTED_IN_HM(cls):
        return cls("SN_EXISTED_IN_HM")
    
    @schemas.classproperty
    def DEVICE_EXISTED(cls):
        return cls("DEVICE_EXISTED")
    
    @schemas.classproperty
    def NETMASK_IP_NOT_NULL(cls):
        return cls("NETMASK_IP_NOT_NULL")
    
    @schemas.classproperty
    def BRANCH_ID_USED(cls):
        return cls("BRANCH_ID_USED")
    
    @schemas.classproperty
    def INVALID_SERVICE_TAG(cls):
        return cls("INVALID_SERVICE_TAG")
    
    @schemas.classproperty
    def RADIO_WIFI1_NOT_SUPPORT(cls):
        return cls("RADIO_WIFI1_NOT_SUPPORT")
    
    @schemas.classproperty
    def RADIO_PROFILE_NOT_EXIST(cls):
        return cls("RADIO_PROFILE_NOT_EXIST")
    
    @schemas.classproperty
    def SDR_PROFILE_NOT_EXIST(cls):
        return cls("SDR_PROFILE_NOT_EXIST")
    
    @schemas.classproperty
    def ADMIN_STATE_NOT_SUPPORT(cls):
        return cls("ADMIN_STATE_NOT_SUPPORT")
    
    @schemas.classproperty
    def WIFI_POWER_NOT_SUPPORT(cls):
        return cls("WIFI_POWER_NOT_SUPPORT")
    
    @schemas.classproperty
    def OPERATION_MODE_NOT_SUPPORT(cls):
        return cls("OPERATION_MODE_NOT_SUPPORT")
    
    @schemas.classproperty
    def COUNTRY_CODE_NOT_SUPPORT(cls):
        return cls("COUNTRY_CODE_NOT_SUPPORT")
    
    @schemas.classproperty
    def WIFI0_CHANNEL_NOT_SUPPORT(cls):
        return cls("WIFI0_CHANNEL_NOT_SUPPORT")
    
    @schemas.classproperty
    def WIFI1_CHANNEL_NOT_SUPPORT(cls):
        return cls("WIFI1_CHANNEL_NOT_SUPPORT")
    
    @schemas.classproperty
    def COUNTRY_CODE_IS_NEEDED(cls):
        return cls("COUNTRY_CODE_IS_NEEDED")
    
    @schemas.classproperty
    def MAC_ADDR_REQUIRED(cls):
        return cls("MAC_ADDR_REQUIRED")
    
    @schemas.classproperty
    def WING_AP_INVALID_ONBOARDING_DATA(cls):
        return cls("WING_AP_INVALID_ONBOARDING_DATA")
    
    @schemas.classproperty
    def NOT_DUAL_BOOT_AP(cls):
        return cls("NOT_DUAL_BOOT_AP")
    
    @schemas.classproperty
    def INVALID_CSV_LOCATION(cls):
        return cls("INVALID_CSV_LOCATION")
    
    @schemas.classproperty
    def NOT_SUPPORTED_FOR_CONNECT(cls):
        return cls("NOT_SUPPORTED_FOR_CONNECT")
    
    @schemas.classproperty
    def DEVICE_EXISTED_ANOTHER_ACCOUNT(cls):
        return cls("DEVICE_EXISTED_ANOTHER_ACCOUNT")
    
    @schemas.classproperty
    def FAILED_IN_DTIS_SERVICE(cls):
        return cls("FAILED_IN_DTIS_SERVICE")
    
    @schemas.classproperty
    def FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED(cls):
        return cls("FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED")
    
    @schemas.classproperty
    def FAILED_DTINSTANCE_ALREADY_ASSOCIATED(cls):
        return cls("FAILED_DTINSTANCE_ALREADY_ASSOCIATED")
    
    @schemas.classproperty
    def FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED(cls):
        return cls("FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED")
    
    @schemas.classproperty
    def FAILED_IN_DTIS_MAX_LICENSE_LIMIT_REACHED(cls):
        return cls("FAILED_IN_DTIS_MAX_LICENSE_LIMIT_REACHED")
    
    @schemas.classproperty
    def FAILED_DTINSTANCE_RELAUNCHED_RECENTLY(cls):
        return cls("FAILED_DTINSTANCE_RELAUNCHED_RECENTLY")
    
    @schemas.classproperty
    def FAILED_COPILOT_DISABLED(cls):
        return cls("FAILED_COPILOT_DISABLED")
    
    @schemas.classproperty
    def FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED_BY_BATCH(cls):
        return cls("FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED_BY_BATCH")
    
    @schemas.classproperty
    def FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED_BY_BATCH(cls):
        return cls("FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED_BY_BATCH")
    
    @schemas.classproperty
    def REACH_MAX_CAP(cls):
        return cls("REACH_MAX_CAP")
    
    @schemas.classproperty
    def NETWORK_POLICY_NOT_FOUND(cls):
        return cls("NETWORK_POLICY_NOT_FOUND")
    
    @schemas.classproperty
    def VERSION_NOT_SUPPORTED(cls):
        return cls("VERSION_NOT_SUPPORTED")
    
    @schemas.classproperty
    def VERSION_DEPRECATED(cls):
        return cls("VERSION_DEPRECATED")
