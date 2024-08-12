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


class XiqUpdateClientMonitorProfileRequest(object):
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
        'name': 'str',
        'description': 'str',
        'association': 'XiqClientMonitorParameters',
        'authentication': 'XiqClientMonitorParameters',
        'networking': 'XiqClientMonitorParameters'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'association': 'association',
        'authentication': 'authentication',
        'networking': 'networking'
    }

    def __init__(self, name=None, description=None, association=None, authentication=None, networking=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateClientMonitorProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._association = None
        self._authentication = None
        self._networking = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if association is not None:
            self.association = association
        if authentication is not None:
            self.authentication = authentication
        if networking is not None:
            self.networking = networking

    @property
    def name(self):
        """Gets the name of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501

        The client monitor profile name  # noqa: E501

        :return: The name of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateClientMonitorProfileRequest.

        The client monitor profile name  # noqa: E501

        :param name: The name of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 32):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501

        The client monitor profile description  # noqa: E501

        :return: The description of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateClientMonitorProfileRequest.

        The client monitor profile description  # noqa: E501

        :param description: The description of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 64):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def association(self):
        """Gets the association of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501


        :return: The association of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :rtype: XiqClientMonitorParameters
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this XiqUpdateClientMonitorProfileRequest.


        :param association: The association of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :type: XiqClientMonitorParameters
        """

        self._association = association

    @property
    def authentication(self):
        """Gets the authentication of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501


        :return: The authentication of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :rtype: XiqClientMonitorParameters
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this XiqUpdateClientMonitorProfileRequest.


        :param authentication: The authentication of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :type: XiqClientMonitorParameters
        """

        self._authentication = authentication

    @property
    def networking(self):
        """Gets the networking of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501


        :return: The networking of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :rtype: XiqClientMonitorParameters
        """
        return self._networking

    @networking.setter
    def networking(self, networking):
        """Sets the networking of this XiqUpdateClientMonitorProfileRequest.


        :param networking: The networking of this XiqUpdateClientMonitorProfileRequest.  # noqa: E501
        :type: XiqClientMonitorParameters
        """

        self._networking = networking

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
        if not isinstance(other, XiqUpdateClientMonitorProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateClientMonitorProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
