# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCertificate(object):
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
        'id': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'cert_type': 'XiqCertificateType',
        'name': 'str',
        'encrypted': 'bool',
        'description': 'str',
        'file_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'cert_type': 'cert_type',
        'name': 'name',
        'encrypted': 'encrypted',
        'description': 'description',
        'file_size': 'file_size'
    }

    def __init__(self, id=None, create_time=None, update_time=None, cert_type=None, name=None, encrypted=None, description=None, file_size=None, local_vars_configuration=None):  # noqa: E501
        """XiqCertificate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._cert_type = None
        self._name = None
        self._encrypted = None
        self._description = None
        self._file_size = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if cert_type is not None:
            self.cert_type = cert_type
        self.name = name
        self.encrypted = encrypted
        if description is not None:
            self.description = description
        self.file_size = file_size

    @property
    def id(self):
        """Gets the id of this XiqCertificate.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqCertificate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqCertificate.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqCertificate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqCertificate.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqCertificate.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqCertificate.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqCertificate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqCertificate.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqCertificate.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqCertificate.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqCertificate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def cert_type(self):
        """Gets the cert_type of this XiqCertificate.  # noqa: E501


        :return: The cert_type of this XiqCertificate.  # noqa: E501
        :rtype: XiqCertificateType
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        """Sets the cert_type of this XiqCertificate.


        :param cert_type: The cert_type of this XiqCertificate.  # noqa: E501
        :type: XiqCertificateType
        """

        self._cert_type = cert_type

    @property
    def name(self):
        """Gets the name of this XiqCertificate.  # noqa: E501

        The certificate file name  # noqa: E501

        :return: The name of this XiqCertificate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqCertificate.

        The certificate file name  # noqa: E501

        :param name: The name of this XiqCertificate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def encrypted(self):
        """Gets the encrypted of this XiqCertificate.  # noqa: E501

        The certificate encrypted or not  # noqa: E501

        :return: The encrypted of this XiqCertificate.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this XiqCertificate.

        The certificate encrypted or not  # noqa: E501

        :param encrypted: The encrypted of this XiqCertificate.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and encrypted is None:  # noqa: E501
            raise ValueError("Invalid value for `encrypted`, must not be `None`")  # noqa: E501

        self._encrypted = encrypted

    @property
    def description(self):
        """Gets the description of this XiqCertificate.  # noqa: E501

        The certificate description  # noqa: E501

        :return: The description of this XiqCertificate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqCertificate.

        The certificate description  # noqa: E501

        :param description: The description of this XiqCertificate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_size(self):
        """Gets the file_size of this XiqCertificate.  # noqa: E501

        The certificate file size  # noqa: E501

        :return: The file_size of this XiqCertificate.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this XiqCertificate.

        The certificate file size  # noqa: E501

        :param file_size: The file_size of this XiqCertificate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and file_size is None:  # noqa: E501
            raise ValueError("Invalid value for `file_size`, must not be `None`")  # noqa: E501

        self._file_size = file_size

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
        if not isinstance(other, XiqCertificate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCertificate):
            return True

        return self.to_dict() != other.to_dict()
