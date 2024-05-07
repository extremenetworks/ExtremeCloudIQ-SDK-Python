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


class XiqPcgPortAssignmentEntryDeviceMeta(object):
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
        'id': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'org_id': 'int',
        'mac_address': 'str',
        'serial_number': 'str',
        'product_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'mac_address': 'mac_address',
        'serial_number': 'serial_number',
        'product_type': 'product_type'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, mac_address=None, serial_number=None, product_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqPcgPortAssignmentEntryDeviceMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._mac_address = None
        self._serial_number = None
        self._product_type = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.mac_address = mac_address
        self.serial_number = serial_number
        self.product_type = product_type

    @property
    def id(self):
        """Gets the id of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqPcgPortAssignmentEntryDeviceMeta.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqPcgPortAssignmentEntryDeviceMeta.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqPcgPortAssignmentEntryDeviceMeta.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqPcgPortAssignmentEntryDeviceMeta.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The mac address  # noqa: E501

        :return: The mac_address of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqPcgPortAssignmentEntryDeviceMeta.

        The mac address  # noqa: E501

        :param mac_address: The mac_address of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mac_address is None:  # noqa: E501
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def serial_number(self):
        """Gets the serial_number of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The serial number  # noqa: E501

        :return: The serial_number of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XiqPcgPortAssignmentEntryDeviceMeta.

        The serial number  # noqa: E501

        :param serial_number: The serial_number of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial_number is None:  # noqa: E501
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def product_type(self):
        """Gets the product_type of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501

        The product type  # noqa: E501

        :return: The product_type of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this XiqPcgPortAssignmentEntryDeviceMeta.

        The product type  # noqa: E501

        :param product_type: The product_type of this XiqPcgPortAssignmentEntryDeviceMeta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and product_type is None:  # noqa: E501
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

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
        if not isinstance(other, XiqPcgPortAssignmentEntryDeviceMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPcgPortAssignmentEntryDeviceMeta):
            return True

        return self.to_dict() != other.to_dict()
