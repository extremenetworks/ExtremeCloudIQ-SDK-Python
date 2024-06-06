# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAlertPolicy(object):
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
        'owner_id': 'int',
        'org_id': 'int',
        'name': 'str',
        'sites': 'list[XiqAlertSite]',
        'event_rules_overview': 'list[XiqAlertEventRulesByCategory]',
        'metric_rules_overview': 'list[XiqAlertMetricRulesByMetricset]'
    }

    attribute_map = {
        'id': 'id',
        'owner_id': 'owner_id',
        'org_id': 'org_id',
        'name': 'name',
        'sites': 'sites',
        'event_rules_overview': 'event_rules_overview',
        'metric_rules_overview': 'metric_rules_overview'
    }

    def __init__(self, id=None, owner_id=None, org_id=None, name=None, sites=None, event_rules_overview=None, metric_rules_overview=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._owner_id = None
        self._org_id = None
        self._name = None
        self._sites = None
        self._event_rules_overview = None
        self._metric_rules_overview = None
        self.discriminator = None

        self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if sites is not None:
            self.sites = sites
        if event_rules_overview is not None:
            self.event_rules_overview = event_rules_overview
        if metric_rules_overview is not None:
            self.metric_rules_overview = metric_rules_overview

    @property
    def id(self):
        """Gets the id of this XiqAlertPolicy.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqAlertPolicy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqAlertPolicy.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqAlertPolicy.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this XiqAlertPolicy.  # noqa: E501

        The owner ID  # noqa: E501

        :return: The owner_id of this XiqAlertPolicy.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this XiqAlertPolicy.

        The owner ID  # noqa: E501

        :param owner_id: The owner_id of this XiqAlertPolicy.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def org_id(self):
        """Gets the org_id of this XiqAlertPolicy.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqAlertPolicy.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqAlertPolicy.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqAlertPolicy.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqAlertPolicy.  # noqa: E501

        The name of the alert policy  # noqa: E501

        :return: The name of this XiqAlertPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqAlertPolicy.

        The name of the alert policy  # noqa: E501

        :param name: The name of this XiqAlertPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sites(self):
        """Gets the sites of this XiqAlertPolicy.  # noqa: E501

        The message metadata type  # noqa: E501

        :return: The sites of this XiqAlertPolicy.  # noqa: E501
        :rtype: list[XiqAlertSite]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this XiqAlertPolicy.

        The message metadata type  # noqa: E501

        :param sites: The sites of this XiqAlertPolicy.  # noqa: E501
        :type: list[XiqAlertSite]
        """

        self._sites = sites

    @property
    def event_rules_overview(self):
        """Gets the event_rules_overview of this XiqAlertPolicy.  # noqa: E501

        A list of overviews of the event-based alert rules, grouped by category.  # noqa: E501

        :return: The event_rules_overview of this XiqAlertPolicy.  # noqa: E501
        :rtype: list[XiqAlertEventRulesByCategory]
        """
        return self._event_rules_overview

    @event_rules_overview.setter
    def event_rules_overview(self, event_rules_overview):
        """Sets the event_rules_overview of this XiqAlertPolicy.

        A list of overviews of the event-based alert rules, grouped by category.  # noqa: E501

        :param event_rules_overview: The event_rules_overview of this XiqAlertPolicy.  # noqa: E501
        :type: list[XiqAlertEventRulesByCategory]
        """

        self._event_rules_overview = event_rules_overview

    @property
    def metric_rules_overview(self):
        """Gets the metric_rules_overview of this XiqAlertPolicy.  # noqa: E501

        A list of overviews of the metric-based alert rules, grouped by metricset.  # noqa: E501

        :return: The metric_rules_overview of this XiqAlertPolicy.  # noqa: E501
        :rtype: list[XiqAlertMetricRulesByMetricset]
        """
        return self._metric_rules_overview

    @metric_rules_overview.setter
    def metric_rules_overview(self, metric_rules_overview):
        """Sets the metric_rules_overview of this XiqAlertPolicy.

        A list of overviews of the metric-based alert rules, grouped by metricset.  # noqa: E501

        :param metric_rules_overview: The metric_rules_overview of this XiqAlertPolicy.  # noqa: E501
        :type: list[XiqAlertMetricRulesByMetricset]
        """

        self._metric_rules_overview = metric_rules_overview

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
        if not isinstance(other, XiqAlertPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertPolicy):
            return True

        return self.to_dict() != other.to_dict()
