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


class XiqUpdateRadiusClient(object):
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
        'shared_secret': 'str',
        'description': 'str',
        'l3_address_profile_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'shared_secret': 'shared_secret',
        'description': 'description',
        'l3_address_profile_id': 'l3_address_profile_id'
    }

    def __init__(self, id=None, shared_secret=None, description=None, l3_address_profile_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateRadiusClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._shared_secret = None
        self._description = None
        self._l3_address_profile_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if shared_secret is not None:
            self.shared_secret = shared_secret
        if description is not None:
            self.description = description
        if l3_address_profile_id is not None:
            self.l3_address_profile_id = l3_address_profile_id

    @property
    def id(self):
        """Gets the id of this XiqUpdateRadiusClient.  # noqa: E501

        The RADIUS client ID, using an existing ID or leave empty to create a new one  # noqa: E501

        :return: The id of this XiqUpdateRadiusClient.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqUpdateRadiusClient.

        The RADIUS client ID, using an existing ID or leave empty to create a new one  # noqa: E501

        :param id: The id of this XiqUpdateRadiusClient.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def shared_secret(self):
        """Gets the shared_secret of this XiqUpdateRadiusClient.  # noqa: E501

        The shared secret of RADIUS client  # noqa: E501

        :return: The shared_secret of this XiqUpdateRadiusClient.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this XiqUpdateRadiusClient.

        The shared secret of RADIUS client  # noqa: E501

        :param shared_secret: The shared_secret of this XiqUpdateRadiusClient.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

    @property
    def description(self):
        """Gets the description of this XiqUpdateRadiusClient.  # noqa: E501

        The RADIUS client description  # noqa: E501

        :return: The description of this XiqUpdateRadiusClient.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateRadiusClient.

        The RADIUS client description  # noqa: E501

        :param description: The description of this XiqUpdateRadiusClient.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def l3_address_profile_id(self):
        """Gets the l3_address_profile_id of this XiqUpdateRadiusClient.  # noqa: E501

        The associate L3 address profile ID  # noqa: E501

        :return: The l3_address_profile_id of this XiqUpdateRadiusClient.  # noqa: E501
        :rtype: int
        """
        return self._l3_address_profile_id

    @l3_address_profile_id.setter
    def l3_address_profile_id(self, l3_address_profile_id):
        """Sets the l3_address_profile_id of this XiqUpdateRadiusClient.

        The associate L3 address profile ID  # noqa: E501

        :param l3_address_profile_id: The l3_address_profile_id of this XiqUpdateRadiusClient.  # noqa: E501
        :type: int
        """

        self._l3_address_profile_id = l3_address_profile_id

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
        if not isinstance(other, XiqUpdateRadiusClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateRadiusClient):
            return True

        return self.to_dict() != other.to_dict()
