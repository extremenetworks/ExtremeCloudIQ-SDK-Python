# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqIpFirewallRule(object):
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
        'create_time': 'datetime',
        'update_time': 'datetime',
        'org_id': 'int',
        'action': 'XiqIpFirewallAction',
        'network_service': 'XiqNetworkService',
        'application_service': 'XiqApplicationService',
        'source_ip': 'XiqL3AddressProfile',
        'destination_ip': 'XiqL3AddressProfile',
        'logging_type': 'XiqLoggingType'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'action': 'action',
        'network_service': 'network_service',
        'application_service': 'application_service',
        'source_ip': 'source_ip',
        'destination_ip': 'destination_ip',
        'logging_type': 'logging_type'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, action=None, network_service=None, application_service=None, source_ip=None, destination_ip=None, logging_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqIpFirewallRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._action = None
        self._network_service = None
        self._application_service = None
        self._source_ip = None
        self._destination_ip = None
        self._logging_type = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if action is not None:
            self.action = action
        if network_service is not None:
            self.network_service = network_service
        if application_service is not None:
            self.application_service = application_service
        if source_ip is not None:
            self.source_ip = source_ip
        if destination_ip is not None:
            self.destination_ip = destination_ip
        if logging_type is not None:
            self.logging_type = logging_type

    @property
    def id(self):
        """Gets the id of this XiqIpFirewallRule.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqIpFirewallRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqIpFirewallRule.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqIpFirewallRule.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqIpFirewallRule.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqIpFirewallRule.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqIpFirewallRule.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqIpFirewallRule.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqIpFirewallRule.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqIpFirewallRule.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqIpFirewallRule.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqIpFirewallRule.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqIpFirewallRule.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqIpFirewallRule.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqIpFirewallRule.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqIpFirewallRule.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def action(self):
        """Gets the action of this XiqIpFirewallRule.  # noqa: E501


        :return: The action of this XiqIpFirewallRule.  # noqa: E501
        :rtype: XiqIpFirewallAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this XiqIpFirewallRule.


        :param action: The action of this XiqIpFirewallRule.  # noqa: E501
        :type: XiqIpFirewallAction
        """

        self._action = action

    @property
    def network_service(self):
        """Gets the network_service of this XiqIpFirewallRule.  # noqa: E501


        :return: The network_service of this XiqIpFirewallRule.  # noqa: E501
        :rtype: XiqNetworkService
        """
        return self._network_service

    @network_service.setter
    def network_service(self, network_service):
        """Sets the network_service of this XiqIpFirewallRule.


        :param network_service: The network_service of this XiqIpFirewallRule.  # noqa: E501
        :type: XiqNetworkService
        """

        self._network_service = network_service

    @property
    def application_service(self):
        """Gets the application_service of this XiqIpFirewallRule.  # noqa: E501


        :return: The application_service of this XiqIpFirewallRule.  # noqa: E501
        :rtype: XiqApplicationService
        """
        return self._application_service

    @application_service.setter
    def application_service(self, application_service):
        """Sets the application_service of this XiqIpFirewallRule.


        :param application_service: The application_service of this XiqIpFirewallRule.  # noqa: E501
        :type: XiqApplicationService
        """

        self._application_service = application_service

    @property
    def source_ip(self):
        """Gets the source_ip of this XiqIpFirewallRule.  # noqa: E501


        :return: The source_ip of this XiqIpFirewallRule.  # noqa: E501
        :rtype: XiqL3AddressProfile
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this XiqIpFirewallRule.


        :param source_ip: The source_ip of this XiqIpFirewallRule.  # noqa: E501
        :type: XiqL3AddressProfile
        """

        self._source_ip = source_ip

    @property
    def destination_ip(self):
        """Gets the destination_ip of this XiqIpFirewallRule.  # noqa: E501


        :return: The destination_ip of this XiqIpFirewallRule.  # noqa: E501
        :rtype: XiqL3AddressProfile
        """
        return self._destination_ip

    @destination_ip.setter
    def destination_ip(self, destination_ip):
        """Sets the destination_ip of this XiqIpFirewallRule.


        :param destination_ip: The destination_ip of this XiqIpFirewallRule.  # noqa: E501
        :type: XiqL3AddressProfile
        """

        self._destination_ip = destination_ip

    @property
    def logging_type(self):
        """Gets the logging_type of this XiqIpFirewallRule.  # noqa: E501


        :return: The logging_type of this XiqIpFirewallRule.  # noqa: E501
        :rtype: XiqLoggingType
        """
        return self._logging_type

    @logging_type.setter
    def logging_type(self, logging_type):
        """Sets the logging_type of this XiqIpFirewallRule.


        :param logging_type: The logging_type of this XiqIpFirewallRule.  # noqa: E501
        :type: XiqLoggingType
        """

        self._logging_type = logging_type

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
        if not isinstance(other, XiqIpFirewallRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIpFirewallRule):
            return True

        return self.to_dict() != other.to_dict()
