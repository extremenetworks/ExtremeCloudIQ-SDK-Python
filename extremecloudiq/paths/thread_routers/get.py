# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from extremecloudiq import api_client, exceptions
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

from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.paged_xiq_thread_router import PagedXiqThreadRouter

from . import path

# Query params


class IdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.Int64Schema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class PageSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_minimum = 1


class LimitSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 100
        inclusive_minimum = 1


class SortFieldSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "SERIAL_NUMBER": "SERIAL_NUMBER",
            "EUI64": "EUI64",
            "EXT_MAC": "EXT_MAC",
            "RLOC16": "RLOC16",
            "GLOBAL_IPV6": "GLOBAL_IPV6",
            "TX_POWER": "TX_POWER",
            "REGION": "REGION",
            "THREAD_PLATFORM": "THREAD_PLATFORM",
            "DEVICE_ROLE": "DEVICE_ROLE",
            "ROUTER_INTERFACE_NAME": "ROUTER_INTERFACE_NAME",
            "ROUTER_INTERFACE_IS_ACTIVE": "ROUTER_INTERFACE_IS_ACTIVE",
            "ROUTER_INTERFACE_IS_BROADCAST": "ROUTER_INTERFACE_IS_BROADCAST",
            "ROUTER_INTERFACE_IS_LOOPBACK": "ROUTER_INTERFACE_IS_LOOPBACK",
            "ROUTER_INTERFACE_IS_POINT_TO_POINT": "ROUTER_INTERFACE_IS_POINT_TO_POINT",
            "ROUTER_INTERFACE_IS_RUNNING": "ROUTER_INTERFACE_IS_RUNNING",
            "ROUTER_INTERFACE_IS_ARP": "ROUTER_INTERFACE_IS_ARP",
            "ROUTER_INTERFACE_IS_PROMISC": "ROUTER_INTERFACE_IS_PROMISC",
            "ROUTER_INTERFACE_IS_ALL_MULTI": "ROUTER_INTERFACE_IS_ALL_MULTI",
            "ROUTER_INTERFACE_IS_MULTICAST": "ROUTER_INTERFACE_IS_MULTICAST",
            "ROUTER_INTERFACE_IS_DYNAMIC": "ROUTER_INTERFACE_IS_DYNAMIC",
            "ROUTER_INTERFACE_MTU": "ROUTER_INTERFACE_MTU",
            "ROUTER_INTERFACE_HW_MAC": "ROUTER_INTERFACE_HW_MAC",
            "ROUTER_INTERFACE_IPV4": "ROUTER_INTERFACE_IPV4",
            "ROUTER_INTERFACE_IPV4_MASK": "ROUTER_INTERFACE_IPV4_MASK",
            "ROUTER_INTERFACE_IPV4_BROADCAST": "ROUTER_INTERFACE_IPV4_BROADCAST",
            "VETH0_INTERFACE_NAME": "VETH0_INTERFACE_NAME",
            "VETH0_IS_ACTIVE": "VETH0_IS_ACTIVE",
            "VETH0_IS_BROADCAST": "VETH0_IS_BROADCAST",
            "VETH0_IS_LOOPBACK": "VETH0_IS_LOOPBACK",
            "VETH0_IS_POINT_TO_POINT": "VETH0_IS_POINT_TO_POINT",
            "VETH0_IS_RUNNING": "VETH0_IS_RUNNING",
            "VETH0_IS_ARP": "VETH0_IS_ARP",
            "VETH0_IS_PROMISC": "VETH0_IS_PROMISC",
            "VETH0_IS_ALL_MULTI": "VETH0_IS_ALL_MULTI",
            "VETH0_IS_MULTICAST": "VETH0_IS_MULTICAST",
            "VETH0_IS_DYNAMIC": "VETH0_IS_DYNAMIC",
            "VETH0_MTU": "VETH0_MTU",
            "VETH0_HW_MAC": "VETH0_HW_MAC",
            "VETH0_IPV4": "VETH0_IPV4",
            "VETH0_IPV4_MASK": "VETH0_IPV4_MASK",
            "VETH0_IPV4_BROADCAST": "VETH0_IPV4_BROADCAST",
            "NETWORK_DATA_LENGTH": "NETWORK_DATA_LENGTH",
            "NETWORK_DATA_MAX_LENGTH": "NETWORK_DATA_MAX_LENGTH",
            "RX_ON_WHEN_IDLE": "RX_ON_WHEN_IDLE",
            "FULL_THREAD_DEVICE": "FULL_THREAD_DEVICE",
            "FULL_NETWORK_DATA": "FULL_NETWORK_DATA",
            "THREAD_VERSION": "THREAD_VERSION",
            "BUILD_VERSION": "BUILD_VERSION",
            "API_VERSION": "API_VERSION",
            "RCP_VERSION": "RCP_VERSION",
            "LEADER_PARTITION_ID": "LEADER_PARTITION_ID",
            "LEADER_WEIGHTING": "LEADER_WEIGHTING",
            "LEADER_FULL_NETWORK_DATA_VERSION": "LEADER_FULL_NETWORK_DATA_VERSION",
            "LEADER_STABLE_NETWORK_DATA_VERSION": "LEADER_STABLE_NETWORK_DATA_VERSION",
            "BORDER_ROUTER_STATE": "BORDER_ROUTER_STATE",
            "BORDER_NAT64_LOCAL_PREFIX": "BORDER_NAT64_LOCAL_PREFIX",
            "BORDER_NAT64_FAVORED_PREFIX": "BORDER_NAT64_FAVORED_PREFIX",
            "BORDER_NAT64_FAVORED_PREFERENCE": "BORDER_NAT64_FAVORED_PREFERENCE",
            "BORDER_NAT64_0MR_LOCAL_PREFIX": "BORDER_NAT64_0MR_LOCAL_PREFIX",
            "BORDER_NAT64_0MR_FAVORED_PREFIX": "BORDER_NAT64_0MR_FAVORED_PREFIX",
            "BORDER_NAT64_0MR_FAVORED_PREFERENCE": "BORDER_NAT64_0MR_FAVORED_PREFERENCE",
            "BORDER_NAT64_640N_LINK_LOCAL_PREFIX": "BORDER_NAT64_640N_LINK_LOCAL_PREFIX",
            "BORDER_NAT64_640N_LINK_FAVORED_PREFIX": "BORDER_NAT64_640N_LINK_FAVORED_PREFIX",
            "BORDER_NAT64_640N_LINK_FAVORED_PREFERENCE": "BORDER_NAT64_640N_LINK_FAVORED_PREFERENCE",
            "BACKBONE_BORDER_ROUTER_STATE": "BACKBONE_BORDER_ROUTER_STATE",
            "BORDER_AGENT_STATE": "BORDER_AGENT_STATE",
            "BORDER_AGENT_UDP_PORT": "BORDER_AGENT_UDP_PORT",
            "COMMISSIONER_STATE": "COMMISSIONER_STATE",
            "NAT64_PREFIX_MANAGER_STATE": "NAT64_PREFIX_MANAGER_STATE",
            "NAT64_TRANSLATOR_STATE": "NAT64_TRANSLATOR_STATE",
            "NAT64_TRANSLATOR_CIDR": "NAT64_TRANSLATOR_CIDR",
            "HOSTNAME": "HOSTNAME",
        }
    
    @schemas.classproperty
    def SERIAL_NUMBER(cls):
        return cls("SERIAL_NUMBER")
    
    @schemas.classproperty
    def EUI64(cls):
        return cls("EUI64")
    
    @schemas.classproperty
    def EXT_MAC(cls):
        return cls("EXT_MAC")
    
    @schemas.classproperty
    def RLOC16(cls):
        return cls("RLOC16")
    
    @schemas.classproperty
    def GLOBAL_IPV6(cls):
        return cls("GLOBAL_IPV6")
    
    @schemas.classproperty
    def TX_POWER(cls):
        return cls("TX_POWER")
    
    @schemas.classproperty
    def REGION(cls):
        return cls("REGION")
    
    @schemas.classproperty
    def THREAD_PLATFORM(cls):
        return cls("THREAD_PLATFORM")
    
    @schemas.classproperty
    def DEVICE_ROLE(cls):
        return cls("DEVICE_ROLE")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_NAME(cls):
        return cls("ROUTER_INTERFACE_NAME")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_ACTIVE(cls):
        return cls("ROUTER_INTERFACE_IS_ACTIVE")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_BROADCAST(cls):
        return cls("ROUTER_INTERFACE_IS_BROADCAST")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_LOOPBACK(cls):
        return cls("ROUTER_INTERFACE_IS_LOOPBACK")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_POINT_TO_POINT(cls):
        return cls("ROUTER_INTERFACE_IS_POINT_TO_POINT")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_RUNNING(cls):
        return cls("ROUTER_INTERFACE_IS_RUNNING")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_ARP(cls):
        return cls("ROUTER_INTERFACE_IS_ARP")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_PROMISC(cls):
        return cls("ROUTER_INTERFACE_IS_PROMISC")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_ALL_MULTI(cls):
        return cls("ROUTER_INTERFACE_IS_ALL_MULTI")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_MULTICAST(cls):
        return cls("ROUTER_INTERFACE_IS_MULTICAST")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IS_DYNAMIC(cls):
        return cls("ROUTER_INTERFACE_IS_DYNAMIC")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_MTU(cls):
        return cls("ROUTER_INTERFACE_MTU")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_HW_MAC(cls):
        return cls("ROUTER_INTERFACE_HW_MAC")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IPV4(cls):
        return cls("ROUTER_INTERFACE_IPV4")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IPV4_MASK(cls):
        return cls("ROUTER_INTERFACE_IPV4_MASK")
    
    @schemas.classproperty
    def ROUTER_INTERFACE_IPV4_BROADCAST(cls):
        return cls("ROUTER_INTERFACE_IPV4_BROADCAST")
    
    @schemas.classproperty
    def VETH0_INTERFACE_NAME(cls):
        return cls("VETH0_INTERFACE_NAME")
    
    @schemas.classproperty
    def VETH0_IS_ACTIVE(cls):
        return cls("VETH0_IS_ACTIVE")
    
    @schemas.classproperty
    def VETH0_IS_BROADCAST(cls):
        return cls("VETH0_IS_BROADCAST")
    
    @schemas.classproperty
    def VETH0_IS_LOOPBACK(cls):
        return cls("VETH0_IS_LOOPBACK")
    
    @schemas.classproperty
    def VETH0_IS_POINT_TO_POINT(cls):
        return cls("VETH0_IS_POINT_TO_POINT")
    
    @schemas.classproperty
    def VETH0_IS_RUNNING(cls):
        return cls("VETH0_IS_RUNNING")
    
    @schemas.classproperty
    def VETH0_IS_ARP(cls):
        return cls("VETH0_IS_ARP")
    
    @schemas.classproperty
    def VETH0_IS_PROMISC(cls):
        return cls("VETH0_IS_PROMISC")
    
    @schemas.classproperty
    def VETH0_IS_ALL_MULTI(cls):
        return cls("VETH0_IS_ALL_MULTI")
    
    @schemas.classproperty
    def VETH0_IS_MULTICAST(cls):
        return cls("VETH0_IS_MULTICAST")
    
    @schemas.classproperty
    def VETH0_IS_DYNAMIC(cls):
        return cls("VETH0_IS_DYNAMIC")
    
    @schemas.classproperty
    def VETH0_MTU(cls):
        return cls("VETH0_MTU")
    
    @schemas.classproperty
    def VETH0_HW_MAC(cls):
        return cls("VETH0_HW_MAC")
    
    @schemas.classproperty
    def VETH0_IPV4(cls):
        return cls("VETH0_IPV4")
    
    @schemas.classproperty
    def VETH0_IPV4_MASK(cls):
        return cls("VETH0_IPV4_MASK")
    
    @schemas.classproperty
    def VETH0_IPV4_BROADCAST(cls):
        return cls("VETH0_IPV4_BROADCAST")
    
    @schemas.classproperty
    def NETWORK_DATA_LENGTH(cls):
        return cls("NETWORK_DATA_LENGTH")
    
    @schemas.classproperty
    def NETWORK_DATA_MAX_LENGTH(cls):
        return cls("NETWORK_DATA_MAX_LENGTH")
    
    @schemas.classproperty
    def RX_ON_WHEN_IDLE(cls):
        return cls("RX_ON_WHEN_IDLE")
    
    @schemas.classproperty
    def FULL_THREAD_DEVICE(cls):
        return cls("FULL_THREAD_DEVICE")
    
    @schemas.classproperty
    def FULL_NETWORK_DATA(cls):
        return cls("FULL_NETWORK_DATA")
    
    @schemas.classproperty
    def THREAD_VERSION(cls):
        return cls("THREAD_VERSION")
    
    @schemas.classproperty
    def BUILD_VERSION(cls):
        return cls("BUILD_VERSION")
    
    @schemas.classproperty
    def API_VERSION(cls):
        return cls("API_VERSION")
    
    @schemas.classproperty
    def RCP_VERSION(cls):
        return cls("RCP_VERSION")
    
    @schemas.classproperty
    def LEADER_PARTITION_ID(cls):
        return cls("LEADER_PARTITION_ID")
    
    @schemas.classproperty
    def LEADER_WEIGHTING(cls):
        return cls("LEADER_WEIGHTING")
    
    @schemas.classproperty
    def LEADER_FULL_NETWORK_DATA_VERSION(cls):
        return cls("LEADER_FULL_NETWORK_DATA_VERSION")
    
    @schemas.classproperty
    def LEADER_STABLE_NETWORK_DATA_VERSION(cls):
        return cls("LEADER_STABLE_NETWORK_DATA_VERSION")
    
    @schemas.classproperty
    def BORDER_ROUTER_STATE(cls):
        return cls("BORDER_ROUTER_STATE")
    
    @schemas.classproperty
    def BORDER_NAT64_LOCAL_PREFIX(cls):
        return cls("BORDER_NAT64_LOCAL_PREFIX")
    
    @schemas.classproperty
    def BORDER_NAT64_FAVORED_PREFIX(cls):
        return cls("BORDER_NAT64_FAVORED_PREFIX")
    
    @schemas.classproperty
    def BORDER_NAT64_FAVORED_PREFERENCE(cls):
        return cls("BORDER_NAT64_FAVORED_PREFERENCE")
    
    @schemas.classproperty
    def BORDER_NAT64_0MR_LOCAL_PREFIX(cls):
        return cls("BORDER_NAT64_0MR_LOCAL_PREFIX")
    
    @schemas.classproperty
    def BORDER_NAT64_0MR_FAVORED_PREFIX(cls):
        return cls("BORDER_NAT64_0MR_FAVORED_PREFIX")
    
    @schemas.classproperty
    def BORDER_NAT64_0MR_FAVORED_PREFERENCE(cls):
        return cls("BORDER_NAT64_0MR_FAVORED_PREFERENCE")
    
    @schemas.classproperty
    def BORDER_NAT64_640N_LINK_LOCAL_PREFIX(cls):
        return cls("BORDER_NAT64_640N_LINK_LOCAL_PREFIX")
    
    @schemas.classproperty
    def BORDER_NAT64_640N_LINK_FAVORED_PREFIX(cls):
        return cls("BORDER_NAT64_640N_LINK_FAVORED_PREFIX")
    
    @schemas.classproperty
    def BORDER_NAT64_640N_LINK_FAVORED_PREFERENCE(cls):
        return cls("BORDER_NAT64_640N_LINK_FAVORED_PREFERENCE")
    
    @schemas.classproperty
    def BACKBONE_BORDER_ROUTER_STATE(cls):
        return cls("BACKBONE_BORDER_ROUTER_STATE")
    
    @schemas.classproperty
    def BORDER_AGENT_STATE(cls):
        return cls("BORDER_AGENT_STATE")
    
    @schemas.classproperty
    def BORDER_AGENT_UDP_PORT(cls):
        return cls("BORDER_AGENT_UDP_PORT")
    
    @schemas.classproperty
    def COMMISSIONER_STATE(cls):
        return cls("COMMISSIONER_STATE")
    
    @schemas.classproperty
    def NAT64_PREFIX_MANAGER_STATE(cls):
        return cls("NAT64_PREFIX_MANAGER_STATE")
    
    @schemas.classproperty
    def NAT64_TRANSLATOR_STATE(cls):
        return cls("NAT64_TRANSLATOR_STATE")
    
    @schemas.classproperty
    def NAT64_TRANSLATOR_CIDR(cls):
        return cls("NAT64_TRANSLATOR_CIDR")
    
    @schemas.classproperty
    def HOSTNAME(cls):
        return cls("HOSTNAME")
