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


class XiqPcgAssignPortsResponse(object):
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
        'policy_id': 'int',
        'policy_name': 'str',
        'pcg_port_assignment_entries': 'list[XiqPcgPortAssignmentEntry]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'pcg_port_assignment_entries': 'pcg_port_assignment_entries'
    }

    def __init__(self, policy_id=None, policy_name=None, pcg_port_assignment_entries=None, local_vars_configuration=None):  # noqa: E501
        """XiqPcgAssignPortsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policy_id = None
        self._policy_name = None
        self._pcg_port_assignment_entries = None
        self.discriminator = None

        self.policy_id = policy_id
        self.policy_name = policy_name
        self.pcg_port_assignment_entries = pcg_port_assignment_entries

    @property
    def policy_id(self):
        """Gets the policy_id of this XiqPcgAssignPortsResponse.  # noqa: E501

        The network policy ID  # noqa: E501

        :return: The policy_id of this XiqPcgAssignPortsResponse.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this XiqPcgAssignPortsResponse.

        The network policy ID  # noqa: E501

        :param policy_id: The policy_id of this XiqPcgAssignPortsResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and policy_id is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_id`, must not be `None`")  # noqa: E501

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this XiqPcgAssignPortsResponse.  # noqa: E501

        The network policy name  # noqa: E501

        :return: The policy_name of this XiqPcgAssignPortsResponse.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this XiqPcgAssignPortsResponse.

        The network policy name  # noqa: E501

        :param policy_name: The policy_name of this XiqPcgAssignPortsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and policy_name is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501

        self._policy_name = policy_name

    @property
    def pcg_port_assignment_entries(self):
        """Gets the pcg_port_assignment_entries of this XiqPcgAssignPortsResponse.  # noqa: E501

        The port assignment entry list  # noqa: E501

        :return: The pcg_port_assignment_entries of this XiqPcgAssignPortsResponse.  # noqa: E501
        :rtype: list[XiqPcgPortAssignmentEntry]
        """
        return self._pcg_port_assignment_entries

    @pcg_port_assignment_entries.setter
    def pcg_port_assignment_entries(self, pcg_port_assignment_entries):
        """Sets the pcg_port_assignment_entries of this XiqPcgAssignPortsResponse.

        The port assignment entry list  # noqa: E501

        :param pcg_port_assignment_entries: The pcg_port_assignment_entries of this XiqPcgAssignPortsResponse.  # noqa: E501
        :type: list[XiqPcgPortAssignmentEntry]
        """
        if self.local_vars_configuration.client_side_validation and pcg_port_assignment_entries is None:  # noqa: E501
            raise ValueError("Invalid value for `pcg_port_assignment_entries`, must not be `None`")  # noqa: E501

        self._pcg_port_assignment_entries = pcg_port_assignment_entries

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
        if not isinstance(other, XiqPcgAssignPortsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPcgAssignPortsResponse):
            return True

        return self.to_dict() != other.to_dict()
