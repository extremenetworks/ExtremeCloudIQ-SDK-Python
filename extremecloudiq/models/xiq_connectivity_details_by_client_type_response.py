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


class XiqConnectivityDetailsByClientTypeResponse(object):
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
        'sites_by_wireless': 'XiqSitesByWirelessEntity',
        'sites_by_wired': 'XiqSitesByWiredEntity'
    }

    attribute_map = {
        'sites_by_wireless': 'sites_by_wireless',
        'sites_by_wired': 'sites_by_wired'
    }

    def __init__(self, sites_by_wireless=None, sites_by_wired=None, local_vars_configuration=None):  # noqa: E501
        """XiqConnectivityDetailsByClientTypeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sites_by_wireless = None
        self._sites_by_wired = None
        self.discriminator = None

        if sites_by_wireless is not None:
            self.sites_by_wireless = sites_by_wireless
        if sites_by_wired is not None:
            self.sites_by_wired = sites_by_wired

    @property
    def sites_by_wireless(self):
        """Gets the sites_by_wireless of this XiqConnectivityDetailsByClientTypeResponse.  # noqa: E501


        :return: The sites_by_wireless of this XiqConnectivityDetailsByClientTypeResponse.  # noqa: E501
        :rtype: XiqSitesByWirelessEntity
        """
        return self._sites_by_wireless

    @sites_by_wireless.setter
    def sites_by_wireless(self, sites_by_wireless):
        """Sets the sites_by_wireless of this XiqConnectivityDetailsByClientTypeResponse.


        :param sites_by_wireless: The sites_by_wireless of this XiqConnectivityDetailsByClientTypeResponse.  # noqa: E501
        :type: XiqSitesByWirelessEntity
        """

        self._sites_by_wireless = sites_by_wireless

    @property
    def sites_by_wired(self):
        """Gets the sites_by_wired of this XiqConnectivityDetailsByClientTypeResponse.  # noqa: E501


        :return: The sites_by_wired of this XiqConnectivityDetailsByClientTypeResponse.  # noqa: E501
        :rtype: XiqSitesByWiredEntity
        """
        return self._sites_by_wired

    @sites_by_wired.setter
    def sites_by_wired(self, sites_by_wired):
        """Sets the sites_by_wired of this XiqConnectivityDetailsByClientTypeResponse.


        :param sites_by_wired: The sites_by_wired of this XiqConnectivityDetailsByClientTypeResponse.  # noqa: E501
        :type: XiqSitesByWiredEntity
        """

        self._sites_by_wired = sites_by_wired

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
        if not isinstance(other, XiqConnectivityDetailsByClientTypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqConnectivityDetailsByClientTypeResponse):
            return True

        return self.to_dict() != other.to_dict()
