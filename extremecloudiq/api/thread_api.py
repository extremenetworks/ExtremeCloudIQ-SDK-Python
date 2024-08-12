# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
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


class ThreadApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_thread_network_topology(self, network_config_ids, **kwargs):  # noqa: E501
        """Get thread network topology  # noqa: E501

        Get thread routers, neighboring routers and end-devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_thread_network_topology(network_config_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] network_config_ids: Thread network config id (required)
        :param list[str] router_fields: The thread router fields to return
        :param list[str] router_views: The views to return thread router fields
        :param list[XiqClientView] client_views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] client_fields: The client fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqThreadNetworkTopology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_thread_network_topology_with_http_info(network_config_ids, **kwargs)  # noqa: E501

    def get_thread_network_topology_with_http_info(self, network_config_ids, **kwargs):  # noqa: E501
        """Get thread network topology  # noqa: E501

        Get thread routers, neighboring routers and end-devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_thread_network_topology_with_http_info(network_config_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] network_config_ids: Thread network config id (required)
        :param list[str] router_fields: The thread router fields to return
        :param list[str] router_views: The views to return thread router fields
        :param list[XiqClientView] client_views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] client_fields: The client fields to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqThreadNetworkTopology, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'network_config_ids',
            'router_fields',
            'router_views',
            'client_views',
            'client_fields'
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
                    " to method get_thread_network_topology" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'network_config_ids' is set
        if self.api_client.client_side_validation and ('network_config_ids' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_config_ids'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_config_ids` when calling `get_thread_network_topology`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'network_config_ids' in local_var_params and local_var_params['network_config_ids'] is not None:  # noqa: E501
            query_params.append(('networkConfigIds', local_var_params['network_config_ids']))  # noqa: E501
            collection_formats['networkConfigIds'] = 'multi'  # noqa: E501
        if 'router_fields' in local_var_params and local_var_params['router_fields'] is not None:  # noqa: E501
            query_params.append(('routerFields', local_var_params['router_fields']))  # noqa: E501
            collection_formats['routerFields'] = 'multi'  # noqa: E501
        if 'router_views' in local_var_params and local_var_params['router_views'] is not None:  # noqa: E501
            query_params.append(('routerViews', local_var_params['router_views']))  # noqa: E501
            collection_formats['routerViews'] = 'multi'  # noqa: E501
        if 'client_views' in local_var_params and local_var_params['client_views'] is not None:  # noqa: E501
            query_params.append(('clientViews', local_var_params['client_views']))  # noqa: E501
            collection_formats['clientViews'] = 'multi'  # noqa: E501
        if 'client_fields' in local_var_params and local_var_params['client_fields'] is not None:  # noqa: E501
            query_params.append(('clientFields', local_var_params['client_fields']))  # noqa: E501
            collection_formats['clientFields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/thread/topology', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqThreadNetworkTopology',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_thread_networks(self, folder_id, **kwargs):  # noqa: E501
        """Get active thread networks  # noqa: E501

        Get thread networks with atleast one device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_thread_networks(folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int folder_id: Thread network config folder id (required)
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param list[str] fields: The thread network config fields to return
        :param list[str] views: The views to return thread network config fields
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqThreadNetworks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_thread_networks_with_http_info(folder_id, **kwargs)  # noqa: E501

    def get_thread_networks_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """Get active thread networks  # noqa: E501

        Get thread networks with atleast one device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_thread_networks_with_http_info(folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int folder_id: Thread network config folder id (required)
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param list[str] fields: The thread network config fields to return
        :param list[str] views: The views to return thread network config fields
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqThreadNetworks, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'folder_id',
            'page',
            'limit',
            'fields',
            'views'
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
                    " to method get_thread_networks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'folder_id' is set
        if self.api_client.client_side_validation and ('folder_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['folder_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `folder_id` when calling `get_thread_networks`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_thread_networks`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_thread_networks`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_thread_networks`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'folder_id' in local_var_params and local_var_params['folder_id'] is not None:  # noqa: E501
            query_params.append(('folderId', local_var_params['folder_id']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'views' in local_var_params and local_var_params['views'] is not None:  # noqa: E501
            query_params.append(('views', local_var_params['views']))  # noqa: E501
            collection_formats['views'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/thread/networks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqThreadNetworks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_thread_routers(self, ids, **kwargs):  # noqa: E501
        """List thread routers  # noqa: E501

        List thread routers with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_thread_routers(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] ids: The thread router IDs (required)
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param str sort_field: The sort field
        :param XiqSortOrder sort_order: The sort order (ascending by default)
        :param list[str] views: The views to return thread router fields
        :param list[str] fields: The thread router fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedXiqThreadRouter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_thread_routers_with_http_info(ids, **kwargs)  # noqa: E501

    def get_thread_routers_with_http_info(self, ids, **kwargs):  # noqa: E501
        """List thread routers  # noqa: E501

        List thread routers with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_thread_routers_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] ids: The thread router IDs (required)
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param str sort_field: The sort field
        :param XiqSortOrder sort_order: The sort order (ascending by default)
        :param list[str] views: The views to return thread router fields
        :param list[str] fields: The thread router fields to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedXiqThreadRouter, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'ids',
            'page',
            'limit',
            'sort_field',
            'sort_order',
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
                    " to method get_thread_routers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ids' is set
        if self.api_client.client_side_validation and ('ids' not in local_var_params or  # noqa: E501
                                                        local_var_params['ids'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ids` when calling `get_thread_routers`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_thread_routers`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_thread_routers`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_thread_routers`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params and local_var_params['ids'] is not None:  # noqa: E501
            query_params.append(('ids', local_var_params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'sort_field' in local_var_params and local_var_params['sort_field'] is not None:  # noqa: E501
            query_params.append(('sortField', local_var_params['sort_field']))  # noqa: E501
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501
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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/thread/routers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedXiqThreadRouter',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
