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

from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_update_missing_vlan_excluded_vlan_response import XiqUpdateMissingVlanExcludedVlanResponse
from extremecloudiq.model.xiq_excluded_vlan_action_type import XiqExcludedVlanActionType

# Query params
ActionTypeSchema = XiqExcludedVlanActionType
DismissSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'action_type': typing.Union[ActionTypeSchema, ],
        'dismiss': typing.Union[DismissSchema, bool, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_action_type = api_client.QueryParameter(
    name="action_type",
    style=api_client.ParameterStyle.FORM,
    schema=ActionTypeSchema,
    required=True,
    explode=True,
)
request_query_dismiss = api_client.QueryParameter(
    name="dismiss",
    style=api_client.ParameterStyle.FORM,
    schema=DismissSchema,
    required=True,
    explode=True,
)
# body param


class SchemaForRequestBodyMultipartFormData(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "csv_file",
        }
        
        class properties:
            csv_file = schemas.BinarySchema
            __annotations__ = {
                "csv_file": csv_file,
            }
    
    csv_file: MetaOapg.properties.csv_file
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["csv_file"]) -> MetaOapg.properties.csv_file: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["csv_file", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["csv_file"]) -> MetaOapg.properties.csv_file: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["csv_file", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        csv_file: typing.Union[MetaOapg.properties.csv_file, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyMultipartFormData':
        return super().__new__(
            cls,
            *_args,
            csv_file=csv_file,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "csv_file",
        }
        
        class properties:
            csv_file = schemas.BinarySchema
            __annotations__ = {
                "csv_file": csv_file,
            }
    
    csv_file: MetaOapg.properties.csv_file
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["csv_file"]) -> MetaOapg.properties.csv_file: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["csv_file", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["csv_file"]) -> MetaOapg.properties.csv_file: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["csv_file", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        csv_file: typing.Union[MetaOapg.properties.csv_file, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            csv_file=csv_file,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyTextCsv(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "csv_file",
        }
        
        class properties:
            csv_file = schemas.BinarySchema
            __annotations__ = {
                "csv_file": csv_file,
            }
    
    csv_file: MetaOapg.properties.csv_file
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["csv_file"]) -> MetaOapg.properties.csv_file: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["csv_file", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["csv_file"]) -> MetaOapg.properties.csv_file: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["csv_file", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        csv_file: typing.Union[MetaOapg.properties.csv_file, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyTextCsv':
        return super().__new__(
            cls,
            *_args,
            csv_file=csv_file,
            _configuration=_configuration,
            **kwargs,
        )


request_body_body = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/csv': api_client.MediaType(
            schema=SchemaForRequestBodyTextCsv),
    },
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
SchemaFor200ResponseBodyApplicationJson = XiqUpdateMissingVlanExcludedVlanResponse


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
    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        content_type: typing_extensions.Literal["multipart/form-data"] = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        content_type: typing_extensions.Literal["text/csv"],
        body: typing.Union[SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _update_missing_vlan_excluded_vlan_csv_oapg(
        self,
        content_type: str = 'multipart/form-data',
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_action_type,
            request_query_dismiss,
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

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
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


class UpdateMissingVlanExcludedVlanCsv(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def update_missing_vlan_excluded_vlan_csv(
        self,
        content_type: typing_extensions.Literal["multipart/form-data"] = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def update_missing_vlan_excluded_vlan_csv(
        self,
        content_type: typing_extensions.Literal["application/json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def update_missing_vlan_excluded_vlan_csv(
        self,
        content_type: typing_extensions.Literal["text/csv"],
        body: typing.Union[SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def update_missing_vlan_excluded_vlan_csv(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def update_missing_vlan_excluded_vlan_csv(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def update_missing_vlan_excluded_vlan_csv(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def update_missing_vlan_excluded_vlan_csv(
        self,
        content_type: str = 'multipart/form-data',
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._update_missing_vlan_excluded_vlan_csv_oapg(
            body=body,
            query_params=query_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["multipart/form-data"] = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"],
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["text/csv"],
        body: typing.Union[SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'multipart/form-data',
        body: typing.Union[SchemaForRequestBodyMultipartFormData, dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, SchemaForRequestBodyTextCsv, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._update_missing_vlan_excluded_vlan_csv_oapg(
            body=body,
            query_params=query_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


