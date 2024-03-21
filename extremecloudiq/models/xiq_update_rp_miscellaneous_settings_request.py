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


class XiqUpdateRpMiscellaneousSettingsRequest(object):
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
        'sla_throughput_level': 'str',
        'radio_range': 'int'
    }

    attribute_map = {
        'sla_throughput_level': 'sla_throughput_level',
        'radio_range': 'radio_range'
    }

    def __init__(self, sla_throughput_level=None, radio_range=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateRpMiscellaneousSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sla_throughput_level = None
        self._radio_range = None
        self.discriminator = None

        if sla_throughput_level is not None:
            self.sla_throughput_level = sla_throughput_level
        if radio_range is not None:
            self.radio_range = radio_range

    @property
    def sla_throughput_level(self):
        """Gets the sla_throughput_level of this XiqUpdateRpMiscellaneousSettingsRequest.  # noqa: E501

        The Client SLA options -- \"NORMAL_DENSITY\", \"HIGH_DENSITY\" (performance-oriented), or \"LOW_DENSITY\" (coverage-oriented)  # noqa: E501

        :return: The sla_throughput_level of this XiqUpdateRpMiscellaneousSettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sla_throughput_level

    @sla_throughput_level.setter
    def sla_throughput_level(self, sla_throughput_level):
        """Sets the sla_throughput_level of this XiqUpdateRpMiscellaneousSettingsRequest.

        The Client SLA options -- \"NORMAL_DENSITY\", \"HIGH_DENSITY\" (performance-oriented), or \"LOW_DENSITY\" (coverage-oriented)  # noqa: E501

        :param sla_throughput_level: The sla_throughput_level of this XiqUpdateRpMiscellaneousSettingsRequest.  # noqa: E501
        :type: str
        """

        self._sla_throughput_level = sla_throughput_level

    @property
    def radio_range(self):
        """Gets the radio_range of this XiqUpdateRpMiscellaneousSettingsRequest.  # noqa: E501

        The Outdoor Deployment for signal distance from 300 to 10000 meters  # noqa: E501

        :return: The radio_range of this XiqUpdateRpMiscellaneousSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._radio_range

    @radio_range.setter
    def radio_range(self, radio_range):
        """Sets the radio_range of this XiqUpdateRpMiscellaneousSettingsRequest.

        The Outdoor Deployment for signal distance from 300 to 10000 meters  # noqa: E501

        :param radio_range: The radio_range of this XiqUpdateRpMiscellaneousSettingsRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                radio_range is not None and radio_range > 10000):  # noqa: E501
            raise ValueError("Invalid value for `radio_range`, must be a value less than or equal to `10000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                radio_range is not None and radio_range < 300):  # noqa: E501
            raise ValueError("Invalid value for `radio_range`, must be a value greater than or equal to `300`")  # noqa: E501

        self._radio_range = radio_range

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
        if not isinstance(other, XiqUpdateRpMiscellaneousSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateRpMiscellaneousSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
