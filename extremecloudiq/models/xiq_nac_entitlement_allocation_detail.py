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


class XiqNacEntitlementAllocationDetail(object):
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
        'owner_id': 'int',
        'serial_no': 'str',
        'display_name': 'str',
        'percentage': 'float',
        'allocated_devices': 'int'
    }

    attribute_map = {
        'owner_id': 'owner_id',
        'serial_no': 'serial_no',
        'display_name': 'display_name',
        'percentage': 'percentage',
        'allocated_devices': 'allocated_devices'
    }

    def __init__(self, owner_id=None, serial_no=None, display_name=None, percentage=None, allocated_devices=None, local_vars_configuration=None):  # noqa: E501
        """XiqNacEntitlementAllocationDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_id = None
        self._serial_no = None
        self._display_name = None
        self._percentage = None
        self._allocated_devices = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if serial_no is not None:
            self.serial_no = serial_no
        if display_name is not None:
            self.display_name = display_name
        if percentage is not None:
            self.percentage = percentage
        if allocated_devices is not None:
            self.allocated_devices = allocated_devices

    @property
    def owner_id(self):
        """Gets the owner_id of this XiqNacEntitlementAllocationDetail.  # noqa: E501

        Owner Id  # noqa: E501

        :return: The owner_id of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this XiqNacEntitlementAllocationDetail.

        Owner Id  # noqa: E501

        :param owner_id: The owner_id of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def serial_no(self):
        """Gets the serial_no of this XiqNacEntitlementAllocationDetail.  # noqa: E501

        Serial number  # noqa: E501

        :return: The serial_no of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :rtype: str
        """
        return self._serial_no

    @serial_no.setter
    def serial_no(self, serial_no):
        """Sets the serial_no of this XiqNacEntitlementAllocationDetail.

        Serial number  # noqa: E501

        :param serial_no: The serial_no of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :type: str
        """

        self._serial_no = serial_no

    @property
    def display_name(self):
        """Gets the display_name of this XiqNacEntitlementAllocationDetail.  # noqa: E501

        Display name  # noqa: E501

        :return: The display_name of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this XiqNacEntitlementAllocationDetail.

        Display name  # noqa: E501

        :param display_name: The display_name of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def percentage(self):
        """Gets the percentage of this XiqNacEntitlementAllocationDetail.  # noqa: E501

        Allocated percentage  # noqa: E501

        :return: The percentage of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this XiqNacEntitlementAllocationDetail.

        Allocated percentage  # noqa: E501

        :param percentage: The percentage of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def allocated_devices(self):
        """Gets the allocated_devices of this XiqNacEntitlementAllocationDetail.  # noqa: E501

        Allocated device count  # noqa: E501

        :return: The allocated_devices of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :rtype: int
        """
        return self._allocated_devices

    @allocated_devices.setter
    def allocated_devices(self, allocated_devices):
        """Sets the allocated_devices of this XiqNacEntitlementAllocationDetail.

        Allocated device count  # noqa: E501

        :param allocated_devices: The allocated_devices of this XiqNacEntitlementAllocationDetail.  # noqa: E501
        :type: int
        """

        self._allocated_devices = allocated_devices

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
        if not isinstance(other, XiqNacEntitlementAllocationDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqNacEntitlementAllocationDetail):
            return True

        return self.to_dict() != other.to_dict()
