# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
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


class CopilotAnomaliesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_devices_by_location(self, **kwargs):  # noqa: E501
        """get_devices_by_location  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_devices_by_location(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param XiqAnomalyType anomaly_type: Anomaly type
        :param int location_id: The location id
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqAnomalyDevicesByLocationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_devices_by_location_with_http_info(**kwargs)  # noqa: E501

    def get_devices_by_location_with_http_info(self, **kwargs):  # noqa: E501
        """get_devices_by_location  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_devices_by_location_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param XiqAnomalyType anomaly_type: Anomaly type
        :param int location_id: The location id
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqAnomalyDevicesByLocationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'anomaly_type',
            'location_id'
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
                    " to method get_devices_by_location" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'anomaly_type' in local_var_params and local_var_params['anomaly_type'] is not None:  # noqa: E501
            query_params.append(('anomalyType', local_var_params['anomaly_type']))  # noqa: E501
        if 'location_id' in local_var_params and local_var_params['location_id'] is not None:  # noqa: E501
            query_params.append(('locationId', local_var_params['location_id']))  # noqa: E501

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
            '/copilot/anomalies/devices-by-location', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqAnomalyDevicesByLocationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_recurrence_channel_stats(self, anomaly_id, **kwargs):  # noqa: E501
        """get_dfs_recurrence_channel_stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dfs_recurrence_channel_stats(anomaly_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str anomaly_id: The anomaly id (required)
        :param int location_id: The location id
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqDfsRecurenceChannelStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dfs_recurrence_channel_stats_with_http_info(anomaly_id, **kwargs)  # noqa: E501

    def get_dfs_recurrence_channel_stats_with_http_info(self, anomaly_id, **kwargs):  # noqa: E501
        """get_dfs_recurrence_channel_stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dfs_recurrence_channel_stats_with_http_info(anomaly_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str anomaly_id: The anomaly id (required)
        :param int location_id: The location id
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqDfsRecurenceChannelStatsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'anomaly_id',
            'location_id'
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
                    " to method get_dfs_recurrence_channel_stats" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'anomaly_id' is set
        if self.api_client.client_side_validation and ('anomaly_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['anomaly_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `anomaly_id` when calling `get_dfs_recurrence_channel_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'anomaly_id' in local_var_params and local_var_params['anomaly_id'] is not None:  # noqa: E501
            query_params.append(('anomalyId', local_var_params['anomaly_id']))  # noqa: E501
        if 'location_id' in local_var_params and local_var_params['location_id'] is not None:  # noqa: E501
            query_params.append(('locationId', local_var_params['location_id']))  # noqa: E501

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
            '/copilot/anomalies/dfs-recurrence/channel-stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqDfsRecurenceChannelStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_recurrence_count_stats(self, anomaly_id, **kwargs):  # noqa: E501
        """get_dfs_recurrence_count_stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dfs_recurrence_count_stats(anomaly_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str anomaly_id: The anomaly id (required)
        :param int location_id: The location id
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqDfsRecurenceCountStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dfs_recurrence_count_stats_with_http_info(anomaly_id, **kwargs)  # noqa: E501

    def get_dfs_recurrence_count_stats_with_http_info(self, anomaly_id, **kwargs):  # noqa: E501
        """get_dfs_recurrence_count_stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dfs_recurrence_count_stats_with_http_info(anomaly_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str anomaly_id: The anomaly id (required)
        :param int location_id: The location id
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqDfsRecurenceCountStatsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'anomaly_id',
            'location_id'
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
                    " to method get_dfs_recurrence_count_stats" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'anomaly_id' is set
        if self.api_client.client_side_validation and ('anomaly_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['anomaly_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `anomaly_id` when calling `get_dfs_recurrence_count_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'anomaly_id' in local_var_params and local_var_params['anomaly_id'] is not None:  # noqa: E501
            query_params.append(('anomalyId', local_var_params['anomaly_id']))  # noqa: E501
        if 'location_id' in local_var_params and local_var_params['location_id'] is not None:  # noqa: E501
            query_params.append(('locationId', local_var_params['location_id']))  # noqa: E501

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
            '/copilot/anomalies/dfs-recurrence/count-stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqDfsRecurenceCountStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_poe_flapping_stats(self, anomaly_id, **kwargs):  # noqa: E501
        """get_poe_flapping_stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_poe_flapping_stats(anomaly_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str anomaly_id: The anomaly id (required)
        :param int location_id: The location id
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqPoeFlappingStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_poe_flapping_stats_with_http_info(anomaly_id, **kwargs)  # noqa: E501

    def get_poe_flapping_stats_with_http_info(self, anomaly_id, **kwargs):  # noqa: E501
        """get_poe_flapping_stats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_poe_flapping_stats_with_http_info(anomaly_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str anomaly_id: The anomaly id (required)
        :param int location_id: The location id
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqPoeFlappingStatsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'anomaly_id',
            'location_id'
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
                    " to method get_poe_flapping_stats" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'anomaly_id' is set
        if self.api_client.client_side_validation and ('anomaly_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['anomaly_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `anomaly_id` when calling `get_poe_flapping_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'anomaly_id' in local_var_params and local_var_params['anomaly_id'] is not None:  # noqa: E501
            query_params.append(('anomalyId', local_var_params['anomaly_id']))  # noqa: E501
        if 'location_id' in local_var_params and local_var_params['location_id'] is not None:  # noqa: E501
            query_params.append(('locationId', local_var_params['location_id']))  # noqa: E501

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
            '/copilot/anomalies/poeflapping/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqPoeFlappingStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_anomaly_locations(self, **kwargs):  # noqa: E501
        """list_anomaly_locations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_anomaly_locations(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param XiqAnomalyType anomaly_type: Anomaly type
        :param int page: Page number, min = 1
        :param int limit: Number of Records, min = 1, max = 100
        :param XiqAnomalySortField sort_field: sort by field
        :param XiqSortOrder sort_order: The sorting order
        :param bool exclude_muted: exclude muted
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqCopilotPagedXiqAnomalyLocationEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_anomaly_locations_with_http_info(**kwargs)  # noqa: E501

    def list_anomaly_locations_with_http_info(self, **kwargs):  # noqa: E501
        """list_anomaly_locations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_anomaly_locations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param XiqAnomalyType anomaly_type: Anomaly type
        :param int page: Page number, min = 1
        :param int limit: Number of Records, min = 1, max = 100
        :param XiqAnomalySortField sort_field: sort by field
        :param XiqSortOrder sort_order: The sorting order
        :param bool exclude_muted: exclude muted
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqCopilotPagedXiqAnomalyLocationEntity, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'anomaly_type',
            'page',
            'limit',
            'sort_field',
            'sort_order',
            'exclude_muted'
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
                    " to method list_anomaly_locations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_anomaly_locations`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_anomaly_locations`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_anomaly_locations`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'anomaly_type' in local_var_params and local_var_params['anomaly_type'] is not None:  # noqa: E501
            query_params.append(('anomalyType', local_var_params['anomaly_type']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'sort_field' in local_var_params and local_var_params['sort_field'] is not None:  # noqa: E501
            query_params.append(('sortField', local_var_params['sort_field']))  # noqa: E501
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501
        if 'exclude_muted' in local_var_params and local_var_params['exclude_muted'] is not None:  # noqa: E501
            query_params.append(('excludeMuted', local_var_params['exclude_muted']))  # noqa: E501

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
            '/copilot/anomalies/locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqCopilotPagedXiqAnomalyLocationEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
