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


class XiqUserProfileAssignment(object):
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
        'name': 'str',
        'description': 'str',
        'authorisation_policy': 'str',
        'folder_ids': 'list[int]',
        'assignment_radius_attribute': 'XiqUserProfileAssignmentRadiusAttribute',
        'user_group': 'list[XiqUserGroup]',
        'mac_object_profiles': 'list[XiqMacObject]',
        'os_object_dhcp': 'list[XiqOsObject]',
        'os_object_https': 'list[XiqOsObject]',
        'schedules': 'list[XiqSchedule]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'authorisation_policy': 'authorisation_policy',
        'folder_ids': 'folder_ids',
        'assignment_radius_attribute': 'assignment_radius_attribute',
        'user_group': 'user_group',
        'mac_object_profiles': 'mac_object_profiles',
        'os_object_dhcp': 'os_object_dhcp',
        'os_object_https': 'os_object_https',
        'schedules': 'schedules'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, authorisation_policy=None, folder_ids=None, assignment_radius_attribute=None, user_group=None, mac_object_profiles=None, os_object_dhcp=None, os_object_https=None, schedules=None, local_vars_configuration=None):  # noqa: E501
        """XiqUserProfileAssignment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._authorisation_policy = None
        self._folder_ids = None
        self._assignment_radius_attribute = None
        self._user_group = None
        self._mac_object_profiles = None
        self._os_object_dhcp = None
        self._os_object_https = None
        self._schedules = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if authorisation_policy is not None:
            self.authorisation_policy = authorisation_policy
        if folder_ids is not None:
            self.folder_ids = folder_ids
        if assignment_radius_attribute is not None:
            self.assignment_radius_attribute = assignment_radius_attribute
        if user_group is not None:
            self.user_group = user_group
        if mac_object_profiles is not None:
            self.mac_object_profiles = mac_object_profiles
        if os_object_dhcp is not None:
            self.os_object_dhcp = os_object_dhcp
        if os_object_https is not None:
            self.os_object_https = os_object_https
        if schedules is not None:
            self.schedules = schedules

    @property
    def id(self):
        """Gets the id of this XiqUserProfileAssignment.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqUserProfileAssignment.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqUserProfileAssignment.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqUserProfileAssignment.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqUserProfileAssignment.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqUserProfileAssignment.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqUserProfileAssignment.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqUserProfileAssignment.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqUserProfileAssignment.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqUserProfileAssignment.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqUserProfileAssignment.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqUserProfileAssignment.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqUserProfileAssignment.  # noqa: E501

        The user profile name  # noqa: E501

        :return: The name of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUserProfileAssignment.

        The user profile name  # noqa: E501

        :param name: The name of this XiqUserProfileAssignment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUserProfileAssignment.  # noqa: E501

        The user profile assignment description  # noqa: E501

        :return: The description of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUserProfileAssignment.

        The user profile assignment description  # noqa: E501

        :param description: The description of this XiqUserProfileAssignment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def authorisation_policy(self):
        """Gets the authorisation_policy of this XiqUserProfileAssignment.  # noqa: E501

        The Authorization policy name  # noqa: E501

        :return: The authorisation_policy of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_policy

    @authorisation_policy.setter
    def authorisation_policy(self, authorisation_policy):
        """Sets the authorisation_policy of this XiqUserProfileAssignment.

        The Authorization policy name  # noqa: E501

        :param authorisation_policy: The authorisation_policy of this XiqUserProfileAssignment.  # noqa: E501
        :type: str
        """

        self._authorisation_policy = authorisation_policy

    @property
    def folder_ids(self):
        """Gets the folder_ids of this XiqUserProfileAssignment.  # noqa: E501

        The location folder Id list  # noqa: E501

        :return: The folder_ids of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: list[int]
        """
        return self._folder_ids

    @folder_ids.setter
    def folder_ids(self, folder_ids):
        """Sets the folder_ids of this XiqUserProfileAssignment.

        The location folder Id list  # noqa: E501

        :param folder_ids: The folder_ids of this XiqUserProfileAssignment.  # noqa: E501
        :type: list[int]
        """

        self._folder_ids = folder_ids

    @property
    def assignment_radius_attribute(self):
        """Gets the assignment_radius_attribute of this XiqUserProfileAssignment.  # noqa: E501


        :return: The assignment_radius_attribute of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: XiqUserProfileAssignmentRadiusAttribute
        """
        return self._assignment_radius_attribute

    @assignment_radius_attribute.setter
    def assignment_radius_attribute(self, assignment_radius_attribute):
        """Sets the assignment_radius_attribute of this XiqUserProfileAssignment.


        :param assignment_radius_attribute: The assignment_radius_attribute of this XiqUserProfileAssignment.  # noqa: E501
        :type: XiqUserProfileAssignmentRadiusAttribute
        """

        self._assignment_radius_attribute = assignment_radius_attribute

    @property
    def user_group(self):
        """Gets the user_group of this XiqUserProfileAssignment.  # noqa: E501

        The set of User groups.  # noqa: E501

        :return: The user_group of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: list[XiqUserGroup]
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this XiqUserProfileAssignment.

        The set of User groups.  # noqa: E501

        :param user_group: The user_group of this XiqUserProfileAssignment.  # noqa: E501
        :type: list[XiqUserGroup]
        """

        self._user_group = user_group

    @property
    def mac_object_profiles(self):
        """Gets the mac_object_profiles of this XiqUserProfileAssignment.  # noqa: E501

        The set of Mac object profiles.  # noqa: E501

        :return: The mac_object_profiles of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: list[XiqMacObject]
        """
        return self._mac_object_profiles

    @mac_object_profiles.setter
    def mac_object_profiles(self, mac_object_profiles):
        """Sets the mac_object_profiles of this XiqUserProfileAssignment.

        The set of Mac object profiles.  # noqa: E501

        :param mac_object_profiles: The mac_object_profiles of this XiqUserProfileAssignment.  # noqa: E501
        :type: list[XiqMacObject]
        """

        self._mac_object_profiles = mac_object_profiles

    @property
    def os_object_dhcp(self):
        """Gets the os_object_dhcp of this XiqUserProfileAssignment.  # noqa: E501

        The set of OS DHCP objects.  # noqa: E501

        :return: The os_object_dhcp of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: list[XiqOsObject]
        """
        return self._os_object_dhcp

    @os_object_dhcp.setter
    def os_object_dhcp(self, os_object_dhcp):
        """Sets the os_object_dhcp of this XiqUserProfileAssignment.

        The set of OS DHCP objects.  # noqa: E501

        :param os_object_dhcp: The os_object_dhcp of this XiqUserProfileAssignment.  # noqa: E501
        :type: list[XiqOsObject]
        """

        self._os_object_dhcp = os_object_dhcp

    @property
    def os_object_https(self):
        """Gets the os_object_https of this XiqUserProfileAssignment.  # noqa: E501

        The set of OS HTTP objects.  # noqa: E501

        :return: The os_object_https of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: list[XiqOsObject]
        """
        return self._os_object_https

    @os_object_https.setter
    def os_object_https(self, os_object_https):
        """Sets the os_object_https of this XiqUserProfileAssignment.

        The set of OS HTTP objects.  # noqa: E501

        :param os_object_https: The os_object_https of this XiqUserProfileAssignment.  # noqa: E501
        :type: list[XiqOsObject]
        """

        self._os_object_https = os_object_https

    @property
    def schedules(self):
        """Gets the schedules of this XiqUserProfileAssignment.  # noqa: E501

        The set of OS HTTP objects.  # noqa: E501

        :return: The schedules of this XiqUserProfileAssignment.  # noqa: E501
        :rtype: list[XiqSchedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this XiqUserProfileAssignment.

        The set of OS HTTP objects.  # noqa: E501

        :param schedules: The schedules of this XiqUserProfileAssignment.  # noqa: E501
        :type: list[XiqSchedule]
        """

        self._schedules = schedules

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
        if not isinstance(other, XiqUserProfileAssignment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUserProfileAssignment):
            return True

        return self.to_dict() != other.to_dict()
