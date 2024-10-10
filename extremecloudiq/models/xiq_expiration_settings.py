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


class XiqExpirationSettings(object):
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
        'expiration_type': 'XiqExpirationType',
        'valid_during_dates': 'XiqValidDuringDateSettings',
        'valid_for_time_period': 'XiqValidForTimePeriodSettings',
        'valid_daily': 'XiqValidDailySettings',
        'expiration_action': 'XiqExpirationActionType',
        'post_expiration_action': 'XiqPostExpirationAction'
    }

    attribute_map = {
        'expiration_type': 'expiration_type',
        'valid_during_dates': 'valid_during_dates',
        'valid_for_time_period': 'valid_for_time_period',
        'valid_daily': 'valid_daily',
        'expiration_action': 'expiration_action',
        'post_expiration_action': 'post_expiration_action'
    }

    def __init__(self, expiration_type=None, valid_during_dates=None, valid_for_time_period=None, valid_daily=None, expiration_action=None, post_expiration_action=None, local_vars_configuration=None):  # noqa: E501
        """XiqExpirationSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expiration_type = None
        self._valid_during_dates = None
        self._valid_for_time_period = None
        self._valid_daily = None
        self._expiration_action = None
        self._post_expiration_action = None
        self.discriminator = None

        if expiration_type is not None:
            self.expiration_type = expiration_type
        if valid_during_dates is not None:
            self.valid_during_dates = valid_during_dates
        if valid_for_time_period is not None:
            self.valid_for_time_period = valid_for_time_period
        if valid_daily is not None:
            self.valid_daily = valid_daily
        if expiration_action is not None:
            self.expiration_action = expiration_action
        if post_expiration_action is not None:
            self.post_expiration_action = post_expiration_action

    @property
    def expiration_type(self):
        """Gets the expiration_type of this XiqExpirationSettings.  # noqa: E501


        :return: The expiration_type of this XiqExpirationSettings.  # noqa: E501
        :rtype: XiqExpirationType
        """
        return self._expiration_type

    @expiration_type.setter
    def expiration_type(self, expiration_type):
        """Sets the expiration_type of this XiqExpirationSettings.


        :param expiration_type: The expiration_type of this XiqExpirationSettings.  # noqa: E501
        :type: XiqExpirationType
        """

        self._expiration_type = expiration_type

    @property
    def valid_during_dates(self):
        """Gets the valid_during_dates of this XiqExpirationSettings.  # noqa: E501


        :return: The valid_during_dates of this XiqExpirationSettings.  # noqa: E501
        :rtype: XiqValidDuringDateSettings
        """
        return self._valid_during_dates

    @valid_during_dates.setter
    def valid_during_dates(self, valid_during_dates):
        """Sets the valid_during_dates of this XiqExpirationSettings.


        :param valid_during_dates: The valid_during_dates of this XiqExpirationSettings.  # noqa: E501
        :type: XiqValidDuringDateSettings
        """

        self._valid_during_dates = valid_during_dates

    @property
    def valid_for_time_period(self):
        """Gets the valid_for_time_period of this XiqExpirationSettings.  # noqa: E501


        :return: The valid_for_time_period of this XiqExpirationSettings.  # noqa: E501
        :rtype: XiqValidForTimePeriodSettings
        """
        return self._valid_for_time_period

    @valid_for_time_period.setter
    def valid_for_time_period(self, valid_for_time_period):
        """Sets the valid_for_time_period of this XiqExpirationSettings.


        :param valid_for_time_period: The valid_for_time_period of this XiqExpirationSettings.  # noqa: E501
        :type: XiqValidForTimePeriodSettings
        """

        self._valid_for_time_period = valid_for_time_period

    @property
    def valid_daily(self):
        """Gets the valid_daily of this XiqExpirationSettings.  # noqa: E501


        :return: The valid_daily of this XiqExpirationSettings.  # noqa: E501
        :rtype: XiqValidDailySettings
        """
        return self._valid_daily

    @valid_daily.setter
    def valid_daily(self, valid_daily):
        """Sets the valid_daily of this XiqExpirationSettings.


        :param valid_daily: The valid_daily of this XiqExpirationSettings.  # noqa: E501
        :type: XiqValidDailySettings
        """

        self._valid_daily = valid_daily

    @property
    def expiration_action(self):
        """Gets the expiration_action of this XiqExpirationSettings.  # noqa: E501


        :return: The expiration_action of this XiqExpirationSettings.  # noqa: E501
        :rtype: XiqExpirationActionType
        """
        return self._expiration_action

    @expiration_action.setter
    def expiration_action(self, expiration_action):
        """Sets the expiration_action of this XiqExpirationSettings.


        :param expiration_action: The expiration_action of this XiqExpirationSettings.  # noqa: E501
        :type: XiqExpirationActionType
        """

        self._expiration_action = expiration_action

    @property
    def post_expiration_action(self):
        """Gets the post_expiration_action of this XiqExpirationSettings.  # noqa: E501


        :return: The post_expiration_action of this XiqExpirationSettings.  # noqa: E501
        :rtype: XiqPostExpirationAction
        """
        return self._post_expiration_action

    @post_expiration_action.setter
    def post_expiration_action(self, post_expiration_action):
        """Sets the post_expiration_action of this XiqExpirationSettings.


        :param post_expiration_action: The post_expiration_action of this XiqExpirationSettings.  # noqa: E501
        :type: XiqPostExpirationAction
        """

        self._post_expiration_action = post_expiration_action

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
        if not isinstance(other, XiqExpirationSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExpirationSettings):
            return True

        return self.to_dict() != other.to_dict()
