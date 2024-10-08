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


class XiqDigitalTwinDevice(object):
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
        'make': 'XiqDigitalTwinMake',
        'model': 'XiqDigitalTwinModel',
        'os_type': 'str',
        'os_version': 'str',
        'vim_modules': 'list[XiqDigitalTwinVimModule]',
        'feat_licenses': 'list[XiqDigitalTwinFeatLicense]'
    }

    attribute_map = {
        'make': 'make',
        'model': 'model',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'vim_modules': 'vim_modules',
        'feat_licenses': 'feat_licenses'
    }

    def __init__(self, make=None, model=None, os_type=None, os_version=None, vim_modules=None, feat_licenses=None, local_vars_configuration=None):  # noqa: E501
        """XiqDigitalTwinDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._make = None
        self._model = None
        self._os_type = None
        self._os_version = None
        self._vim_modules = None
        self._feat_licenses = None
        self.discriminator = None

        self.make = make
        self.model = model
        if os_type is not None:
            self.os_type = os_type
        self.os_version = os_version
        if vim_modules is not None:
            self.vim_modules = vim_modules
        if feat_licenses is not None:
            self.feat_licenses = feat_licenses

    @property
    def make(self):
        """Gets the make of this XiqDigitalTwinDevice.  # noqa: E501


        :return: The make of this XiqDigitalTwinDevice.  # noqa: E501
        :rtype: XiqDigitalTwinMake
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this XiqDigitalTwinDevice.


        :param make: The make of this XiqDigitalTwinDevice.  # noqa: E501
        :type: XiqDigitalTwinMake
        """
        if self.local_vars_configuration.client_side_validation and make is None:  # noqa: E501
            raise ValueError("Invalid value for `make`, must not be `None`")  # noqa: E501

        self._make = make

    @property
    def model(self):
        """Gets the model of this XiqDigitalTwinDevice.  # noqa: E501


        :return: The model of this XiqDigitalTwinDevice.  # noqa: E501
        :rtype: XiqDigitalTwinModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this XiqDigitalTwinDevice.


        :param model: The model of this XiqDigitalTwinDevice.  # noqa: E501
        :type: XiqDigitalTwinModel
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def os_type(self):
        """Gets the os_type of this XiqDigitalTwinDevice.  # noqa: E501

        The Digital Twin device OS type.  # noqa: E501

        :return: The os_type of this XiqDigitalTwinDevice.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this XiqDigitalTwinDevice.

        The Digital Twin device OS type.  # noqa: E501

        :param os_type: The os_type of this XiqDigitalTwinDevice.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this XiqDigitalTwinDevice.  # noqa: E501

        The Digital Twin device OS version.  # noqa: E501

        :return: The os_version of this XiqDigitalTwinDevice.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this XiqDigitalTwinDevice.

        The Digital Twin device OS version.  # noqa: E501

        :param os_version: The os_version of this XiqDigitalTwinDevice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and os_version is None:  # noqa: E501
            raise ValueError("Invalid value for `os_version`, must not be `None`")  # noqa: E501

        self._os_version = os_version

    @property
    def vim_modules(self):
        """Gets the vim_modules of this XiqDigitalTwinDevice.  # noqa: E501

        The Digital Twin VIM modules.  # noqa: E501

        :return: The vim_modules of this XiqDigitalTwinDevice.  # noqa: E501
        :rtype: list[XiqDigitalTwinVimModule]
        """
        return self._vim_modules

    @vim_modules.setter
    def vim_modules(self, vim_modules):
        """Sets the vim_modules of this XiqDigitalTwinDevice.

        The Digital Twin VIM modules.  # noqa: E501

        :param vim_modules: The vim_modules of this XiqDigitalTwinDevice.  # noqa: E501
        :type: list[XiqDigitalTwinVimModule]
        """

        self._vim_modules = vim_modules

    @property
    def feat_licenses(self):
        """Gets the feat_licenses of this XiqDigitalTwinDevice.  # noqa: E501

        The Digital Twin feature licenses.  # noqa: E501

        :return: The feat_licenses of this XiqDigitalTwinDevice.  # noqa: E501
        :rtype: list[XiqDigitalTwinFeatLicense]
        """
        return self._feat_licenses

    @feat_licenses.setter
    def feat_licenses(self, feat_licenses):
        """Sets the feat_licenses of this XiqDigitalTwinDevice.

        The Digital Twin feature licenses.  # noqa: E501

        :param feat_licenses: The feat_licenses of this XiqDigitalTwinDevice.  # noqa: E501
        :type: list[XiqDigitalTwinFeatLicense]
        """

        self._feat_licenses = feat_licenses

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
        if not isinstance(other, XiqDigitalTwinDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDigitalTwinDevice):
            return True

        return self.to_dict() != other.to_dict()
