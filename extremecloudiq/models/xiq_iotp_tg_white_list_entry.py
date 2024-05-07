# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqIotpTgWhiteListEntry(object):
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
        'long_eui': 'str',
        'pskd': 'str'
    }

    attribute_map = {
        'long_eui': 'long_eui',
        'pskd': 'pskd'
    }

    def __init__(self, long_eui=None, pskd=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotpTgWhiteListEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._long_eui = None
        self._pskd = None
        self.discriminator = None

        self.long_eui = long_eui
        self.pskd = pskd

    @property
    def long_eui(self):
        """Gets the long_eui of this XiqIotpTgWhiteListEntry.  # noqa: E501

        The factory-assigned IEEE EUI-64. (16 hex digits) or * to match any joiner. FFFFFFFFFFFFFFFF is reserved.  # noqa: E501

        :return: The long_eui of this XiqIotpTgWhiteListEntry.  # noqa: E501
        :rtype: str
        """
        return self._long_eui

    @long_eui.setter
    def long_eui(self, long_eui):
        """Sets the long_eui of this XiqIotpTgWhiteListEntry.

        The factory-assigned IEEE EUI-64. (16 hex digits) or * to match any joiner. FFFFFFFFFFFFFFFF is reserved.  # noqa: E501

        :param long_eui: The long_eui of this XiqIotpTgWhiteListEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and long_eui is None:  # noqa: E501
            raise ValueError("Invalid value for `long_eui`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                long_eui is not None and not re.search(r'^([*]|[0-9a-fA-F]{16})$', long_eui)):  # noqa: E501
            raise ValueError(r"Invalid value for `long_eui`, must be a follow pattern or equal to `/^([*]|[0-9a-fA-F]{16})$/`")  # noqa: E501

        self._long_eui = long_eui

    @property
    def pskd(self):
        """Gets the pskd of this XiqIotpTgWhiteListEntry.  # noqa: E501

        The PSKd (Pre-Shared-Key for the Device) is the Joining Device Credential encoded using base32-thread.  A Joining Device Credential is encoded as uppercase, alphanumeric characters (base32-thread: 0-9,A-Y excluding I,O,Q, and Z for readability)  with a minimum length of 6 such characters and a maximum length of 32 such characters.  # noqa: E501

        :return: The pskd of this XiqIotpTgWhiteListEntry.  # noqa: E501
        :rtype: str
        """
        return self._pskd

    @pskd.setter
    def pskd(self, pskd):
        """Sets the pskd of this XiqIotpTgWhiteListEntry.

        The PSKd (Pre-Shared-Key for the Device) is the Joining Device Credential encoded using base32-thread.  A Joining Device Credential is encoded as uppercase, alphanumeric characters (base32-thread: 0-9,A-Y excluding I,O,Q, and Z for readability)  with a minimum length of 6 such characters and a maximum length of 32 such characters.  # noqa: E501

        :param pskd: The pskd of this XiqIotpTgWhiteListEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pskd is None:  # noqa: E501
            raise ValueError("Invalid value for `pskd`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pskd is not None and len(pskd) > 32):
            raise ValueError("Invalid value for `pskd`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pskd is not None and len(pskd) < 6):
            raise ValueError("Invalid value for `pskd`, length must be greater than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pskd is not None and not re.search(r'^[0-9ABCDEFGHJKLMNPRSTUVWXY]+$', pskd)):  # noqa: E501
            raise ValueError(r"Invalid value for `pskd`, must be a follow pattern or equal to `/^[0-9ABCDEFGHJKLMNPRSTUVWXY]+$/`")  # noqa: E501

        self._pskd = pskd

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
        if not isinstance(other, XiqIotpTgWhiteListEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotpTgWhiteListEntry):
            return True

        return self.to_dict() != other.to_dict()
