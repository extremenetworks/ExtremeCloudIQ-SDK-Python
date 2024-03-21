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


class XiqAlertPolicyFilter(object):
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
        'name': 'str',
        'site_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'site_ids': 'site_ids'
    }

    def __init__(self, name=None, site_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertPolicyFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._site_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.site_ids = site_ids

    @property
    def name(self):
        """Gets the name of this XiqAlertPolicyFilter.  # noqa: E501

        The policy name.  # noqa: E501

        :return: The name of this XiqAlertPolicyFilter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqAlertPolicyFilter.

        The policy name.  # noqa: E501

        :param name: The name of this XiqAlertPolicyFilter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def site_ids(self):
        """Gets the site_ids of this XiqAlertPolicyFilter.  # noqa: E501

        The site ID list.  # noqa: E501

        :return: The site_ids of this XiqAlertPolicyFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        """Sets the site_ids of this XiqAlertPolicyFilter.

        The site ID list.  # noqa: E501

        :param site_ids: The site_ids of this XiqAlertPolicyFilter.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and site_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `site_ids`, must not be `None`")  # noqa: E501

        self._site_ids = site_ids

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
        if not isinstance(other, XiqAlertPolicyFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertPolicyFilter):
            return True

        return self.to_dict() != other.to_dict()
