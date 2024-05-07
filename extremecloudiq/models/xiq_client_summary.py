# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqClientSummary(object):
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
        'connected_wireless_client_count': 'int',
        'detected_wired_client_count': 'int',
        'connected_thread_client_count': 'int'
    }

    attribute_map = {
        'connected_wireless_client_count': 'connected_wireless_client_count',
        'detected_wired_client_count': 'detected_wired_client_count',
        'connected_thread_client_count': 'connected_thread_client_count'
    }

    def __init__(self, connected_wireless_client_count=None, detected_wired_client_count=None, connected_thread_client_count=None, local_vars_configuration=None):  # noqa: E501
        """XiqClientSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connected_wireless_client_count = None
        self._detected_wired_client_count = None
        self._connected_thread_client_count = None
        self.discriminator = None

        if connected_wireless_client_count is not None:
            self.connected_wireless_client_count = connected_wireless_client_count
        if detected_wired_client_count is not None:
            self.detected_wired_client_count = detected_wired_client_count
        if connected_thread_client_count is not None:
            self.connected_thread_client_count = connected_thread_client_count

    @property
    def connected_wireless_client_count(self):
        """Gets the connected_wireless_client_count of this XiqClientSummary.  # noqa: E501

        The connected wireless client count  # noqa: E501

        :return: The connected_wireless_client_count of this XiqClientSummary.  # noqa: E501
        :rtype: int
        """
        return self._connected_wireless_client_count

    @connected_wireless_client_count.setter
    def connected_wireless_client_count(self, connected_wireless_client_count):
        """Sets the connected_wireless_client_count of this XiqClientSummary.

        The connected wireless client count  # noqa: E501

        :param connected_wireless_client_count: The connected_wireless_client_count of this XiqClientSummary.  # noqa: E501
        :type: int
        """

        self._connected_wireless_client_count = connected_wireless_client_count

    @property
    def detected_wired_client_count(self):
        """Gets the detected_wired_client_count of this XiqClientSummary.  # noqa: E501

        The detected wired client count  # noqa: E501

        :return: The detected_wired_client_count of this XiqClientSummary.  # noqa: E501
        :rtype: int
        """
        return self._detected_wired_client_count

    @detected_wired_client_count.setter
    def detected_wired_client_count(self, detected_wired_client_count):
        """Sets the detected_wired_client_count of this XiqClientSummary.

        The detected wired client count  # noqa: E501

        :param detected_wired_client_count: The detected_wired_client_count of this XiqClientSummary.  # noqa: E501
        :type: int
        """

        self._detected_wired_client_count = detected_wired_client_count

    @property
    def connected_thread_client_count(self):
        """Gets the connected_thread_client_count of this XiqClientSummary.  # noqa: E501

        The connected thread client count  # noqa: E501

        :return: The connected_thread_client_count of this XiqClientSummary.  # noqa: E501
        :rtype: int
        """
        return self._connected_thread_client_count

    @connected_thread_client_count.setter
    def connected_thread_client_count(self, connected_thread_client_count):
        """Sets the connected_thread_client_count of this XiqClientSummary.

        The connected thread client count  # noqa: E501

        :param connected_thread_client_count: The connected_thread_client_count of this XiqClientSummary.  # noqa: E501
        :type: int
        """

        self._connected_thread_client_count = connected_thread_client_count

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
        if not isinstance(other, XiqClientSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClientSummary):
            return True

        return self.to_dict() != other.to_dict()
