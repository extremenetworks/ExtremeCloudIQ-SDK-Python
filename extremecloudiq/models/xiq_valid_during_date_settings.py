# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqValidDuringDateSettings(object):
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
        'start_date_time': 'XiqDateTimeType',
        'end_date_time': 'XiqDateTimeType',
        'time_zone': 'str'
    }

    attribute_map = {
        'start_date_time': 'start_date_time',
        'end_date_time': 'end_date_time',
        'time_zone': 'time_zone'
    }

    def __init__(self, start_date_time=None, end_date_time=None, time_zone=None, local_vars_configuration=None):  # noqa: E501
        """XiqValidDuringDateSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_date_time = None
        self._end_date_time = None
        self._time_zone = None
        self.discriminator = None

        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.time_zone = time_zone

    @property
    def start_date_time(self):
        """Gets the start_date_time of this XiqValidDuringDateSettings.  # noqa: E501


        :return: The start_date_time of this XiqValidDuringDateSettings.  # noqa: E501
        :rtype: XiqDateTimeType
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this XiqValidDuringDateSettings.


        :param start_date_time: The start_date_time of this XiqValidDuringDateSettings.  # noqa: E501
        :type: XiqDateTimeType
        """
        if self.local_vars_configuration.client_side_validation and start_date_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")  # noqa: E501

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this XiqValidDuringDateSettings.  # noqa: E501


        :return: The end_date_time of this XiqValidDuringDateSettings.  # noqa: E501
        :rtype: XiqDateTimeType
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this XiqValidDuringDateSettings.


        :param end_date_time: The end_date_time of this XiqValidDuringDateSettings.  # noqa: E501
        :type: XiqDateTimeType
        """
        if self.local_vars_configuration.client_side_validation and end_date_time is None:  # noqa: E501
            raise ValueError("Invalid value for `end_date_time`, must not be `None`")  # noqa: E501

        self._end_date_time = end_date_time

    @property
    def time_zone(self):
        """Gets the time_zone of this XiqValidDuringDateSettings.  # noqa: E501

        The date/time timezone  # noqa: E501

        :return: The time_zone of this XiqValidDuringDateSettings.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this XiqValidDuringDateSettings.

        The date/time timezone  # noqa: E501

        :param time_zone: The time_zone of this XiqValidDuringDateSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and time_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501

        self._time_zone = time_zone

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
        if not isinstance(other, XiqValidDuringDateSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqValidDuringDateSettings):
            return True

        return self.to_dict() != other.to_dict()
