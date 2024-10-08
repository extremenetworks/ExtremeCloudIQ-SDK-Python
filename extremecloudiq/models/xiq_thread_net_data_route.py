# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqThreadNetDataRoute(object):
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
        'prefix': 'str',
        'nat64': 'bool',
        'stable': 'bool',
        'route_preference': 'str',
        'added_by_rloc16': 'str',
        'added_by_ext_mac': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'nat64': 'nat64',
        'stable': 'stable',
        'route_preference': 'route_preference',
        'added_by_rloc16': 'added_by_rloc16',
        'added_by_ext_mac': 'added_by_ext_mac'
    }

    def __init__(self, prefix=None, nat64=None, stable=None, route_preference=None, added_by_rloc16=None, added_by_ext_mac=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadNetDataRoute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prefix = None
        self._nat64 = None
        self._stable = None
        self._route_preference = None
        self._added_by_rloc16 = None
        self._added_by_ext_mac = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if nat64 is not None:
            self.nat64 = nat64
        if stable is not None:
            self.stable = stable
        if route_preference is not None:
            self.route_preference = route_preference
        if added_by_rloc16 is not None:
            self.added_by_rloc16 = added_by_rloc16
        if added_by_ext_mac is not None:
            self.added_by_ext_mac = added_by_ext_mac

    @property
    def prefix(self):
        """Gets the prefix of this XiqThreadNetDataRoute.  # noqa: E501


        :return: The prefix of this XiqThreadNetDataRoute.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this XiqThreadNetDataRoute.


        :param prefix: The prefix of this XiqThreadNetDataRoute.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def nat64(self):
        """Gets the nat64 of this XiqThreadNetDataRoute.  # noqa: E501


        :return: The nat64 of this XiqThreadNetDataRoute.  # noqa: E501
        :rtype: bool
        """
        return self._nat64

    @nat64.setter
    def nat64(self, nat64):
        """Sets the nat64 of this XiqThreadNetDataRoute.


        :param nat64: The nat64 of this XiqThreadNetDataRoute.  # noqa: E501
        :type: bool
        """

        self._nat64 = nat64

    @property
    def stable(self):
        """Gets the stable of this XiqThreadNetDataRoute.  # noqa: E501


        :return: The stable of this XiqThreadNetDataRoute.  # noqa: E501
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        """Sets the stable of this XiqThreadNetDataRoute.


        :param stable: The stable of this XiqThreadNetDataRoute.  # noqa: E501
        :type: bool
        """

        self._stable = stable

    @property
    def route_preference(self):
        """Gets the route_preference of this XiqThreadNetDataRoute.  # noqa: E501


        :return: The route_preference of this XiqThreadNetDataRoute.  # noqa: E501
        :rtype: str
        """
        return self._route_preference

    @route_preference.setter
    def route_preference(self, route_preference):
        """Sets the route_preference of this XiqThreadNetDataRoute.


        :param route_preference: The route_preference of this XiqThreadNetDataRoute.  # noqa: E501
        :type: str
        """

        self._route_preference = route_preference

    @property
    def added_by_rloc16(self):
        """Gets the added_by_rloc16 of this XiqThreadNetDataRoute.  # noqa: E501


        :return: The added_by_rloc16 of this XiqThreadNetDataRoute.  # noqa: E501
        :rtype: str
        """
        return self._added_by_rloc16

    @added_by_rloc16.setter
    def added_by_rloc16(self, added_by_rloc16):
        """Sets the added_by_rloc16 of this XiqThreadNetDataRoute.


        :param added_by_rloc16: The added_by_rloc16 of this XiqThreadNetDataRoute.  # noqa: E501
        :type: str
        """

        self._added_by_rloc16 = added_by_rloc16

    @property
    def added_by_ext_mac(self):
        """Gets the added_by_ext_mac of this XiqThreadNetDataRoute.  # noqa: E501


        :return: The added_by_ext_mac of this XiqThreadNetDataRoute.  # noqa: E501
        :rtype: str
        """
        return self._added_by_ext_mac

    @added_by_ext_mac.setter
    def added_by_ext_mac(self, added_by_ext_mac):
        """Sets the added_by_ext_mac of this XiqThreadNetDataRoute.


        :param added_by_ext_mac: The added_by_ext_mac of this XiqThreadNetDataRoute.  # noqa: E501
        :type: str
        """

        self._added_by_ext_mac = added_by_ext_mac

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
        if not isinstance(other, XiqThreadNetDataRoute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadNetDataRoute):
            return True

        return self.to_dict() != other.to_dict()
