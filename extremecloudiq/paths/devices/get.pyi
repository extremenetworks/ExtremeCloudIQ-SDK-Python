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
from extremecloudiq.model.xiq_device_sort_field import XiqDeviceSortField
from extremecloudiq.model.xiq_device_null_field import XiqDeviceNullField
from extremecloudiq.model.xiq_device_field import XiqDeviceField
from extremecloudiq.model.xiq_device_view import XiqDeviceView
from extremecloudiq.model.xiq_device_admin_state import XiqDeviceAdminState
from extremecloudiq.model.paged_xiq_device import PagedXiqDevice
from extremecloudiq.model.xiq_device_type import XiqDeviceType

# Query params


class PageSchema(
    schemas.Int32Schema
):
    pass


class LimitSchema(
    schemas.Int32Schema
):
    pass
LocationIdSchema = schemas.Int64Schema
ConnectedSchema = schemas.BoolSchema


class AdminStatesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['XiqDeviceAdminState']:
            return XiqDeviceAdminState

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['XiqDeviceAdminState'], typing.List['XiqDeviceAdminState']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AdminStatesSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'XiqDeviceAdminState':
        return super().__getitem__(i)


class MacAddressesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MacAddressesSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class SnsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SnsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class HostnamesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'HostnamesSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
SortFieldSchema = XiqDeviceSortField
OrderSchema = XiqSortOrder


class ViewsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['XiqDeviceView']:
            return XiqDeviceView

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['XiqDeviceView'], typing.List['XiqDeviceView']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ViewsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'XiqDeviceView':
        return super().__getitem__(i)


class FieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['XiqDeviceField']:
            return XiqDeviceField

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['XiqDeviceField'], typing.List['XiqDeviceField']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'XiqDeviceField':
        return super().__getitem__(i)


class DeviceTypesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['XiqDeviceType']:
            return XiqDeviceType

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['XiqDeviceType'], typing.List['XiqDeviceType']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DeviceTypesSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'XiqDeviceType':
        return super().__getitem__(i)
NullFieldSchema = XiqDeviceNullField


class LocationIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.Int64Schema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LocationIdsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ModelAsyncSchema = schemas.BoolSchema
ConfigMismatchSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'locationId': typing.Union[LocationIdSchema, decimal.Decimal, int, ],
        'connected': typing.Union[ConnectedSchema, bool, ],
        'adminStates': typing.Union[AdminStatesSchema, list, tuple, ],
        'macAddresses': typing.Union[MacAddressesSchema, list, tuple, ],
        'sns': typing.Union[SnsSchema, list, tuple, ],
        'hostnames': typing.Union[HostnamesSchema, list, tuple, ],
        'sortField': typing.Union[SortFieldSchema, ],
        'order': typing.Union[OrderSchema, ],
        'views': typing.Union[ViewsSchema, list, tuple, ],
        'fields': typing.Union[FieldsSchema, list, tuple, ],
        'deviceTypes': typing.Union[DeviceTypesSchema, list, tuple, ],
        'nullField': typing.Union[NullFieldSchema, ],
        'locationIds': typing.Union[LocationIdsSchema, list, tuple, ],
        'async': typing.Union[ModelAsyncSchema, bool, ],
        'configMismatch': typing.Union[ConfigMismatchSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
request_query_location_id = api_client.QueryParameter(
    name="locationId",
    style=api_client.ParameterStyle.FORM,
    schema=LocationIdSchema,
    explode=True,
)
request_query_connected = api_client.QueryParameter(
    name="connected",
    style=api_client.ParameterStyle.FORM,
    schema=ConnectedSchema,
    explode=True,
)
request_query_admin_states = api_client.QueryParameter(
    name="adminStates",
    style=api_client.ParameterStyle.FORM,
    schema=AdminStatesSchema,
    explode=True,
)
request_query_mac_addresses = api_client.QueryParameter(
    name="macAddresses",
    style=api_client.ParameterStyle.FORM,
    schema=MacAddressesSchema,
    explode=True,
)
request_query_sns = api_client.QueryParameter(
    name="sns",
    style=api_client.ParameterStyle.FORM,
    schema=SnsSchema,
    explode=True,
)
request_query_hostnames = api_client.QueryParameter(
    name="hostnames",
    style=api_client.ParameterStyle.FORM,
    schema=HostnamesSchema,
    explode=True,
)
request_query_sort_field = api_client.QueryParameter(
    name="sortField",
    style=api_client.ParameterStyle.FORM,
    schema=SortFieldSchema,
    explode=True,
)
request_query_order = api_client.QueryParameter(
    name="order",
    style=api_client.ParameterStyle.FORM,
    schema=OrderSchema,
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
request_query_device_types = api_client.QueryParameter(
    name="deviceTypes",
    style=api_client.ParameterStyle.FORM,
    schema=DeviceTypesSchema,
    explode=True,
)
request_query_null_field = api_client.QueryParameter(
    name="nullField",
    style=api_client.ParameterStyle.FORM,
    schema=NullFieldSchema,
    explode=True,
)
request_query_location_ids = api_client.QueryParameter(
    name="locationIds",
    style=api_client.ParameterStyle.FORM,
    schema=LocationIdsSchema,
    explode=True,
)
request_query__async = api_client.QueryParameter(
    name="async",
    style=api_client.ParameterStyle.FORM,
    schema=ModelAsyncSchema,
    explode=True,
)
request_query_config_mismatch = api_client.QueryParameter(
    name="configMismatch",
    style=api_client.ParameterStyle.FORM,
    schema=ConfigMismatchSchema,
    explode=True,
)
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
SchemaFor200ResponseBodyApplicationJson = PagedXiqDevice


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _list_devices_oapg(
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
    def _list_devices_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _list_devices_oapg(
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

    def _list_devices_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        [LRO] List devices
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_limit,
            request_query_location_id,
            request_query_connected,
            request_query_admin_states,
            request_query_mac_addresses,
            request_query_sns,
            request_query_hostnames,
            request_query_sort_field,
            request_query_order,
            request_query_views,
            request_query_fields,
            request_query_device_types,
            request_query_null_field,
            request_query_location_ids,
            request_query__async,
            request_query_config_mismatch,
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


class ListDevices(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def list_devices(
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
    def list_devices(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def list_devices(
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

    def list_devices(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_devices_oapg(
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
        return self._list_devices_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


