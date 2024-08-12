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


class XiqPcgAssignPortsRequest(object):
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
        'port_assignments': 'list[XiqPcgPortAssignment]'
    }

    attribute_map = {
        'port_assignments': 'port_assignments'
    }

    def __init__(self, port_assignments=None, local_vars_configuration=None):  # noqa: E501
        """XiqPcgAssignPortsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._port_assignments = None
        self.discriminator = None

        self.port_assignments = port_assignments

    @property
    def port_assignments(self):
        """Gets the port_assignments of this XiqPcgAssignPortsRequest.  # noqa: E501

        The port assignment list  # noqa: E501

        :return: The port_assignments of this XiqPcgAssignPortsRequest.  # noqa: E501
        :rtype: list[XiqPcgPortAssignment]
        """
        return self._port_assignments

    @port_assignments.setter
    def port_assignments(self, port_assignments):
        """Sets the port_assignments of this XiqPcgAssignPortsRequest.

        The port assignment list  # noqa: E501

        :param port_assignments: The port_assignments of this XiqPcgAssignPortsRequest.  # noqa: E501
        :type: list[XiqPcgPortAssignment]
        """
        if self.local_vars_configuration.client_side_validation and port_assignments is None:  # noqa: E501
            raise ValueError("Invalid value for `port_assignments`, must not be `None`")  # noqa: E501

        self._port_assignments = port_assignments

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
        if not isinstance(other, XiqPcgAssignPortsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPcgAssignPortsRequest):
            return True

        return self.to_dict() != other.to_dict()
