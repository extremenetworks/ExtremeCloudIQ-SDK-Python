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


class XiqIotpMaBleScanApplication(object):
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
        'min_rss': 'int',
        'uuid': 'str',
        'vendors': 'list[XiqIotpMaBleScanVendor]',
        'app_type': 'XiqIotpMaBleScanAppType'
    }

    attribute_map = {
        'min_rss': 'min_rss',
        'uuid': 'uuid',
        'vendors': 'vendors',
        'app_type': 'app_type'
    }

    def __init__(self, min_rss=None, uuid=None, vendors=None, app_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotpMaBleScanApplication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min_rss = None
        self._uuid = None
        self._vendors = None
        self._app_type = None
        self.discriminator = None

        if min_rss is not None:
            self.min_rss = min_rss
        if uuid is not None:
            self.uuid = uuid
        if vendors is not None:
            self.vendors = vendors
        self.app_type = app_type

    @property
    def min_rss(self):
        """Gets the min_rss of this XiqIotpMaBleScanApplication.  # noqa: E501

        BLE Scan application minimum Received Signal Strength value, in dBm.  # noqa: E501

        :return: The min_rss of this XiqIotpMaBleScanApplication.  # noqa: E501
        :rtype: int
        """
        return self._min_rss

    @min_rss.setter
    def min_rss(self, min_rss):
        """Sets the min_rss of this XiqIotpMaBleScanApplication.

        BLE Scan application minimum Received Signal Strength value, in dBm.  # noqa: E501

        :param min_rss: The min_rss of this XiqIotpMaBleScanApplication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                min_rss is not None and min_rss > 20):  # noqa: E501
            raise ValueError("Invalid value for `min_rss`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_rss is not None and min_rss < -120):  # noqa: E501
            raise ValueError("Invalid value for `min_rss`, must be a value greater than or equal to `-120`")  # noqa: E501

        self._min_rss = min_rss

    @property
    def uuid(self):
        """Gets the uuid of this XiqIotpMaBleScanApplication.  # noqa: E501

        BLE Scan iBeacon application UUID, for BLE Scan applications of type IBEACON.  # noqa: E501

        :return: The uuid of this XiqIotpMaBleScanApplication.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this XiqIotpMaBleScanApplication.

        BLE Scan iBeacon application UUID, for BLE Scan applications of type IBEACON.  # noqa: E501

        :param uuid: The uuid of this XiqIotpMaBleScanApplication.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and not re.search(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', uuid)):  # noqa: E501
            raise ValueError(r"Invalid value for `uuid`, must be a follow pattern or equal to `/^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/`")  # noqa: E501

        self._uuid = uuid

    @property
    def vendors(self):
        """Gets the vendors of this XiqIotpMaBleScanApplication.  # noqa: E501

        Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC.  # noqa: E501

        :return: The vendors of this XiqIotpMaBleScanApplication.  # noqa: E501
        :rtype: list[XiqIotpMaBleScanVendor]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """Sets the vendors of this XiqIotpMaBleScanApplication.

        Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC.  # noqa: E501

        :param vendors: The vendors of this XiqIotpMaBleScanApplication.  # noqa: E501
        :type: list[XiqIotpMaBleScanVendor]
        """

        self._vendors = vendors

    @property
    def app_type(self):
        """Gets the app_type of this XiqIotpMaBleScanApplication.  # noqa: E501


        :return: The app_type of this XiqIotpMaBleScanApplication.  # noqa: E501
        :rtype: XiqIotpMaBleScanAppType
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this XiqIotpMaBleScanApplication.


        :param app_type: The app_type of this XiqIotpMaBleScanApplication.  # noqa: E501
        :type: XiqIotpMaBleScanAppType
        """
        if self.local_vars_configuration.client_side_validation and app_type is None:  # noqa: E501
            raise ValueError("Invalid value for `app_type`, must not be `None`")  # noqa: E501

        self._app_type = app_type

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
        if not isinstance(other, XiqIotpMaBleScanApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotpMaBleScanApplication):
            return True

        return self.to_dict() != other.to_dict()
