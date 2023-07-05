# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceField(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ID = "ID"
    CREATE_TIME = "CREATE_TIME"
    UPDATE_TIME = "UPDATE_TIME"
    ORG_ID = "ORG_ID"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    SERVICE_TAG = "SERVICE_TAG"
    MAC_ADDRESS = "MAC_ADDRESS"
    DEVICE_FUNCTION = "DEVICE_FUNCTION"
    PRODUCT_TYPE = "PRODUCT_TYPE"
    HOSTNAME = "HOSTNAME"
    IP_ADDRESS = "IP_ADDRESS"
    SOFTWARE_VERSION = "SOFTWARE_VERSION"
    DEVICE_ADMIN_STATE = "DEVICE_ADMIN_STATE"
    CONNECTED = "CONNECTED"
    LAST_CONNECT_TIME = "LAST_CONNECT_TIME"
    NETWORK_POLICY_NAME = "NETWORK_POLICY_NAME"
    NETWORK_POLICY_ID = "NETWORK_POLICY_ID"
    NTP_SERVER_ADDRESS = "NTP_SERVER_ADDRESS"
    DNS_SERVER_ADDRESS = "DNS_SERVER_ADDRESS"
    SUBNET_MASK = "SUBNET_MASK"
    DEFAULT_GATEWAY = "DEFAULT_GATEWAY"
    IPV6_ADDRESS = "IPV6_ADDRESS"
    IPV6_NETMASK = "IPV6_NETMASK"
    SIMULATED = "SIMULATED"
    DISPLAY_VERSION = "DISPLAY_VERSION"
    ACTIVE_CLIENTS = "ACTIVE_CLIENTS"
    LOCATION_ID = "LOCATION_ID"
    LOCATIONS = "LOCATIONS"
    DESCRIPTION = "DESCRIPTION"
    COUNTRY_CODE = "COUNTRY_CODE"
    LLDP_CDP_INFO = "LLDP_CDP_INFO"

    allowable_values = [ID, CREATE_TIME, UPDATE_TIME, ORG_ID, SERIAL_NUMBER, SERVICE_TAG, MAC_ADDRESS, DEVICE_FUNCTION, PRODUCT_TYPE, HOSTNAME, IP_ADDRESS, SOFTWARE_VERSION, DEVICE_ADMIN_STATE, CONNECTED, LAST_CONNECT_TIME, NETWORK_POLICY_NAME, NETWORK_POLICY_ID, NTP_SERVER_ADDRESS, DNS_SERVER_ADDRESS, SUBNET_MASK, DEFAULT_GATEWAY, IPV6_ADDRESS, IPV6_NETMASK, SIMULATED, DISPLAY_VERSION, ACTIVE_CLIENTS, LOCATION_ID, LOCATIONS, DESCRIPTION, COUNTRY_CODE, LLDP_CDP_INFO]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, XiqDeviceField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceField):
            return True

        return self.to_dict() != other.to_dict()
