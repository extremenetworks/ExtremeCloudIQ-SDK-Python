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


class ServicesHealth(object):
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
        'overall_score': 'int',
        'network_services_score': 'int',
        'authentication_services_score': 'int',
        'management_services_score': 'int'
    }

    attribute_map = {
        'overall_score': 'overall_score',
        'network_services_score': 'network_services_score',
        'authentication_services_score': 'authentication_services_score',
        'management_services_score': 'management_services_score'
    }

    def __init__(self, overall_score=None, network_services_score=None, authentication_services_score=None, management_services_score=None, local_vars_configuration=None):  # noqa: E501
        """ServicesHealth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall_score = None
        self._network_services_score = None
        self._authentication_services_score = None
        self._management_services_score = None
        self.discriminator = None

        if overall_score is not None:
            self.overall_score = overall_score
        if network_services_score is not None:
            self.network_services_score = network_services_score
        if authentication_services_score is not None:
            self.authentication_services_score = authentication_services_score
        if management_services_score is not None:
            self.management_services_score = management_services_score

    @property
    def overall_score(self):
        """Gets the overall_score of this ServicesHealth.  # noqa: E501

        The overall health score  # noqa: E501

        :return: The overall_score of this ServicesHealth.  # noqa: E501
        :rtype: int
        """
        return self._overall_score

    @overall_score.setter
    def overall_score(self, overall_score):
        """Sets the overall_score of this ServicesHealth.

        The overall health score  # noqa: E501

        :param overall_score: The overall_score of this ServicesHealth.  # noqa: E501
        :type: int
        """

        self._overall_score = overall_score

    @property
    def network_services_score(self):
        """Gets the network_services_score of this ServicesHealth.  # noqa: E501

        The health score of network services  # noqa: E501

        :return: The network_services_score of this ServicesHealth.  # noqa: E501
        :rtype: int
        """
        return self._network_services_score

    @network_services_score.setter
    def network_services_score(self, network_services_score):
        """Sets the network_services_score of this ServicesHealth.

        The health score of network services  # noqa: E501

        :param network_services_score: The network_services_score of this ServicesHealth.  # noqa: E501
        :type: int
        """

        self._network_services_score = network_services_score

    @property
    def authentication_services_score(self):
        """Gets the authentication_services_score of this ServicesHealth.  # noqa: E501

        The health score of authentication services  # noqa: E501

        :return: The authentication_services_score of this ServicesHealth.  # noqa: E501
        :rtype: int
        """
        return self._authentication_services_score

    @authentication_services_score.setter
    def authentication_services_score(self, authentication_services_score):
        """Sets the authentication_services_score of this ServicesHealth.

        The health score of authentication services  # noqa: E501

        :param authentication_services_score: The authentication_services_score of this ServicesHealth.  # noqa: E501
        :type: int
        """

        self._authentication_services_score = authentication_services_score

    @property
    def management_services_score(self):
        """Gets the management_services_score of this ServicesHealth.  # noqa: E501

        The health score of management services  # noqa: E501

        :return: The management_services_score of this ServicesHealth.  # noqa: E501
        :rtype: int
        """
        return self._management_services_score

    @management_services_score.setter
    def management_services_score(self, management_services_score):
        """Sets the management_services_score of this ServicesHealth.

        The health score of management services  # noqa: E501

        :param management_services_score: The management_services_score of this ServicesHealth.  # noqa: E501
        :type: int
        """

        self._management_services_score = management_services_score

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
        if not isinstance(other, ServicesHealth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServicesHealth):
            return True

        return self.to_dict() != other.to_dict()
