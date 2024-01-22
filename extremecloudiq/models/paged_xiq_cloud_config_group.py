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


class PagedXiqCloudConfigGroup(object):
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
        'page': 'int',
        'count': 'int',
        'total_pages': 'int',
        'total_count': 'int',
        'data': 'list[XiqCloudConfigGroup]'
    }

    attribute_map = {
        'page': 'page',
        'count': 'count',
        'total_pages': 'total_pages',
        'total_count': 'total_count',
        'data': 'data'
    }

    def __init__(self, page=None, count=None, total_pages=None, total_count=None, data=None, local_vars_configuration=None):  # noqa: E501
        """PagedXiqCloudConfigGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page = None
        self._count = None
        self._total_pages = None
        self._total_count = None
        self._data = None
        self.discriminator = None

        self.page = page
        self.count = count
        self.total_pages = total_pages
        self.total_count = total_count
        if data is not None:
            self.data = data

    @property
    def page(self):
        """Gets the page of this PagedXiqCloudConfigGroup.  # noqa: E501

        The current page number  # noqa: E501

        :return: The page of this PagedXiqCloudConfigGroup.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PagedXiqCloudConfigGroup.

        The current page number  # noqa: E501

        :param page: The page of this PagedXiqCloudConfigGroup.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and page is None:  # noqa: E501
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def count(self):
        """Gets the count of this PagedXiqCloudConfigGroup.  # noqa: E501

        The element count of the current page  # noqa: E501

        :return: The count of this PagedXiqCloudConfigGroup.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PagedXiqCloudConfigGroup.

        The element count of the current page  # noqa: E501

        :param count: The count of this PagedXiqCloudConfigGroup.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def total_pages(self):
        """Gets the total_pages of this PagedXiqCloudConfigGroup.  # noqa: E501

        The total page number based on request page size  # noqa: E501

        :return: The total_pages of this PagedXiqCloudConfigGroup.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PagedXiqCloudConfigGroup.

        The total page number based on request page size  # noqa: E501

        :param total_pages: The total_pages of this PagedXiqCloudConfigGroup.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_pages is None:  # noqa: E501
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def total_count(self):
        """Gets the total_count of this PagedXiqCloudConfigGroup.  # noqa: E501

        The total element count  # noqa: E501

        :return: The total_count of this PagedXiqCloudConfigGroup.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PagedXiqCloudConfigGroup.

        The total element count  # noqa: E501

        :param total_count: The total_count of this PagedXiqCloudConfigGroup.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def data(self):
        """Gets the data of this PagedXiqCloudConfigGroup.  # noqa: E501

        The data in the current page  # noqa: E501

        :return: The data of this PagedXiqCloudConfigGroup.  # noqa: E501
        :rtype: list[XiqCloudConfigGroup]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PagedXiqCloudConfigGroup.

        The data in the current page  # noqa: E501

        :param data: The data of this PagedXiqCloudConfigGroup.  # noqa: E501
        :type: list[XiqCloudConfigGroup]
        """

        self._data = data

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
        if not isinstance(other, PagedXiqCloudConfigGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagedXiqCloudConfigGroup):
            return True

        return self.to_dict() != other.to_dict()
