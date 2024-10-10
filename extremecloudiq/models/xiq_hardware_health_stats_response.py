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


class XiqHardwareHealthStatsResponse(object):
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
        'hd_device_stats_entities': 'list[XiqHardwareHealthDeviceStatsEntity]',
        'hd_packet_counts_entities': 'list[XiqHardwareHealthPacketCountsEntity]',
        'hd_reboot_stats_entities': 'list[XiqHardwareHealthRebootStatsEntity]'
    }

    attribute_map = {
        'hd_device_stats_entities': 'hd_device_stats_entities',
        'hd_packet_counts_entities': 'hd_packet_counts_entities',
        'hd_reboot_stats_entities': 'hd_reboot_stats_entities'
    }

    def __init__(self, hd_device_stats_entities=None, hd_packet_counts_entities=None, hd_reboot_stats_entities=None, local_vars_configuration=None):  # noqa: E501
        """XiqHardwareHealthStatsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hd_device_stats_entities = None
        self._hd_packet_counts_entities = None
        self._hd_reboot_stats_entities = None
        self.discriminator = None

        if hd_device_stats_entities is not None:
            self.hd_device_stats_entities = hd_device_stats_entities
        if hd_packet_counts_entities is not None:
            self.hd_packet_counts_entities = hd_packet_counts_entities
        if hd_reboot_stats_entities is not None:
            self.hd_reboot_stats_entities = hd_reboot_stats_entities

    @property
    def hd_device_stats_entities(self):
        """Gets the hd_device_stats_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501

        the anomaly devices data  # noqa: E501

        :return: The hd_device_stats_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501
        :rtype: list[XiqHardwareHealthDeviceStatsEntity]
        """
        return self._hd_device_stats_entities

    @hd_device_stats_entities.setter
    def hd_device_stats_entities(self, hd_device_stats_entities):
        """Sets the hd_device_stats_entities of this XiqHardwareHealthStatsResponse.

        the anomaly devices data  # noqa: E501

        :param hd_device_stats_entities: The hd_device_stats_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501
        :type: list[XiqHardwareHealthDeviceStatsEntity]
        """

        self._hd_device_stats_entities = hd_device_stats_entities

    @property
    def hd_packet_counts_entities(self):
        """Gets the hd_packet_counts_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501

        the anomaly devices data  # noqa: E501

        :return: The hd_packet_counts_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501
        :rtype: list[XiqHardwareHealthPacketCountsEntity]
        """
        return self._hd_packet_counts_entities

    @hd_packet_counts_entities.setter
    def hd_packet_counts_entities(self, hd_packet_counts_entities):
        """Sets the hd_packet_counts_entities of this XiqHardwareHealthStatsResponse.

        the anomaly devices data  # noqa: E501

        :param hd_packet_counts_entities: The hd_packet_counts_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501
        :type: list[XiqHardwareHealthPacketCountsEntity]
        """

        self._hd_packet_counts_entities = hd_packet_counts_entities

    @property
    def hd_reboot_stats_entities(self):
        """Gets the hd_reboot_stats_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501

        the anomaly devices data  # noqa: E501

        :return: The hd_reboot_stats_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501
        :rtype: list[XiqHardwareHealthRebootStatsEntity]
        """
        return self._hd_reboot_stats_entities

    @hd_reboot_stats_entities.setter
    def hd_reboot_stats_entities(self, hd_reboot_stats_entities):
        """Sets the hd_reboot_stats_entities of this XiqHardwareHealthStatsResponse.

        the anomaly devices data  # noqa: E501

        :param hd_reboot_stats_entities: The hd_reboot_stats_entities of this XiqHardwareHealthStatsResponse.  # noqa: E501
        :type: list[XiqHardwareHealthRebootStatsEntity]
        """

        self._hd_reboot_stats_entities = hd_reboot_stats_entities

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
        if not isinstance(other, XiqHardwareHealthStatsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqHardwareHealthStatsResponse):
            return True

        return self.to_dict() != other.to_dict()