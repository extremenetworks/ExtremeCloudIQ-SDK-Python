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


class XiqAnomalyDevicesByLocationResponse(object):
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
        'location_entity': 'XiqAnomalyLocationEntity',
        'devices': 'list[XiqAnomalyDeviceEntity]'
    }

    attribute_map = {
        'location_entity': 'location_entity',
        'devices': 'devices'
    }

    def __init__(self, location_entity=None, devices=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomalyDevicesByLocationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location_entity = None
        self._devices = None
        self.discriminator = None

        if location_entity is not None:
            self.location_entity = location_entity
        if devices is not None:
            self.devices = devices

    @property
    def location_entity(self):
        """Gets the location_entity of this XiqAnomalyDevicesByLocationResponse.  # noqa: E501


        :return: The location_entity of this XiqAnomalyDevicesByLocationResponse.  # noqa: E501
        :rtype: XiqAnomalyLocationEntity
        """
        return self._location_entity

    @location_entity.setter
    def location_entity(self, location_entity):
        """Sets the location_entity of this XiqAnomalyDevicesByLocationResponse.


        :param location_entity: The location_entity of this XiqAnomalyDevicesByLocationResponse.  # noqa: E501
        :type: XiqAnomalyLocationEntity
        """

        self._location_entity = location_entity

    @property
    def devices(self):
        """Gets the devices of this XiqAnomalyDevicesByLocationResponse.  # noqa: E501

        the anomaly devices data  # noqa: E501

        :return: The devices of this XiqAnomalyDevicesByLocationResponse.  # noqa: E501
        :rtype: list[XiqAnomalyDeviceEntity]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this XiqAnomalyDevicesByLocationResponse.

        the anomaly devices data  # noqa: E501

        :param devices: The devices of this XiqAnomalyDevicesByLocationResponse.  # noqa: E501
        :type: list[XiqAnomalyDeviceEntity]
        """

        self._devices = devices

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
        if not isinstance(other, XiqAnomalyDevicesByLocationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomalyDevicesByLocationResponse):
            return True

        return self.to_dict() != other.to_dict()
