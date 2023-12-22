# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceInstallationReport(object):
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
        'onboarded': 'bool',
        'location_name': 'str',
        'network_policy_name': 'str',
        'device_template_name': 'str',
        'ip_address': 'str',
        'default_gateway': 'str',
        'ntp_server': 'str',
        'dns_server': 'str',
        'enable_poe': 'bool',
        'xiq_connectivity': 'bool',
        'image_count': 'int',
        'image_names': 'list[str]'
    }

    attribute_map = {
        'onboarded': 'onboarded',
        'location_name': 'location_name',
        'network_policy_name': 'network_policy_name',
        'device_template_name': 'device_template_name',
        'ip_address': 'ip_address',
        'default_gateway': 'default_gateway',
        'ntp_server': 'ntp_server',
        'dns_server': 'dns_server',
        'enable_poe': 'enable_poe',
        'xiq_connectivity': 'xiq_connectivity',
        'image_count': 'image_count',
        'image_names': 'image_names'
    }

    def __init__(self, onboarded=None, location_name=None, network_policy_name=None, device_template_name=None, ip_address=None, default_gateway=None, ntp_server=None, dns_server=None, enable_poe=None, xiq_connectivity=None, image_count=None, image_names=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceInstallationReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._onboarded = None
        self._location_name = None
        self._network_policy_name = None
        self._device_template_name = None
        self._ip_address = None
        self._default_gateway = None
        self._ntp_server = None
        self._dns_server = None
        self._enable_poe = None
        self._xiq_connectivity = None
        self._image_count = None
        self._image_names = None
        self.discriminator = None

        if onboarded is not None:
            self.onboarded = onboarded
        if location_name is not None:
            self.location_name = location_name
        if network_policy_name is not None:
            self.network_policy_name = network_policy_name
        if device_template_name is not None:
            self.device_template_name = device_template_name
        if ip_address is not None:
            self.ip_address = ip_address
        if default_gateway is not None:
            self.default_gateway = default_gateway
        if ntp_server is not None:
            self.ntp_server = ntp_server
        if dns_server is not None:
            self.dns_server = dns_server
        if enable_poe is not None:
            self.enable_poe = enable_poe
        if xiq_connectivity is not None:
            self.xiq_connectivity = xiq_connectivity
        if image_count is not None:
            self.image_count = image_count
        if image_names is not None:
            self.image_names = image_names

    @property
    def onboarded(self):
        """Gets the onboarded of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The onboarded of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: bool
        """
        return self._onboarded

    @onboarded.setter
    def onboarded(self, onboarded):
        """Sets the onboarded of this XiqDeviceInstallationReport.


        :param onboarded: The onboarded of this XiqDeviceInstallationReport.  # noqa: E501
        :type: bool
        """

        self._onboarded = onboarded

    @property
    def location_name(self):
        """Gets the location_name of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The location_name of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this XiqDeviceInstallationReport.


        :param location_name: The location_name of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def network_policy_name(self):
        """Gets the network_policy_name of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The network_policy_name of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._network_policy_name

    @network_policy_name.setter
    def network_policy_name(self, network_policy_name):
        """Sets the network_policy_name of this XiqDeviceInstallationReport.


        :param network_policy_name: The network_policy_name of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._network_policy_name = network_policy_name

    @property
    def device_template_name(self):
        """Gets the device_template_name of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The device_template_name of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._device_template_name

    @device_template_name.setter
    def device_template_name(self, device_template_name):
        """Sets the device_template_name of this XiqDeviceInstallationReport.


        :param device_template_name: The device_template_name of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._device_template_name = device_template_name

    @property
    def ip_address(self):
        """Gets the ip_address of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The ip_address of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this XiqDeviceInstallationReport.


        :param ip_address: The ip_address of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def default_gateway(self):
        """Gets the default_gateway of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The default_gateway of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._default_gateway

    @default_gateway.setter
    def default_gateway(self, default_gateway):
        """Sets the default_gateway of this XiqDeviceInstallationReport.


        :param default_gateway: The default_gateway of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._default_gateway = default_gateway

    @property
    def ntp_server(self):
        """Gets the ntp_server of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The ntp_server of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._ntp_server

    @ntp_server.setter
    def ntp_server(self, ntp_server):
        """Sets the ntp_server of this XiqDeviceInstallationReport.


        :param ntp_server: The ntp_server of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._ntp_server = ntp_server

    @property
    def dns_server(self):
        """Gets the dns_server of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The dns_server of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: str
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        """Sets the dns_server of this XiqDeviceInstallationReport.


        :param dns_server: The dns_server of this XiqDeviceInstallationReport.  # noqa: E501
        :type: str
        """

        self._dns_server = dns_server

    @property
    def enable_poe(self):
        """Gets the enable_poe of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The enable_poe of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: bool
        """
        return self._enable_poe

    @enable_poe.setter
    def enable_poe(self, enable_poe):
        """Sets the enable_poe of this XiqDeviceInstallationReport.


        :param enable_poe: The enable_poe of this XiqDeviceInstallationReport.  # noqa: E501
        :type: bool
        """

        self._enable_poe = enable_poe

    @property
    def xiq_connectivity(self):
        """Gets the xiq_connectivity of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The xiq_connectivity of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: bool
        """
        return self._xiq_connectivity

    @xiq_connectivity.setter
    def xiq_connectivity(self, xiq_connectivity):
        """Sets the xiq_connectivity of this XiqDeviceInstallationReport.


        :param xiq_connectivity: The xiq_connectivity of this XiqDeviceInstallationReport.  # noqa: E501
        :type: bool
        """

        self._xiq_connectivity = xiq_connectivity

    @property
    def image_count(self):
        """Gets the image_count of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The image_count of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: int
        """
        return self._image_count

    @image_count.setter
    def image_count(self, image_count):
        """Sets the image_count of this XiqDeviceInstallationReport.


        :param image_count: The image_count of this XiqDeviceInstallationReport.  # noqa: E501
        :type: int
        """

        self._image_count = image_count

    @property
    def image_names(self):
        """Gets the image_names of this XiqDeviceInstallationReport.  # noqa: E501


        :return: The image_names of this XiqDeviceInstallationReport.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_names

    @image_names.setter
    def image_names(self, image_names):
        """Sets the image_names of this XiqDeviceInstallationReport.


        :param image_names: The image_names of this XiqDeviceInstallationReport.  # noqa: E501
        :type: list[str]
        """

        self._image_names = image_names

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
        if not isinstance(other, XiqDeviceInstallationReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceInstallationReport):
            return True

        return self.to_dict() != other.to_dict()
