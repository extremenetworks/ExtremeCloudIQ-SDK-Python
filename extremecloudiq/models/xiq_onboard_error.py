# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqOnboardError(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNKNOWN = "UNKNOWN"
    SUCCEED = "SUCCEED"
    EXIST_IN_REDIRECT = "EXIST_IN_REDIRECT"
    FAILED_IN_DB = "FAILED_IN_DB"
    FAILED_STORE_IN_REDIRECT = "FAILED_STORE_IN_REDIRECT"
    SN_IS_NOT_RIGHT = "SN_IS_NOT_RIGHT"
    PRODUCT_TYPE_NOT_EXIST = "PRODUCT_TYPE_NOT_EXIST"
    REACH_MAX_SIZE = "REACH_MAX_SIZE"
    NOT_SUPPORT_DEVICE = "NOT_SUPPORT_DEVICE"
    SN_EXISTED_IN_HM = "SN_EXISTED_IN_HM"
    DEVICE_EXISTED = "DEVICE_EXISTED"
    NETMASK_IP_NOT_NULL = "NETMASK_IP_NOT_NULL"
    BRANCH_ID_USED = "BRANCH_ID_USED"
    INVALID_SERVICE_TAG = "INVALID_SERVICE_TAG"
    RADIO_WIFI1_NOT_SUPPORT = "RADIO_WIFI1_NOT_SUPPORT"
    RADIO_PROFILE_NOT_EXIST = "RADIO_PROFILE_NOT_EXIST"
    SDR_PROFILE_NOT_EXIST = "SDR_PROFILE_NOT_EXIST"
    ADMIN_STATE_NOT_SUPPORT = "ADMIN_STATE_NOT_SUPPORT"
    WIFI_POWER_NOT_SUPPORT = "WIFI_POWER_NOT_SUPPORT"
    OPERATION_MODE_NOT_SUPPORT = "OPERATION_MODE_NOT_SUPPORT"
    COUNTRY_CODE_NOT_SUPPORT = "COUNTRY_CODE_NOT_SUPPORT"
    WIFI0_CHANNEL_NOT_SUPPORT = "WIFI0_CHANNEL_NOT_SUPPORT"
    WIFI1_CHANNEL_NOT_SUPPORT = "WIFI1_CHANNEL_NOT_SUPPORT"
    COUNTRY_CODE_IS_NEEDED = "COUNTRY_CODE_IS_NEEDED"
    MAC_ADDR_REQUIRED = "MAC_ADDR_REQUIRED"
    WING_AP_INVALID_ONBOARDING_DATA = "WING_AP_INVALID_ONBOARDING_DATA"
    NOT_DUAL_BOOT_AP = "NOT_DUAL_BOOT_AP"
    INVALID_CSV_LOCATION = "INVALID_CSV_LOCATION"
    NOT_SUPPORTED_FOR_CONNECT = "NOT_SUPPORTED_FOR_CONNECT"
    DEVICE_EXISTED_ANOTHER_ACCOUNT = "DEVICE_EXISTED_ANOTHER_ACCOUNT"
    FAILED_IN_DTIS_SERVICE = "FAILED_IN_DTIS_SERVICE"
    FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED = "FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED"
    FAILED_DTINSTANCE_ALREADY_ASSOCIATED = "FAILED_DTINSTANCE_ALREADY_ASSOCIATED"
    FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED = "FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED"
    FAILED_IN_DTIS_MAX_LICENSE_LIMIT_REACHED = "FAILED_IN_DTIS_MAX_LICENSE_LIMIT_REACHED"
    FAILED_DTINSTANCE_RELAUNCHED_RECENTLY = "FAILED_DTINSTANCE_RELAUNCHED_RECENTLY"
    FAILED_COPILOT_DISABLED = "FAILED_COPILOT_DISABLED"
    FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED_BY_BATCH = "FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED_BY_BATCH"
    FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED_BY_BATCH = "FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED_BY_BATCH"
    NETWORK_POLICY_NOT_FOUND = "NETWORK_POLICY_NOT_FOUND"

    allowable_values = [UNKNOWN, SUCCEED, EXIST_IN_REDIRECT, FAILED_IN_DB, FAILED_STORE_IN_REDIRECT, SN_IS_NOT_RIGHT, PRODUCT_TYPE_NOT_EXIST, REACH_MAX_SIZE, NOT_SUPPORT_DEVICE, SN_EXISTED_IN_HM, DEVICE_EXISTED, NETMASK_IP_NOT_NULL, BRANCH_ID_USED, INVALID_SERVICE_TAG, RADIO_WIFI1_NOT_SUPPORT, RADIO_PROFILE_NOT_EXIST, SDR_PROFILE_NOT_EXIST, ADMIN_STATE_NOT_SUPPORT, WIFI_POWER_NOT_SUPPORT, OPERATION_MODE_NOT_SUPPORT, COUNTRY_CODE_NOT_SUPPORT, WIFI0_CHANNEL_NOT_SUPPORT, WIFI1_CHANNEL_NOT_SUPPORT, COUNTRY_CODE_IS_NEEDED, MAC_ADDR_REQUIRED, WING_AP_INVALID_ONBOARDING_DATA, NOT_DUAL_BOOT_AP, INVALID_CSV_LOCATION, NOT_SUPPORTED_FOR_CONNECT, DEVICE_EXISTED_ANOTHER_ACCOUNT, FAILED_IN_DTIS_SERVICE, FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED, FAILED_DTINSTANCE_ALREADY_ASSOCIATED, FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED, FAILED_IN_DTIS_MAX_LICENSE_LIMIT_REACHED, FAILED_DTINSTANCE_RELAUNCHED_RECENTLY, FAILED_COPILOT_DISABLED, FAILED_IN_DTIS_MAX_CONCURRENT_LIMIT_REACHED_BY_BATCH, FAILED_IN_DTIS_MAX_OVERALL_LIMIT_REACHED_BY_BATCH, NETWORK_POLICY_NOT_FOUND]  # noqa: E501

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
        """XiqOnboardError - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, XiqOnboardError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqOnboardError):
            return True

        return self.to_dict() != other.to_dict()
