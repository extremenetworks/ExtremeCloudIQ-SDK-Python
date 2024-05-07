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


class XiqAnomalyAffectedCount(object):
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
        'total_anomaly_count': 'int',
        'affected_location_count': 'int',
        'affected_devices_count': 'int'
    }

    attribute_map = {
        'total_anomaly_count': 'total_anomaly_count',
        'affected_location_count': 'affected_location_count',
        'affected_devices_count': 'affected_devices_count'
    }

    def __init__(self, total_anomaly_count=None, affected_location_count=None, affected_devices_count=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomalyAffectedCount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_anomaly_count = None
        self._affected_location_count = None
        self._affected_devices_count = None
        self.discriminator = None

        self.total_anomaly_count = total_anomaly_count
        self.affected_location_count = affected_location_count
        self.affected_devices_count = affected_devices_count

    @property
    def total_anomaly_count(self):
        """Gets the total_anomaly_count of this XiqAnomalyAffectedCount.  # noqa: E501

        The total anomaly count  # noqa: E501

        :return: The total_anomaly_count of this XiqAnomalyAffectedCount.  # noqa: E501
        :rtype: int
        """
        return self._total_anomaly_count

    @total_anomaly_count.setter
    def total_anomaly_count(self, total_anomaly_count):
        """Sets the total_anomaly_count of this XiqAnomalyAffectedCount.

        The total anomaly count  # noqa: E501

        :param total_anomaly_count: The total_anomaly_count of this XiqAnomalyAffectedCount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_anomaly_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_anomaly_count`, must not be `None`")  # noqa: E501

        self._total_anomaly_count = total_anomaly_count

    @property
    def affected_location_count(self):
        """Gets the affected_location_count of this XiqAnomalyAffectedCount.  # noqa: E501

        The affected location count  # noqa: E501

        :return: The affected_location_count of this XiqAnomalyAffectedCount.  # noqa: E501
        :rtype: int
        """
        return self._affected_location_count

    @affected_location_count.setter
    def affected_location_count(self, affected_location_count):
        """Sets the affected_location_count of this XiqAnomalyAffectedCount.

        The affected location count  # noqa: E501

        :param affected_location_count: The affected_location_count of this XiqAnomalyAffectedCount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and affected_location_count is None:  # noqa: E501
            raise ValueError("Invalid value for `affected_location_count`, must not be `None`")  # noqa: E501

        self._affected_location_count = affected_location_count

    @property
    def affected_devices_count(self):
        """Gets the affected_devices_count of this XiqAnomalyAffectedCount.  # noqa: E501

        The affected devices count  # noqa: E501

        :return: The affected_devices_count of this XiqAnomalyAffectedCount.  # noqa: E501
        :rtype: int
        """
        return self._affected_devices_count

    @affected_devices_count.setter
    def affected_devices_count(self, affected_devices_count):
        """Sets the affected_devices_count of this XiqAnomalyAffectedCount.

        The affected devices count  # noqa: E501

        :param affected_devices_count: The affected_devices_count of this XiqAnomalyAffectedCount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and affected_devices_count is None:  # noqa: E501
            raise ValueError("Invalid value for `affected_devices_count`, must not be `None`")  # noqa: E501

        self._affected_devices_count = affected_devices_count

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
        if not isinstance(other, XiqAnomalyAffectedCount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomalyAffectedCount):
            return True

        return self.to_dict() != other.to_dict()
