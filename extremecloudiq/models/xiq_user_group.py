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


class XiqUserGroup(object):
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
        'predefined': 'bool',
        'password_db_location': 'XiqPasswordDbLocation',
        'password_type': 'XiqPasswordType',
        'pcg_use_only': 'bool',
        'pcg_type': 'XiqPcgType',
        'ppsk_use_only': 'bool',
        'enable_cwp_reg': 'bool',
        'password_settings': 'XiqPasswordSettings',
        'expiration_settings': 'XiqExpirationSettings',
        'delivery_settings': 'XiqDeliverySettings',
        'user_count': 'int',
        'ssids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'predefined': 'predefined',
        'password_db_location': 'password_db_location',
        'password_type': 'password_type',
        'pcg_use_only': 'pcg_use_only',
        'pcg_type': 'pcg_type',
        'ppsk_use_only': 'ppsk_use_only',
        'enable_cwp_reg': 'enable_cwp_reg',
        'password_settings': 'password_settings',
        'expiration_settings': 'expiration_settings',
        'delivery_settings': 'delivery_settings',
        'user_count': 'user_count',
        'ssids': 'ssids'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, predefined=None, password_db_location=None, password_type=None, pcg_use_only=None, pcg_type=None, ppsk_use_only=None, enable_cwp_reg=None, password_settings=None, expiration_settings=None, delivery_settings=None, user_count=None, ssids=None, local_vars_configuration=None):  # noqa: E501
        """XiqUserGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._predefined = None
        self._password_db_location = None
        self._password_type = None
        self._pcg_use_only = None
        self._pcg_type = None
        self._ppsk_use_only = None
        self._enable_cwp_reg = None
        self._password_settings = None
        self._expiration_settings = None
        self._delivery_settings = None
        self._user_count = None
        self._ssids = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.name = name
        if description is not None:
            self.description = description
        self.predefined = predefined
        self.password_db_location = password_db_location
        self.password_type = password_type
        if pcg_use_only is not None:
            self.pcg_use_only = pcg_use_only
        if pcg_type is not None:
            self.pcg_type = pcg_type
        if ppsk_use_only is not None:
            self.ppsk_use_only = ppsk_use_only
        if enable_cwp_reg is not None:
            self.enable_cwp_reg = enable_cwp_reg
        self.password_settings = password_settings
        self.expiration_settings = expiration_settings
        self.delivery_settings = delivery_settings
        self.user_count = user_count
        self.ssids = ssids

    @property
    def id(self):
        """Gets the id of this XiqUserGroup.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqUserGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqUserGroup.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqUserGroup.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqUserGroup.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqUserGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqUserGroup.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqUserGroup.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqUserGroup.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqUserGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqUserGroup.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqUserGroup.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqUserGroup.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqUserGroup.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqUserGroup.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqUserGroup.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqUserGroup.  # noqa: E501

        The user group name  # noqa: E501

        :return: The name of this XiqUserGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUserGroup.

        The user group name  # noqa: E501

        :param name: The name of this XiqUserGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUserGroup.  # noqa: E501

        The user group description  # noqa: E501

        :return: The description of this XiqUserGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUserGroup.

        The user group description  # noqa: E501

        :param description: The description of this XiqUserGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def predefined(self):
        """Gets the predefined of this XiqUserGroup.  # noqa: E501

        Whether it is predefined  # noqa: E501

        :return: The predefined of this XiqUserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqUserGroup.

        Whether it is predefined  # noqa: E501

        :param predefined: The predefined of this XiqUserGroup.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and predefined is None:  # noqa: E501
            raise ValueError("Invalid value for `predefined`, must not be `None`")  # noqa: E501

        self._predefined = predefined

    @property
    def password_db_location(self):
        """Gets the password_db_location of this XiqUserGroup.  # noqa: E501


        :return: The password_db_location of this XiqUserGroup.  # noqa: E501
        :rtype: XiqPasswordDbLocation
        """
        return self._password_db_location

    @password_db_location.setter
    def password_db_location(self, password_db_location):
        """Sets the password_db_location of this XiqUserGroup.


        :param password_db_location: The password_db_location of this XiqUserGroup.  # noqa: E501
        :type: XiqPasswordDbLocation
        """
        if self.local_vars_configuration.client_side_validation and password_db_location is None:  # noqa: E501
            raise ValueError("Invalid value for `password_db_location`, must not be `None`")  # noqa: E501

        self._password_db_location = password_db_location

    @property
    def password_type(self):
        """Gets the password_type of this XiqUserGroup.  # noqa: E501


        :return: The password_type of this XiqUserGroup.  # noqa: E501
        :rtype: XiqPasswordType
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this XiqUserGroup.


        :param password_type: The password_type of this XiqUserGroup.  # noqa: E501
        :type: XiqPasswordType
        """
        if self.local_vars_configuration.client_side_validation and password_type is None:  # noqa: E501
            raise ValueError("Invalid value for `password_type`, must not be `None`")  # noqa: E501

        self._password_type = password_type

    @property
    def pcg_use_only(self):
        """Gets the pcg_use_only of this XiqUserGroup.  # noqa: E501

         Whether it's for PCG use only  # noqa: E501

        :return: The pcg_use_only of this XiqUserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._pcg_use_only

    @pcg_use_only.setter
    def pcg_use_only(self, pcg_use_only):
        """Sets the pcg_use_only of this XiqUserGroup.

         Whether it's for PCG use only  # noqa: E501

        :param pcg_use_only: The pcg_use_only of this XiqUserGroup.  # noqa: E501
        :type: bool
        """

        self._pcg_use_only = pcg_use_only

    @property
    def pcg_type(self):
        """Gets the pcg_type of this XiqUserGroup.  # noqa: E501


        :return: The pcg_type of this XiqUserGroup.  # noqa: E501
        :rtype: XiqPcgType
        """
        return self._pcg_type

    @pcg_type.setter
    def pcg_type(self, pcg_type):
        """Sets the pcg_type of this XiqUserGroup.


        :param pcg_type: The pcg_type of this XiqUserGroup.  # noqa: E501
        :type: XiqPcgType
        """

        self._pcg_type = pcg_type

    @property
    def ppsk_use_only(self):
        """Gets the ppsk_use_only of this XiqUserGroup.  # noqa: E501

        Whether it's for PPSK use only  # noqa: E501

        :return: The ppsk_use_only of this XiqUserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._ppsk_use_only

    @ppsk_use_only.setter
    def ppsk_use_only(self, ppsk_use_only):
        """Sets the ppsk_use_only of this XiqUserGroup.

        Whether it's for PPSK use only  # noqa: E501

        :param ppsk_use_only: The ppsk_use_only of this XiqUserGroup.  # noqa: E501
        :type: bool
        """

        self._ppsk_use_only = ppsk_use_only

    @property
    def enable_cwp_reg(self):
        """Gets the enable_cwp_reg of this XiqUserGroup.  # noqa: E501

        Whether to enable CWP registration setting  # noqa: E501

        :return: The enable_cwp_reg of this XiqUserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cwp_reg

    @enable_cwp_reg.setter
    def enable_cwp_reg(self, enable_cwp_reg):
        """Sets the enable_cwp_reg of this XiqUserGroup.

        Whether to enable CWP registration setting  # noqa: E501

        :param enable_cwp_reg: The enable_cwp_reg of this XiqUserGroup.  # noqa: E501
        :type: bool
        """

        self._enable_cwp_reg = enable_cwp_reg

    @property
    def password_settings(self):
        """Gets the password_settings of this XiqUserGroup.  # noqa: E501


        :return: The password_settings of this XiqUserGroup.  # noqa: E501
        :rtype: XiqPasswordSettings
        """
        return self._password_settings

    @password_settings.setter
    def password_settings(self, password_settings):
        """Sets the password_settings of this XiqUserGroup.


        :param password_settings: The password_settings of this XiqUserGroup.  # noqa: E501
        :type: XiqPasswordSettings
        """
        if self.local_vars_configuration.client_side_validation and password_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `password_settings`, must not be `None`")  # noqa: E501

        self._password_settings = password_settings

    @property
    def expiration_settings(self):
        """Gets the expiration_settings of this XiqUserGroup.  # noqa: E501


        :return: The expiration_settings of this XiqUserGroup.  # noqa: E501
        :rtype: XiqExpirationSettings
        """
        return self._expiration_settings

    @expiration_settings.setter
    def expiration_settings(self, expiration_settings):
        """Sets the expiration_settings of this XiqUserGroup.


        :param expiration_settings: The expiration_settings of this XiqUserGroup.  # noqa: E501
        :type: XiqExpirationSettings
        """
        if self.local_vars_configuration.client_side_validation and expiration_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration_settings`, must not be `None`")  # noqa: E501

        self._expiration_settings = expiration_settings

    @property
    def delivery_settings(self):
        """Gets the delivery_settings of this XiqUserGroup.  # noqa: E501


        :return: The delivery_settings of this XiqUserGroup.  # noqa: E501
        :rtype: XiqDeliverySettings
        """
        return self._delivery_settings

    @delivery_settings.setter
    def delivery_settings(self, delivery_settings):
        """Sets the delivery_settings of this XiqUserGroup.


        :param delivery_settings: The delivery_settings of this XiqUserGroup.  # noqa: E501
        :type: XiqDeliverySettings
        """
        if self.local_vars_configuration.client_side_validation and delivery_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_settings`, must not be `None`")  # noqa: E501

        self._delivery_settings = delivery_settings

    @property
    def user_count(self):
        """Gets the user_count of this XiqUserGroup.  # noqa: E501

        The user count  # noqa: E501

        :return: The user_count of this XiqUserGroup.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this XiqUserGroup.

        The user count  # noqa: E501

        :param user_count: The user_count of this XiqUserGroup.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_count is None:  # noqa: E501
            raise ValueError("Invalid value for `user_count`, must not be `None`")  # noqa: E501

        self._user_count = user_count

    @property
    def ssids(self):
        """Gets the ssids of this XiqUserGroup.  # noqa: E501

        The ssids  # noqa: E501

        :return: The ssids of this XiqUserGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssids

    @ssids.setter
    def ssids(self, ssids):
        """Sets the ssids of this XiqUserGroup.

        The ssids  # noqa: E501

        :param ssids: The ssids of this XiqUserGroup.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and ssids is None:  # noqa: E501
            raise ValueError("Invalid value for `ssids`, must not be `None`")  # noqa: E501

        self._ssids = ssids

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
        if not isinstance(other, XiqUserGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUserGroup):
            return True

        return self.to_dict() != other.to_dict()
