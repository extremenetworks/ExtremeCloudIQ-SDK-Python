# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqClientField(object):
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
    ORG_NAME = "ORG_NAME"
    LOCATION_ID = "LOCATION_ID"
    LOCATIONS = "LOCATIONS"
    HOSTNAME = "HOSTNAME"
    MAC_ADDRESS = "MAC_ADDRESS"
    IP_ADDRESS = "IP_ADDRESS"
    IPV6_ADDRESS = "IPV6_ADDRESS"
    OS_TYPE = "OS_TYPE"
    DEVICE_ID = "DEVICE_ID"
    DEVICE_FUNCTION = "DEVICE_FUNCTION"
    DEVICE_NAME = "DEVICE_NAME"
    USERNAME = "USERNAME"
    USER_PROFILE_NAME = "USER_PROFILE_NAME"
    CONNECTED = "CONNECTED"
    ONLINE_TIME = "ONLINE_TIME"
    OFFLINE_TIME = "OFFLINE_TIME"
    VLAN = "VLAN"
    CONNECTION_TYPE = "CONNECTION_TYPE"
    SSID = "SSID"
    PORT = "PORT"
    BSSID = "BSSID"
    PORT_TYPE_NAME = "PORT_TYPE_NAME"
    INTERFACE_NAME = "INTERFACE_NAME"
    AUTH = "AUTH"
    ENCRYPTION_METHOD = "ENCRYPTION_METHOD"
    CHANNEL = "CHANNEL"
    CLIENT_HEALTH = "CLIENT_HEALTH"
    APPLICATION_HEALTH = "APPLICATION_HEALTH"
    NETWORK_HEALTH = "NETWORK_HEALTH"
    RADIO_HEALTH = "RADIO_HEALTH"
    RSSI = "RSSI"
    SNR = "SNR"
    RADIO_TYPE = "RADIO_TYPE"
    WING_AP = "WING_AP"
    VENDOR = "VENDOR"
    MOBILITY = "MOBILITY"
    CATEGORY = "CATEGORY"
    DESCRIPTION = "DESCRIPTION"
    DEVICE_MAC_ADDRESS = "DEVICE_MAC_ADDRESS"
    ALIAS = "ALIAS"
    PRODUCT_TYPE = "PRODUCT_TYPE"
    TH_RLOC16 = "TH_RLOC16"
    TH_CHILD_ID = "TH_CHILD_ID"
    TH_TIMEOUT = "TH_TIMEOUT"
    TH_SUPERVISION_INTERVAL = "TH_SUPERVISION_INTERVAL"
    TH_NETDATA_VERSION = "TH_NETDATA_VERSION"
    TH_CSL_SYNCED = "TH_CSL_SYNCED"
    TH_IP_ADDRESSES = "TH_IP_ADDRESSES"
    TH_ROUTER_LAST_REPORTED = "TH_ROUTER_LAST_REPORTED"
    THREAD_CONNECTED = "THREAD_CONNECTED"

    allowable_values = [ID, CREATE_TIME, UPDATE_TIME, ORG_ID, ORG_NAME, LOCATION_ID, LOCATIONS, HOSTNAME, MAC_ADDRESS, IP_ADDRESS, IPV6_ADDRESS, OS_TYPE, DEVICE_ID, DEVICE_FUNCTION, DEVICE_NAME, USERNAME, USER_PROFILE_NAME, CONNECTED, ONLINE_TIME, OFFLINE_TIME, VLAN, CONNECTION_TYPE, SSID, PORT, BSSID, PORT_TYPE_NAME, INTERFACE_NAME, AUTH, ENCRYPTION_METHOD, CHANNEL, CLIENT_HEALTH, APPLICATION_HEALTH, NETWORK_HEALTH, RADIO_HEALTH, RSSI, SNR, RADIO_TYPE, WING_AP, VENDOR, MOBILITY, CATEGORY, DESCRIPTION, DEVICE_MAC_ADDRESS, ALIAS, PRODUCT_TYPE, TH_RLOC16, TH_CHILD_ID, TH_TIMEOUT, TH_SUPERVISION_INTERVAL, TH_NETDATA_VERSION, TH_CSL_SYNCED, TH_IP_ADDRESSES, TH_ROUTER_LAST_REPORTED, THREAD_CONNECTED]  # noqa: E501

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
        """XiqClientField - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, XiqClientField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClientField):
            return True

        return self.to_dict() != other.to_dict()
