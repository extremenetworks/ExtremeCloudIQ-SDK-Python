# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqSsid(object):
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
        'broadcast_name': 'str',
        'description': 'str',
        'predefined': 'bool',
        'advanced_settings_id': 'int',
        'enable_user_profile_assignment': 'bool',
        'enable_radius_attribute_user_profile_assignment': 'bool',
        'attribute_type': 'XiqAttributeType',
        'attribute_key': 'int',
        'access_security': 'XiqSsidAccessSecurity',
        'radius_client_profile': 'XiqRadiusClientProfile',
        'default_user_profile': 'int',
        'vendor_id': 'int',
        'user_profile_assignment_rules': 'list[XiqUserProfileAssignmentRule]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'broadcast_name': 'broadcast_name',
        'description': 'description',
        'predefined': 'predefined',
        'advanced_settings_id': 'advanced_settings_id',
        'enable_user_profile_assignment': 'enable_user_profile_assignment',
        'enable_radius_attribute_user_profile_assignment': 'enable_radius_attribute_user_profile_assignment',
        'attribute_type': 'attribute_type',
        'attribute_key': 'attribute_key',
        'access_security': 'access_security',
        'radius_client_profile': 'radius_client_profile',
        'default_user_profile': 'default_user_profile',
        'vendor_id': 'vendor_id',
        'user_profile_assignment_rules': 'user_profile_assignment_rules'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, broadcast_name=None, description=None, predefined=None, advanced_settings_id=None, enable_user_profile_assignment=None, enable_radius_attribute_user_profile_assignment=None, attribute_type=None, attribute_key=None, access_security=None, radius_client_profile=None, default_user_profile=None, vendor_id=None, user_profile_assignment_rules=None, local_vars_configuration=None):  # noqa: E501
        """XiqSsid - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._broadcast_name = None
        self._description = None
        self._predefined = None
        self._advanced_settings_id = None
        self._enable_user_profile_assignment = None
        self._enable_radius_attribute_user_profile_assignment = None
        self._attribute_type = None
        self._attribute_key = None
        self._access_security = None
        self._radius_client_profile = None
        self._default_user_profile = None
        self._vendor_id = None
        self._user_profile_assignment_rules = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.name = name
        self.broadcast_name = broadcast_name
        if description is not None:
            self.description = description
        self.predefined = predefined
        if advanced_settings_id is not None:
            self.advanced_settings_id = advanced_settings_id
        if enable_user_profile_assignment is not None:
            self.enable_user_profile_assignment = enable_user_profile_assignment
        if enable_radius_attribute_user_profile_assignment is not None:
            self.enable_radius_attribute_user_profile_assignment = enable_radius_attribute_user_profile_assignment
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if attribute_key is not None:
            self.attribute_key = attribute_key
        if access_security is not None:
            self.access_security = access_security
        if radius_client_profile is not None:
            self.radius_client_profile = radius_client_profile
        if default_user_profile is not None:
            self.default_user_profile = default_user_profile
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if user_profile_assignment_rules is not None:
            self.user_profile_assignment_rules = user_profile_assignment_rules

    @property
    def id(self):
        """Gets the id of this XiqSsid.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqSsid.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqSsid.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqSsid.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqSsid.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqSsid.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqSsid.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqSsid.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqSsid.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqSsid.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqSsid.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqSsid.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqSsid.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqSsid.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqSsid.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqSsid.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqSsid.  # noqa: E501

        The SSID profile name  # noqa: E501

        :return: The name of this XiqSsid.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqSsid.

        The SSID profile name  # noqa: E501

        :param name: The name of this XiqSsid.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def broadcast_name(self):
        """Gets the broadcast_name of this XiqSsid.  # noqa: E501

        The SSID broadcast name  # noqa: E501

        :return: The broadcast_name of this XiqSsid.  # noqa: E501
        :rtype: str
        """
        return self._broadcast_name

    @broadcast_name.setter
    def broadcast_name(self, broadcast_name):
        """Sets the broadcast_name of this XiqSsid.

        The SSID broadcast name  # noqa: E501

        :param broadcast_name: The broadcast_name of this XiqSsid.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and broadcast_name is None:  # noqa: E501
            raise ValueError("Invalid value for `broadcast_name`, must not be `None`")  # noqa: E501

        self._broadcast_name = broadcast_name

    @property
    def description(self):
        """Gets the description of this XiqSsid.  # noqa: E501

        The SSID description  # noqa: E501

        :return: The description of this XiqSsid.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqSsid.

        The SSID description  # noqa: E501

        :param description: The description of this XiqSsid.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def predefined(self):
        """Gets the predefined of this XiqSsid.  # noqa: E501

        Whether it is predefined  # noqa: E501

        :return: The predefined of this XiqSsid.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqSsid.

        Whether it is predefined  # noqa: E501

        :param predefined: The predefined of this XiqSsid.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and predefined is None:  # noqa: E501
            raise ValueError("Invalid value for `predefined`, must not be `None`")  # noqa: E501

        self._predefined = predefined

    @property
    def advanced_settings_id(self):
        """Gets the advanced_settings_id of this XiqSsid.  # noqa: E501

        The SSID advanced settings ID.  # noqa: E501

        :return: The advanced_settings_id of this XiqSsid.  # noqa: E501
        :rtype: int
        """
        return self._advanced_settings_id

    @advanced_settings_id.setter
    def advanced_settings_id(self, advanced_settings_id):
        """Sets the advanced_settings_id of this XiqSsid.

        The SSID advanced settings ID.  # noqa: E501

        :param advanced_settings_id: The advanced_settings_id of this XiqSsid.  # noqa: E501
        :type: int
        """

        self._advanced_settings_id = advanced_settings_id

    @property
    def enable_user_profile_assignment(self):
        """Gets the enable_user_profile_assignment of this XiqSsid.  # noqa: E501

        The flag to enable User Profile Assignment.  # noqa: E501

        :return: The enable_user_profile_assignment of this XiqSsid.  # noqa: E501
        :rtype: bool
        """
        return self._enable_user_profile_assignment

    @enable_user_profile_assignment.setter
    def enable_user_profile_assignment(self, enable_user_profile_assignment):
        """Sets the enable_user_profile_assignment of this XiqSsid.

        The flag to enable User Profile Assignment.  # noqa: E501

        :param enable_user_profile_assignment: The enable_user_profile_assignment of this XiqSsid.  # noqa: E501
        :type: bool
        """

        self._enable_user_profile_assignment = enable_user_profile_assignment

    @property
    def enable_radius_attribute_user_profile_assignment(self):
        """Gets the enable_radius_attribute_user_profile_assignment of this XiqSsid.  # noqa: E501

        The flag to enable Radius Attribute User Profile Assignment.  # noqa: E501

        :return: The enable_radius_attribute_user_profile_assignment of this XiqSsid.  # noqa: E501
        :rtype: bool
        """
        return self._enable_radius_attribute_user_profile_assignment

    @enable_radius_attribute_user_profile_assignment.setter
    def enable_radius_attribute_user_profile_assignment(self, enable_radius_attribute_user_profile_assignment):
        """Sets the enable_radius_attribute_user_profile_assignment of this XiqSsid.

        The flag to enable Radius Attribute User Profile Assignment.  # noqa: E501

        :param enable_radius_attribute_user_profile_assignment: The enable_radius_attribute_user_profile_assignment of this XiqSsid.  # noqa: E501
        :type: bool
        """

        self._enable_radius_attribute_user_profile_assignment = enable_radius_attribute_user_profile_assignment

    @property
    def attribute_type(self):
        """Gets the attribute_type of this XiqSsid.  # noqa: E501


        :return: The attribute_type of this XiqSsid.  # noqa: E501
        :rtype: XiqAttributeType
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this XiqSsid.


        :param attribute_type: The attribute_type of this XiqSsid.  # noqa: E501
        :type: XiqAttributeType
        """

        self._attribute_type = attribute_type

    @property
    def attribute_key(self):
        """Gets the attribute_key of this XiqSsid.  # noqa: E501

        The SSID attribute key.  # noqa: E501

        :return: The attribute_key of this XiqSsid.  # noqa: E501
        :rtype: int
        """
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, attribute_key):
        """Sets the attribute_key of this XiqSsid.

        The SSID attribute key.  # noqa: E501

        :param attribute_key: The attribute_key of this XiqSsid.  # noqa: E501
        :type: int
        """

        self._attribute_key = attribute_key

    @property
    def access_security(self):
        """Gets the access_security of this XiqSsid.  # noqa: E501


        :return: The access_security of this XiqSsid.  # noqa: E501
        :rtype: XiqSsidAccessSecurity
        """
        return self._access_security

    @access_security.setter
    def access_security(self, access_security):
        """Sets the access_security of this XiqSsid.


        :param access_security: The access_security of this XiqSsid.  # noqa: E501
        :type: XiqSsidAccessSecurity
        """

        self._access_security = access_security

    @property
    def radius_client_profile(self):
        """Gets the radius_client_profile of this XiqSsid.  # noqa: E501


        :return: The radius_client_profile of this XiqSsid.  # noqa: E501
        :rtype: XiqRadiusClientProfile
        """
        return self._radius_client_profile

    @radius_client_profile.setter
    def radius_client_profile(self, radius_client_profile):
        """Sets the radius_client_profile of this XiqSsid.


        :param radius_client_profile: The radius_client_profile of this XiqSsid.  # noqa: E501
        :type: XiqRadiusClientProfile
        """

        self._radius_client_profile = radius_client_profile

    @property
    def default_user_profile(self):
        """Gets the default_user_profile of this XiqSsid.  # noqa: E501

        The default User Profile ID.  # noqa: E501

        :return: The default_user_profile of this XiqSsid.  # noqa: E501
        :rtype: int
        """
        return self._default_user_profile

    @default_user_profile.setter
    def default_user_profile(self, default_user_profile):
        """Sets the default_user_profile of this XiqSsid.

        The default User Profile ID.  # noqa: E501

        :param default_user_profile: The default_user_profile of this XiqSsid.  # noqa: E501
        :type: int
        """

        self._default_user_profile = default_user_profile

    @property
    def vendor_id(self):
        """Gets the vendor_id of this XiqSsid.  # noqa: E501

        The vendor id, when the Attribute type is CUSTOM.  # noqa: E501

        :return: The vendor_id of this XiqSsid.  # noqa: E501
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this XiqSsid.

        The vendor id, when the Attribute type is CUSTOM.  # noqa: E501

        :param vendor_id: The vendor_id of this XiqSsid.  # noqa: E501
        :type: int
        """

        self._vendor_id = vendor_id

    @property
    def user_profile_assignment_rules(self):
        """Gets the user_profile_assignment_rules of this XiqSsid.  # noqa: E501

        The SSID user profile assignment rules.  # noqa: E501

        :return: The user_profile_assignment_rules of this XiqSsid.  # noqa: E501
        :rtype: list[XiqUserProfileAssignmentRule]
        """
        return self._user_profile_assignment_rules

    @user_profile_assignment_rules.setter
    def user_profile_assignment_rules(self, user_profile_assignment_rules):
        """Sets the user_profile_assignment_rules of this XiqSsid.

        The SSID user profile assignment rules.  # noqa: E501

        :param user_profile_assignment_rules: The user_profile_assignment_rules of this XiqSsid.  # noqa: E501
        :type: list[XiqUserProfileAssignmentRule]
        """

        self._user_profile_assignment_rules = user_profile_assignment_rules

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
        if not isinstance(other, XiqSsid):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSsid):
            return True

        return self.to_dict() != other.to_dict()
