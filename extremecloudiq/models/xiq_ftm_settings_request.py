# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqFtmSettingsRequest(object):
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
        'wgs84_override': 'bool',
        'wgs84': 'XiqWgs84',
        'zsubelement_override': 'bool',
        'zsubelement': 'XiqZsubelement',
        'civic_address_override': 'bool',
        'civic_address': 'str'
    }

    attribute_map = {
        'wgs84_override': 'wgs84_override',
        'wgs84': 'wgs84',
        'zsubelement_override': 'zsubelement_override',
        'zsubelement': 'zsubelement',
        'civic_address_override': 'civic_address_override',
        'civic_address': 'civic_address'
    }

    def __init__(self, wgs84_override=None, wgs84=None, zsubelement_override=None, zsubelement=None, civic_address_override=None, civic_address=None, local_vars_configuration=None):  # noqa: E501
        """XiqFtmSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wgs84_override = None
        self._wgs84 = None
        self._zsubelement_override = None
        self._zsubelement = None
        self._civic_address_override = None
        self._civic_address = None
        self.discriminator = None

        self.wgs84_override = wgs84_override
        if wgs84 is not None:
            self.wgs84 = wgs84
        self.zsubelement_override = zsubelement_override
        if zsubelement is not None:
            self.zsubelement = zsubelement
        self.civic_address_override = civic_address_override
        if civic_address is not None:
            self.civic_address = civic_address

    @property
    def wgs84_override(self):
        """Gets the wgs84_override of this XiqFtmSettingsRequest.  # noqa: E501

        World Geodetic System 1984 (WGS84) override.  # noqa: E501

        :return: The wgs84_override of this XiqFtmSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._wgs84_override

    @wgs84_override.setter
    def wgs84_override(self, wgs84_override):
        """Sets the wgs84_override of this XiqFtmSettingsRequest.

        World Geodetic System 1984 (WGS84) override.  # noqa: E501

        :param wgs84_override: The wgs84_override of this XiqFtmSettingsRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and wgs84_override is None:  # noqa: E501
            raise ValueError("Invalid value for `wgs84_override`, must not be `None`")  # noqa: E501

        self._wgs84_override = wgs84_override

    @property
    def wgs84(self):
        """Gets the wgs84 of this XiqFtmSettingsRequest.  # noqa: E501


        :return: The wgs84 of this XiqFtmSettingsRequest.  # noqa: E501
        :rtype: XiqWgs84
        """
        return self._wgs84

    @wgs84.setter
    def wgs84(self, wgs84):
        """Sets the wgs84 of this XiqFtmSettingsRequest.


        :param wgs84: The wgs84 of this XiqFtmSettingsRequest.  # noqa: E501
        :type: XiqWgs84
        """

        self._wgs84 = wgs84

    @property
    def zsubelement_override(self):
        """Gets the zsubelement_override of this XiqFtmSettingsRequest.  # noqa: E501

        Z-subelement override.  # noqa: E501

        :return: The zsubelement_override of this XiqFtmSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._zsubelement_override

    @zsubelement_override.setter
    def zsubelement_override(self, zsubelement_override):
        """Sets the zsubelement_override of this XiqFtmSettingsRequest.

        Z-subelement override.  # noqa: E501

        :param zsubelement_override: The zsubelement_override of this XiqFtmSettingsRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and zsubelement_override is None:  # noqa: E501
            raise ValueError("Invalid value for `zsubelement_override`, must not be `None`")  # noqa: E501

        self._zsubelement_override = zsubelement_override

    @property
    def zsubelement(self):
        """Gets the zsubelement of this XiqFtmSettingsRequest.  # noqa: E501


        :return: The zsubelement of this XiqFtmSettingsRequest.  # noqa: E501
        :rtype: XiqZsubelement
        """
        return self._zsubelement

    @zsubelement.setter
    def zsubelement(self, zsubelement):
        """Sets the zsubelement of this XiqFtmSettingsRequest.


        :param zsubelement: The zsubelement of this XiqFtmSettingsRequest.  # noqa: E501
        :type: XiqZsubelement
        """

        self._zsubelement = zsubelement

    @property
    def civic_address_override(self):
        """Gets the civic_address_override of this XiqFtmSettingsRequest.  # noqa: E501

        Civic Address override.  # noqa: E501

        :return: The civic_address_override of this XiqFtmSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._civic_address_override

    @civic_address_override.setter
    def civic_address_override(self, civic_address_override):
        """Sets the civic_address_override of this XiqFtmSettingsRequest.

        Civic Address override.  # noqa: E501

        :param civic_address_override: The civic_address_override of this XiqFtmSettingsRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and civic_address_override is None:  # noqa: E501
            raise ValueError("Invalid value for `civic_address_override`, must not be `None`")  # noqa: E501

        self._civic_address_override = civic_address_override

    @property
    def civic_address(self):
        """Gets the civic_address of this XiqFtmSettingsRequest.  # noqa: E501

        Civic Address as hex encoded RFC4776 formatted string.  # noqa: E501

        :return: The civic_address of this XiqFtmSettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._civic_address

    @civic_address.setter
    def civic_address(self, civic_address):
        """Sets the civic_address of this XiqFtmSettingsRequest.

        Civic Address as hex encoded RFC4776 formatted string.  # noqa: E501

        :param civic_address: The civic_address of this XiqFtmSettingsRequest.  # noqa: E501
        :type: str
        """

        self._civic_address = civic_address

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
        if not isinstance(other, XiqFtmSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqFtmSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
