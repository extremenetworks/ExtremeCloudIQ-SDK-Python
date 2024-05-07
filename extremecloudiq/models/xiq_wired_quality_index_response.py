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


class XiqWiredQualityIndexResponse(object):
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
        'hardware_score': 'int',
        'quality_index': 'int'
    }

    attribute_map = {
        'hardware_score': 'hardware_score',
        'quality_index': 'quality_index'
    }

    def __init__(self, hardware_score=None, quality_index=None, local_vars_configuration=None):  # noqa: E501
        """XiqWiredQualityIndexResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hardware_score = None
        self._quality_index = None
        self.discriminator = None

        if hardware_score is not None:
            self.hardware_score = hardware_score
        if quality_index is not None:
            self.quality_index = quality_index

    @property
    def hardware_score(self):
        """Gets the hardware_score of this XiqWiredQualityIndexResponse.  # noqa: E501

        the hardware score  # noqa: E501

        :return: The hardware_score of this XiqWiredQualityIndexResponse.  # noqa: E501
        :rtype: int
        """
        return self._hardware_score

    @hardware_score.setter
    def hardware_score(self, hardware_score):
        """Sets the hardware_score of this XiqWiredQualityIndexResponse.

        the hardware score  # noqa: E501

        :param hardware_score: The hardware_score of this XiqWiredQualityIndexResponse.  # noqa: E501
        :type: int
        """

        self._hardware_score = hardware_score

    @property
    def quality_index(self):
        """Gets the quality_index of this XiqWiredQualityIndexResponse.  # noqa: E501

        the quality index  # noqa: E501

        :return: The quality_index of this XiqWiredQualityIndexResponse.  # noqa: E501
        :rtype: int
        """
        return self._quality_index

    @quality_index.setter
    def quality_index(self, quality_index):
        """Sets the quality_index of this XiqWiredQualityIndexResponse.

        the quality index  # noqa: E501

        :param quality_index: The quality_index of this XiqWiredQualityIndexResponse.  # noqa: E501
        :type: int
        """

        self._quality_index = quality_index

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
        if not isinstance(other, XiqWiredQualityIndexResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWiredQualityIndexResponse):
            return True

        return self.to_dict() != other.to_dict()
