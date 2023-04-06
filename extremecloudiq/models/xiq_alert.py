# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAlert(object):
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
        'id': 'str',
        'owner_id': 'int',
        'timestamp': 'datetime',
        'org_id': 'int',
        'type': 'str',
        'summary': 'str',
        'severity': 'XiqAlertSeverity',
        'category': 'XiqAlertCategory',
        'source': 'XiqAlertSource',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'owner_id': 'owner_id',
        'timestamp': 'timestamp',
        'org_id': 'org_id',
        'type': 'type',
        'summary': 'summary',
        'severity': 'severity',
        'category': 'category',
        'source': 'source',
        'tags': 'tags'
    }

    def __init__(self, id=None, owner_id=None, timestamp=None, org_id=None, type=None, summary=None, severity=None, category=None, source=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._owner_id = None
        self._timestamp = None
        self._org_id = None
        self._type = None
        self._summary = None
        self._severity = None
        self._category = None
        self._source = None
        self._tags = None
        self.discriminator = None

        self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        self.timestamp = timestamp
        if org_id is not None:
            self.org_id = org_id
        if type is not None:
            self.type = type
        if summary is not None:
            self.summary = summary
        if severity is not None:
            self.severity = severity
        if category is not None:
            self.category = category
        if source is not None:
            self.source = source
        self.tags = tags

    @property
    def id(self):
        """Gets the id of this XiqAlert.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqAlert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqAlert.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqAlert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this XiqAlert.  # noqa: E501

        The owner ID  # noqa: E501

        :return: The owner_id of this XiqAlert.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this XiqAlert.

        The owner ID  # noqa: E501

        :param owner_id: The owner_id of this XiqAlert.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqAlert.  # noqa: E501

        The alert create time  # noqa: E501

        :return: The timestamp of this XiqAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqAlert.

        The alert create time  # noqa: E501

        :param timestamp: The timestamp of this XiqAlert.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def org_id(self):
        """Gets the org_id of this XiqAlert.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqAlert.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqAlert.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqAlert.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def type(self):
        """Gets the type of this XiqAlert.  # noqa: E501

        The alert type  # noqa: E501

        :return: The type of this XiqAlert.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XiqAlert.

        The alert type  # noqa: E501

        :param type: The type of this XiqAlert.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def summary(self):
        """Gets the summary of this XiqAlert.  # noqa: E501

        A high-level, text summary message of the event. Will be used to construct an alert's description.  # noqa: E501

        :return: The summary of this XiqAlert.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this XiqAlert.

        A high-level, text summary message of the event. Will be used to construct an alert's description.  # noqa: E501

        :param summary: The summary of this XiqAlert.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def severity(self):
        """Gets the severity of this XiqAlert.  # noqa: E501


        :return: The severity of this XiqAlert.  # noqa: E501
        :rtype: XiqAlertSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this XiqAlert.


        :param severity: The severity of this XiqAlert.  # noqa: E501
        :type: XiqAlertSeverity
        """

        self._severity = severity

    @property
    def category(self):
        """Gets the category of this XiqAlert.  # noqa: E501


        :return: The category of this XiqAlert.  # noqa: E501
        :rtype: XiqAlertCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this XiqAlert.


        :param category: The category of this XiqAlert.  # noqa: E501
        :type: XiqAlertCategory
        """

        self._category = category

    @property
    def source(self):
        """Gets the source of this XiqAlert.  # noqa: E501


        :return: The source of this XiqAlert.  # noqa: E501
        :rtype: XiqAlertSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this XiqAlert.


        :param source: The source of this XiqAlert.  # noqa: E501
        :type: XiqAlertSource
        """

        self._source = source

    @property
    def tags(self):
        """Gets the tags of this XiqAlert.  # noqa: E501

        Additional information for the alert  # noqa: E501

        :return: The tags of this XiqAlert.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this XiqAlert.

        Additional information for the alert  # noqa: E501

        :param tags: The tags of this XiqAlert.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if not isinstance(other, XiqAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlert):
            return True

        return self.to_dict() != other.to_dict()
