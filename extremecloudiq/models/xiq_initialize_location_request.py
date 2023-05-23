# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqInitializeLocationRequest(object):
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
        'organization': 'str',
        'country': 'XiqCountryCode'
    }

    attribute_map = {
        'organization': 'organization',
        'country': 'country'
    }

    def __init__(self, organization=None, country=None, local_vars_configuration=None):  # noqa: E501
        """XiqInitializeLocationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._organization = None
        self._country = None
        self.discriminator = None

        self.organization = organization
        self.country = country

    @property
    def organization(self):
        """Gets the organization of this XiqInitializeLocationRequest.  # noqa: E501

        The organization name.  # noqa: E501

        :return: The organization of this XiqInitializeLocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this XiqInitializeLocationRequest.

        The organization name.  # noqa: E501

        :param organization: The organization of this XiqInitializeLocationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def country(self):
        """Gets the country of this XiqInitializeLocationRequest.  # noqa: E501


        :return: The country of this XiqInitializeLocationRequest.  # noqa: E501
        :rtype: XiqCountryCode
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this XiqInitializeLocationRequest.


        :param country: The country of this XiqInitializeLocationRequest.  # noqa: E501
        :type: XiqCountryCode
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

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
        if not isinstance(other, XiqInitializeLocationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqInitializeLocationRequest):
            return True

        return self.to_dict() != other.to_dict()
