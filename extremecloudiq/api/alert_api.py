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


class AlertApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def count_alerts_by_group(self, group, start_time, end_time, **kwargs):  # noqa: E501
        """Count the alerts by different grouping  # noqa: E501

        Count the number of alerts and events based on Severity, Category, and Alert Type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_alerts_by_group(group, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param XiqAlertGroupQuery group: The group to count from (required)
        :param int start_time: The start time for counting the alerts (required)
        :param int end_time: The end time for counting the alerts (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.count_alerts_by_group_with_http_info(group, start_time, end_time, **kwargs)  # noqa: E501

    def count_alerts_by_group_with_http_info(self, group, start_time, end_time, **kwargs):  # noqa: E501
        """Count the alerts by different grouping  # noqa: E501

        Count the number of alerts and events based on Severity, Category, and Alert Type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_alerts_by_group_with_http_info(group, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param XiqAlertGroupQuery group: The group to count from (required)
        :param int start_time: The start time for counting the alerts (required)
        :param int end_time: The end time for counting the alerts (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(dict(str, int), status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'group',
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
                    " to method count_alerts_by_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group' is set
        if self.api_client.client_side_validation and ('group' not in local_var_params or  # noqa: E501
                                                        local_var_params['group'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group` when calling `count_alerts_by_group`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_time` when calling `count_alerts_by_group`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_time` when calling `count_alerts_by_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']  # noqa: E501

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
            '/alerts/count-by-{group}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_alerts(self, start_time, end_time, **kwargs):  # noqa: E501
        """List the alerts  # noqa: E501

        List a page of alerts by filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_alerts(start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int start_time: The start time for querying alerts in milliseconds (required)
        :param int end_time: The end time for querying alerts in milliseconds (required)
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param XiqAlertSeverity severity: The alert severity to filter
        :param XiqAlertCategory category: The alert category to filter
        :param str alert_type: The alert type to filter
        :param str keyword: The keyword to filter, such as device SN or MAC address
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedXiqAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_alerts_with_http_info(start_time, end_time, **kwargs)  # noqa: E501

    def list_alerts_with_http_info(self, start_time, end_time, **kwargs):  # noqa: E501
        """List the alerts  # noqa: E501

        List a page of alerts by filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_alerts_with_http_info(start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int start_time: The start time for querying alerts in milliseconds (required)
        :param int end_time: The end time for querying alerts in milliseconds (required)
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param XiqAlertSeverity severity: The alert severity to filter
        :param XiqAlertCategory category: The alert category to filter
        :param str alert_type: The alert type to filter
        :param str keyword: The keyword to filter, such as device SN or MAC address
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedXiqAlert, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'start_time',
            'end_time',
            'page',
            'limit',
            'severity',
            'category',
            'alert_type',
            'keyword'
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
                    " to method list_alerts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_time` when calling `list_alerts`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_time'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_time` when calling `list_alerts`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_alerts`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_alerts`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_alerts`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'start_time' in local_var_params and local_var_params['start_time'] is not None:  # noqa: E501
            query_params.append(('startTime', local_var_params['start_time']))  # noqa: E501
        if 'end_time' in local_var_params and local_var_params['end_time'] is not None:  # noqa: E501
            query_params.append(('endTime', local_var_params['end_time']))  # noqa: E501
        if 'severity' in local_var_params and local_var_params['severity'] is not None:  # noqa: E501
            query_params.append(('severity', local_var_params['severity']))  # noqa: E501
        if 'category' in local_var_params and local_var_params['category'] is not None:  # noqa: E501
            query_params.append(('category', local_var_params['category']))  # noqa: E501
        if 'alert_type' in local_var_params and local_var_params['alert_type'] is not None:  # noqa: E501
            query_params.append(('alertType', local_var_params['alert_type']))  # noqa: E501
        if 'keyword' in local_var_params and local_var_params['keyword'] is not None:  # noqa: E501
            query_params.append(('keyword', local_var_params['keyword']))  # noqa: E501

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
            '/alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedXiqAlert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
