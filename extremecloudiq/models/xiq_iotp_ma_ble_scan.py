# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqIotpMaBleScan(object):
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
        'destination': 'XiqIotpMaBleScanDestination',
        'applications': 'list[XiqIotpMaBleScanApplication]'
    }

    attribute_map = {
        'destination': 'destination',
        'applications': 'applications'
    }

    def __init__(self, destination=None, applications=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotpMaBleScan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination = None
        self._applications = None
        self.discriminator = None

        if destination is not None:
            self.destination = destination
        if applications is not None:
            self.applications = applications

    @property
    def destination(self):
        """Gets the destination of this XiqIotpMaBleScan.  # noqa: E501


        :return: The destination of this XiqIotpMaBleScan.  # noqa: E501
        :rtype: XiqIotpMaBleScanDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this XiqIotpMaBleScan.


        :param destination: The destination of this XiqIotpMaBleScan.  # noqa: E501
        :type: XiqIotpMaBleScanDestination
        """

        self._destination = destination

    @property
    def applications(self):
        """Gets the applications of this XiqIotpMaBleScan.  # noqa: E501

        Collection of BLE Scan applications  # noqa: E501

        :return: The applications of this XiqIotpMaBleScan.  # noqa: E501
        :rtype: list[XiqIotpMaBleScanApplication]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this XiqIotpMaBleScan.

        Collection of BLE Scan applications  # noqa: E501

        :param applications: The applications of this XiqIotpMaBleScan.  # noqa: E501
        :type: list[XiqIotpMaBleScanApplication]
        """

        self._applications = applications

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
        if not isinstance(other, XiqIotpMaBleScan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotpMaBleScan):
            return True

        return self.to_dict() != other.to_dict()