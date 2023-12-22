# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
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


class EssentialsExtremeLocationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_client_last_location(self, client_mac, floor_id, parent_id, **kwargs):  # noqa: E501
        """Get the last known location of the client  # noqa: E501

        Get the last known location of the client on the floor plan.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_last_location(client_mac, floor_id, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str client_mac: The mac address of client (required)
        :param int floor_id: Location Id of the floor (required)
        :param int parent_id: Location Id of the floor's parent (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EssentialsElocLastKnownLocation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_client_last_location_with_http_info(client_mac, floor_id, parent_id, **kwargs)  # noqa: E501

    def get_client_last_location_with_http_info(self, client_mac, floor_id, parent_id, **kwargs):  # noqa: E501
        """Get the last known location of the client  # noqa: E501

        Get the last known location of the client on the floor plan.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_last_location_with_http_info(client_mac, floor_id, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str client_mac: The mac address of client (required)
        :param int floor_id: Location Id of the floor (required)
        :param int parent_id: Location Id of the floor's parent (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EssentialsElocLastKnownLocation, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'client_mac',
            'floor_id',
            'parent_id'
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
                    " to method get_client_last_location" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'client_mac' is set
        if self.api_client.client_side_validation and ('client_mac' not in local_var_params or  # noqa: E501
                                                        local_var_params['client_mac'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `client_mac` when calling `get_client_last_location`")  # noqa: E501
        # verify the required parameter 'floor_id' is set
        if self.api_client.client_side_validation and ('floor_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['floor_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `floor_id` when calling `get_client_last_location`")  # noqa: E501
        # verify the required parameter 'parent_id' is set
        if self.api_client.client_side_validation and ('parent_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['parent_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `parent_id` when calling `get_client_last_location`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_mac' in local_var_params:
            path_params['clientMac'] = local_var_params['client_mac']  # noqa: E501

        query_params = []
        if 'floor_id' in local_var_params and local_var_params['floor_id'] is not None:  # noqa: E501
            query_params.append(('floorId', local_var_params['floor_id']))  # noqa: E501
        if 'parent_id' in local_var_params and local_var_params['parent_id'] is not None:  # noqa: E501
            query_params.append(('parentId', local_var_params['parent_id']))  # noqa: E501

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
            '/essentials/eloc/clients/{clientMac}/last-known-location', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EssentialsElocLastKnownLocation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
