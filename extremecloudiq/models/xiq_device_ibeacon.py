# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceIbeacon(object):
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
        'device_id': 'int',
        'enabled': 'bool',
        'major': 'int',
        'minor': 'int',
        'power': 'int',
        'enable_monitoring': 'bool'
    }

    attribute_map = {
        'device_id': 'device_id',
        'enabled': 'enabled',
        'major': 'major',
        'minor': 'minor',
        'power': 'power',
        'enable_monitoring': 'enable_monitoring'
    }

    def __init__(self, device_id=None, enabled=None, major=None, minor=None, power=None, enable_monitoring=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceIbeacon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._enabled = None
        self._major = None
        self._minor = None
        self._power = None
        self._enable_monitoring = None
        self.discriminator = None

        self.device_id = device_id
        if enabled is not None:
            self.enabled = enabled
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if power is not None:
            self.power = power
        if enable_monitoring is not None:
            self.enable_monitoring = enable_monitoring

    @property
    def device_id(self):
        """Gets the device_id of this XiqDeviceIbeacon.  # noqa: E501

        The device ID.  # noqa: E501

        :return: The device_id of this XiqDeviceIbeacon.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqDeviceIbeacon.

        The device ID.  # noqa: E501

        :param device_id: The device_id of this XiqDeviceIbeacon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def enabled(self):
        """Gets the enabled of this XiqDeviceIbeacon.  # noqa: E501

        Whether the device beacon is enabled.  # noqa: E501

        :return: The enabled of this XiqDeviceIbeacon.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this XiqDeviceIbeacon.

        Whether the device beacon is enabled.  # noqa: E501

        :param enabled: The enabled of this XiqDeviceIbeacon.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def major(self):
        """Gets the major of this XiqDeviceIbeacon.  # noqa: E501

        Identification of a subset of beacons in a geographical venue.  # noqa: E501

        :return: The major of this XiqDeviceIbeacon.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this XiqDeviceIbeacon.

        Identification of a subset of beacons in a geographical venue.  # noqa: E501

        :param major: The major of this XiqDeviceIbeacon.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                major is not None and major > 65635):  # noqa: E501
            raise ValueError("Invalid value for `major`, must be a value less than or equal to `65635`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                major is not None and major < 0):  # noqa: E501
            raise ValueError("Invalid value for `major`, must be a value greater than or equal to `0`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this XiqDeviceIbeacon.  # noqa: E501

        Identification of a beacon in a specific location.  # noqa: E501

        :return: The minor of this XiqDeviceIbeacon.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this XiqDeviceIbeacon.

        Identification of a beacon in a specific location.  # noqa: E501

        :param minor: The minor of this XiqDeviceIbeacon.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                minor is not None and minor > 65635):  # noqa: E501
            raise ValueError("Invalid value for `minor`, must be a value less than or equal to `65635`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                minor is not None and minor < 0):  # noqa: E501
            raise ValueError("Invalid value for `minor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._minor = minor

    @property
    def power(self):
        """Gets the power of this XiqDeviceIbeacon.  # noqa: E501

        The transmission power in dBm.  # noqa: E501

        :return: The power of this XiqDeviceIbeacon.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this XiqDeviceIbeacon.

        The transmission power in dBm.  # noqa: E501

        :param power: The power of this XiqDeviceIbeacon.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power is not None and power > 127):  # noqa: E501
            raise ValueError("Invalid value for `power`, must be a value less than or equal to `127`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                power is not None and power < -128):  # noqa: E501
            raise ValueError("Invalid value for `power`, must be a value greater than or equal to `-128`")  # noqa: E501

        self._power = power

    @property
    def enable_monitoring(self):
        """Gets the enable_monitoring of this XiqDeviceIbeacon.  # noqa: E501

        Whether iBeacon monitoring is enabled.  # noqa: E501

        :return: The enable_monitoring of this XiqDeviceIbeacon.  # noqa: E501
        :rtype: bool
        """
        return self._enable_monitoring

    @enable_monitoring.setter
    def enable_monitoring(self, enable_monitoring):
        """Sets the enable_monitoring of this XiqDeviceIbeacon.

        Whether iBeacon monitoring is enabled.  # noqa: E501

        :param enable_monitoring: The enable_monitoring of this XiqDeviceIbeacon.  # noqa: E501
        :type: bool
        """

        self._enable_monitoring = enable_monitoring

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
        if not isinstance(other, XiqDeviceIbeacon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceIbeacon):
            return True

        return self.to_dict() != other.to_dict()
