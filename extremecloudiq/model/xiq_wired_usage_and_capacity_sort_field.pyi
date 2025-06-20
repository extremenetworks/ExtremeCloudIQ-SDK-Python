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


class XiqWiredUsageAndCapacitySortField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def UNSPECIFIED(cls):
        return cls("UNSPECIFIED")
    
    @schemas.classproperty
    def DEVICE_HOSTNAME(cls):
        return cls("DEVICE_HOSTNAME")
    
    @schemas.classproperty
    def DEVICE_IP(cls):
        return cls("DEVICE_IP")
    
    @schemas.classproperty
    def SITE(cls):
        return cls("SITE")
    
    @schemas.classproperty
    def TOTAL_CLIENTS_COUNT(cls):
        return cls("TOTAL_CLIENTS_COUNT")
    
    @schemas.classproperty
    def TOTAL_ISSUE_CLIENTS_COUNT(cls):
        return cls("TOTAL_ISSUE_CLIENTS_COUNT")
    
    @schemas.classproperty
    def TOTAL_BANDWIDTH_UTILIZED(cls):
        return cls("TOTAL_BANDWIDTH_UTILIZED")
    
    @schemas.classproperty
    def TOTAL_THROUGHPUT_RX(cls):
        return cls("TOTAL_THROUGHPUT_RX")
    
    @schemas.classproperty
    def TOTAL_THROUGHPUT_TX(cls):
        return cls("TOTAL_THROUGHPUT_TX")
    
    @schemas.classproperty
    def TOTAL_UNICAST_PACKETS(cls):
        return cls("TOTAL_UNICAST_PACKETS")
    
    @schemas.classproperty
    def TOTAL_MULTICAST_PACKETS(cls):
        return cls("TOTAL_MULTICAST_PACKETS")
    
    @schemas.classproperty
    def TOTAL_BROADCAST_PACKETS(cls):
        return cls("TOTAL_BROADCAST_PACKETS")
    
    @schemas.classproperty
    def TOTAL_QUEUE_TX_PKTS(cls):
        return cls("TOTAL_QUEUE_TX_PKTS")
    
    @schemas.classproperty
    def TOTAL_QUEUE_CONGESTION_PKTS(cls):
        return cls("TOTAL_QUEUE_CONGESTION_PKTS")
