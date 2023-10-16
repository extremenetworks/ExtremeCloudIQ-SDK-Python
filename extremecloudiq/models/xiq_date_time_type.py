# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDateTimeType(object):
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
        'day_of_month': 'int',
        'month': 'int',
        'year': 'int',
        'hour_of_day': 'int',
        'minute_of_hour': 'int'
    }

    attribute_map = {
        'day_of_month': 'day_of_month',
        'month': 'month',
        'year': 'year',
        'hour_of_day': 'hour_of_day',
        'minute_of_hour': 'minute_of_hour'
    }

    def __init__(self, day_of_month=None, month=None, year=None, hour_of_day=None, minute_of_hour=None, local_vars_configuration=None):  # noqa: E501
        """XiqDateTimeType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._day_of_month = None
        self._month = None
        self._year = None
        self._hour_of_day = None
        self._minute_of_hour = None
        self.discriminator = None

        self.day_of_month = day_of_month
        self.month = month
        self.year = year
        self.hour_of_day = hour_of_day
        self.minute_of_hour = minute_of_hour

    @property
    def day_of_month(self):
        """Gets the day_of_month of this XiqDateTimeType.  # noqa: E501

        The day of month  # noqa: E501

        :return: The day_of_month of this XiqDateTimeType.  # noqa: E501
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this XiqDateTimeType.

        The day of month  # noqa: E501

        :param day_of_month: The day_of_month of this XiqDateTimeType.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and day_of_month is None:  # noqa: E501
            raise ValueError("Invalid value for `day_of_month`, must not be `None`")  # noqa: E501

        self._day_of_month = day_of_month

    @property
    def month(self):
        """Gets the month of this XiqDateTimeType.  # noqa: E501

        The month  # noqa: E501

        :return: The month of this XiqDateTimeType.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this XiqDateTimeType.

        The month  # noqa: E501

        :param month: The month of this XiqDateTimeType.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def year(self):
        """Gets the year of this XiqDateTimeType.  # noqa: E501

        The year  # noqa: E501

        :return: The year of this XiqDateTimeType.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this XiqDateTimeType.

        The year  # noqa: E501

        :param year: The year of this XiqDateTimeType.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def hour_of_day(self):
        """Gets the hour_of_day of this XiqDateTimeType.  # noqa: E501

        The 24-hour format hour of day  # noqa: E501

        :return: The hour_of_day of this XiqDateTimeType.  # noqa: E501
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        """Sets the hour_of_day of this XiqDateTimeType.

        The 24-hour format hour of day  # noqa: E501

        :param hour_of_day: The hour_of_day of this XiqDateTimeType.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hour_of_day is None:  # noqa: E501
            raise ValueError("Invalid value for `hour_of_day`, must not be `None`")  # noqa: E501

        self._hour_of_day = hour_of_day

    @property
    def minute_of_hour(self):
        """Gets the minute_of_hour of this XiqDateTimeType.  # noqa: E501

        The minute of the hour  # noqa: E501

        :return: The minute_of_hour of this XiqDateTimeType.  # noqa: E501
        :rtype: int
        """
        return self._minute_of_hour

    @minute_of_hour.setter
    def minute_of_hour(self, minute_of_hour):
        """Sets the minute_of_hour of this XiqDateTimeType.

        The minute of the hour  # noqa: E501

        :param minute_of_hour: The minute_of_hour of this XiqDateTimeType.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and minute_of_hour is None:  # noqa: E501
            raise ValueError("Invalid value for `minute_of_hour`, must not be `None`")  # noqa: E501

        self._minute_of_hour = minute_of_hour

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
        if not isinstance(other, XiqDateTimeType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDateTimeType):
            return True

        return self.to_dict() != other.to_dict()
