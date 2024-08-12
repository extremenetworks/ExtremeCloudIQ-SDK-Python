# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqValidTimePeriodAfterIdCreation(object):
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
        'valid_time_period': 'int',
        'valid_time_period_unit': 'XiqDateTimeUnitType'
    }

    attribute_map = {
        'valid_time_period': 'valid_time_period',
        'valid_time_period_unit': 'valid_time_period_unit'
    }

    def __init__(self, valid_time_period=None, valid_time_period_unit=None, local_vars_configuration=None):  # noqa: E501
        """XiqValidTimePeriodAfterIdCreation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._valid_time_period = None
        self._valid_time_period_unit = None
        self.discriminator = None

        self.valid_time_period = valid_time_period
        self.valid_time_period_unit = valid_time_period_unit

    @property
    def valid_time_period(self):
        """Gets the valid_time_period of this XiqValidTimePeriodAfterIdCreation.  # noqa: E501

        The valid time period after account creation  # noqa: E501

        :return: The valid_time_period of this XiqValidTimePeriodAfterIdCreation.  # noqa: E501
        :rtype: int
        """
        return self._valid_time_period

    @valid_time_period.setter
    def valid_time_period(self, valid_time_period):
        """Sets the valid_time_period of this XiqValidTimePeriodAfterIdCreation.

        The valid time period after account creation  # noqa: E501

        :param valid_time_period: The valid_time_period of this XiqValidTimePeriodAfterIdCreation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and valid_time_period is None:  # noqa: E501
            raise ValueError("Invalid value for `valid_time_period`, must not be `None`")  # noqa: E501

        self._valid_time_period = valid_time_period

    @property
    def valid_time_period_unit(self):
        """Gets the valid_time_period_unit of this XiqValidTimePeriodAfterIdCreation.  # noqa: E501


        :return: The valid_time_period_unit of this XiqValidTimePeriodAfterIdCreation.  # noqa: E501
        :rtype: XiqDateTimeUnitType
        """
        return self._valid_time_period_unit

    @valid_time_period_unit.setter
    def valid_time_period_unit(self, valid_time_period_unit):
        """Sets the valid_time_period_unit of this XiqValidTimePeriodAfterIdCreation.


        :param valid_time_period_unit: The valid_time_period_unit of this XiqValidTimePeriodAfterIdCreation.  # noqa: E501
        :type: XiqDateTimeUnitType
        """
        if self.local_vars_configuration.client_side_validation and valid_time_period_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `valid_time_period_unit`, must not be `None`")  # noqa: E501

        self._valid_time_period_unit = valid_time_period_unit

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
        if not isinstance(other, XiqValidTimePeriodAfterIdCreation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqValidTimePeriodAfterIdCreation):
            return True

        return self.to_dict() != other.to_dict()
