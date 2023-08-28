# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateRpWmmQosSettingsRequest(object):
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
        'arbitration_interframe_space': 'int',
        'min_contention_window': 'int',
        'max_contention_window': 'int',
        'transmission_opportunity_limit': 'int',
        'enable_no_ack': 'bool'
    }

    attribute_map = {
        'arbitration_interframe_space': 'arbitration_interframe_space',
        'min_contention_window': 'min_contention_window',
        'max_contention_window': 'max_contention_window',
        'transmission_opportunity_limit': 'transmission_opportunity_limit',
        'enable_no_ack': 'enable_no_ack'
    }

    def __init__(self, arbitration_interframe_space=None, min_contention_window=None, max_contention_window=None, transmission_opportunity_limit=None, enable_no_ack=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateRpWmmQosSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._arbitration_interframe_space = None
        self._min_contention_window = None
        self._max_contention_window = None
        self._transmission_opportunity_limit = None
        self._enable_no_ack = None
        self.discriminator = None

        if arbitration_interframe_space is not None:
            self.arbitration_interframe_space = arbitration_interframe_space
        if min_contention_window is not None:
            self.min_contention_window = min_contention_window
        if max_contention_window is not None:
            self.max_contention_window = max_contention_window
        if transmission_opportunity_limit is not None:
            self.transmission_opportunity_limit = transmission_opportunity_limit
        if enable_no_ack is not None:
            self.enable_no_ack = enable_no_ack

    @property
    def arbitration_interframe_space(self):
        """Gets the arbitration_interframe_space of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501

        The Arbitration Interframe space, in the range of 1 to 15.  # noqa: E501

        :return: The arbitration_interframe_space of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._arbitration_interframe_space

    @arbitration_interframe_space.setter
    def arbitration_interframe_space(self, arbitration_interframe_space):
        """Sets the arbitration_interframe_space of this XiqUpdateRpWmmQosSettingsRequest.

        The Arbitration Interframe space, in the range of 1 to 15.  # noqa: E501

        :param arbitration_interframe_space: The arbitration_interframe_space of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                arbitration_interframe_space is not None and arbitration_interframe_space > 15):  # noqa: E501
            raise ValueError("Invalid value for `arbitration_interframe_space`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                arbitration_interframe_space is not None and arbitration_interframe_space < 1):  # noqa: E501
            raise ValueError("Invalid value for `arbitration_interframe_space`, must be a value greater than or equal to `1`")  # noqa: E501

        self._arbitration_interframe_space = arbitration_interframe_space

    @property
    def min_contention_window(self):
        """Gets the min_contention_window of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501

        The Minimum Contention window, in the range of 1 to 15.  # noqa: E501

        :return: The min_contention_window of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_contention_window

    @min_contention_window.setter
    def min_contention_window(self, min_contention_window):
        """Sets the min_contention_window of this XiqUpdateRpWmmQosSettingsRequest.

        The Minimum Contention window, in the range of 1 to 15.  # noqa: E501

        :param min_contention_window: The min_contention_window of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                min_contention_window is not None and min_contention_window > 15):  # noqa: E501
            raise ValueError("Invalid value for `min_contention_window`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_contention_window is not None and min_contention_window < 1):  # noqa: E501
            raise ValueError("Invalid value for `min_contention_window`, must be a value greater than or equal to `1`")  # noqa: E501

        self._min_contention_window = min_contention_window

    @property
    def max_contention_window(self):
        """Gets the max_contention_window of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501

        The Maximum Contention window, in the range of 1 to 15.  # noqa: E501

        :return: The max_contention_window of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_contention_window

    @max_contention_window.setter
    def max_contention_window(self, max_contention_window):
        """Sets the max_contention_window of this XiqUpdateRpWmmQosSettingsRequest.

        The Maximum Contention window, in the range of 1 to 15.  # noqa: E501

        :param max_contention_window: The max_contention_window of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_contention_window is not None and max_contention_window > 15):  # noqa: E501
            raise ValueError("Invalid value for `max_contention_window`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_contention_window is not None and max_contention_window < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_contention_window`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_contention_window = max_contention_window

    @property
    def transmission_opportunity_limit(self):
        """Gets the transmission_opportunity_limit of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501

        The Transmission Opportunity limit, in the range of 0 to 8192.  # noqa: E501

        :return: The transmission_opportunity_limit of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._transmission_opportunity_limit

    @transmission_opportunity_limit.setter
    def transmission_opportunity_limit(self, transmission_opportunity_limit):
        """Sets the transmission_opportunity_limit of this XiqUpdateRpWmmQosSettingsRequest.

        The Transmission Opportunity limit, in the range of 0 to 8192.  # noqa: E501

        :param transmission_opportunity_limit: The transmission_opportunity_limit of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                transmission_opportunity_limit is not None and transmission_opportunity_limit > 8192):  # noqa: E501
            raise ValueError("Invalid value for `transmission_opportunity_limit`, must be a value less than or equal to `8192`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmission_opportunity_limit is not None and transmission_opportunity_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `transmission_opportunity_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transmission_opportunity_limit = transmission_opportunity_limit

    @property
    def enable_no_ack(self):
        """Gets the enable_no_ack of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501

        Whether to enable No Acknowledgment  # noqa: E501

        :return: The enable_no_ack of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_no_ack

    @enable_no_ack.setter
    def enable_no_ack(self, enable_no_ack):
        """Sets the enable_no_ack of this XiqUpdateRpWmmQosSettingsRequest.

        Whether to enable No Acknowledgment  # noqa: E501

        :param enable_no_ack: The enable_no_ack of this XiqUpdateRpWmmQosSettingsRequest.  # noqa: E501
        :type: bool
        """

        self._enable_no_ack = enable_no_ack

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
        if not isinstance(other, XiqUpdateRpWmmQosSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateRpWmmQosSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
