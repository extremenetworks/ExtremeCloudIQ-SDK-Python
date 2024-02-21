# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqExternalRadiusServer(object):
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
        'shared_secret': 'str',
        'authentication_port': 'int',
        'accounting_port': 'int',
        'server_type': 'XiqRadiusServerType',
        'ip_address': 'str',
        'enable_a3': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'shared_secret': 'shared_secret',
        'authentication_port': 'authentication_port',
        'accounting_port': 'accounting_port',
        'server_type': 'server_type',
        'ip_address': 'ip_address',
        'enable_a3': 'enable_a3'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, shared_secret=None, authentication_port=None, accounting_port=None, server_type=None, ip_address=None, enable_a3=None, local_vars_configuration=None):  # noqa: E501
        """XiqExternalRadiusServer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._shared_secret = None
        self._authentication_port = None
        self._accounting_port = None
        self._server_type = None
        self._ip_address = None
        self._enable_a3 = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.name = name
        if shared_secret is not None:
            self.shared_secret = shared_secret
        self.authentication_port = authentication_port
        self.accounting_port = accounting_port
        self.server_type = server_type
        self.ip_address = ip_address
        self.enable_a3 = enable_a3

    @property
    def id(self):
        """Gets the id of this XiqExternalRadiusServer.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqExternalRadiusServer.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqExternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqExternalRadiusServer.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqExternalRadiusServer.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqExternalRadiusServer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqExternalRadiusServer.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqExternalRadiusServer.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqExternalRadiusServer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqExternalRadiusServer.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqExternalRadiusServer.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqExternalRadiusServer.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqExternalRadiusServer.  # noqa: E501

        The external RADIUS server name  # noqa: E501

        :return: The name of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqExternalRadiusServer.

        The external RADIUS server name  # noqa: E501

        :param name: The name of this XiqExternalRadiusServer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def shared_secret(self):
        """Gets the shared_secret of this XiqExternalRadiusServer.  # noqa: E501

        The shared secret for the external RADIUS server (optional)  # noqa: E501

        :return: The shared_secret of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this XiqExternalRadiusServer.

        The shared secret for the external RADIUS server (optional)  # noqa: E501

        :param shared_secret: The shared_secret of this XiqExternalRadiusServer.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

    @property
    def authentication_port(self):
        """Gets the authentication_port of this XiqExternalRadiusServer.  # noqa: E501

        The authentication port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :return: The authentication_port of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._authentication_port

    @authentication_port.setter
    def authentication_port(self, authentication_port):
        """Sets the authentication_port of this XiqExternalRadiusServer.

        The authentication port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :param authentication_port: The authentication_port of this XiqExternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and authentication_port is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_port`, must not be `None`")  # noqa: E501

        self._authentication_port = authentication_port

    @property
    def accounting_port(self):
        """Gets the accounting_port of this XiqExternalRadiusServer.  # noqa: E501

        The accounting port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :return: The accounting_port of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._accounting_port

    @accounting_port.setter
    def accounting_port(self, accounting_port):
        """Sets the accounting_port of this XiqExternalRadiusServer.

        The accounting port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :param accounting_port: The accounting_port of this XiqExternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and accounting_port is None:  # noqa: E501
            raise ValueError("Invalid value for `accounting_port`, must not be `None`")  # noqa: E501

        self._accounting_port = accounting_port

    @property
    def server_type(self):
        """Gets the server_type of this XiqExternalRadiusServer.  # noqa: E501


        :return: The server_type of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: XiqRadiusServerType
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this XiqExternalRadiusServer.


        :param server_type: The server_type of this XiqExternalRadiusServer.  # noqa: E501
        :type: XiqRadiusServerType
        """
        if self.local_vars_configuration.client_side_validation and server_type is None:  # noqa: E501
            raise ValueError("Invalid value for `server_type`, must not be `None`")  # noqa: E501

        self._server_type = server_type

    @property
    def ip_address(self):
        """Gets the ip_address of this XiqExternalRadiusServer.  # noqa: E501

        The ip address or hostname of the RADIUS server  # noqa: E501

        :return: The ip_address of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this XiqExternalRadiusServer.

        The ip address or hostname of the RADIUS server  # noqa: E501

        :param ip_address: The ip_address of this XiqExternalRadiusServer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ip_address is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def enable_a3(self):
        """Gets the enable_a3 of this XiqExternalRadiusServer.  # noqa: E501

        Indicates whether this is an Extreme A3 RADIUS server or not, cannot be updated after creation. Please set it to false if it is not an Extreme A3 RADIUS server.  # noqa: E501

        :return: The enable_a3 of this XiqExternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_a3

    @enable_a3.setter
    def enable_a3(self, enable_a3):
        """Sets the enable_a3 of this XiqExternalRadiusServer.

        Indicates whether this is an Extreme A3 RADIUS server or not, cannot be updated after creation. Please set it to false if it is not an Extreme A3 RADIUS server.  # noqa: E501

        :param enable_a3: The enable_a3 of this XiqExternalRadiusServer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_a3 is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_a3`, must not be `None`")  # noqa: E501

        self._enable_a3 = enable_a3

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
        if not isinstance(other, XiqExternalRadiusServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExternalRadiusServer):
            return True

        return self.to_dict() != other.to_dict()