SortOrderSchema = XiqSortOrder


class ViewsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "BASIC": "BASIC",
                    "DETAIL": "DETAIL",
                    "FULL": "FULL",
                }
            
            @schemas.classproperty
            def BASIC(cls):
                return cls("BASIC")
            
            @schemas.classproperty
            def DETAIL(cls):
                return cls("DETAIL")
            
            @schemas.classproperty
            def FULL(cls):
                return cls("FULL")

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ViewsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class FieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "DEVICE_ID": "DEVICE_ID",
                    "SERIAL_NUMBER": "SERIAL_NUMBER",
                    "EUI64": "EUI64",
                    "EXT_MAC": "EXT_MAC",
                    "RLOC16": "RLOC16",
                    "GLOBAL_IPV6": "GLOBAL_IPV6",
                    "TX_POWER": "TX_POWER",
                    "REGION": "REGION",
                    "THREAD_PLATFORM": "THREAD_PLATFORM",
                    "DEVICE_ROLE": "DEVICE_ROLE",
                    "ROUTER_INTERFACE": "ROUTER_INTERFACE",
                    "VETH0": "VETH0",
                    "NETWORK_DATA": "NETWORK_DATA",
                    "THREAD_MLE_LINK_MODE": "THREAD_MLE_LINK_MODE",
                    "THREAD_VERSION": "THREAD_VERSION",
                    "LEADER_SERVICE": "LEADER_SERVICE",
                    "BORDER_ROUTER_SERVICE": "BORDER_ROUTER_SERVICE",
                    "BACKBONE_BORDER_ROUTER_SERVICE": "BACKBONE_BORDER_ROUTER_SERVICE",
                    "BORDER_AGENT_SERVICE": "BORDER_AGENT_SERVICE",
                    "COMMISSIONER_SERVICE": "COMMISSIONER_SERVICE",
                    "NAT64_SERVICE": "NAT64_SERVICE",
                    "NETWORK_CONFIG": "NETWORK_CONFIG",
                    "OWNER_ID": "OWNER_ID",
                    "ORG_ID": "ORG_ID",
                    "ID": "ID",
                    "CREATE_TIME": "CREATE_TIME",
                    "UPDATE_TIME": "UPDATE_TIME",
                    "ACTIVE_CLIENTS": "ACTIVE_CLIENTS",
                    "HOSTNAME": "HOSTNAME",
                    "LAST_REPORTED": "LAST_REPORTED",
                    "THREAD_CONNECTED": "THREAD_CONNECTED",
                }
            
            @schemas.classproperty
            def DEVICE_ID(cls):
                return cls("DEVICE_ID")
            
            @schemas.classproperty
            def SERIAL_NUMBER(cls):
                return cls("SERIAL_NUMBER")
            
            @schemas.classproperty
            def EUI64(cls):
                return cls("EUI64")
            
            @schemas.classproperty
            def EXT_MAC(cls):
                return cls("EXT_MAC")
            
            @schemas.classproperty
            def RLOC16(cls):
                return cls("RLOC16")
            
            @schemas.classproperty
            def GLOBAL_IPV6(cls):
                return cls("GLOBAL_IPV6")
            
            @schemas.classproperty
            def TX_POWER(cls):
                return cls("TX_POWER")
            
            @schemas.classproperty
            def REGION(cls):
                return cls("REGION")
            
            @schemas.classproperty
            def THREAD_PLATFORM(cls):
                return cls("THREAD_PLATFORM")
            
            @schemas.classproperty
            def DEVICE_ROLE(cls):
                return cls("DEVICE_ROLE")
            
            @schemas.classproperty
            def ROUTER_INTERFACE(cls):
                return cls("ROUTER_INTERFACE")
            
            @schemas.classproperty
            def VETH0(cls):
                return cls("VETH0")
            
            @schemas.classproperty
            def NETWORK_DATA(cls):
                return cls("NETWORK_DATA")
            
            @schemas.classproperty
            def THREAD_MLE_LINK_MODE(cls):
                return cls("THREAD_MLE_LINK_MODE")
            
            @schemas.classproperty
            def THREAD_VERSION(cls):
                return cls("THREAD_VERSION")
            
            @schemas.classproperty
            def LEADER_SERVICE(cls):
                return cls("LEADER_SERVICE")
            
            @schemas.classproperty
            def BORDER_ROUTER_SERVICE(cls):
                return cls("BORDER_ROUTER_SERVICE")
            
            @schemas.classproperty
            def BACKBONE_BORDER_ROUTER_SERVICE(cls):
                return cls("BACKBONE_BORDER_ROUTER_SERVICE")
            
            @schemas.classproperty
            def BORDER_AGENT_SERVICE(cls):
                return cls("BORDER_AGENT_SERVICE")
            
            @schemas.classproperty
            def COMMISSIONER_SERVICE(cls):
                return cls("COMMISSIONER_SERVICE")
            
            @schemas.classproperty
            def NAT64_SERVICE(cls):
                return cls("NAT64_SERVICE")
            
            @schemas.classproperty
            def NETWORK_CONFIG(cls):
                return cls("NETWORK_CONFIG")
            
            @schemas.classproperty
            def OWNER_ID(cls):
                return cls("OWNER_ID")
            
            @schemas.classproperty
            def ORG_ID(cls):
                return cls("ORG_ID")
            
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
            def ACTIVE_CLIENTS(cls):
                return cls("ACTIVE_CLIENTS")
            
            @schemas.classproperty
            def HOSTNAME(cls):
                return cls("HOSTNAME")
            
            @schemas.classproperty
            def LAST_REPORTED(cls):
                return cls("LAST_REPORTED")
            
            @schemas.classproperty
            def THREAD_CONNECTED(cls):
                return cls("THREAD_CONNECTED")

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'ids': typing.Union[IdsSchema, list, tuple, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'sortField': typing.Union[SortFieldSchema, str, ],
        'sortOrder': typing.Union[SortOrderSchema, ],
        'views': typing.Union[ViewsSchema, list, tuple, ],
        'fields': typing.Union[FieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    required=True,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_sort_field = api_client.QueryParameter(
    name="sortField",
    style=api_client.ParameterStyle.FORM,
    schema=SortFieldSchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sortOrder",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
request_query_views = api_client.QueryParameter(
    name="views",
    style=api_client.ParameterStyle.FORM,
    schema=ViewsSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
_auth = [
    'Bearer',
]
SchemaFor401ResponseBodyApplicationJson = XiqError


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = XiqError


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor503ResponseBodyApplicationJson = XiqError


@dataclass
class ApiResponseFor503(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor503ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_503 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor503,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor503ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = XiqError


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = PagedXiqThreadRouter


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '401': _response_for_401,
    '400': _response_for_400,
    '503': _response_for_503,
    '500': _response_for_500,
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_thread_routers_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_thread_routers_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_thread_routers_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_thread_routers_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        List thread routers
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_ids,
            request_query_page,
            request_query_limit,
            request_query_sort_field,
            request_query_sort_order,
            request_query_views,
            request_query_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetThreadRouters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_thread_routers(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_thread_routers(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_thread_routers(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_thread_routers(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_thread_routers_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_thread_routers_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


