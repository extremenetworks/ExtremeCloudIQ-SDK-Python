# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqPcgPortAssignmentEntry(object):
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
        'device_id': 'int',
        'eth1_user_id': 'int',
        'eth2_user_id': 'int',
        'eth3_user_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'device_id': 'device_id',
        'eth1_user_id': 'eth1_user_id',
        'eth2_user_id': 'eth2_user_id',
        'eth3_user_id': 'eth3_user_id'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, device_id=None, eth1_user_id=None, eth2_user_id=None, eth3_user_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqPcgPortAssignmentEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._device_id = None
        self._eth1_user_id = None
        self._eth2_user_id = None
        self._eth3_user_id = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.device_id = device_id
        if eth1_user_id is not None:
            self.eth1_user_id = eth1_user_id
        if eth2_user_id is not None:
            self.eth2_user_id = eth2_user_id
        if eth3_user_id is not None:
            self.eth3_user_id = eth3_user_id

    @property
    def id(self):
        """Gets the id of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqPcgPortAssignmentEntry.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqPcgPortAssignmentEntry.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqPcgPortAssignmentEntry.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqPcgPortAssignmentEntry.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def device_id(self):
        """Gets the device_id of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The device ID of AP150W  # noqa: E501

        :return: The device_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqPcgPortAssignmentEntry.

        The device ID of AP150W  # noqa: E501

        :param device_id: The device_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def eth1_user_id(self):
        """Gets the eth1_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The eth1 user ID, get available users from \"/pcgs/key-based/network-policy-{policyId}/users\"  # noqa: E501

        :return: The eth1_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._eth1_user_id

    @eth1_user_id.setter
    def eth1_user_id(self, eth1_user_id):
        """Sets the eth1_user_id of this XiqPcgPortAssignmentEntry.

        The eth1 user ID, get available users from \"/pcgs/key-based/network-policy-{policyId}/users\"  # noqa: E501

        :param eth1_user_id: The eth1_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: int
        """

        self._eth1_user_id = eth1_user_id

    @property
    def eth2_user_id(self):
        """Gets the eth2_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The eth2 user ID, get available users from \"/pcgs/key-based/network-policy-{policyId}/users\"  # noqa: E501

        :return: The eth2_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._eth2_user_id

    @eth2_user_id.setter
    def eth2_user_id(self, eth2_user_id):
        """Sets the eth2_user_id of this XiqPcgPortAssignmentEntry.

        The eth2 user ID, get available users from \"/pcgs/key-based/network-policy-{policyId}/users\"  # noqa: E501

        :param eth2_user_id: The eth2_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: int
        """

        self._eth2_user_id = eth2_user_id

    @property
    def eth3_user_id(self):
        """Gets the eth3_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501

        The eth3 user ID, get available users from \"/pcgs/key-based/network-policy-{policyId}/users\"  # noqa: E501

        :return: The eth3_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._eth3_user_id

    @eth3_user_id.setter
    def eth3_user_id(self, eth3_user_id):
        """Sets the eth3_user_id of this XiqPcgPortAssignmentEntry.

        The eth3 user ID, get available users from \"/pcgs/key-based/network-policy-{policyId}/users\"  # noqa: E501

        :param eth3_user_id: The eth3_user_id of this XiqPcgPortAssignmentEntry.  # noqa: E501
        :type: int
        """

        self._eth3_user_id = eth3_user_id

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
        if not isinstance(other, XiqPcgPortAssignmentEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPcgPortAssignmentEntry):
            return True

        return self.to_dict() != other.to_dict()
