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


class XiqUpdateExternalRadiusServerRequest(object):
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
        'shared_secret': 'str',
        'authentication_port': 'int',
        'accounting_port': 'int',
        'server_type': 'XiqRadiusServerType',
        'ip_addr': 'str'
    }

    attribute_map = {
        'name': 'name',
        'shared_secret': 'shared_secret',
        'authentication_port': 'authentication_port',
        'accounting_port': 'accounting_port',
        'server_type': 'server_type',
        'ip_addr': 'ip_addr'
    }

    def __init__(self, name=None, shared_secret=None, authentication_port=1812, accounting_port=1813, server_type=None, ip_addr=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateExternalRadiusServerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._shared_secret = None
        self._authentication_port = None
        self._accounting_port = None
        self._server_type = None
        self._ip_addr = None
        self.discriminator = None

        self.name = name
        if shared_secret is not None:
            self.shared_secret = shared_secret
        self.authentication_port = authentication_port
        self.accounting_port = accounting_port
        self.server_type = server_type
        self.ip_addr = ip_addr

    @property
    def name(self):
        """Gets the name of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501

        The external RADIUS server name  # noqa: E501

        :return: The name of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateExternalRadiusServerRequest.

        The external RADIUS server name  # noqa: E501

        :param name: The name of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def shared_secret(self):
        """Gets the shared_secret of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501

        The shared secret for the external RADIUS server (optional)  # noqa: E501

        :return: The shared_secret of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this XiqUpdateExternalRadiusServerRequest.

        The shared secret for the external RADIUS server (optional)  # noqa: E501

        :param shared_secret: The shared_secret of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

    @property
    def authentication_port(self):
        """Gets the authentication_port of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501

        The authentication port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :return: The authentication_port of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._authentication_port

    @authentication_port.setter
    def authentication_port(self, authentication_port):
        """Sets the authentication_port of this XiqUpdateExternalRadiusServerRequest.

        The authentication port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :param authentication_port: The authentication_port of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and authentication_port is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_port`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                authentication_port is not None and authentication_port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `authentication_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                authentication_port is not None and authentication_port < 1):  # noqa: E501
            raise ValueError("Invalid value for `authentication_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._authentication_port = authentication_port

    @property
    def accounting_port(self):
        """Gets the accounting_port of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501

        The accounting port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :return: The accounting_port of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._accounting_port

    @accounting_port.setter
    def accounting_port(self, accounting_port):
        """Sets the accounting_port of this XiqUpdateExternalRadiusServerRequest.

        The accounting port for the external RADIUS server (1 ~ 65535)  # noqa: E501

        :param accounting_port: The accounting_port of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and accounting_port is None:  # noqa: E501
            raise ValueError("Invalid value for `accounting_port`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accounting_port is not None and accounting_port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `accounting_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accounting_port is not None and accounting_port < 1):  # noqa: E501
            raise ValueError("Invalid value for `accounting_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._accounting_port = accounting_port

    @property
    def server_type(self):
        """Gets the server_type of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501


        :return: The server_type of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :rtype: XiqRadiusServerType
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this XiqUpdateExternalRadiusServerRequest.


        :param server_type: The server_type of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :type: XiqRadiusServerType
        """
        if self.local_vars_configuration.client_side_validation and server_type is None:  # noqa: E501
            raise ValueError("Invalid value for `server_type`, must not be `None`")  # noqa: E501

        self._server_type = server_type

    @property
    def ip_addr(self):
        """Gets the ip_addr of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501

        The IP address or hostname of the RADIUS server  # noqa: E501

        :return: The ip_addr of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this XiqUpdateExternalRadiusServerRequest.

        The IP address or hostname of the RADIUS server  # noqa: E501

        :param ip_addr: The ip_addr of this XiqUpdateExternalRadiusServerRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ip_addr is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_addr`, must not be `None`")  # noqa: E501

        self._ip_addr = ip_addr

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
        if not isinstance(other, XiqUpdateExternalRadiusServerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateExternalRadiusServerRequest):
            return True

        return self.to_dict() != other.to_dict()
