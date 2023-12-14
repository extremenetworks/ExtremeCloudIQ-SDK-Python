# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqExternalUser(object):
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
        'login_name': 'str',
        'user_role': 'XiqUserRole',
        'org_id': 'int',
        'location_ids': 'list[int]',
        'grantee_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'login_name': 'login_name',
        'user_role': 'user_role',
        'org_id': 'org_id',
        'location_ids': 'location_ids',
        'grantee_id': 'grantee_id'
    }

    def __init__(self, id=None, create_time=None, update_time=None, login_name=None, user_role=None, org_id=None, location_ids=None, grantee_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqExternalUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._login_name = None
        self._user_role = None
        self._org_id = None
        self._location_ids = None
        self._grantee_id = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.login_name = login_name
        self.user_role = user_role
        if org_id is not None:
            self.org_id = org_id
        if location_ids is not None:
            self.location_ids = location_ids
        if grantee_id is not None:
            self.grantee_id = grantee_id

    @property
    def id(self):
        """Gets the id of this XiqExternalUser.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqExternalUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqExternalUser.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqExternalUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqExternalUser.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqExternalUser.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqExternalUser.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqExternalUser.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqExternalUser.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqExternalUser.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqExternalUser.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqExternalUser.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def login_name(self):
        """Gets the login_name of this XiqExternalUser.  # noqa: E501

        Login name, i.e. username or login Email  # noqa: E501

        :return: The login_name of this XiqExternalUser.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this XiqExternalUser.

        Login name, i.e. username or login Email  # noqa: E501

        :param login_name: The login_name of this XiqExternalUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and login_name is None:  # noqa: E501
            raise ValueError("Invalid value for `login_name`, must not be `None`")  # noqa: E501

        self._login_name = login_name

    @property
    def user_role(self):
        """Gets the user_role of this XiqExternalUser.  # noqa: E501


        :return: The user_role of this XiqExternalUser.  # noqa: E501
        :rtype: XiqUserRole
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this XiqExternalUser.


        :param user_role: The user_role of this XiqExternalUser.  # noqa: E501
        :type: XiqUserRole
        """
        if self.local_vars_configuration.client_side_validation and user_role is None:  # noqa: E501
            raise ValueError("Invalid value for `user_role`, must not be `None`")  # noqa: E501

        self._user_role = user_role

    @property
    def org_id(self):
        """Gets the org_id of this XiqExternalUser.  # noqa: E501

        The HIQ organization ID if it is HIQ user.  # noqa: E501

        :return: The org_id of this XiqExternalUser.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqExternalUser.

        The HIQ organization ID if it is HIQ user.  # noqa: E501

        :param org_id: The org_id of this XiqExternalUser.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def location_ids(self):
        """Gets the location_ids of this XiqExternalUser.  # noqa: E501

        The assigned location IDs.  # noqa: E501

        :return: The location_ids of this XiqExternalUser.  # noqa: E501
        :rtype: list[int]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """Sets the location_ids of this XiqExternalUser.

        The assigned location IDs.  # noqa: E501

        :param location_ids: The location_ids of this XiqExternalUser.  # noqa: E501
        :type: list[int]
        """

        self._location_ids = location_ids

    @property
    def grantee_id(self):
        """Gets the grantee_id of this XiqExternalUser.  # noqa: E501

        The home VIQ user ID of external user.  # noqa: E501

        :return: The grantee_id of this XiqExternalUser.  # noqa: E501
        :rtype: int
        """
        return self._grantee_id

    @grantee_id.setter
    def grantee_id(self, grantee_id):
        """Sets the grantee_id of this XiqExternalUser.

        The home VIQ user ID of external user.  # noqa: E501

        :param grantee_id: The grantee_id of this XiqExternalUser.  # noqa: E501
        :type: int
        """

        self._grantee_id = grantee_id

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
        if not isinstance(other, XiqExternalUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExternalUser):
            return True

        return self.to_dict() != other.to_dict()
