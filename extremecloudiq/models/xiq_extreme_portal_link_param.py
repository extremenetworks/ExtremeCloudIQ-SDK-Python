# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqExtremePortalLinkParam(object):
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
        'base_url': 'str',
        'client_id': 'str',
        'response_type': 'str',
        'redirect_url': 'str',
        'state': 'str',
        'extreme_portal_url': 'str',
        'extr_sfdc_license_landing_url': 'str'
    }

    attribute_map = {
        'base_url': 'base_url',
        'client_id': 'client_id',
        'response_type': 'response_type',
        'redirect_url': 'redirect_url',
        'state': 'state',
        'extreme_portal_url': 'extreme_portal_url',
        'extr_sfdc_license_landing_url': 'extr_sfdc_license_landing_url'
    }

    def __init__(self, base_url=None, client_id=None, response_type=None, redirect_url=None, state=None, extreme_portal_url=None, extr_sfdc_license_landing_url=None, local_vars_configuration=None):  # noqa: E501
        """XiqExtremePortalLinkParam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_url = None
        self._client_id = None
        self._response_type = None
        self._redirect_url = None
        self._state = None
        self._extreme_portal_url = None
        self._extr_sfdc_license_landing_url = None
        self.discriminator = None

        if base_url is not None:
            self.base_url = base_url
        if client_id is not None:
            self.client_id = client_id
        if response_type is not None:
            self.response_type = response_type
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if state is not None:
            self.state = state
        if extreme_portal_url is not None:
            self.extreme_portal_url = extreme_portal_url
        if extr_sfdc_license_landing_url is not None:
            self.extr_sfdc_license_landing_url = extr_sfdc_license_landing_url

    @property
    def base_url(self):
        """Gets the base_url of this XiqExtremePortalLinkParam.  # noqa: E501

        Base Url  # noqa: E501

        :return: The base_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this XiqExtremePortalLinkParam.

        Base Url  # noqa: E501

        :param base_url: The base_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def client_id(self):
        """Gets the client_id of this XiqExtremePortalLinkParam.  # noqa: E501

        Client Id  # noqa: E501

        :return: The client_id of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this XiqExtremePortalLinkParam.

        Client Id  # noqa: E501

        :param client_id: The client_id of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def response_type(self):
        """Gets the response_type of this XiqExtremePortalLinkParam.  # noqa: E501

        Oauth response type, \"code\"  # noqa: E501

        :return: The response_type of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this XiqExtremePortalLinkParam.

        Oauth response type, \"code\"  # noqa: E501

        :param response_type: The response_type of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._response_type = response_type

    @property
    def redirect_url(self):
        """Gets the redirect_url of this XiqExtremePortalLinkParam.  # noqa: E501

        Oauth callback Url  # noqa: E501

        :return: The redirect_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this XiqExtremePortalLinkParam.

        Oauth callback Url  # noqa: E501

        :param redirect_url: The redirect_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def state(self):
        """Gets the state of this XiqExtremePortalLinkParam.  # noqa: E501

        Oauth state  # noqa: E501

        :return: The state of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this XiqExtremePortalLinkParam.

        Oauth state  # noqa: E501

        :param state: The state of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def extreme_portal_url(self):
        """Gets the extreme_portal_url of this XiqExtremePortalLinkParam.  # noqa: E501

        Extreme portal Url  # noqa: E501

        :return: The extreme_portal_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._extreme_portal_url

    @extreme_portal_url.setter
    def extreme_portal_url(self, extreme_portal_url):
        """Sets the extreme_portal_url of this XiqExtremePortalLinkParam.

        Extreme portal Url  # noqa: E501

        :param extreme_portal_url: The extreme_portal_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._extreme_portal_url = extreme_portal_url

    @property
    def extr_sfdc_license_landing_url(self):
        """Gets the extr_sfdc_license_landing_url of this XiqExtremePortalLinkParam.  # noqa: E501

        Extreme portal license landing Url  # noqa: E501

        :return: The extr_sfdc_license_landing_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :rtype: str
        """
        return self._extr_sfdc_license_landing_url

    @extr_sfdc_license_landing_url.setter
    def extr_sfdc_license_landing_url(self, extr_sfdc_license_landing_url):
        """Sets the extr_sfdc_license_landing_url of this XiqExtremePortalLinkParam.

        Extreme portal license landing Url  # noqa: E501

        :param extr_sfdc_license_landing_url: The extr_sfdc_license_landing_url of this XiqExtremePortalLinkParam.  # noqa: E501
        :type: str
        """

        self._extr_sfdc_license_landing_url = extr_sfdc_license_landing_url

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
        if not isinstance(other, XiqExtremePortalLinkParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExtremePortalLinkParam):
            return True

        return self.to_dict() != other.to_dict()
