# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqViqLicense(object):
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
        'status': 'XiqLicenseStatus',
        'active_date': 'datetime',
        'expire_date': 'datetime',
        'entitlement_key': 'str',
        'entitlement_type': 'XiqEntitlementType',
        'mode': 'XiqLicenseMode',
        'devices': 'int',
        'activated': 'int',
        'available': 'int',
        'license_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status': 'status',
        'active_date': 'active_date',
        'expire_date': 'expire_date',
        'entitlement_key': 'entitlement_key',
        'entitlement_type': 'entitlement_type',
        'mode': 'mode',
        'devices': 'devices',
        'activated': 'activated',
        'available': 'available',
        'license_type': 'license_type'
    }

    def __init__(self, id=None, create_time=None, update_time=None, status=None, active_date=None, expire_date=None, entitlement_key=None, entitlement_type=None, mode=None, devices=None, activated=None, available=None, license_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqViqLicense - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._active_date = None
        self._expire_date = None
        self._entitlement_key = None
        self._entitlement_type = None
        self._mode = None
        self._devices = None
        self._activated = None
        self._available = None
        self._license_type = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if status is not None:
            self.status = status
        if active_date is not None:
            self.active_date = active_date
        if expire_date is not None:
            self.expire_date = expire_date
        if entitlement_key is not None:
            self.entitlement_key = entitlement_key
        if entitlement_type is not None:
            self.entitlement_type = entitlement_type
        if mode is not None:
            self.mode = mode
        if devices is not None:
            self.devices = devices
        if activated is not None:
            self.activated = activated
        if available is not None:
            self.available = available
        if license_type is not None:
            self.license_type = license_type

    @property
    def id(self):
        """Gets the id of this XiqViqLicense.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqViqLicense.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqViqLicense.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqViqLicense.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqViqLicense.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqViqLicense.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqViqLicense.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqViqLicense.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqViqLicense.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqViqLicense.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqViqLicense.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqViqLicense.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def status(self):
        """Gets the status of this XiqViqLicense.  # noqa: E501


        :return: The status of this XiqViqLicense.  # noqa: E501
        :rtype: XiqLicenseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqViqLicense.


        :param status: The status of this XiqViqLicense.  # noqa: E501
        :type: XiqLicenseStatus
        """

        self._status = status

    @property
    def active_date(self):
        """Gets the active_date of this XiqViqLicense.  # noqa: E501

        The active date  # noqa: E501

        :return: The active_date of this XiqViqLicense.  # noqa: E501
        :rtype: datetime
        """
        return self._active_date

    @active_date.setter
    def active_date(self, active_date):
        """Sets the active_date of this XiqViqLicense.

        The active date  # noqa: E501

        :param active_date: The active_date of this XiqViqLicense.  # noqa: E501
        :type: datetime
        """

        self._active_date = active_date

    @property
    def expire_date(self):
        """Gets the expire_date of this XiqViqLicense.  # noqa: E501

        The expire date  # noqa: E501

        :return: The expire_date of this XiqViqLicense.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this XiqViqLicense.

        The expire date  # noqa: E501

        :param expire_date: The expire_date of this XiqViqLicense.  # noqa: E501
        :type: datetime
        """

        self._expire_date = expire_date

    @property
    def entitlement_key(self):
        """Gets the entitlement_key of this XiqViqLicense.  # noqa: E501

        The entitlement key  # noqa: E501

        :return: The entitlement_key of this XiqViqLicense.  # noqa: E501
        :rtype: str
        """
        return self._entitlement_key

    @entitlement_key.setter
    def entitlement_key(self, entitlement_key):
        """Sets the entitlement_key of this XiqViqLicense.

        The entitlement key  # noqa: E501

        :param entitlement_key: The entitlement_key of this XiqViqLicense.  # noqa: E501
        :type: str
        """

        self._entitlement_key = entitlement_key

    @property
    def entitlement_type(self):
        """Gets the entitlement_type of this XiqViqLicense.  # noqa: E501


        :return: The entitlement_type of this XiqViqLicense.  # noqa: E501
        :rtype: XiqEntitlementType
        """
        return self._entitlement_type

    @entitlement_type.setter
    def entitlement_type(self, entitlement_type):
        """Sets the entitlement_type of this XiqViqLicense.


        :param entitlement_type: The entitlement_type of this XiqViqLicense.  # noqa: E501
        :type: XiqEntitlementType
        """

        self._entitlement_type = entitlement_type

    @property
    def mode(self):
        """Gets the mode of this XiqViqLicense.  # noqa: E501


        :return: The mode of this XiqViqLicense.  # noqa: E501
        :rtype: XiqLicenseMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this XiqViqLicense.


        :param mode: The mode of this XiqViqLicense.  # noqa: E501
        :type: XiqLicenseMode
        """

        self._mode = mode

    @property
    def devices(self):
        """Gets the devices of this XiqViqLicense.  # noqa: E501

        The device number  # noqa: E501

        :return: The devices of this XiqViqLicense.  # noqa: E501
        :rtype: int
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this XiqViqLicense.

        The device number  # noqa: E501

        :param devices: The devices of this XiqViqLicense.  # noqa: E501
        :type: int
        """

        self._devices = devices

    @property
    def activated(self):
        """Gets the activated of this XiqViqLicense.  # noqa: E501

        The activated device number  # noqa: E501

        :return: The activated of this XiqViqLicense.  # noqa: E501
        :rtype: int
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this XiqViqLicense.

        The activated device number  # noqa: E501

        :param activated: The activated of this XiqViqLicense.  # noqa: E501
        :type: int
        """

        self._activated = activated

    @property
    def available(self):
        """Gets the available of this XiqViqLicense.  # noqa: E501

        The available device number  # noqa: E501

        :return: The available of this XiqViqLicense.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this XiqViqLicense.

        The available device number  # noqa: E501

        :param available: The available of this XiqViqLicense.  # noqa: E501
        :type: int
        """

        self._available = available

    @property
    def license_type(self):
        """Gets the license_type of this XiqViqLicense.  # noqa: E501

        The Gemalto license type  # noqa: E501

        :return: The license_type of this XiqViqLicense.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this XiqViqLicense.

        The Gemalto license type  # noqa: E501

        :param license_type: The license_type of this XiqViqLicense.  # noqa: E501
        :type: str
        """

        self._license_type = license_type

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
        if not isinstance(other, XiqViqLicense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqViqLicense):
            return True

        return self.to_dict() != other.to_dict()
