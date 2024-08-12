# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqIotProfileRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'app_id': 'XiqIotApplicationId',
        'thread_gateway': 'XiqIotProfileThreadGateway',
        'app_supported': 'XiqIotApplicationSupported',
        'ble_beacon': 'XiqIotpMaBleBeacon',
        'ble_scan': 'XiqIotpMaBleScan'
    }

    attribute_map = {
        'name': 'name',
        'app_id': 'app_id',
        'thread_gateway': 'thread_gateway',
        'app_supported': 'app_supported',
        'ble_beacon': 'ble_beacon',
        'ble_scan': 'ble_scan'
    }

    def __init__(self, name=None, app_id=None, thread_gateway=None, app_supported=None, ble_beacon=None, ble_scan=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._app_id = None
        self._thread_gateway = None
        self._app_supported = None
        self._ble_beacon = None
        self._ble_scan = None
        self.discriminator = None

        self.name = name
        self.app_id = app_id
        if thread_gateway is not None:
            self.thread_gateway = thread_gateway
        self.app_supported = app_supported
        if ble_beacon is not None:
            self.ble_beacon = ble_beacon
        if ble_scan is not None:
            self.ble_scan = ble_scan

    @property
    def name(self):
        """Gets the name of this XiqIotProfileRequest.  # noqa: E501

        The IoT profile name  # noqa: E501

        :return: The name of this XiqIotProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqIotProfileRequest.

        The IoT profile name  # noqa: E501

        :param name: The name of this XiqIotProfileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this XiqIotProfileRequest.  # noqa: E501


        :return: The app_id of this XiqIotProfileRequest.  # noqa: E501
        :rtype: XiqIotApplicationId
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this XiqIotProfileRequest.


        :param app_id: The app_id of this XiqIotProfileRequest.  # noqa: E501
        :type: XiqIotApplicationId
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def thread_gateway(self):
        """Gets the thread_gateway of this XiqIotProfileRequest.  # noqa: E501


        :return: The thread_gateway of this XiqIotProfileRequest.  # noqa: E501
        :rtype: XiqIotProfileThreadGateway
        """
        return self._thread_gateway

    @thread_gateway.setter
    def thread_gateway(self, thread_gateway):
        """Sets the thread_gateway of this XiqIotProfileRequest.


        :param thread_gateway: The thread_gateway of this XiqIotProfileRequest.  # noqa: E501
        :type: XiqIotProfileThreadGateway
        """

        self._thread_gateway = thread_gateway

    @property
    def app_supported(self):
        """Gets the app_supported of this XiqIotProfileRequest.  # noqa: E501


        :return: The app_supported of this XiqIotProfileRequest.  # noqa: E501
        :rtype: XiqIotApplicationSupported
        """
        return self._app_supported

    @app_supported.setter
    def app_supported(self, app_supported):
        """Sets the app_supported of this XiqIotProfileRequest.


        :param app_supported: The app_supported of this XiqIotProfileRequest.  # noqa: E501
        :type: XiqIotApplicationSupported
        """
        if self.local_vars_configuration.client_side_validation and app_supported is None:  # noqa: E501
            raise ValueError("Invalid value for `app_supported`, must not be `None`")  # noqa: E501

        self._app_supported = app_supported

    @property
    def ble_beacon(self):
        """Gets the ble_beacon of this XiqIotProfileRequest.  # noqa: E501


        :return: The ble_beacon of this XiqIotProfileRequest.  # noqa: E501
        :rtype: XiqIotpMaBleBeacon
        """
        return self._ble_beacon

    @ble_beacon.setter
    def ble_beacon(self, ble_beacon):
        """Sets the ble_beacon of this XiqIotProfileRequest.


        :param ble_beacon: The ble_beacon of this XiqIotProfileRequest.  # noqa: E501
        :type: XiqIotpMaBleBeacon
        """

        self._ble_beacon = ble_beacon

    @property
    def ble_scan(self):
        """Gets the ble_scan of this XiqIotProfileRequest.  # noqa: E501


        :return: The ble_scan of this XiqIotProfileRequest.  # noqa: E501
        :rtype: XiqIotpMaBleScan
        """
        return self._ble_scan

    @ble_scan.setter
    def ble_scan(self, ble_scan):
        """Sets the ble_scan of this XiqIotProfileRequest.


        :param ble_scan: The ble_scan of this XiqIotProfileRequest.  # noqa: E501
        :type: XiqIotpMaBleScan
        """

        self._ble_scan = ble_scan

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, XiqIotProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
