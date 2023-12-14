# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCredentialLog(object):
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
        'username': 'str',
        'vhm_id': 'str',
        'org_id': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'vhm_id': 'vhm_id',
        'org_id': 'org_id',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, username=None, vhm_id=None, org_id=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """XiqCredentialLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._vhm_id = None
        self._org_id = None
        self._timestamp = None
        self.discriminator = None

        self.id = id
        if username is not None:
            self.username = username
        if vhm_id is not None:
            self.vhm_id = vhm_id
        if org_id is not None:
            self.org_id = org_id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this XiqCredentialLog.  # noqa: E501

        The Credential log id  # noqa: E501

        :return: The id of this XiqCredentialLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqCredentialLog.

        The Credential log id  # noqa: E501

        :param id: The id of this XiqCredentialLog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this XiqCredentialLog.  # noqa: E501

        The username  # noqa: E501

        :return: The username of this XiqCredentialLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this XiqCredentialLog.

        The username  # noqa: E501

        :param username: The username of this XiqCredentialLog.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def vhm_id(self):
        """Gets the vhm_id of this XiqCredentialLog.  # noqa: E501

        The vhm id  # noqa: E501

        :return: The vhm_id of this XiqCredentialLog.  # noqa: E501
        :rtype: str
        """
        return self._vhm_id

    @vhm_id.setter
    def vhm_id(self, vhm_id):
        """Sets the vhm_id of this XiqCredentialLog.

        The vhm id  # noqa: E501

        :param vhm_id: The vhm_id of this XiqCredentialLog.  # noqa: E501
        :type: str
        """

        self._vhm_id = vhm_id

    @property
    def org_id(self):
        """Gets the org_id of this XiqCredentialLog.  # noqa: E501

        The org id  # noqa: E501

        :return: The org_id of this XiqCredentialLog.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqCredentialLog.

        The org id  # noqa: E501

        :param org_id: The org_id of this XiqCredentialLog.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqCredentialLog.  # noqa: E501

        The credential log timestamp  # noqa: E501

        :return: The timestamp of this XiqCredentialLog.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqCredentialLog.

        The credential log timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqCredentialLog.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, XiqCredentialLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCredentialLog):
            return True

        return self.to_dict() != other.to_dict()
