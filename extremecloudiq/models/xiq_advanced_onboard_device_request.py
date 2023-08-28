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


class XiqAdvancedOnboardDeviceRequest(object):
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
        'extreme': 'list[XiqExtremeDevice]',
        'exos': 'list[XiqExosDevice]',
        'voss': 'list[XiqVossDevice]',
        'wing': 'list[XiqWingDevice]',
        'dell': 'list[XiqDellDevice]',
        'dt': 'list[XiqDigitalTwinOnboardDevice]',
        'unmanaged': 'bool'
    }

    attribute_map = {
        'extreme': 'extreme',
        'exos': 'exos',
        'voss': 'voss',
        'wing': 'wing',
        'dell': 'dell',
        'dt': 'dt',
        'unmanaged': 'unmanaged'
    }

    def __init__(self, extreme=None, exos=None, voss=None, wing=None, dell=None, dt=None, unmanaged=None, local_vars_configuration=None):  # noqa: E501
        """XiqAdvancedOnboardDeviceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._extreme = None
        self._exos = None
        self._voss = None
        self._wing = None
        self._dell = None
        self._dt = None
        self._unmanaged = None
        self.discriminator = None

        if extreme is not None:
            self.extreme = extreme
        if exos is not None:
            self.exos = exos
        if voss is not None:
            self.voss = voss
        if wing is not None:
            self.wing = wing
        if dell is not None:
            self.dell = dell
        if dt is not None:
            self.dt = dt
        if unmanaged is not None:
            self.unmanaged = unmanaged

    @property
    def extreme(self):
        """Gets the extreme of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        The selected target devices  # noqa: E501

        :return: The extreme of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: list[XiqExtremeDevice]
        """
        return self._extreme

    @extreme.setter
    def extreme(self, extreme):
        """Sets the extreme of this XiqAdvancedOnboardDeviceRequest.

        The selected target devices  # noqa: E501

        :param extreme: The extreme of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: list[XiqExtremeDevice]
        """

        self._extreme = extreme

    @property
    def exos(self):
        """Gets the exos of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        The selected target devices  # noqa: E501

        :return: The exos of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: list[XiqExosDevice]
        """
        return self._exos

    @exos.setter
    def exos(self, exos):
        """Sets the exos of this XiqAdvancedOnboardDeviceRequest.

        The selected target devices  # noqa: E501

        :param exos: The exos of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: list[XiqExosDevice]
        """

        self._exos = exos

    @property
    def voss(self):
        """Gets the voss of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        The selected target devices  # noqa: E501

        :return: The voss of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: list[XiqVossDevice]
        """
        return self._voss

    @voss.setter
    def voss(self, voss):
        """Sets the voss of this XiqAdvancedOnboardDeviceRequest.

        The selected target devices  # noqa: E501

        :param voss: The voss of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: list[XiqVossDevice]
        """

        self._voss = voss

    @property
    def wing(self):
        """Gets the wing of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        The selected target devices  # noqa: E501

        :return: The wing of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: list[XiqWingDevice]
        """
        return self._wing

    @wing.setter
    def wing(self, wing):
        """Sets the wing of this XiqAdvancedOnboardDeviceRequest.

        The selected target devices  # noqa: E501

        :param wing: The wing of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: list[XiqWingDevice]
        """

        self._wing = wing

    @property
    def dell(self):
        """Gets the dell of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        The selected target devices  # noqa: E501

        :return: The dell of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: list[XiqDellDevice]
        """
        return self._dell

    @dell.setter
    def dell(self, dell):
        """Sets the dell of this XiqAdvancedOnboardDeviceRequest.

        The selected target devices  # noqa: E501

        :param dell: The dell of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: list[XiqDellDevice]
        """

        self._dell = dell

    @property
    def dt(self):
        """Gets the dt of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        The selected target devices  # noqa: E501

        :return: The dt of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: list[XiqDigitalTwinOnboardDevice]
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """Sets the dt of this XiqAdvancedOnboardDeviceRequest.

        The selected target devices  # noqa: E501

        :param dt: The dt of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: list[XiqDigitalTwinOnboardDevice]
        """

        self._dt = dt

    @property
    def unmanaged(self):
        """Gets the unmanaged of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501

        Whether to unmanage the devices  # noqa: E501

        :return: The unmanaged of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unmanaged

    @unmanaged.setter
    def unmanaged(self, unmanaged):
        """Sets the unmanaged of this XiqAdvancedOnboardDeviceRequest.

        Whether to unmanage the devices  # noqa: E501

        :param unmanaged: The unmanaged of this XiqAdvancedOnboardDeviceRequest.  # noqa: E501
        :type: bool
        """

        self._unmanaged = unmanaged

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
        if not isinstance(other, XiqAdvancedOnboardDeviceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAdvancedOnboardDeviceRequest):
            return True

        return self.to_dict() != other.to_dict()
