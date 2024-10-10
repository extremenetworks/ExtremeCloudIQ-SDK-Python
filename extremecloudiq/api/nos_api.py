# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
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


class NOSApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_device(self, device_id, xiq_get_device_infoby_nos_request, **kwargs):  # noqa: E501
        """Get device info for a specific device  # noqa: E501

        Get device info for a specific device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device(device_id, xiq_get_device_infoby_nos_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int device_id: The device ID (required)
        :param XiqGetDeviceInfobyNosRequest xiq_get_device_infoby_nos_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqGetDeviceInfoByNos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_device_with_http_info(device_id, xiq_get_device_infoby_nos_request, **kwargs)  # noqa: E501

    def get_device_with_http_info(self, device_id, xiq_get_device_infoby_nos_request, **kwargs):  # noqa: E501
        """Get device info for a specific device  # noqa: E501

        Get device info for a specific device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_with_http_info(device_id, xiq_get_device_infoby_nos_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int device_id: The device ID (required)
        :param XiqGetDeviceInfobyNosRequest xiq_get_device_infoby_nos_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XiqGetDeviceInfoByNos, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'device_id',
            'xiq_get_device_infoby_nos_request'
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
                    " to method get_device" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'device_id' is set
        if self.api_client.client_side_validation and ('device_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['device_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `device_id` when calling `get_device`")  # noqa: E501
        # verify the required parameter 'xiq_get_device_infoby_nos_request' is set
        if self.api_client.client_side_validation and ('xiq_get_device_infoby_nos_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['xiq_get_device_infoby_nos_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `xiq_get_device_infoby_nos_request` when calling `get_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['deviceId'] = local_var_params['device_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'xiq_get_device_infoby_nos_request' in local_var_params:
            body_params = local_var_params['xiq_get_device_infoby_nos_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/nos/device/{deviceId}/nos-api', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XiqGetDeviceInfoByNos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)