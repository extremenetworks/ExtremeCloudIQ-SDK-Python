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


class XiqDeploymentPolicy(object):
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
        'enable_complete_configuration_update': 'bool',
        'firmware_upgrade_policy': 'XiqFirmwareUpgradePolicy',
        'firmware_activate_option': 'XiqFirmwareActivateOption'
    }

    attribute_map = {
        'enable_complete_configuration_update': 'enable_complete_configuration_update',
        'firmware_upgrade_policy': 'firmware_upgrade_policy',
        'firmware_activate_option': 'firmware_activate_option'
    }

    def __init__(self, enable_complete_configuration_update=None, firmware_upgrade_policy=None, firmware_activate_option=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeploymentPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_complete_configuration_update = None
        self._firmware_upgrade_policy = None
        self._firmware_activate_option = None
        self.discriminator = None

        self.enable_complete_configuration_update = enable_complete_configuration_update
        if firmware_upgrade_policy is not None:
            self.firmware_upgrade_policy = firmware_upgrade_policy
        if firmware_activate_option is not None:
            self.firmware_activate_option = firmware_activate_option

    @property
    def enable_complete_configuration_update(self):
        """Gets the enable_complete_configuration_update of this XiqDeploymentPolicy.  # noqa: E501

        true if update complete configuration, otherwise update delta configuration. Note: ExtremeCloud IQ will neither upgrade device firmware nor reboot device for a delta configuration push. That means that the other parameters for firmware upgrade and activation are not required when this is false.  # noqa: E501

        :return: The enable_complete_configuration_update of this XiqDeploymentPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_complete_configuration_update

    @enable_complete_configuration_update.setter
    def enable_complete_configuration_update(self, enable_complete_configuration_update):
        """Sets the enable_complete_configuration_update of this XiqDeploymentPolicy.

        true if update complete configuration, otherwise update delta configuration. Note: ExtremeCloud IQ will neither upgrade device firmware nor reboot device for a delta configuration push. That means that the other parameters for firmware upgrade and activation are not required when this is false.  # noqa: E501

        :param enable_complete_configuration_update: The enable_complete_configuration_update of this XiqDeploymentPolicy.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_complete_configuration_update is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_complete_configuration_update`, must not be `None`")  # noqa: E501

        self._enable_complete_configuration_update = enable_complete_configuration_update

    @property
    def firmware_upgrade_policy(self):
        """Gets the firmware_upgrade_policy of this XiqDeploymentPolicy.  # noqa: E501


        :return: The firmware_upgrade_policy of this XiqDeploymentPolicy.  # noqa: E501
        :rtype: XiqFirmwareUpgradePolicy
        """
        return self._firmware_upgrade_policy

    @firmware_upgrade_policy.setter
    def firmware_upgrade_policy(self, firmware_upgrade_policy):
        """Sets the firmware_upgrade_policy of this XiqDeploymentPolicy.


        :param firmware_upgrade_policy: The firmware_upgrade_policy of this XiqDeploymentPolicy.  # noqa: E501
        :type: XiqFirmwareUpgradePolicy
        """

        self._firmware_upgrade_policy = firmware_upgrade_policy

    @property
    def firmware_activate_option(self):
        """Gets the firmware_activate_option of this XiqDeploymentPolicy.  # noqa: E501


        :return: The firmware_activate_option of this XiqDeploymentPolicy.  # noqa: E501
        :rtype: XiqFirmwareActivateOption
        """
        return self._firmware_activate_option

    @firmware_activate_option.setter
    def firmware_activate_option(self, firmware_activate_option):
        """Sets the firmware_activate_option of this XiqDeploymentPolicy.


        :param firmware_activate_option: The firmware_activate_option of this XiqDeploymentPolicy.  # noqa: E501
        :type: XiqFirmwareActivateOption
        """

        self._firmware_activate_option = firmware_activate_option

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
        if not isinstance(other, XiqDeploymentPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeploymentPolicy):
            return True

        return self.to_dict() != other.to_dict()
