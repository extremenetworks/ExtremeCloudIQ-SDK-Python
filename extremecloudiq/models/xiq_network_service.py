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


class XiqNetworkService(object):
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
        'name': 'str',
        'description': 'str',
        'ip_protocol': 'XiqNetworkIpProtocol',
        'protocol_number': 'int',
        'port_number': 'int',
        'alg_type': 'XiqNetworkAlgType',
        'service_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'ip_protocol': 'ip_protocol',
        'protocol_number': 'protocol_number',
        'port_number': 'port_number',
        'alg_type': 'alg_type',
        'service_type': 'service_type'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, ip_protocol=None, protocol_number=None, port_number=None, alg_type=None, service_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqNetworkService - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._ip_protocol = None
        self._protocol_number = None
        self._port_number = None
        self._alg_type = None
        self._service_type = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ip_protocol is not None:
            self.ip_protocol = ip_protocol
        if protocol_number is not None:
            self.protocol_number = protocol_number
        if port_number is not None:
            self.port_number = port_number
        if alg_type is not None:
            self.alg_type = alg_type
        self.service_type = service_type

    @property
    def id(self):
        """Gets the id of this XiqNetworkService.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqNetworkService.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqNetworkService.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqNetworkService.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqNetworkService.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqNetworkService.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqNetworkService.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqNetworkService.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqNetworkService.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqNetworkService.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqNetworkService.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqNetworkService.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqNetworkService.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqNetworkService.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqNetworkService.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqNetworkService.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqNetworkService.  # noqa: E501

        The Network Service name  # noqa: E501

        :return: The name of this XiqNetworkService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqNetworkService.

        The Network Service name  # noqa: E501

        :param name: The name of this XiqNetworkService.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqNetworkService.  # noqa: E501

        The Network Service description  # noqa: E501

        :return: The description of this XiqNetworkService.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqNetworkService.

        The Network Service description  # noqa: E501

        :param description: The description of this XiqNetworkService.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this XiqNetworkService.  # noqa: E501


        :return: The ip_protocol of this XiqNetworkService.  # noqa: E501
        :rtype: XiqNetworkIpProtocol
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this XiqNetworkService.


        :param ip_protocol: The ip_protocol of this XiqNetworkService.  # noqa: E501
        :type: XiqNetworkIpProtocol
        """

        self._ip_protocol = ip_protocol

    @property
    def protocol_number(self):
        """Gets the protocol_number of this XiqNetworkService.  # noqa: E501

        The Network Protocol Number  # noqa: E501

        :return: The protocol_number of this XiqNetworkService.  # noqa: E501
        :rtype: int
        """
        return self._protocol_number

    @protocol_number.setter
    def protocol_number(self, protocol_number):
        """Sets the protocol_number of this XiqNetworkService.

        The Network Protocol Number  # noqa: E501

        :param protocol_number: The protocol_number of this XiqNetworkService.  # noqa: E501
        :type: int
        """

        self._protocol_number = protocol_number

    @property
    def port_number(self):
        """Gets the port_number of this XiqNetworkService.  # noqa: E501

        The Network Port Number  # noqa: E501

        :return: The port_number of this XiqNetworkService.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this XiqNetworkService.

        The Network Port Number  # noqa: E501

        :param port_number: The port_number of this XiqNetworkService.  # noqa: E501
        :type: int
        """

        self._port_number = port_number

    @property
    def alg_type(self):
        """Gets the alg_type of this XiqNetworkService.  # noqa: E501


        :return: The alg_type of this XiqNetworkService.  # noqa: E501
        :rtype: XiqNetworkAlgType
        """
        return self._alg_type

    @alg_type.setter
    def alg_type(self, alg_type):
        """Sets the alg_type of this XiqNetworkService.


        :param alg_type: The alg_type of this XiqNetworkService.  # noqa: E501
        :type: XiqNetworkAlgType
        """

        self._alg_type = alg_type

    @property
    def service_type(self):
        """Gets the service_type of this XiqNetworkService.  # noqa: E501

        The Service Type.  # noqa: E501

        :return: The service_type of this XiqNetworkService.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this XiqNetworkService.

        The Service Type.  # noqa: E501

        :param service_type: The service_type of this XiqNetworkService.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501
        allowed_values = ["NETWORK", "APPLICATION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and service_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `service_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_type, allowed_values)
            )

        self._service_type = service_type

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
        if not isinstance(other, XiqNetworkService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqNetworkService):
            return True

        return self.to_dict() != other.to_dict()
