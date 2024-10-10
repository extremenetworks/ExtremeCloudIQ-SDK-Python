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


class XiqGetAfcSpectrumForApRequest(object):
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
        'owner_id': 'int',
        'site_name': 'str',
        'region': 'str',
        'input_info': 'list[XiqAfcInputInfo]'
    }

    attribute_map = {
        'owner_id': 'owner_id',
        'site_name': 'site_name',
        'region': 'region',
        'input_info': 'input_info'
    }

    def __init__(self, owner_id=None, site_name=None, region=None, input_info=None, local_vars_configuration=None):  # noqa: E501
        """XiqGetAfcSpectrumForApRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_id = None
        self._site_name = None
        self._region = None
        self._input_info = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if site_name is not None:
            self.site_name = site_name
        if region is not None:
            self.region = region
        if input_info is not None:
            self.input_info = input_info

    @property
    def owner_id(self):
        """Gets the owner_id of this XiqGetAfcSpectrumForApRequest.  # noqa: E501


        :return: The owner_id of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this XiqGetAfcSpectrumForApRequest.


        :param owner_id: The owner_id of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def site_name(self):
        """Gets the site_name of this XiqGetAfcSpectrumForApRequest.  # noqa: E501


        :return: The site_name of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this XiqGetAfcSpectrumForApRequest.


        :param site_name: The site_name of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

    @property
    def region(self):
        """Gets the region of this XiqGetAfcSpectrumForApRequest.  # noqa: E501


        :return: The region of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this XiqGetAfcSpectrumForApRequest.


        :param region: The region of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["US", "UNRECOGNIZED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and region not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `region` ({0}), must be one of {1}"  # noqa: E501
                .format(region, allowed_values)
            )

        self._region = region

    @property
    def input_info(self):
        """Gets the input_info of this XiqGetAfcSpectrumForApRequest.  # noqa: E501


        :return: The input_info of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :rtype: list[XiqAfcInputInfo]
        """
        return self._input_info

    @input_info.setter
    def input_info(self, input_info):
        """Sets the input_info of this XiqGetAfcSpectrumForApRequest.


        :param input_info: The input_info of this XiqGetAfcSpectrumForApRequest.  # noqa: E501
        :type: list[XiqAfcInputInfo]
        """

        self._input_info = input_info

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
        if not isinstance(other, XiqGetAfcSpectrumForApRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqGetAfcSpectrumForApRequest):
            return True

        return self.to_dict() != other.to_dict()