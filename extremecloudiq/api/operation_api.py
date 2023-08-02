# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from extremecloudiq.api_client import ApiClient
from extremecloudiq.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OperationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_operation(self, operation_id, **kwargs):  # noqa: E501
        """Cancel Long-Running Operation (LRO)  # noqa: E501

        When the cancelable is true in operation metadata the clients are allowed to send a cancel request to ask the backend to cancel the operation. The server makes its best effort to cancel the operation, but success is not guaranteed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_operation(operation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str operation_id: The operation ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_operation_with_http_info(operation_id, **kwargs)  # noqa: E501

    def cancel_operation_with_http_info(self, operation_id, **kwargs):  # noqa: E501
        """Cancel Long-Running Operation (LRO)  # noqa: E501

        When the cancelable is true in operation metadata the clients are allowed to send a cancel request to ask the backend to cancel the operation. The server makes its best effort to cancel the operation, but success is not guaranteed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_operation_with_http_info(operation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str operation_id: The operation ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'operation_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_operation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'operation_id' is set
        if self.api_client.client_side_validation and ('operation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['operation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `operation_id` when calling `cancel_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'operation_id' in local_var_params:
            path_params['operationId'] = local_var_params['operation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/operations/{operationId}/:cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_operation(self, operation_id, **kwargs):  # noqa: E501
        """Delete Long-Running Operation (LRO)  # noqa: E501

        The Long-Running Operation (LRO) can be deleted when the operation is done or in PENDING status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_operation(operation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str operation_id: The operation ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_operation_with_http_info(operation_id, **kwargs)  # noqa: E501

    def delete_operation_with_http_info(self, operation_id, **kwargs):  # noqa: E501
        """Delete Long-Running Operation (LRO)  # noqa: E501

        The Long-Running Operation (LRO) can be deleted when the operation is done or in PENDING status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_operation_with_http_info(operation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str operation_id: The operation ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'operation_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_operation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'operation_id' is set
        if self.api_client.client_side_validation and ('operation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['operation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `operation_id` when calling `delete_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'operation_id' in local_var_params:
            path_params['operationId'] = local_var_params['operation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/operations/{operationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_operation(self, operation_id, **kwargs):  # noqa: E501
        """Get Long-Running Operation (LRO) status and result  # noqa: E501

        Get the Long-Running Operation (LRO) status and result. The response will include either result or error if the operation is done.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation(operation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str operation_id: The operation ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqOperationObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_operation_with_http_info(operation_id, **kwargs)  # noqa: E501

    def get_operation_with_http_info(self, operation_id, **kwargs):  # noqa: E501
        """Get Long-Running Operation (LRO) status and result  # noqa: E501

        Get the Long-Running Operation (LRO) status and result. The response will include either result or error if the operation is done.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_with_http_info(operation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str operation_id: The operation ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqOperationObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'operation_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'operation_id' is set
        if self.api_client.client_side_validation and ('operation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['operation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `operation_id` when calling `get_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'operation_id' in local_var_params:
            path_params['operationId'] = local_var_params['operation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/operations/{operationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqOperationObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
