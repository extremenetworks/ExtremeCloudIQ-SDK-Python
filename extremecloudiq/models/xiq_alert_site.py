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


class XiqAlertSite(object):
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
        'site_id': 'int',
        'site_name': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'site_name': 'site_name'
    }

    def __init__(self, site_id=None, site_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertSite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._site_id = None
        self._site_name = None
        self.discriminator = None

        self.site_id = site_id
        if site_name is not None:
            self.site_name = site_name

    @property
    def site_id(self):
        """Gets the site_id of this XiqAlertSite.  # noqa: E501

        The unique identifier of site  # noqa: E501

        :return: The site_id of this XiqAlertSite.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this XiqAlertSite.

        The unique identifier of site  # noqa: E501

        :param site_id: The site_id of this XiqAlertSite.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and site_id is None:  # noqa: E501
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def site_name(self):
        """Gets the site_name of this XiqAlertSite.  # noqa: E501

        The site name of the alert policy site  # noqa: E501

        :return: The site_name of this XiqAlertSite.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this XiqAlertSite.

        The site name of the alert policy site  # noqa: E501

        :param site_name: The site_name of this XiqAlertSite.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

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
        if not isinstance(other, XiqAlertSite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertSite):
            return True

        return self.to_dict() != other.to_dict()
