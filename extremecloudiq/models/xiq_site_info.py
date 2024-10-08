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


class XiqSiteInfo(object):
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
        'device_ids': 'list[int]',
        'overview': 'XiqDeploymentOverviewDetails'
    }

    attribute_map = {
        'site_id': 'site_id',
        'device_ids': 'device_ids',
        'overview': 'overview'
    }

    def __init__(self, site_id=None, device_ids=None, overview=None, local_vars_configuration=None):  # noqa: E501
        """XiqSiteInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._site_id = None
        self._device_ids = None
        self._overview = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if device_ids is not None:
            self.device_ids = device_ids
        if overview is not None:
            self.overview = overview

    @property
    def site_id(self):
        """Gets the site_id of this XiqSiteInfo.  # noqa: E501

        The site ID  # noqa: E501

        :return: The site_id of this XiqSiteInfo.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this XiqSiteInfo.

        The site ID  # noqa: E501

        :param site_id: The site_id of this XiqSiteInfo.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def device_ids(self):
        """Gets the device_ids of this XiqSiteInfo.  # noqa: E501

        The device IDs  # noqa: E501

        :return: The device_ids of this XiqSiteInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this XiqSiteInfo.

        The device IDs  # noqa: E501

        :param device_ids: The device_ids of this XiqSiteInfo.  # noqa: E501
        :type: list[int]
        """

        self._device_ids = device_ids

    @property
    def overview(self):
        """Gets the overview of this XiqSiteInfo.  # noqa: E501


        :return: The overview of this XiqSiteInfo.  # noqa: E501
        :rtype: XiqDeploymentOverviewDetails
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this XiqSiteInfo.


        :param overview: The overview of this XiqSiteInfo.  # noqa: E501
        :type: XiqDeploymentOverviewDetails
        """

        self._overview = overview

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
        if not isinstance(other, XiqSiteInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSiteInfo):
            return True

        return self.to_dict() != other.to_dict()
