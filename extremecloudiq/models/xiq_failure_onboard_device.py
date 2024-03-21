# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqFailureOnboardDevice(object):
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
        'serial_number': 'str',
        'error': 'XiqOnboardError'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'error': 'error'
    }

    def __init__(self, serial_number=None, error=None, local_vars_configuration=None):  # noqa: E501
        """XiqFailureOnboardDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._serial_number = None
        self._error = None
        self.discriminator = None

        self.serial_number = serial_number
        if error is not None:
            self.error = error

    @property
    def serial_number(self):
        """Gets the serial_number of this XiqFailureOnboardDevice.  # noqa: E501

        The serial number  # noqa: E501

        :return: The serial_number of this XiqFailureOnboardDevice.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XiqFailureOnboardDevice.

        The serial number  # noqa: E501

        :param serial_number: The serial_number of this XiqFailureOnboardDevice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial_number is None:  # noqa: E501
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def error(self):
        """Gets the error of this XiqFailureOnboardDevice.  # noqa: E501


        :return: The error of this XiqFailureOnboardDevice.  # noqa: E501
        :rtype: XiqOnboardError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this XiqFailureOnboardDevice.


        :param error: The error of this XiqFailureOnboardDevice.  # noqa: E501
        :type: XiqOnboardError
        """

        self._error = error

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
        if not isinstance(other, XiqFailureOnboardDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqFailureOnboardDevice):
            return True

        return self.to_dict() != other.to_dict()
