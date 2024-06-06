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


class NetworkHealth(object):
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
        'overall_score': 'int',
        'internet_availability_score': 'int',
        'internet_performance': 'int',
        'network_usage': 'int'
    }

    attribute_map = {
        'overall_score': 'overall_score',
        'internet_availability_score': 'internet_availability_score',
        'internet_performance': 'internet_performance',
        'network_usage': 'network_usage'
    }

    def __init__(self, overall_score=None, internet_availability_score=None, internet_performance=None, network_usage=None, local_vars_configuration=None):  # noqa: E501
        """NetworkHealth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall_score = None
        self._internet_availability_score = None
        self._internet_performance = None
        self._network_usage = None
        self.discriminator = None

        if overall_score is not None:
            self.overall_score = overall_score
        if internet_availability_score is not None:
            self.internet_availability_score = internet_availability_score
        if internet_performance is not None:
            self.internet_performance = internet_performance
        if network_usage is not None:
            self.network_usage = network_usage

    @property
    def overall_score(self):
        """Gets the overall_score of this NetworkHealth.  # noqa: E501

        The overall health score  # noqa: E501

        :return: The overall_score of this NetworkHealth.  # noqa: E501
        :rtype: int
        """
        return self._overall_score

    @overall_score.setter
    def overall_score(self, overall_score):
        """Sets the overall_score of this NetworkHealth.

        The overall health score  # noqa: E501

        :param overall_score: The overall_score of this NetworkHealth.  # noqa: E501
        :type: int
        """

        self._overall_score = overall_score

    @property
    def internet_availability_score(self):
        """Gets the internet_availability_score of this NetworkHealth.  # noqa: E501

        The overall internet availability score  # noqa: E501

        :return: The internet_availability_score of this NetworkHealth.  # noqa: E501
        :rtype: int
        """
        return self._internet_availability_score

    @internet_availability_score.setter
    def internet_availability_score(self, internet_availability_score):
        """Sets the internet_availability_score of this NetworkHealth.

        The overall internet availability score  # noqa: E501

        :param internet_availability_score: The internet_availability_score of this NetworkHealth.  # noqa: E501
        :type: int
        """

        self._internet_availability_score = internet_availability_score

    @property
    def internet_performance(self):
        """Gets the internet_performance of this NetworkHealth.  # noqa: E501

        The internet performance value in milli-seconds  # noqa: E501

        :return: The internet_performance of this NetworkHealth.  # noqa: E501
        :rtype: int
        """
        return self._internet_performance

    @internet_performance.setter
    def internet_performance(self, internet_performance):
        """Sets the internet_performance of this NetworkHealth.

        The internet performance value in milli-seconds  # noqa: E501

        :param internet_performance: The internet_performance of this NetworkHealth.  # noqa: E501
        :type: int
        """

        self._internet_performance = internet_performance

    @property
    def network_usage(self):
        """Gets the network_usage of this NetworkHealth.  # noqa: E501

        The network usage value in MB  # noqa: E501

        :return: The network_usage of this NetworkHealth.  # noqa: E501
        :rtype: int
        """
        return self._network_usage

    @network_usage.setter
    def network_usage(self, network_usage):
        """Sets the network_usage of this NetworkHealth.

        The network usage value in MB  # noqa: E501

        :param network_usage: The network_usage of this NetworkHealth.  # noqa: E501
        :type: int
        """

        self._network_usage = network_usage

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
        if not isinstance(other, NetworkHealth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkHealth):
            return True

        return self.to_dict() != other.to_dict()
