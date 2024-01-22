# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateLdapServerRequest(object):
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
        'description': 'str',
        'enable_tls': 'bool',
        'bind_dn': 'str',
        'bind_dn_password': 'str',
        'base_dn': 'str',
        'l3_address_profile_id': 'int',
        'protocol_type': 'XiqLdapProtocolType',
        'enable_strip_realm_name': 'bool',
        'destination_port': 'int',
        'verification_mode': 'XiqLdapServerVerificationMode',
        'ca_certificate_id': 'int',
        'client_certificate_id': 'int',
        'client_key_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enable_tls': 'enable_tls',
        'bind_dn': 'bind_dn',
        'bind_dn_password': 'bind_dn_password',
        'base_dn': 'base_dn',
        'l3_address_profile_id': 'l3_address_profile_id',
        'protocol_type': 'protocol_type',
        'enable_strip_realm_name': 'enable_strip_realm_name',
        'destination_port': 'destination_port',
        'verification_mode': 'verification_mode',
        'ca_certificate_id': 'ca_certificate_id',
        'client_certificate_id': 'client_certificate_id',
        'client_key_id': 'client_key_id'
    }

    def __init__(self, name=None, description=None, enable_tls=None, bind_dn=None, bind_dn_password=None, base_dn=None, l3_address_profile_id=None, protocol_type=None, enable_strip_realm_name=None, destination_port=None, verification_mode=None, ca_certificate_id=None, client_certificate_id=None, client_key_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateLdapServerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._enable_tls = None
        self._bind_dn = None
        self._bind_dn_password = None
        self._base_dn = None
        self._l3_address_profile_id = None
        self._protocol_type = None
        self._enable_strip_realm_name = None
        self._destination_port = None
        self._verification_mode = None
        self._ca_certificate_id = None
        self._client_certificate_id = None
        self._client_key_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enable_tls is not None:
            self.enable_tls = enable_tls
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_dn_password is not None:
            self.bind_dn_password = bind_dn_password
        if base_dn is not None:
            self.base_dn = base_dn
        if l3_address_profile_id is not None:
            self.l3_address_profile_id = l3_address_profile_id
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if enable_strip_realm_name is not None:
            self.enable_strip_realm_name = enable_strip_realm_name
        if destination_port is not None:
            self.destination_port = destination_port
        if verification_mode is not None:
            self.verification_mode = verification_mode
        if ca_certificate_id is not None:
            self.ca_certificate_id = ca_certificate_id
        if client_certificate_id is not None:
            self.client_certificate_id = client_certificate_id
        if client_key_id is not None:
            self.client_key_id = client_key_id

    @property
    def name(self):
        """Gets the name of this XiqUpdateLdapServerRequest.  # noqa: E501

        The LDAP server name  # noqa: E501

        :return: The name of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateLdapServerRequest.

        The LDAP server name  # noqa: E501

        :param name: The name of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUpdateLdapServerRequest.  # noqa: E501

        The LDAP server description  # noqa: E501

        :return: The description of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateLdapServerRequest.

        The LDAP server description  # noqa: E501

        :param description: The description of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_tls(self):
        """Gets the enable_tls of this XiqUpdateLdapServerRequest.  # noqa: E501

        enable TLS or not, if ture, caCertificateId, clientCertificateId and clientKeyId must be specified  # noqa: E501

        :return: The enable_tls of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls

    @enable_tls.setter
    def enable_tls(self, enable_tls):
        """Sets the enable_tls of this XiqUpdateLdapServerRequest.

        enable TLS or not, if ture, caCertificateId, clientCertificateId and clientKeyId must be specified  # noqa: E501

        :param enable_tls: The enable_tls of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: bool
        """

        self._enable_tls = enable_tls

    @property
    def bind_dn(self):
        """Gets the bind_dn of this XiqUpdateLdapServerRequest.  # noqa: E501

        The LDAP server bind DN name  # noqa: E501

        :return: The bind_dn of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this XiqUpdateLdapServerRequest.

        The LDAP server bind DN name  # noqa: E501

        :param bind_dn: The bind_dn of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_dn_password(self):
        """Gets the bind_dn_password of this XiqUpdateLdapServerRequest.  # noqa: E501

        The LDAP server bind DN password  # noqa: E501

        :return: The bind_dn_password of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn_password

    @bind_dn_password.setter
    def bind_dn_password(self, bind_dn_password):
        """Sets the bind_dn_password of this XiqUpdateLdapServerRequest.

        The LDAP server bind DN password  # noqa: E501

        :param bind_dn_password: The bind_dn_password of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: str
        """

        self._bind_dn_password = bind_dn_password

    @property
    def base_dn(self):
        """Gets the base_dn of this XiqUpdateLdapServerRequest.  # noqa: E501

        The RADIUS user base DN  # noqa: E501

        :return: The base_dn of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this XiqUpdateLdapServerRequest.

        The RADIUS user base DN  # noqa: E501

        :param base_dn: The base_dn of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def l3_address_profile_id(self):
        """Gets the l3_address_profile_id of this XiqUpdateLdapServerRequest.  # noqa: E501

        The L3 address profile ID  # noqa: E501

        :return: The l3_address_profile_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._l3_address_profile_id

    @l3_address_profile_id.setter
    def l3_address_profile_id(self, l3_address_profile_id):
        """Sets the l3_address_profile_id of this XiqUpdateLdapServerRequest.

        The L3 address profile ID  # noqa: E501

        :param l3_address_profile_id: The l3_address_profile_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: int
        """

        self._l3_address_profile_id = l3_address_profile_id

    @property
    def protocol_type(self):
        """Gets the protocol_type of this XiqUpdateLdapServerRequest.  # noqa: E501


        :return: The protocol_type of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: XiqLdapProtocolType
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this XiqUpdateLdapServerRequest.


        :param protocol_type: The protocol_type of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: XiqLdapProtocolType
        """

        self._protocol_type = protocol_type

    @property
    def enable_strip_realm_name(self):
        """Gets the enable_strip_realm_name of this XiqUpdateLdapServerRequest.  # noqa: E501

        enable strip realm name or not  # noqa: E501

        :return: The enable_strip_realm_name of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_strip_realm_name

    @enable_strip_realm_name.setter
    def enable_strip_realm_name(self, enable_strip_realm_name):
        """Sets the enable_strip_realm_name of this XiqUpdateLdapServerRequest.

        enable strip realm name or not  # noqa: E501

        :param enable_strip_realm_name: The enable_strip_realm_name of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: bool
        """

        self._enable_strip_realm_name = enable_strip_realm_name

    @property
    def destination_port(self):
        """Gets the destination_port of this XiqUpdateLdapServerRequest.  # noqa: E501

        The LDAP server destination port (1 ~ 65535)  # noqa: E501

        :return: The destination_port of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this XiqUpdateLdapServerRequest.

        The LDAP server destination port (1 ~ 65535)  # noqa: E501

        :param destination_port: The destination_port of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                destination_port is not None and destination_port < 1):  # noqa: E501
            raise ValueError("Invalid value for `destination_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._destination_port = destination_port

    @property
    def verification_mode(self):
        """Gets the verification_mode of this XiqUpdateLdapServerRequest.  # noqa: E501


        :return: The verification_mode of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: XiqLdapServerVerificationMode
        """
        return self._verification_mode

    @verification_mode.setter
    def verification_mode(self, verification_mode):
        """Sets the verification_mode of this XiqUpdateLdapServerRequest.


        :param verification_mode: The verification_mode of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: XiqLdapServerVerificationMode
        """

        self._verification_mode = verification_mode

    @property
    def ca_certificate_id(self):
        """Gets the ca_certificate_id of this XiqUpdateLdapServerRequest.  # noqa: E501

        The CA certificate ID, refer to XiqCertificate  # noqa: E501

        :return: The ca_certificate_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._ca_certificate_id

    @ca_certificate_id.setter
    def ca_certificate_id(self, ca_certificate_id):
        """Sets the ca_certificate_id of this XiqUpdateLdapServerRequest.

        The CA certificate ID, refer to XiqCertificate  # noqa: E501

        :param ca_certificate_id: The ca_certificate_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: int
        """

        self._ca_certificate_id = ca_certificate_id

    @property
    def client_certificate_id(self):
        """Gets the client_certificate_id of this XiqUpdateLdapServerRequest.  # noqa: E501

        The client certificate ID, refer to XiqCertificate  # noqa: E501

        :return: The client_certificate_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_certificate_id

    @client_certificate_id.setter
    def client_certificate_id(self, client_certificate_id):
        """Sets the client_certificate_id of this XiqUpdateLdapServerRequest.

        The client certificate ID, refer to XiqCertificate  # noqa: E501

        :param client_certificate_id: The client_certificate_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: int
        """

        self._client_certificate_id = client_certificate_id

    @property
    def client_key_id(self):
        """Gets the client_key_id of this XiqUpdateLdapServerRequest.  # noqa: E501

        The client key ID, refer to XiqCertificate  # noqa: E501

        :return: The client_key_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_key_id

    @client_key_id.setter
    def client_key_id(self, client_key_id):
        """Sets the client_key_id of this XiqUpdateLdapServerRequest.

        The client key ID, refer to XiqCertificate  # noqa: E501

        :param client_key_id: The client_key_id of this XiqUpdateLdapServerRequest.  # noqa: E501
        :type: int
        """

        self._client_key_id = client_key_id

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
        if not isinstance(other, XiqUpdateLdapServerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateLdapServerRequest):
            return True

        return self.to_dict() != other.to_dict()
