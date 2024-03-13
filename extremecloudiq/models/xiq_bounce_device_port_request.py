# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqBounceDevicePortRequest(object):
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
        'device_id': 'int',
        'port_number': 'str',
        'bounce_port_reason': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'port_number': 'port_number',
        'bounce_port_reason': 'bounce_port_reason'
    }

    def __init__(self, device_id=None, port_number=None, bounce_port_reason=None, local_vars_configuration=None):  # noqa: E501
        """XiqBounceDevicePortRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._port_number = None
        self._bounce_port_reason = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if port_number is not None:
            self.port_number = port_number
        if bounce_port_reason is not None:
            self.bounce_port_reason = bounce_port_reason

    @property
    def device_id(self):
        """Gets the device_id of this XiqBounceDevicePortRequest.  # noqa: E501

        The device id  # noqa: E501

        :return: The device_id of this XiqBounceDevicePortRequest.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqBounceDevicePortRequest.

        The device id  # noqa: E501

        :param device_id: The device_id of this XiqBounceDevicePortRequest.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def port_number(self):
        """Gets the port_number of this XiqBounceDevicePortRequest.  # noqa: E501

        The port number of the device (eg. 1,2, ..)  # noqa: E501

        :return: The port_number of this XiqBounceDevicePortRequest.  # noqa: E501
        :rtype: str
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this XiqBounceDevicePortRequest.

        The port number of the device (eg. 1,2, ..)  # noqa: E501

        :param port_number: The port_number of this XiqBounceDevicePortRequest.  # noqa: E501
        :type: str
        """

        self._port_number = port_number

    @property
    def bounce_port_reason(self):
        """Gets the bounce_port_reason of this XiqBounceDevicePortRequest.  # noqa: E501

        The reason to bounce the port of the device (eg. reset the inline power on the port so that the connected AP can be restarted)  # noqa: E501

        :return: The bounce_port_reason of this XiqBounceDevicePortRequest.  # noqa: E501
        :rtype: str
        """
        return self._bounce_port_reason

    @bounce_port_reason.setter
    def bounce_port_reason(self, bounce_port_reason):
        """Sets the bounce_port_reason of this XiqBounceDevicePortRequest.

        The reason to bounce the port of the device (eg. reset the inline power on the port so that the connected AP can be restarted)  # noqa: E501

        :param bounce_port_reason: The bounce_port_reason of this XiqBounceDevicePortRequest.  # noqa: E501
        :type: str
        """

        self._bounce_port_reason = bounce_port_reason

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
        if not isinstance(other, XiqBounceDevicePortRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqBounceDevicePortRequest):
            return True

        return self.to_dict() != other.to_dict()
