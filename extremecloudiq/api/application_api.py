# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
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


class ApplicationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_application_top_clients_usage(self, id, n, start_time, end_time, **kwargs):  # noqa: E501
        """List the TopN clients for a application  # noqa: E501

        List the TopN clients by usage for a specific application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_application_top_clients_usage(id, n, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The application ID (required)
        :param int n: The TopN number (required)
        :param int start_time: The start time for querying top client usage of application (required)
        :param int end_time: The end time for querying top application usage of application (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqApplicationTopClientsUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_application_top_clients_usage_with_http_info(id, n, start_time, end_time, **kwargs)  # noqa: E501

    def list_application_top_clients_usage_with_http_info(self, id, n, start_time, end_time, **kwargs):  # noqa: E501
        """List the TopN clients for a application  # noqa: E501

        List the TopN clients by usage for a specific application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_application_top_clients_usage_with_http_info(id, n, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The application ID (required)
        :param int n: The TopN number (required)
        :param int start_time: The start time for querying top client usage of application (required)
        :param int end_time: The end time for querying top application usage of application (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[XiqApplicationTopClientsUsage], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'n',
            'start_time',
            'end_time'
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
                    " to method list_application_top_clients_usage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `list_application_top_clients_usage`")  # noqa: E501
        # verify the required parameter 'n' is set
        if self.api_client.client_side_validation and ('n' not in local_var_params or  # noqa: E501
                                                        local_var_params['n'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `n` when calling `list_application_top_clients_usage`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_time` when calling `list_application_top_clients_usage`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_time` when calling `list_application_top_clients_usage`")  # noqa: E501

        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `list_application_top_clients_usage`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `list_application_top_clients_usage`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'n' in local_var_params:
            path_params['n'] = local_var_params['n']  # noqa: E501

        query_params = []
        if 'start_time' in local_var_params and local_var_params['start_time'] is not None:  # noqa: E501
            query_params.append(('startTime', local_var_params['start_time']))  # noqa: E501
        if 'end_time' in local_var_params and local_var_params['end_time'] is not None:  # noqa: E501
            query_params.append(('endTime', local_var_params['end_time']))  # noqa: E501

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
            '/applications/{id}/clients/top{n}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[XiqApplicationTopClientsUsage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_applications(self, **kwargs):  # noqa: E501
        """List the applications  # noqa: E501

        List a page of applications by filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_applications(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param str name: Application Name
        :param XiqApplicationDetectionProtocol detection_protocol: Application Detection Protocol, only for custom Application
        :param XiqApplicationDetectionType detection_type: Application Detection Type, only for custom Application
        :param bool predefined: Flag to filter predefined or custom Application
        :param XiqApplicationSortField sort_field: The sort field
        :param XiqSortOrder order: The sort order (ascending by default)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedXiqApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_applications_with_http_info(**kwargs)  # noqa: E501

    def list_applications_with_http_info(self, **kwargs):  # noqa: E501
        """List the applications  # noqa: E501

        List a page of applications by filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_applications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param str name: Application Name
        :param XiqApplicationDetectionProtocol detection_protocol: Application Detection Protocol, only for custom Application
        :param XiqApplicationDetectionType detection_type: Application Detection Type, only for custom Application
        :param bool predefined: Flag to filter predefined or custom Application
        :param XiqApplicationSortField sort_field: The sort field
        :param XiqSortOrder order: The sort order (ascending by default)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedXiqApplication, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'page',
            'limit',
            'name',
            'detection_protocol',
            'detection_type',
            'predefined',
            'sort_field',
            'order'
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
                    " to method list_applications" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_applications`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_applications`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_applications`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'detection_protocol' in local_var_params and local_var_params['detection_protocol'] is not None:  # noqa: E501
            query_params.append(('detectionProtocol', local_var_params['detection_protocol']))  # noqa: E501
        if 'detection_type' in local_var_params and local_var_params['detection_type'] is not None:  # noqa: E501
            query_params.append(('detectionType', local_var_params['detection_type']))  # noqa: E501
        if 'predefined' in local_var_params and local_var_params['predefined'] is not None:  # noqa: E501
            query_params.append(('predefined', local_var_params['predefined']))  # noqa: E501
        if 'sort_field' in local_var_params and local_var_params['sort_field'] is not None:  # noqa: E501
            query_params.append(('sortField', local_var_params['sort_field']))  # noqa: E501
        if 'order' in local_var_params and local_var_params['order'] is not None:  # noqa: E501
            query_params.append(('order', local_var_params['order']))  # noqa: E501

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
            '/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedXiqApplication',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_top_applications_usage(self, n, start_time, end_time, **kwargs):  # noqa: E501
        """List the TopN applications  # noqa: E501

        List the TopN applications by usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_top_applications_usage(n, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int n: The TopN number (required)
        :param int start_time: The start time for querying top application usage (required)
        :param int end_time: The end time for querying top application usage (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqTopApplicationsUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_top_applications_usage_with_http_info(n, start_time, end_time, **kwargs)  # noqa: E501

    def list_top_applications_usage_with_http_info(self, n, start_time, end_time, **kwargs):  # noqa: E501
        """List the TopN applications  # noqa: E501

        List the TopN applications by usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_top_applications_usage_with_http_info(n, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int n: The TopN number (required)
        :param int start_time: The start time for querying top application usage (required)
        :param int end_time: The end time for querying top application usage (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[XiqTopApplicationsUsage], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'n',
            'start_time',
            'end_time'
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
                    " to method list_top_applications_usage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'n' is set
        if self.api_client.client_side_validation and ('n' not in local_var_params or  # noqa: E501
                                                        local_var_params['n'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `n` when calling `list_top_applications_usage`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_time` when calling `list_top_applications_usage`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_time` when calling `list_top_applications_usage`")  # noqa: E501

        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `list_top_applications_usage`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `list_top_applications_usage`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'n' in local_var_params:
            path_params['n'] = local_var_params['n']  # noqa: E501

        query_params = []
        if 'start_time' in local_var_params and local_var_params['start_time'] is not None:  # noqa: E501
            query_params.append(('startTime', local_var_params['start_time']))  # noqa: E501
        if 'end_time' in local_var_params and local_var_params['end_time'] is not None:  # noqa: E501
            query_params.append(('endTime', local_var_params['end_time']))  # noqa: E501

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
            '/applications/top{n}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[XiqTopApplicationsUsage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
