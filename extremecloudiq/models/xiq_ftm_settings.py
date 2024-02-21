# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqFtmSettings(object):
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
        'wgs84_override': 'bool',
        'wgs84': 'XiqWgs84',
        'zsubelement_override': 'bool',
        'zsubelement': 'XiqZsubelement',
        'civic_address_override': 'bool',
        'civic_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'wgs84_override': 'wgs84_override',
        'wgs84': 'wgs84',
        'zsubelement_override': 'zsubelement_override',
        'zsubelement': 'zsubelement',
        'civic_address_override': 'civic_address_override',
        'civic_address': 'civic_address'
    }

    def __init__(self, id=None, create_time=None, update_time=None, wgs84_override=None, wgs84=None, zsubelement_override=None, zsubelement=None, civic_address_override=None, civic_address=None, local_vars_configuration=None):  # noqa: E501
        """XiqFtmSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._wgs84_override = None
        self._wgs84 = None
        self._zsubelement_override = None
        self._zsubelement = None
        self._civic_address_override = None
        self._civic_address = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.wgs84_override = wgs84_override
        if wgs84 is not None:
            self.wgs84 = wgs84
        self.zsubelement_override = zsubelement_override
        if zsubelement is not None:
            self.zsubelement = zsubelement
        self.civic_address_override = civic_address_override
        if civic_address is not None:
            self.civic_address = civic_address

    @property
    def id(self):
        """Gets the id of this XiqFtmSettings.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqFtmSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqFtmSettings.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqFtmSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqFtmSettings.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqFtmSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqFtmSettings.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqFtmSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqFtmSettings.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqFtmSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqFtmSettings.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqFtmSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def wgs84_override(self):
        """Gets the wgs84_override of this XiqFtmSettings.  # noqa: E501

        World Geodetic System 1984 (WGS84) override  # noqa: E501

        :return: The wgs84_override of this XiqFtmSettings.  # noqa: E501
        :rtype: bool
        """
        return self._wgs84_override

    @wgs84_override.setter
    def wgs84_override(self, wgs84_override):
        """Sets the wgs84_override of this XiqFtmSettings.

        World Geodetic System 1984 (WGS84) override  # noqa: E501

        :param wgs84_override: The wgs84_override of this XiqFtmSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and wgs84_override is None:  # noqa: E501
            raise ValueError("Invalid value for `wgs84_override`, must not be `None`")  # noqa: E501

        self._wgs84_override = wgs84_override

    @property
    def wgs84(self):
        """Gets the wgs84 of this XiqFtmSettings.  # noqa: E501


        :return: The wgs84 of this XiqFtmSettings.  # noqa: E501
        :rtype: XiqWgs84
        """
        return self._wgs84

    @wgs84.setter
    def wgs84(self, wgs84):
        """Sets the wgs84 of this XiqFtmSettings.


        :param wgs84: The wgs84 of this XiqFtmSettings.  # noqa: E501
        :type: XiqWgs84
        """

        self._wgs84 = wgs84

    @property
    def zsubelement_override(self):
        """Gets the zsubelement_override of this XiqFtmSettings.  # noqa: E501

        Z Subelement override.  # noqa: E501

        :return: The zsubelement_override of this XiqFtmSettings.  # noqa: E501
        :rtype: bool
        """
        return self._zsubelement_override

    @zsubelement_override.setter
    def zsubelement_override(self, zsubelement_override):
        """Sets the zsubelement_override of this XiqFtmSettings.

        Z Subelement override.  # noqa: E501

        :param zsubelement_override: The zsubelement_override of this XiqFtmSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and zsubelement_override is None:  # noqa: E501
            raise ValueError("Invalid value for `zsubelement_override`, must not be `None`")  # noqa: E501

        self._zsubelement_override = zsubelement_override

    @property
    def zsubelement(self):
        """Gets the zsubelement of this XiqFtmSettings.  # noqa: E501


        :return: The zsubelement of this XiqFtmSettings.  # noqa: E501
        :rtype: XiqZsubelement
        """
        return self._zsubelement

    @zsubelement.setter
    def zsubelement(self, zsubelement):
        """Sets the zsubelement of this XiqFtmSettings.


        :param zsubelement: The zsubelement of this XiqFtmSettings.  # noqa: E501
        :type: XiqZsubelement
        """

        self._zsubelement = zsubelement

    @property
    def civic_address_override(self):
        """Gets the civic_address_override of this XiqFtmSettings.  # noqa: E501

        Civic Address override.  # noqa: E501

        :return: The civic_address_override of this XiqFtmSettings.  # noqa: E501
        :rtype: bool
        """
        return self._civic_address_override

    @civic_address_override.setter
    def civic_address_override(self, civic_address_override):
        """Sets the civic_address_override of this XiqFtmSettings.

        Civic Address override.  # noqa: E501

        :param civic_address_override: The civic_address_override of this XiqFtmSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and civic_address_override is None:  # noqa: E501
            raise ValueError("Invalid value for `civic_address_override`, must not be `None`")  # noqa: E501

        self._civic_address_override = civic_address_override

    @property
    def civic_address(self):
        """Gets the civic_address of this XiqFtmSettings.  # noqa: E501

        Civic Address as hex encoded RFC4776 formatted string.  # noqa: E501

        :return: The civic_address of this XiqFtmSettings.  # noqa: E501
        :rtype: str
        """
        return self._civic_address

    @civic_address.setter
    def civic_address(self, civic_address):
        """Sets the civic_address of this XiqFtmSettings.

        Civic Address as hex encoded RFC4776 formatted string.  # noqa: E501

        :param civic_address: The civic_address of this XiqFtmSettings.  # noqa: E501
        :type: str
        """

        self._civic_address = civic_address

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
        if not isinstance(other, XiqFtmSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqFtmSettings):
            return True

        return self.to_dict() != other.to_dict()
