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


class XiqViqLinkedCuidInfo(object):
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
        'system_cuid': 'str',
        'shared_cuid': 'str',
        'viq_id': 'str',
        'link_status': 'str',
        'link_error': 'str'
    }

    attribute_map = {
        'system_cuid': 'system_cuid',
        'shared_cuid': 'shared_cuid',
        'viq_id': 'viq_id',
        'link_status': 'link_status',
        'link_error': 'link_error'
    }

    def __init__(self, system_cuid=None, shared_cuid=None, viq_id=None, link_status=None, link_error=None, local_vars_configuration=None):  # noqa: E501
        """XiqViqLinkedCuidInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_cuid = None
        self._shared_cuid = None
        self._viq_id = None
        self._link_status = None
        self._link_error = None
        self.discriminator = None

        if system_cuid is not None:
            self.system_cuid = system_cuid
        if shared_cuid is not None:
            self.shared_cuid = shared_cuid
        if viq_id is not None:
            self.viq_id = viq_id
        if link_status is not None:
            self.link_status = link_status
        if link_error is not None:
            self.link_error = link_error

    @property
    def system_cuid(self):
        """Gets the system_cuid of this XiqViqLinkedCuidInfo.  # noqa: E501

        The system CUID.  # noqa: E501

        :return: The system_cuid of this XiqViqLinkedCuidInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_cuid

    @system_cuid.setter
    def system_cuid(self, system_cuid):
        """Sets the system_cuid of this XiqViqLinkedCuidInfo.

        The system CUID.  # noqa: E501

        :param system_cuid: The system_cuid of this XiqViqLinkedCuidInfo.  # noqa: E501
        :type: str
        """

        self._system_cuid = system_cuid

    @property
    def shared_cuid(self):
        """Gets the shared_cuid of this XiqViqLinkedCuidInfo.  # noqa: E501

        The shared CUID.  # noqa: E501

        :return: The shared_cuid of this XiqViqLinkedCuidInfo.  # noqa: E501
        :rtype: str
        """
        return self._shared_cuid

    @shared_cuid.setter
    def shared_cuid(self, shared_cuid):
        """Sets the shared_cuid of this XiqViqLinkedCuidInfo.

        The shared CUID.  # noqa: E501

        :param shared_cuid: The shared_cuid of this XiqViqLinkedCuidInfo.  # noqa: E501
        :type: str
        """

        self._shared_cuid = shared_cuid

    @property
    def viq_id(self):
        """Gets the viq_id of this XiqViqLinkedCuidInfo.  # noqa: E501

        The VIQ Id.  # noqa: E501

        :return: The viq_id of this XiqViqLinkedCuidInfo.  # noqa: E501
        :rtype: str
        """
        return self._viq_id

    @viq_id.setter
    def viq_id(self, viq_id):
        """Sets the viq_id of this XiqViqLinkedCuidInfo.

        The VIQ Id.  # noqa: E501

        :param viq_id: The viq_id of this XiqViqLinkedCuidInfo.  # noqa: E501
        :type: str
        """

        self._viq_id = viq_id

    @property
    def link_status(self):
        """Gets the link_status of this XiqViqLinkedCuidInfo.  # noqa: E501

        The license link status for the VIQ.  # noqa: E501

        :return: The link_status of this XiqViqLinkedCuidInfo.  # noqa: E501
        :rtype: str
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        """Sets the link_status of this XiqViqLinkedCuidInfo.

        The license link status for the VIQ.  # noqa: E501

        :param link_status: The link_status of this XiqViqLinkedCuidInfo.  # noqa: E501
        :type: str
        """

        self._link_status = link_status

    @property
    def link_error(self):
        """Gets the link_error of this XiqViqLinkedCuidInfo.  # noqa: E501

        The license link error message for the VIQ.  # noqa: E501

        :return: The link_error of this XiqViqLinkedCuidInfo.  # noqa: E501
        :rtype: str
        """
        return self._link_error

    @link_error.setter
    def link_error(self, link_error):
        """Sets the link_error of this XiqViqLinkedCuidInfo.

        The license link error message for the VIQ.  # noqa: E501

        :param link_error: The link_error of this XiqViqLinkedCuidInfo.  # noqa: E501
        :type: str
        """

        self._link_error = link_error

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
        if not isinstance(other, XiqViqLinkedCuidInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqViqLinkedCuidInfo):
            return True

        return self.to_dict() != other.to_dict()
