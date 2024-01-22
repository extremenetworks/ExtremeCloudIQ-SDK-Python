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


class XiqIotProfileThreadGateway(object):
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
        'short_pan_id': 'str',
        'ext_pan_id': 'str',
        'master_key': 'str',
        'network_name': 'str',
        'channel': 'int',
        'comm_credentials': 'str',
        'comm_timeout': 'int',
        'enable_nat64': 'bool',
        'white_list': 'list[XiqIotpTgWhiteListEntry]'
    }

    attribute_map = {
        'short_pan_id': 'short_pan_id',
        'ext_pan_id': 'ext_pan_id',
        'master_key': 'master_key',
        'network_name': 'network_name',
        'channel': 'channel',
        'comm_credentials': 'comm_credentials',
        'comm_timeout': 'comm_timeout',
        'enable_nat64': 'enable_nat64',
        'white_list': 'white_list'
    }

    def __init__(self, short_pan_id=None, ext_pan_id=None, master_key=None, network_name=None, channel=None, comm_credentials=None, comm_timeout=None, enable_nat64=None, white_list=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotProfileThreadGateway - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._short_pan_id = None
        self._ext_pan_id = None
        self._master_key = None
        self._network_name = None
        self._channel = None
        self._comm_credentials = None
        self._comm_timeout = None
        self._enable_nat64 = None
        self._white_list = None
        self.discriminator = None

        self.short_pan_id = short_pan_id
        self.ext_pan_id = ext_pan_id
        self.master_key = master_key
        self.network_name = network_name
        self.channel = channel
        if comm_credentials is not None:
            self.comm_credentials = comm_credentials
        if comm_timeout is not None:
            self.comm_timeout = comm_timeout
        if enable_nat64 is not None:
            self.enable_nat64 = enable_nat64
        if white_list is not None:
            self.white_list = white_list

    @property
    def short_pan_id(self):
        """Gets the short_pan_id of this XiqIotProfileThreadGateway.  # noqa: E501

        The Personal Area Network (PAN) ID. (4 hex digits). FFFF is reserved.  # noqa: E501

        :return: The short_pan_id of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: str
        """
        return self._short_pan_id

    @short_pan_id.setter
    def short_pan_id(self, short_pan_id):
        """Sets the short_pan_id of this XiqIotProfileThreadGateway.

        The Personal Area Network (PAN) ID. (4 hex digits). FFFF is reserved.  # noqa: E501

        :param short_pan_id: The short_pan_id of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and short_pan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `short_pan_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                short_pan_id is not None and len(short_pan_id) > 4):
            raise ValueError("Invalid value for `short_pan_id`, length must be less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                short_pan_id is not None and len(short_pan_id) < 4):
            raise ValueError("Invalid value for `short_pan_id`, length must be greater than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                short_pan_id is not None and not re.search(r'^[0-9a-fA-F]+$', short_pan_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `short_pan_id`, must be a follow pattern or equal to `/^[0-9a-fA-F]+$/`")  # noqa: E501

        self._short_pan_id = short_pan_id

    @property
    def ext_pan_id(self):
        """Gets the ext_pan_id of this XiqIotProfileThreadGateway.  # noqa: E501

        The Extended Personal Area Network (PAN) ID. (16 hex digits)  # noqa: E501

        :return: The ext_pan_id of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: str
        """
        return self._ext_pan_id

    @ext_pan_id.setter
    def ext_pan_id(self, ext_pan_id):
        """Sets the ext_pan_id of this XiqIotProfileThreadGateway.

        The Extended Personal Area Network (PAN) ID. (16 hex digits)  # noqa: E501

        :param ext_pan_id: The ext_pan_id of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ext_pan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ext_pan_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ext_pan_id is not None and len(ext_pan_id) > 16):
            raise ValueError("Invalid value for `ext_pan_id`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ext_pan_id is not None and len(ext_pan_id) < 16):
            raise ValueError("Invalid value for `ext_pan_id`, length must be greater than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ext_pan_id is not None and not re.search(r'^[0-9a-fA-F]+$', ext_pan_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `ext_pan_id`, must be a follow pattern or equal to `/^[0-9a-fA-F]+$/`")  # noqa: E501

        self._ext_pan_id = ext_pan_id

    @property
    def master_key(self):
        """Gets the master_key of this XiqIotProfileThreadGateway.  # noqa: E501

        The network key is used to secure access to the Thread network. It is used to encrypt and authenticate all messages on the network. (32 hex digits)  # noqa: E501

        :return: The master_key of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: str
        """
        return self._master_key

    @master_key.setter
    def master_key(self, master_key):
        """Sets the master_key of this XiqIotProfileThreadGateway.

        The network key is used to secure access to the Thread network. It is used to encrypt and authenticate all messages on the network. (32 hex digits)  # noqa: E501

        :param master_key: The master_key of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and master_key is None:  # noqa: E501
            raise ValueError("Invalid value for `master_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                master_key is not None and len(master_key) > 32):
            raise ValueError("Invalid value for `master_key`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                master_key is not None and len(master_key) < 32):
            raise ValueError("Invalid value for `master_key`, length must be greater than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                master_key is not None and not re.search(r'^[0-9a-fA-F]+$', master_key)):  # noqa: E501
            raise ValueError(r"Invalid value for `master_key`, must be a follow pattern or equal to `/^[0-9a-fA-F]+$/`")  # noqa: E501

        self._master_key = master_key

    @property
    def network_name(self):
        """Gets the network_name of this XiqIotProfileThreadGateway.  # noqa: E501

        A human-readable name for the network, up to 16 bytes in length.  # noqa: E501

        :return: The network_name of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """Sets the network_name of this XiqIotProfileThreadGateway.

        A human-readable name for the network, up to 16 bytes in length.  # noqa: E501

        :param network_name: The network_name of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `network_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                network_name is not None and len(network_name) > 16):
            raise ValueError("Invalid value for `network_name`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                network_name is not None and len(network_name) < 1):
            raise ValueError("Invalid value for `network_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._network_name = network_name

    @property
    def channel(self):
        """Gets the channel of this XiqIotProfileThreadGateway.  # noqa: E501

        802.15.4 channel number, 11-26  # noqa: E501

        :return: The channel of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this XiqIotProfileThreadGateway.

        802.15.4 channel number, 11-26  # noqa: E501

        :param channel: The channel of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                channel is not None and channel < 0):  # noqa: E501
            raise ValueError("Invalid value for `channel`, must be a value greater than or equal to `0`")  # noqa: E501

        self._channel = channel

    @property
    def comm_credentials(self):
        """Gets the comm_credentials of this XiqIotProfileThreadGateway.  # noqa: E501

        The Commissioner Credential is used along with the Extended PAN ID and Network Name to create the PSKc (Pre-Shared Key for the Commissioner).  # noqa: E501

        :return: The comm_credentials of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: str
        """
        return self._comm_credentials

    @comm_credentials.setter
    def comm_credentials(self, comm_credentials):
        """Sets the comm_credentials of this XiqIotProfileThreadGateway.

        The Commissioner Credential is used along with the Extended PAN ID and Network Name to create the PSKc (Pre-Shared Key for the Commissioner).  # noqa: E501

        :param comm_credentials: The comm_credentials of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                comm_credentials is not None and len(comm_credentials) > 255):
            raise ValueError("Invalid value for `comm_credentials`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                comm_credentials is not None and len(comm_credentials) < 6):
            raise ValueError("Invalid value for `comm_credentials`, length must be greater than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                comm_credentials is not None and not re.search(r'^.{6,255}$', comm_credentials)):  # noqa: E501
            raise ValueError(r"Invalid value for `comm_credentials`, must be a follow pattern or equal to `/^.{6,255}$/`")  # noqa: E501

        self._comm_credentials = comm_credentials

    @property
    def comm_timeout(self):
        """Gets the comm_timeout of this XiqIotProfileThreadGateway.  # noqa: E501

        After this timeout the Commissioner will shutdown. The default is 120 sec. but the max is approximately 23 days.  # noqa: E501

        :return: The comm_timeout of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: int
        """
        return self._comm_timeout

    @comm_timeout.setter
    def comm_timeout(self, comm_timeout):
        """Sets the comm_timeout of this XiqIotProfileThreadGateway.

        After this timeout the Commissioner will shutdown. The default is 120 sec. but the max is approximately 23 days.  # noqa: E501

        :param comm_timeout: The comm_timeout of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                comm_timeout is not None and comm_timeout > 2000000):  # noqa: E501
            raise ValueError("Invalid value for `comm_timeout`, must be a value less than or equal to `2000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                comm_timeout is not None and comm_timeout < 1):  # noqa: E501
            raise ValueError("Invalid value for `comm_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._comm_timeout = comm_timeout

    @property
    def enable_nat64(self):
        """Gets the enable_nat64 of this XiqIotProfileThreadGateway.  # noqa: E501

        Enable NAT64 functions including the translator and the prefix publishing.  # noqa: E501

        :return: The enable_nat64 of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: bool
        """
        return self._enable_nat64

    @enable_nat64.setter
    def enable_nat64(self, enable_nat64):
        """Sets the enable_nat64 of this XiqIotProfileThreadGateway.

        Enable NAT64 functions including the translator and the prefix publishing.  # noqa: E501

        :param enable_nat64: The enable_nat64 of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: bool
        """

        self._enable_nat64 = enable_nat64

    @property
    def white_list(self):
        """Gets the white_list of this XiqIotProfileThreadGateway.  # noqa: E501


        :return: The white_list of this XiqIotProfileThreadGateway.  # noqa: E501
        :rtype: list[XiqIotpTgWhiteListEntry]
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        """Sets the white_list of this XiqIotProfileThreadGateway.


        :param white_list: The white_list of this XiqIotProfileThreadGateway.  # noqa: E501
        :type: list[XiqIotpTgWhiteListEntry]
        """

        self._white_list = white_list

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
        if not isinstance(other, XiqIotProfileThreadGateway):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotProfileThreadGateway):
            return True

        return self.to_dict() != other.to_dict()
