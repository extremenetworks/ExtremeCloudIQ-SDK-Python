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


class XiqThreadStopCommissionerRequest(object):
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
        'interface_name': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'interface_name': 'interface_name'
    }

    def __init__(self, device_id=None, interface_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadStopCommissionerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._interface_name = None
        self.discriminator = None

        self.device_id = device_id
        if interface_name is not None:
            self.interface_name = interface_name

    @property
    def device_id(self):
        """Gets the device_id of this XiqThreadStopCommissionerRequest.  # noqa: E501

        The device id  # noqa: E501

        :return: The device_id of this XiqThreadStopCommissionerRequest.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqThreadStopCommissionerRequest.

        The device id  # noqa: E501

        :param device_id: The device_id of this XiqThreadStopCommissionerRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqThreadStopCommissionerRequest.  # noqa: E501

        The IoT interface on which to stop the Commissioner.  # noqa: E501

        :return: The interface_name of this XiqThreadStopCommissionerRequest.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqThreadStopCommissionerRequest.

        The IoT interface on which to stop the Commissioner.  # noqa: E501

        :param interface_name: The interface_name of this XiqThreadStopCommissionerRequest.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

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
        if not isinstance(other, XiqThreadStopCommissionerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadStopCommissionerRequest):
            return True

        return self.to_dict() != other.to_dict()
