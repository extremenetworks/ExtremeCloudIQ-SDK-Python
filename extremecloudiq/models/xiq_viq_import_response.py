# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqViqImportResponse(object):
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
        'log_file_name': 'str',
        'import_status': 'str'
    }

    attribute_map = {
        'log_file_name': 'log_file_name',
        'import_status': 'import_status'
    }

    def __init__(self, log_file_name=None, import_status=None, local_vars_configuration=None):  # noqa: E501
        """XiqViqImportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._log_file_name = None
        self._import_status = None
        self.discriminator = None

        self.log_file_name = log_file_name
        self.import_status = import_status

    @property
    def log_file_name(self):
        """Gets the log_file_name of this XiqViqImportResponse.  # noqa: E501

        The import log file name  # noqa: E501

        :return: The log_file_name of this XiqViqImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._log_file_name

    @log_file_name.setter
    def log_file_name(self, log_file_name):
        """Sets the log_file_name of this XiqViqImportResponse.

        The import log file name  # noqa: E501

        :param log_file_name: The log_file_name of this XiqViqImportResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and log_file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `log_file_name`, must not be `None`")  # noqa: E501

        self._log_file_name = log_file_name

    @property
    def import_status(self):
        """Gets the import_status of this XiqViqImportResponse.  # noqa: E501

        The import status  # noqa: E501

        :return: The import_status of this XiqViqImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        """Sets the import_status of this XiqViqImportResponse.

        The import status  # noqa: E501

        :param import_status: The import_status of this XiqViqImportResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and import_status is None:  # noqa: E501
            raise ValueError("Invalid value for `import_status`, must not be `None`")  # noqa: E501

        self._import_status = import_status

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
        if not isinstance(other, XiqViqImportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqViqImportResponse):
            return True

        return self.to_dict() != other.to_dict()
