# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAssignDevicesLocationRequest(object):
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
        'devices': 'XiqDeviceFilter',
        'device_location': 'XiqDeviceLocationAssignment'
    }

    attribute_map = {
        'devices': 'devices',
        'device_location': 'device_location'
    }

    def __init__(self, devices=None, device_location=None, local_vars_configuration=None):  # noqa: E501
        """XiqAssignDevicesLocationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._devices = None
        self._device_location = None
        self.discriminator = None

        self.devices = devices
        self.device_location = device_location

    @property
    def devices(self):
        """Gets the devices of this XiqAssignDevicesLocationRequest.  # noqa: E501


        :return: The devices of this XiqAssignDevicesLocationRequest.  # noqa: E501
        :rtype: XiqDeviceFilter
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this XiqAssignDevicesLocationRequest.


        :param devices: The devices of this XiqAssignDevicesLocationRequest.  # noqa: E501
        :type: XiqDeviceFilter
        """
        if self.local_vars_configuration.client_side_validation and devices is None:  # noqa: E501
            raise ValueError("Invalid value for `devices`, must not be `None`")  # noqa: E501

        self._devices = devices

    @property
    def device_location(self):
        """Gets the device_location of this XiqAssignDevicesLocationRequest.  # noqa: E501


        :return: The device_location of this XiqAssignDevicesLocationRequest.  # noqa: E501
        :rtype: XiqDeviceLocationAssignment
        """
        return self._device_location

    @device_location.setter
    def device_location(self, device_location):
        """Sets the device_location of this XiqAssignDevicesLocationRequest.


        :param device_location: The device_location of this XiqAssignDevicesLocationRequest.  # noqa: E501
        :type: XiqDeviceLocationAssignment
        """
        if self.local_vars_configuration.client_side_validation and device_location is None:  # noqa: E501
            raise ValueError("Invalid value for `device_location`, must not be `None`")  # noqa: E501

        self._device_location = device_location

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
        if not isinstance(other, XiqAssignDevicesLocationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAssignDevicesLocationRequest):
            return True

        return self.to_dict() != other.to_dict()
