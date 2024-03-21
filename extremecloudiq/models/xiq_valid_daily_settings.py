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


class XiqValidDailySettings(object):
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
        'daily_start_hour': 'int',
        'daily_start_minute': 'int',
        'daily_end_hour': 'int',
        'daily_end_minute': 'int'
    }

    attribute_map = {
        'daily_start_hour': 'daily_start_hour',
        'daily_start_minute': 'daily_start_minute',
        'daily_end_hour': 'daily_end_hour',
        'daily_end_minute': 'daily_end_minute'
    }

    def __init__(self, daily_start_hour=None, daily_start_minute=None, daily_end_hour=None, daily_end_minute=None, local_vars_configuration=None):  # noqa: E501
        """XiqValidDailySettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._daily_start_hour = None
        self._daily_start_minute = None
        self._daily_end_hour = None
        self._daily_end_minute = None
        self.discriminator = None

        self.daily_start_hour = daily_start_hour
        self.daily_start_minute = daily_start_minute
        self.daily_end_hour = daily_end_hour
        self.daily_end_minute = daily_end_minute

    @property
    def daily_start_hour(self):
        """Gets the daily_start_hour of this XiqValidDailySettings.  # noqa: E501

        The 24-hour format start hour of the day  # noqa: E501

        :return: The daily_start_hour of this XiqValidDailySettings.  # noqa: E501
        :rtype: int
        """
        return self._daily_start_hour

    @daily_start_hour.setter
    def daily_start_hour(self, daily_start_hour):
        """Sets the daily_start_hour of this XiqValidDailySettings.

        The 24-hour format start hour of the day  # noqa: E501

        :param daily_start_hour: The daily_start_hour of this XiqValidDailySettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and daily_start_hour is None:  # noqa: E501
            raise ValueError("Invalid value for `daily_start_hour`, must not be `None`")  # noqa: E501

        self._daily_start_hour = daily_start_hour

    @property
    def daily_start_minute(self):
        """Gets the daily_start_minute of this XiqValidDailySettings.  # noqa: E501

        The minute of the hour  # noqa: E501

        :return: The daily_start_minute of this XiqValidDailySettings.  # noqa: E501
        :rtype: int
        """
        return self._daily_start_minute

    @daily_start_minute.setter
    def daily_start_minute(self, daily_start_minute):
        """Sets the daily_start_minute of this XiqValidDailySettings.

        The minute of the hour  # noqa: E501

        :param daily_start_minute: The daily_start_minute of this XiqValidDailySettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and daily_start_minute is None:  # noqa: E501
            raise ValueError("Invalid value for `daily_start_minute`, must not be `None`")  # noqa: E501

        self._daily_start_minute = daily_start_minute

    @property
    def daily_end_hour(self):
        """Gets the daily_end_hour of this XiqValidDailySettings.  # noqa: E501

        The 24-hour format end hour of day the end  # noqa: E501

        :return: The daily_end_hour of this XiqValidDailySettings.  # noqa: E501
        :rtype: int
        """
        return self._daily_end_hour

    @daily_end_hour.setter
    def daily_end_hour(self, daily_end_hour):
        """Sets the daily_end_hour of this XiqValidDailySettings.

        The 24-hour format end hour of day the end  # noqa: E501

        :param daily_end_hour: The daily_end_hour of this XiqValidDailySettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and daily_end_hour is None:  # noqa: E501
            raise ValueError("Invalid value for `daily_end_hour`, must not be `None`")  # noqa: E501

        self._daily_end_hour = daily_end_hour

    @property
    def daily_end_minute(self):
        """Gets the daily_end_minute of this XiqValidDailySettings.  # noqa: E501

        The minute of the hour  # noqa: E501

        :return: The daily_end_minute of this XiqValidDailySettings.  # noqa: E501
        :rtype: int
        """
        return self._daily_end_minute

    @daily_end_minute.setter
    def daily_end_minute(self, daily_end_minute):
        """Sets the daily_end_minute of this XiqValidDailySettings.

        The minute of the hour  # noqa: E501

        :param daily_end_minute: The daily_end_minute of this XiqValidDailySettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and daily_end_minute is None:  # noqa: E501
            raise ValueError("Invalid value for `daily_end_minute`, must not be `None`")  # noqa: E501

        self._daily_end_minute = daily_end_minute

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
        if not isinstance(other, XiqValidDailySettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqValidDailySettings):
            return True

        return self.to_dict() != other.to_dict()
