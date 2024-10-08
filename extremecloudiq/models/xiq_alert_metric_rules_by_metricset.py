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


class XiqAlertMetricRulesByMetricset(object):
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
        'metricset_id': 'int',
        'metricset_name': 'str',
        'rules': 'list[XiqAlertRuleOverview]'
    }

    attribute_map = {
        'metricset_id': 'metricset_id',
        'metricset_name': 'metricset_name',
        'rules': 'rules'
    }

    def __init__(self, metricset_id=None, metricset_name=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertMetricRulesByMetricset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metricset_id = None
        self._metricset_name = None
        self._rules = None
        self.discriminator = None

        self.metricset_id = metricset_id
        self.metricset_name = metricset_name
        self.rules = rules

    @property
    def metricset_id(self):
        """Gets the metricset_id of this XiqAlertMetricRulesByMetricset.  # noqa: E501

        The unique identifier of the metricset.  # noqa: E501

        :return: The metricset_id of this XiqAlertMetricRulesByMetricset.  # noqa: E501
        :rtype: int
        """
        return self._metricset_id

    @metricset_id.setter
    def metricset_id(self, metricset_id):
        """Sets the metricset_id of this XiqAlertMetricRulesByMetricset.

        The unique identifier of the metricset.  # noqa: E501

        :param metricset_id: The metricset_id of this XiqAlertMetricRulesByMetricset.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and metricset_id is None:  # noqa: E501
            raise ValueError("Invalid value for `metricset_id`, must not be `None`")  # noqa: E501

        self._metricset_id = metricset_id

    @property
    def metricset_name(self):
        """Gets the metricset_name of this XiqAlertMetricRulesByMetricset.  # noqa: E501

        The human-readable name of the metricset.  # noqa: E501

        :return: The metricset_name of this XiqAlertMetricRulesByMetricset.  # noqa: E501
        :rtype: str
        """
        return self._metricset_name

    @metricset_name.setter
    def metricset_name(self, metricset_name):
        """Sets the metricset_name of this XiqAlertMetricRulesByMetricset.

        The human-readable name of the metricset.  # noqa: E501

        :param metricset_name: The metricset_name of this XiqAlertMetricRulesByMetricset.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and metricset_name is None:  # noqa: E501
            raise ValueError("Invalid value for `metricset_name`, must not be `None`")  # noqa: E501

        self._metricset_name = metricset_name

    @property
    def rules(self):
        """Gets the rules of this XiqAlertMetricRulesByMetricset.  # noqa: E501

        A list of overviews of the metric-based alert rules, grouped by metricset.  # noqa: E501

        :return: The rules of this XiqAlertMetricRulesByMetricset.  # noqa: E501
        :rtype: list[XiqAlertRuleOverview]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this XiqAlertMetricRulesByMetricset.

        A list of overviews of the metric-based alert rules, grouped by metricset.  # noqa: E501

        :param rules: The rules of this XiqAlertMetricRulesByMetricset.  # noqa: E501
        :type: list[XiqAlertRuleOverview]
        """
        if self.local_vars_configuration.client_side_validation and rules is None:  # noqa: E501
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

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
        if not isinstance(other, XiqAlertMetricRulesByMetricset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertMetricRulesByMetricset):
            return True

        return self.to_dict() != other.to_dict()
