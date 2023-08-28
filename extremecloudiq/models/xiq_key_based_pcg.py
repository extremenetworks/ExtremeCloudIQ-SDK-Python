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


class XiqKeyBasedPcg(object):
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
        'policy_id': 'int',
        'policy_name': 'str',
        'ssid_name': 'str',
        'enabled': 'bool',
        'users': 'list[XiqKeyBasedPcgUser]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'ssid_name': 'ssid_name',
        'enabled': 'enabled',
        'users': 'users'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, policy_id=None, policy_name=None, ssid_name=None, enabled=None, users=None, local_vars_configuration=None):  # noqa: E501
        """XiqKeyBasedPcg - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._policy_id = None
        self._policy_name = None
        self._ssid_name = None
        self._enabled = None
        self._users = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.ssid_name = ssid_name
        self.enabled = enabled
        if users is not None:
            self.users = users

    @property
    def id(self):
        """Gets the id of this XiqKeyBasedPcg.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqKeyBasedPcg.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqKeyBasedPcg.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqKeyBasedPcg.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqKeyBasedPcg.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqKeyBasedPcg.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqKeyBasedPcg.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqKeyBasedPcg.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqKeyBasedPcg.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqKeyBasedPcg.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqKeyBasedPcg.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqKeyBasedPcg.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def policy_id(self):
        """Gets the policy_id of this XiqKeyBasedPcg.  # noqa: E501

        The network policy ID  # noqa: E501

        :return: The policy_id of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this XiqKeyBasedPcg.

        The network policy ID  # noqa: E501

        :param policy_id: The policy_id of this XiqKeyBasedPcg.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and policy_id is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_id`, must not be `None`")  # noqa: E501

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this XiqKeyBasedPcg.  # noqa: E501

        The network policy name  # noqa: E501

        :return: The policy_name of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this XiqKeyBasedPcg.

        The network policy name  # noqa: E501

        :param policy_name: The policy_name of this XiqKeyBasedPcg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and policy_name is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501

        self._policy_name = policy_name

    @property
    def ssid_name(self):
        """Gets the ssid_name of this XiqKeyBasedPcg.  # noqa: E501

        The SSID name  # noqa: E501

        :return: The ssid_name of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: str
        """
        return self._ssid_name

    @ssid_name.setter
    def ssid_name(self, ssid_name):
        """Sets the ssid_name of this XiqKeyBasedPcg.

        The SSID name  # noqa: E501

        :param ssid_name: The ssid_name of this XiqKeyBasedPcg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ssid_name is None:  # noqa: E501
            raise ValueError("Invalid value for `ssid_name`, must not be `None`")  # noqa: E501

        self._ssid_name = ssid_name

    @property
    def enabled(self):
        """Gets the enabled of this XiqKeyBasedPcg.  # noqa: E501

        Enabled Key Based PCG  # noqa: E501

        :return: The enabled of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this XiqKeyBasedPcg.

        Enabled Key Based PCG  # noqa: E501

        :param enabled: The enabled of this XiqKeyBasedPcg.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def users(self):
        """Gets the users of this XiqKeyBasedPcg.  # noqa: E501

        The XIQ key based PCG users  # noqa: E501

        :return: The users of this XiqKeyBasedPcg.  # noqa: E501
        :rtype: list[XiqKeyBasedPcgUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this XiqKeyBasedPcg.

        The XIQ key based PCG users  # noqa: E501

        :param users: The users of this XiqKeyBasedPcg.  # noqa: E501
        :type: list[XiqKeyBasedPcgUser]
        """

        self._users = users

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
        if not isinstance(other, XiqKeyBasedPcg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqKeyBasedPcg):
            return True

        return self.to_dict() != other.to_dict()
