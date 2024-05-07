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


class XiqDigitalTwinDevices(object):
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
        'dts': 'list[XiqDigitalTwinDevice]'
    }

    attribute_map = {
        'dts': 'dts'
    }

    def __init__(self, dts=None, local_vars_configuration=None):  # noqa: E501
        """XiqDigitalTwinDevices - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dts = None
        self.discriminator = None

        if dts is not None:
            self.dts = dts

    @property
    def dts(self):
        """Gets the dts of this XiqDigitalTwinDevices.  # noqa: E501

        The Digital Twin devices to onboard.  # noqa: E501

        :return: The dts of this XiqDigitalTwinDevices.  # noqa: E501
        :rtype: list[XiqDigitalTwinDevice]
        """
        return self._dts

    @dts.setter
    def dts(self, dts):
        """Sets the dts of this XiqDigitalTwinDevices.

        The Digital Twin devices to onboard.  # noqa: E501

        :param dts: The dts of this XiqDigitalTwinDevices.  # noqa: E501
        :type: list[XiqDigitalTwinDevice]
        """

        self._dts = dts

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
        if not isinstance(other, XiqDigitalTwinDevices):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDigitalTwinDevices):
            return True

        return self.to_dict() != other.to_dict()
