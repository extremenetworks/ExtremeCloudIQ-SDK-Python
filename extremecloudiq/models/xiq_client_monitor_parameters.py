# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqClientMonitorParameters(object):
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
        'trigger_times': 'int',
        'report_interval': 'int'
    }

    attribute_map = {
        'trigger_times': 'trigger_times',
        'report_interval': 'report_interval'
    }

    def __init__(self, trigger_times=None, report_interval=None, local_vars_configuration=None):  # noqa: E501
        """XiqClientMonitorParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._trigger_times = None
        self._report_interval = None
        self.discriminator = None

        if trigger_times is not None:
            self.trigger_times = trigger_times
        if report_interval is not None:
            self.report_interval = report_interval

    @property
    def trigger_times(self):
        """Gets the trigger_times of this XiqClientMonitorParameters.  # noqa: E501

        The trigger times, min = 1, max = 10  # noqa: E501

        :return: The trigger_times of this XiqClientMonitorParameters.  # noqa: E501
        :rtype: int
        """
        return self._trigger_times

    @trigger_times.setter
    def trigger_times(self, trigger_times):
        """Sets the trigger_times of this XiqClientMonitorParameters.

        The trigger times, min = 1, max = 10  # noqa: E501

        :param trigger_times: The trigger_times of this XiqClientMonitorParameters.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                trigger_times is not None and trigger_times > 10):  # noqa: E501
            raise ValueError("Invalid value for `trigger_times`, must be a value less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trigger_times is not None and trigger_times < 1):  # noqa: E501
            raise ValueError("Invalid value for `trigger_times`, must be a value greater than or equal to `1`")  # noqa: E501

        self._trigger_times = trigger_times

    @property
    def report_interval(self):
        """Gets the report_interval of this XiqClientMonitorParameters.  # noqa: E501

        The report interval, min = 30, max = 3600 seconds  # noqa: E501

        :return: The report_interval of this XiqClientMonitorParameters.  # noqa: E501
        :rtype: int
        """
        return self._report_interval

    @report_interval.setter
    def report_interval(self, report_interval):
        """Sets the report_interval of this XiqClientMonitorParameters.

        The report interval, min = 30, max = 3600 seconds  # noqa: E501

        :param report_interval: The report_interval of this XiqClientMonitorParameters.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                report_interval is not None and report_interval > 3600):  # noqa: E501
            raise ValueError("Invalid value for `report_interval`, must be a value less than or equal to `3600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                report_interval is not None and report_interval < 30):  # noqa: E501
            raise ValueError("Invalid value for `report_interval`, must be a value greater than or equal to `30`")  # noqa: E501

        self._report_interval = report_interval

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
        if not isinstance(other, XiqClientMonitorParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClientMonitorParameters):
            return True

        return self.to_dict() != other.to_dict()
