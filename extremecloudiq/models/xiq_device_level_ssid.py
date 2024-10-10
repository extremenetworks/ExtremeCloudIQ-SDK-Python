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


class XiqDeviceLevelSsid(object):
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
        'ssid_id': 'int',
        'ssid': 'str',
        'passphrase': 'str'
    }

    attribute_map = {
        'ssid_id': 'ssid_id',
        'ssid': 'ssid',
        'passphrase': 'passphrase'
    }

    def __init__(self, ssid_id=None, ssid=None, passphrase=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceLevelSsid - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ssid_id = None
        self._ssid = None
        self._passphrase = None
        self.discriminator = None

        self.ssid_id = ssid_id
        if ssid is not None:
            self.ssid = ssid
        if passphrase is not None:
            self.passphrase = passphrase

    @property
    def ssid_id(self):
        """Gets the ssid_id of this XiqDeviceLevelSsid.  # noqa: E501

        The SSID ID to override, cannot be null.  # noqa: E501

        :return: The ssid_id of this XiqDeviceLevelSsid.  # noqa: E501
        :rtype: int
        """
        return self._ssid_id

    @ssid_id.setter
    def ssid_id(self, ssid_id):
        """Sets the ssid_id of this XiqDeviceLevelSsid.

        The SSID ID to override, cannot be null.  # noqa: E501

        :param ssid_id: The ssid_id of this XiqDeviceLevelSsid.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ssid_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ssid_id`, must not be `None`")  # noqa: E501

        self._ssid_id = ssid_id

    @property
    def ssid(self):
        """Gets the ssid of this XiqDeviceLevelSsid.  # noqa: E501

        The broadcast ssid name to override. Can only override if the SSID profile is OPEN or PSK mode.  # noqa: E501

        :return: The ssid of this XiqDeviceLevelSsid.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this XiqDeviceLevelSsid.

        The broadcast ssid name to override. Can only override if the SSID profile is OPEN or PSK mode.  # noqa: E501

        :param ssid: The ssid of this XiqDeviceLevelSsid.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def passphrase(self):
        """Gets the passphrase of this XiqDeviceLevelSsid.  # noqa: E501

        The ssid passphrase to override. Can only override if the SSID profile is in PSK mode.  # noqa: E501

        :return: The passphrase of this XiqDeviceLevelSsid.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this XiqDeviceLevelSsid.

        The ssid passphrase to override. Can only override if the SSID profile is in PSK mode.  # noqa: E501

        :param passphrase: The passphrase of this XiqDeviceLevelSsid.  # noqa: E501
        :type: str
        """

        self._passphrase = passphrase

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
        if not isinstance(other, XiqDeviceLevelSsid):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceLevelSsid):
            return True

        return self.to_dict() != other.to_dict()
