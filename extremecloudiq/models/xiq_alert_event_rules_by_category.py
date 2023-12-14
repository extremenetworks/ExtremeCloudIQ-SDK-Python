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


class XiqAlertEventRulesByCategory(object):
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
        'category_id': 'int',
        'category_name': 'str',
        'rules': 'list[XiqAlertRuleOverview]'
    }

    attribute_map = {
        'category_id': 'category_id',
        'category_name': 'category_name',
        'rules': 'rules'
    }

    def __init__(self, category_id=None, category_name=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertEventRulesByCategory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category_id = None
        self._category_name = None
        self._rules = None
        self.discriminator = None

        self.category_id = category_id
        self.category_name = category_name
        self.rules = rules

    @property
    def category_id(self):
        """Gets the category_id of this XiqAlertEventRulesByCategory.  # noqa: E501

        The unique identifier of category ID.  # noqa: E501

        :return: The category_id of this XiqAlertEventRulesByCategory.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this XiqAlertEventRulesByCategory.

        The unique identifier of category ID.  # noqa: E501

        :param category_id: The category_id of this XiqAlertEventRulesByCategory.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and category_id is None:  # noqa: E501
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this XiqAlertEventRulesByCategory.  # noqa: E501

        The category name of category  # noqa: E501

        :return: The category_name of this XiqAlertEventRulesByCategory.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this XiqAlertEventRulesByCategory.

        The category name of category  # noqa: E501

        :param category_name: The category_name of this XiqAlertEventRulesByCategory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category_name is None:  # noqa: E501
            raise ValueError("Invalid value for `category_name`, must not be `None`")  # noqa: E501

        self._category_name = category_name

    @property
    def rules(self):
        """Gets the rules of this XiqAlertEventRulesByCategory.  # noqa: E501

        A list of overviews of the event-based alert rules, grouped by event.  # noqa: E501

        :return: The rules of this XiqAlertEventRulesByCategory.  # noqa: E501
        :rtype: list[XiqAlertRuleOverview]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this XiqAlertEventRulesByCategory.

        A list of overviews of the event-based alert rules, grouped by event.  # noqa: E501

        :param rules: The rules of this XiqAlertEventRulesByCategory.  # noqa: E501
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
        if not isinstance(other, XiqAlertEventRulesByCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertEventRulesByCategory):
            return True

        return self.to_dict() != other.to_dict()
