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


class XiqSitesByWiredEntity(object):
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
        'low_quality_score_count': 'int',
        'medium_quality_score_count': 'int',
        'high_quality_score_count': 'int',
        'total_locations_count': 'int'
    }

    attribute_map = {
        'low_quality_score_count': 'low_quality_score_count',
        'medium_quality_score_count': 'medium_quality_score_count',
        'high_quality_score_count': 'high_quality_score_count',
        'total_locations_count': 'total_locations_count'
    }

    def __init__(self, low_quality_score_count=None, medium_quality_score_count=None, high_quality_score_count=None, total_locations_count=None, local_vars_configuration=None):  # noqa: E501
        """XiqSitesByWiredEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._low_quality_score_count = None
        self._medium_quality_score_count = None
        self._high_quality_score_count = None
        self._total_locations_count = None
        self.discriminator = None

        if low_quality_score_count is not None:
            self.low_quality_score_count = low_quality_score_count
        if medium_quality_score_count is not None:
            self.medium_quality_score_count = medium_quality_score_count
        if high_quality_score_count is not None:
            self.high_quality_score_count = high_quality_score_count
        if total_locations_count is not None:
            self.total_locations_count = total_locations_count

    @property
    def low_quality_score_count(self):
        """Gets the low_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501

        Locations count with low severity  # noqa: E501

        :return: The low_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501
        :rtype: int
        """
        return self._low_quality_score_count

    @low_quality_score_count.setter
    def low_quality_score_count(self, low_quality_score_count):
        """Sets the low_quality_score_count of this XiqSitesByWiredEntity.

        Locations count with low severity  # noqa: E501

        :param low_quality_score_count: The low_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501
        :type: int
        """

        self._low_quality_score_count = low_quality_score_count

    @property
    def medium_quality_score_count(self):
        """Gets the medium_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501

        Locations count with medium severity  # noqa: E501

        :return: The medium_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501
        :rtype: int
        """
        return self._medium_quality_score_count

    @medium_quality_score_count.setter
    def medium_quality_score_count(self, medium_quality_score_count):
        """Sets the medium_quality_score_count of this XiqSitesByWiredEntity.

        Locations count with medium severity  # noqa: E501

        :param medium_quality_score_count: The medium_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501
        :type: int
        """

        self._medium_quality_score_count = medium_quality_score_count

    @property
    def high_quality_score_count(self):
        """Gets the high_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501

        Locations count with high severity  # noqa: E501

        :return: The high_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501
        :rtype: int
        """
        return self._high_quality_score_count

    @high_quality_score_count.setter
    def high_quality_score_count(self, high_quality_score_count):
        """Sets the high_quality_score_count of this XiqSitesByWiredEntity.

        Locations count with high severity  # noqa: E501

        :param high_quality_score_count: The high_quality_score_count of this XiqSitesByWiredEntity.  # noqa: E501
        :type: int
        """

        self._high_quality_score_count = high_quality_score_count

    @property
    def total_locations_count(self):
        """Gets the total_locations_count of this XiqSitesByWiredEntity.  # noqa: E501

        Total Locations count by severity  # noqa: E501

        :return: The total_locations_count of this XiqSitesByWiredEntity.  # noqa: E501
        :rtype: int
        """
        return self._total_locations_count

    @total_locations_count.setter
    def total_locations_count(self, total_locations_count):
        """Sets the total_locations_count of this XiqSitesByWiredEntity.

        Total Locations count by severity  # noqa: E501

        :param total_locations_count: The total_locations_count of this XiqSitesByWiredEntity.  # noqa: E501
        :type: int
        """

        self._total_locations_count = total_locations_count

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
        if not isinstance(other, XiqSitesByWiredEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSitesByWiredEntity):
            return True

        return self.to_dict() != other.to_dict()
