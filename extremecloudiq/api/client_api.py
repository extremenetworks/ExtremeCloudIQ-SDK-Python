# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
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


class ClientApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_client(self, id, **kwargs):  # noqa: E501
        """Get client info  # noqa: E501

        Get client detailed information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The client ID (required)
        :param list[XiqClientView] views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] fields: The client fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_client_with_http_info(id, **kwargs)  # noqa: E501

    def get_client_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get client info  # noqa: E501

        Get client detailed information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The client ID (required)
        :param list[XiqClientView] views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] fields: The client fields to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqClient, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'views',
            'fields'
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
                    " to method get_client" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_client`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'views' in local_var_params and local_var_params['views'] is not None:  # noqa: E501
            query_params.append(('views', local_var_params['views']))  # noqa: E501
            collection_formats['views'] = 'multi'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501

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
            '/clients/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqClient',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_client_summary(self, **kwargs):  # noqa: E501
        """Get client summary metrics  # noqa: E501

        Get number of connected wireless clients and number of detected wired clients.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] location_ids: The location IDs
        :param list[int] device_ids: The device IDs
        :param list[int] vlans: The associate VLAN IDs
        :param list[str] user_profile_names: The user profile names
        :param list[str] ssids: The SSIDs
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClientSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_client_summary_with_http_info(**kwargs)  # noqa: E501

    def get_client_summary_with_http_info(self, **kwargs):  # noqa: E501
        """Get client summary metrics  # noqa: E501

        Get number of connected wireless clients and number of detected wired clients.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] location_ids: The location IDs
        :param list[int] device_ids: The device IDs
        :param list[int] vlans: The associate VLAN IDs
        :param list[str] user_profile_names: The user profile names
        :param list[str] ssids: The SSIDs
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqClientSummary, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_ids',
            'device_ids',
            'vlans',
            'user_profile_names',
            'ssids'
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
                    " to method get_client_summary" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_ids' in local_var_params and local_var_params['location_ids'] is not None:  # noqa: E501
            query_params.append(('locationIds', local_var_params['location_ids']))  # noqa: E501
            collection_formats['locationIds'] = 'multi'  # noqa: E501
        if 'device_ids' in local_var_params and local_var_params['device_ids'] is not None:  # noqa: E501
            query_params.append(('deviceIds', local_var_params['device_ids']))  # noqa: E501
            collection_formats['deviceIds'] = 'multi'  # noqa: E501
        if 'vlans' in local_var_params and local_var_params['vlans'] is not None:  # noqa: E501
            query_params.append(('vlans', local_var_params['vlans']))  # noqa: E501
            collection_formats['vlans'] = 'multi'  # noqa: E501
        if 'user_profile_names' in local_var_params and local_var_params['user_profile_names'] is not None:  # noqa: E501
            query_params.append(('userProfileNames', local_var_params['user_profile_names']))  # noqa: E501
            collection_formats['userProfileNames'] = 'multi'  # noqa: E501
        if 'ssids' in local_var_params and local_var_params['ssids'] is not None:  # noqa: E501
            query_params.append(('ssids', local_var_params['ssids']))  # noqa: E501
            collection_formats['ssids'] = 'multi'  # noqa: E501

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
            '/clients/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqClientSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_client_usage(self, client_ids, start_time, end_time, **kwargs):  # noqa: E501
        """Get usage per client  # noqa: E501

        Get the client usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_usage(client_ids, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] client_ids: The client IDs (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970 (required)
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970 (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqClientUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_client_usage_with_http_info(client_ids, start_time, end_time, **kwargs)  # noqa: E501

    def get_client_usage_with_http_info(self, client_ids, start_time, end_time, **kwargs):  # noqa: E501
        """Get usage per client  # noqa: E501

        Get the client usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_usage_with_http_info(client_ids, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] client_ids: The client IDs (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970 (required)
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970 (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[XiqClientUsage], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'client_ids',
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
                    " to method get_client_usage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'client_ids' is set
        if self.api_client.client_side_validation and ('client_ids' not in local_var_params or  # noqa: E501
                                                        local_var_params['client_ids'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `client_ids` when calling `get_client_usage`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_time` when calling `get_client_usage`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_time` when calling `get_client_usage`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_ids' in local_var_params and local_var_params['client_ids'] is not None:  # noqa: E501
            query_params.append(('clientIds', local_var_params['client_ids']))  # noqa: E501
            collection_formats['clientIds'] = 'multi'  # noqa: E501
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
            '/clients/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[XiqClientUsage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_active_clients(self, **kwargs):  # noqa: E501
        """List active clients  # noqa: E501

        List active clients with filters and pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_active_clients(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] location_ids: The location IDs
        :param list[int] device_ids: The device IDs
        :param list[int] vlans: The associate vlan IDs
        :param list[str] user_profile_names: The user profile names
        :param list[str] ssids: The SSIDs
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param list[XiqClientView] views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] fields: The client fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedXiqClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_active_clients_with_http_info(**kwargs)  # noqa: E501

    def list_active_clients_with_http_info(self, **kwargs):  # noqa: E501
        """List active clients  # noqa: E501

        List active clients with filters and pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_active_clients_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] location_ids: The location IDs
        :param list[int] device_ids: The device IDs
        :param list[int] vlans: The associate vlan IDs
        :param list[str] user_profile_names: The user profile names
        :param list[str] ssids: The SSIDs
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param list[XiqClientView] views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] fields: The client fields to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedXiqClient, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_ids',
            'device_ids',
            'vlans',
            'user_profile_names',
            'ssids',
            'page',
            'limit',
            'views',
            'fields'
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
                    " to method list_active_clients" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_active_clients`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_active_clients`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_active_clients`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_ids' in local_var_params and local_var_params['location_ids'] is not None:  # noqa: E501
            query_params.append(('locationIds', local_var_params['location_ids']))  # noqa: E501
            collection_formats['locationIds'] = 'multi'  # noqa: E501
        if 'device_ids' in local_var_params and local_var_params['device_ids'] is not None:  # noqa: E501
            query_params.append(('deviceIds', local_var_params['device_ids']))  # noqa: E501
            collection_formats['deviceIds'] = 'multi'  # noqa: E501
        if 'vlans' in local_var_params and local_var_params['vlans'] is not None:  # noqa: E501
            query_params.append(('vlans', local_var_params['vlans']))  # noqa: E501
            collection_formats['vlans'] = 'multi'  # noqa: E501
        if 'user_profile_names' in local_var_params and local_var_params['user_profile_names'] is not None:  # noqa: E501
            query_params.append(('userProfileNames', local_var_params['user_profile_names']))  # noqa: E501
            collection_formats['userProfileNames'] = 'multi'  # noqa: E501
        if 'ssids' in local_var_params and local_var_params['ssids'] is not None:  # noqa: E501
            query_params.append(('ssids', local_var_params['ssids']))  # noqa: E501
            collection_formats['ssids'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'views' in local_var_params and local_var_params['views'] is not None:  # noqa: E501
            query_params.append(('views', local_var_params['views']))  # noqa: E501
            collection_formats['views'] = 'multi'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501

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
            '/clients/active', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedXiqClient',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
