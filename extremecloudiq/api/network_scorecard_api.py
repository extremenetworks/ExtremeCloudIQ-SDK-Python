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


class NetworkScorecardApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_client_health(self, location_id, **kwargs):  # noqa: E501
        """Get the overall client health score  # noqa: E501

        Get the clients health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_health(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ClientHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_client_health_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_client_health_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the overall client health score  # noqa: E501

        Get the clients health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_health_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ClientHealth, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id',
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
                    " to method get_client_health" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_client_health`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['locationId'] = local_var_params['location_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/network-scorecard/clientHealth/{locationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientHealth',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_health(self, location_id, **kwargs):  # noqa: E501
        """Get the overall device health score  # noqa: E501

        Get the devices health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_health(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeviceHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_device_health_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_device_health_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the overall device health score  # noqa: E501

        Get the devices health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_health_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeviceHealth, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id',
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
                    " to method get_device_health" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_device_health`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['locationId'] = local_var_params['location_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/network-scorecard/deviceHealth/{locationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceHealth',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_network_health(self, location_id, **kwargs):  # noqa: E501
        """Get the overall network health score  # noqa: E501

        Get the network health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_network_health(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NetworkHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_network_health_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_network_health_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the overall network health score  # noqa: E501

        Get the network health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_network_health_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NetworkHealth, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id',
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
                    " to method get_network_health" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_network_health`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['locationId'] = local_var_params['location_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/network-scorecard/networkHealth/{locationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NetworkHealth',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_services_health(self, location_id, **kwargs):  # noqa: E501
        """Get the overall services health score  # noqa: E501

        Get the  health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_services_health(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ServicesHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_services_health_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_services_health_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the overall services health score  # noqa: E501

        Get the  health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_services_health_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ServicesHealth, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id',
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
                    " to method get_services_health" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_services_health`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['locationId'] = local_var_params['location_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/network-scorecard/servicesHealth/{locationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServicesHealth',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wifi_health(self, location_id, **kwargs):  # noqa: E501
        """Get the overall wifi health score  # noqa: E501

        Get the wifi health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wifi_health(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WifiHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_wifi_health_with_http_info(location_id, **kwargs)  # noqa: E501

    def get_wifi_health_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """Get the overall wifi health score  # noqa: E501

        Get the wifi health score over the period  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wifi_health_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int location_id: The location folder ID (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WifiHealth, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'location_id',
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
                    " to method get_wifi_health" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['location_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `location_id` when calling `get_wifi_health`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_id' in local_var_params:
            path_params['locationId'] = local_var_params['location_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/network-scorecard/wifiHealth/{locationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WifiHealth',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
