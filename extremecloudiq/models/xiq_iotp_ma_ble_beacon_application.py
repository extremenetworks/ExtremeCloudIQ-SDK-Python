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


class XiqIotpMaBleBeaconApplication(object):
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
        'measured_rss': 'int',
        'advertise_interval': 'int',
        'tx_power': 'int',
        'major': 'int',
        'minor': 'int',
        'uuid': 'str',
        'url': 'str',
        'app_type': 'XiqIotpMaBleBeaconAppType'
    }

    attribute_map = {
        'measured_rss': 'measured_rss',
        'advertise_interval': 'advertise_interval',
        'tx_power': 'tx_power',
        'major': 'major',
        'minor': 'minor',
        'uuid': 'uuid',
        'url': 'url',
        'app_type': 'app_type'
    }

    def __init__(self, measured_rss=None, advertise_interval=None, tx_power=None, major=None, minor=None, uuid=None, url=None, app_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotpMaBleBeaconApplication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._measured_rss = None
        self._advertise_interval = None
        self._tx_power = None
        self._major = None
        self._minor = None
        self._uuid = None
        self._url = None
        self._app_type = None
        self.discriminator = None

        if measured_rss is not None:
            self.measured_rss = measured_rss
        if advertise_interval is not None:
            self.advertise_interval = advertise_interval
        if tx_power is not None:
            self.tx_power = tx_power
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if uuid is not None:
            self.uuid = uuid
        if url is not None:
            self.url = url
        self.app_type = app_type

    @property
    def measured_rss(self):
        """Gets the measured_rss of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        BLE Beacon application measured Received Signal Strength value, in dBm.  # noqa: E501

        :return: The measured_rss of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: int
        """
        return self._measured_rss

    @measured_rss.setter
    def measured_rss(self, measured_rss):
        """Sets the measured_rss of this XiqIotpMaBleBeaconApplication.

        BLE Beacon application measured Received Signal Strength value, in dBm.  # noqa: E501

        :param measured_rss: The measured_rss of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                measured_rss is not None and measured_rss > 15):  # noqa: E501
            raise ValueError("Invalid value for `measured_rss`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                measured_rss is not None and measured_rss < -120):  # noqa: E501
            raise ValueError("Invalid value for `measured_rss`, must be a value greater than or equal to `-120`")  # noqa: E501

        self._measured_rss = measured_rss

    @property
    def advertise_interval(self):
        """Gets the advertise_interval of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        BLE Beacon application advertisement interval value in ms.  # noqa: E501

        :return: The advertise_interval of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: int
        """
        return self._advertise_interval

    @advertise_interval.setter
    def advertise_interval(self, advertise_interval):
        """Sets the advertise_interval of this XiqIotpMaBleBeaconApplication.

        BLE Beacon application advertisement interval value in ms.  # noqa: E501

        :param advertise_interval: The advertise_interval of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                advertise_interval is not None and advertise_interval > 10240):  # noqa: E501
            raise ValueError("Invalid value for `advertise_interval`, must be a value less than or equal to `10240`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                advertise_interval is not None and advertise_interval < 100):  # noqa: E501
            raise ValueError("Invalid value for `advertise_interval`, must be a value greater than or equal to `100`")  # noqa: E501

        self._advertise_interval = advertise_interval

    @property
    def tx_power(self):
        """Gets the tx_power of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        // The BLE Beacon transmit power, in dBm.  # noqa: E501

        :return: The tx_power of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: int
        """
        return self._tx_power

    @tx_power.setter
    def tx_power(self, tx_power):
        """Sets the tx_power of this XiqIotpMaBleBeaconApplication.

        // The BLE Beacon transmit power, in dBm.  # noqa: E501

        :param tx_power: The tx_power of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                tx_power is not None and tx_power > 3):  # noqa: E501
            raise ValueError("Invalid value for `tx_power`, must be a value less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tx_power is not None and tx_power < -16):  # noqa: E501
            raise ValueError("Invalid value for `tx_power`, must be a value greater than or equal to `-16`")  # noqa: E501

        self._tx_power = tx_power

    @property
    def major(self):
        """Gets the major of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        BLE Beacon application major value, for BLE Beacon applications of type IBEACON.  # noqa: E501

        :return: The major of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this XiqIotpMaBleBeaconApplication.

        BLE Beacon application major value, for BLE Beacon applications of type IBEACON.  # noqa: E501

        :param major: The major of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                major is not None and major > 65535):  # noqa: E501
            raise ValueError("Invalid value for `major`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                major is not None and major < 0):  # noqa: E501
            raise ValueError("Invalid value for `major`, must be a value greater than or equal to `0`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        BLE Beacon application minor value, for BLE Beacon applications of type IBEACON.  # noqa: E501

        :return: The minor of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this XiqIotpMaBleBeaconApplication.

        BLE Beacon application minor value, for BLE Beacon applications of type IBEACON.  # noqa: E501

        :param minor: The minor of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                minor is not None and minor > 65535):  # noqa: E501
            raise ValueError("Invalid value for `minor`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                minor is not None and minor < 0):  # noqa: E501
            raise ValueError("Invalid value for `minor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._minor = minor

    @property
    def uuid(self):
        """Gets the uuid of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        BLE Beacon application UUID, for BLE Beacon applications of type IBEACON.  # noqa: E501

        :return: The uuid of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this XiqIotpMaBleBeaconApplication.

        BLE Beacon application UUID, for BLE Beacon applications of type IBEACON.  # noqa: E501

        :param uuid: The uuid of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and not re.search(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', uuid)):  # noqa: E501
            raise ValueError(r"Invalid value for `uuid`, must be a follow pattern or equal to `/^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/`")  # noqa: E501

        self._uuid = uuid

    @property
    def url(self):
        """Gets the url of this XiqIotpMaBleBeaconApplication.  # noqa: E501

        BLE Beacon Eddystone URL, for BLE Beacon applications of type EDDYSTONE_URL.  # noqa: E501

        :return: The url of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this XiqIotpMaBleBeaconApplication.

        BLE Beacon Eddystone URL, for BLE Beacon applications of type EDDYSTONE_URL.  # noqa: E501

        :param url: The url of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 34):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `34`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 0):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `0`")  # noqa: E501

        self._url = url

    @property
    def app_type(self):
        """Gets the app_type of this XiqIotpMaBleBeaconApplication.  # noqa: E501


        :return: The app_type of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :rtype: XiqIotpMaBleBeaconAppType
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this XiqIotpMaBleBeaconApplication.


        :param app_type: The app_type of this XiqIotpMaBleBeaconApplication.  # noqa: E501
        :type: XiqIotpMaBleBeaconAppType
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
        if not isinstance(other, XiqIotpMaBleBeaconApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotpMaBleBeaconApplication):
            return True

        return self.to_dict() != other.to_dict()