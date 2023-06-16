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


class XiqViq(object):
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
        'devices': 'int',
        'standalone': 'bool',
        'expired': 'bool',
        'customer_id': 'str',
        'vhm_id': 'str',
        'owner_id': 'int',
        'licenses': 'list[XiqViqLicense]'
    }

    attribute_map = {
        'devices': 'devices',
        'standalone': 'standalone',
        'expired': 'expired',
        'customer_id': 'customer_id',
        'vhm_id': 'vhm_id',
        'owner_id': 'owner_id',
        'licenses': 'licenses'
    }

    def __init__(self, devices=None, standalone=None, expired=None, customer_id=None, vhm_id=None, owner_id=None, licenses=None, local_vars_configuration=None):  # noqa: E501
        """XiqViq - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._devices = None
        self._standalone = None
        self._expired = None
        self._customer_id = None
        self._vhm_id = None
        self._owner_id = None
        self._licenses = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if standalone is not None:
            self.standalone = standalone
        if expired is not None:
            self.expired = expired
        if customer_id is not None:
            self.customer_id = customer_id
        if vhm_id is not None:
            self.vhm_id = vhm_id
        if owner_id is not None:
            self.owner_id = owner_id
        if licenses is not None:
            self.licenses = licenses

    @property
    def devices(self):
        """Gets the devices of this XiqViq.  # noqa: E501

        Total # of all licensed devices  # noqa: E501

        :return: The devices of this XiqViq.  # noqa: E501
        :rtype: int
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this XiqViq.

        Total # of all licensed devices  # noqa: E501

        :param devices: The devices of this XiqViq.  # noqa: E501
        :type: int
        """

        self._devices = devices

    @property
    def standalone(self):
        """Gets the standalone of this XiqViq.  # noqa: E501

        Returns true if HIQ is not enabled, otherwise returns false  # noqa: E501

        :return: The standalone of this XiqViq.  # noqa: E501
        :rtype: bool
        """
        return self._standalone

    @standalone.setter
    def standalone(self, standalone):
        """Sets the standalone of this XiqViq.

        Returns true if HIQ is not enabled, otherwise returns false  # noqa: E501

        :param standalone: The standalone of this XiqViq.  # noqa: E501
        :type: bool
        """

        self._standalone = standalone

    @property
    def expired(self):
        """Gets the expired of this XiqViq.  # noqa: E501

        Whether VIQ is expired  # noqa: E501

        :return: The expired of this XiqViq.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this XiqViq.

        Whether VIQ is expired  # noqa: E501

        :param expired: The expired of this XiqViq.  # noqa: E501
        :type: bool
        """

        self._expired = expired

    @property
    def customer_id(self):
        """Gets the customer_id of this XiqViq.  # noqa: E501

        The customer ID, also known as Salesforce customer ID  # noqa: E501

        :return: The customer_id of this XiqViq.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this XiqViq.

        The customer ID, also known as Salesforce customer ID  # noqa: E501

        :param customer_id: The customer_id of this XiqViq.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def vhm_id(self):
        """Gets the vhm_id of this XiqViq.  # noqa: E501

        The VIQ ID  # noqa: E501

        :return: The vhm_id of this XiqViq.  # noqa: E501
        :rtype: str
        """
        return self._vhm_id

    @vhm_id.setter
    def vhm_id(self, vhm_id):
        """Sets the vhm_id of this XiqViq.

        The VIQ ID  # noqa: E501

        :param vhm_id: The vhm_id of this XiqViq.  # noqa: E501
        :type: str
        """

        self._vhm_id = vhm_id

    @property
    def owner_id(self):
        """Gets the owner_id of this XiqViq.  # noqa: E501

        The owner account ID  # noqa: E501

        :return: The owner_id of this XiqViq.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this XiqViq.

        The owner account ID  # noqa: E501

        :param owner_id: The owner_id of this XiqViq.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def licenses(self):
        """Gets the licenses of this XiqViq.  # noqa: E501

        The license list  # noqa: E501

        :return: The licenses of this XiqViq.  # noqa: E501
        :rtype: list[XiqViqLicense]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this XiqViq.

        The license list  # noqa: E501

        :param licenses: The licenses of this XiqViq.  # noqa: E501
        :type: list[XiqViqLicense]
        """

        self._licenses = licenses

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
        if not isinstance(other, XiqViq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqViq):
            return True

        return self.to_dict() != other.to_dict()
