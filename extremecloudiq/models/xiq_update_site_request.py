# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateSiteRequest(object):
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
        'parent_id': 'int',
        'name': 'str',
        'address': 'XiqAddress',
        'country_code': 'int',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'name': 'name',
        'address': 'address',
        'country_code': 'country_code',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, parent_id=None, name=None, address=None, country_code=None, latitude=None, longitude=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateSiteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parent_id = None
        self._name = None
        self._address = None
        self._country_code = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        self.name = name
        if address is not None:
            self.address = address
        self.country_code = country_code
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def parent_id(self):
        """Gets the parent_id of this XiqUpdateSiteRequest.  # noqa: E501

        The parent site group ID  # noqa: E501

        :return: The parent_id of this XiqUpdateSiteRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this XiqUpdateSiteRequest.

        The parent site group ID  # noqa: E501

        :param parent_id: The parent_id of this XiqUpdateSiteRequest.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this XiqUpdateSiteRequest.  # noqa: E501

        The site name  # noqa: E501

        :return: The name of this XiqUpdateSiteRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateSiteRequest.

        The site name  # noqa: E501

        :param name: The name of this XiqUpdateSiteRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this XiqUpdateSiteRequest.  # noqa: E501


        :return: The address of this XiqUpdateSiteRequest.  # noqa: E501
        :rtype: XiqAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this XiqUpdateSiteRequest.


        :param address: The address of this XiqUpdateSiteRequest.  # noqa: E501
        :type: XiqAddress
        """

        self._address = address

    @property
    def country_code(self):
        """Gets the country_code of this XiqUpdateSiteRequest.  # noqa: E501

        The site country code. Get the list of country codes from /countries XAPI.  # noqa: E501

        :return: The country_code of this XiqUpdateSiteRequest.  # noqa: E501
        :rtype: int
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this XiqUpdateSiteRequest.

        The site country code. Get the list of country codes from /countries XAPI.  # noqa: E501

        :param country_code: The country_code of this XiqUpdateSiteRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and country_code is None:  # noqa: E501
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def latitude(self):
        """Gets the latitude of this XiqUpdateSiteRequest.  # noqa: E501

        The latitude coordinate for the site  # noqa: E501

        :return: The latitude of this XiqUpdateSiteRequest.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this XiqUpdateSiteRequest.

        The latitude coordinate for the site  # noqa: E501

        :param latitude: The latitude of this XiqUpdateSiteRequest.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this XiqUpdateSiteRequest.  # noqa: E501

        The longitude coordinate for the site  # noqa: E501

        :return: The longitude of this XiqUpdateSiteRequest.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this XiqUpdateSiteRequest.

        The longitude coordinate for the site  # noqa: E501

        :param longitude: The longitude of this XiqUpdateSiteRequest.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if not isinstance(other, XiqUpdateSiteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateSiteRequest):
            return True

        return self.to_dict() != other.to_dict()
