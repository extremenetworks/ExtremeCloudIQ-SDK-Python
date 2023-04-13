# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeploymentOverview(object):
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
        'in_progress_devices': 'int',
        'total_progress': 'int'
    }

    attribute_map = {
        'in_progress_devices': 'in_progress_devices',
        'total_progress': 'total_progress'
    }

    def __init__(self, in_progress_devices=None, total_progress=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeploymentOverview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._in_progress_devices = None
        self._total_progress = None
        self.discriminator = None

        self.in_progress_devices = in_progress_devices
        self.total_progress = total_progress

    @property
    def in_progress_devices(self):
        """Gets the in_progress_devices of this XiqDeploymentOverview.  # noqa: E501

        The device count with in progress deployment  # noqa: E501

        :return: The in_progress_devices of this XiqDeploymentOverview.  # noqa: E501
        :rtype: int
        """
        return self._in_progress_devices

    @in_progress_devices.setter
    def in_progress_devices(self, in_progress_devices):
        """Sets the in_progress_devices of this XiqDeploymentOverview.

        The device count with in progress deployment  # noqa: E501

        :param in_progress_devices: The in_progress_devices of this XiqDeploymentOverview.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and in_progress_devices is None:  # noqa: E501
            raise ValueError("Invalid value for `in_progress_devices`, must not be `None`")  # noqa: E501

        self._in_progress_devices = in_progress_devices

    @property
    def total_progress(self):
        """Gets the total_progress of this XiqDeploymentOverview.  # noqa: E501

        The total progress, range from 0 to 100  # noqa: E501

        :return: The total_progress of this XiqDeploymentOverview.  # noqa: E501
        :rtype: int
        """
        return self._total_progress

    @total_progress.setter
    def total_progress(self, total_progress):
        """Sets the total_progress of this XiqDeploymentOverview.

        The total progress, range from 0 to 100  # noqa: E501

        :param total_progress: The total_progress of this XiqDeploymentOverview.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_progress is None:  # noqa: E501
            raise ValueError("Invalid value for `total_progress`, must not be `None`")  # noqa: E501

        self._total_progress = total_progress

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
        if not isinstance(other, XiqDeploymentOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeploymentOverview):
            return True

        return self.to_dict() != other.to_dict()
