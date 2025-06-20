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


class XiqNetworkPolicyType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The network policy type
    """


    class MetaOapg:
        enum_value_to_name = {
            "NETWORK_ACCESS_AND_SWITCHING": "NETWORK_ACCESS_AND_SWITCHING",
            "BRANCH_ROUTING": "BRANCH_ROUTING",
            "WIRELESS_ACCESS": "WIRELESS_ACCESS",
            "SWITCHING": "SWITCHING",
            "NETWORK_ACCESS_AND_SWITCHING_AND_BR": "NETWORK_ACCESS_AND_SWITCHING_AND_BR",
            "NETWORK_ACCESS_AND_BRANCH_ROUTING": "NETWORK_ACCESS_AND_BRANCH_ROUTING",
            "SWITCHING_AND_BRANCH_ROUTING": "SWITCHING_AND_BRANCH_ROUTING",
        }
    
    @schemas.classproperty
    def NETWORK_ACCESS_AND_SWITCHING(cls):
        return cls("NETWORK_ACCESS_AND_SWITCHING")
    
    @schemas.classproperty
    def BRANCH_ROUTING(cls):
        return cls("BRANCH_ROUTING")
    
    @schemas.classproperty
    def WIRELESS_ACCESS(cls):
        return cls("WIRELESS_ACCESS")
    
    @schemas.classproperty
    def SWITCHING(cls):
        return cls("SWITCHING")
    
    @schemas.classproperty
    def NETWORK_ACCESS_AND_SWITCHING_AND_BR(cls):
        return cls("NETWORK_ACCESS_AND_SWITCHING_AND_BR")
    
    @schemas.classproperty
    def NETWORK_ACCESS_AND_BRANCH_ROUTING(cls):
        return cls("NETWORK_ACCESS_AND_BRANCH_ROUTING")
    
    @schemas.classproperty
    def SWITCHING_AND_BRANCH_ROUTING(cls):
        return cls("SWITCHING_AND_BRANCH_ROUTING")
