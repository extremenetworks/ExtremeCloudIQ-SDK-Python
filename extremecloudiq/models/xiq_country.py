# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCountry(object):
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
        'dial_code': 'str',
        'alpha2_code': 'str',
        'country_code': 'int',
        'internal_country_codes': 'list[int]',
        'short_name': 'str',
        'name_en': 'str',
        'name_jp': 'str',
        'name_fr': 'str',
        'name_de': 'str',
        'name_it': 'str',
        'name_pt': 'str',
        'name_zh': 'str',
        'name_es': 'str',
        'name_ko': 'str'
    }

    attribute_map = {
        'dial_code': 'dial_code',
        'alpha2_code': 'alpha2_code',
        'country_code': 'country_code',
        'internal_country_codes': 'internal_country_codes',
        'short_name': 'short_name',
        'name_en': 'name_en',
        'name_jp': 'name_jp',
        'name_fr': 'name_fr',
        'name_de': 'name_de',
        'name_it': 'name_it',
        'name_pt': 'name_pt',
        'name_zh': 'name_zh',
        'name_es': 'name_es',
        'name_ko': 'name_ko'
    }

    def __init__(self, dial_code=None, alpha2_code=None, country_code=None, internal_country_codes=None, short_name=None, name_en=None, name_jp=None, name_fr=None, name_de=None, name_it=None, name_pt=None, name_zh=None, name_es=None, name_ko=None, local_vars_configuration=None):  # noqa: E501
        """XiqCountry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dial_code = None
        self._alpha2_code = None
        self._country_code = None
        self._internal_country_codes = None
        self._short_name = None
        self._name_en = None
        self._name_jp = None
        self._name_fr = None
        self._name_de = None
        self._name_it = None
        self._name_pt = None
        self._name_zh = None
        self._name_es = None
        self._name_ko = None
        self.discriminator = None

        if dial_code is not None:
            self.dial_code = dial_code
        if alpha2_code is not None:
            self.alpha2_code = alpha2_code
        if country_code is not None:
            self.country_code = country_code
        if internal_country_codes is not None:
            self.internal_country_codes = internal_country_codes
        if short_name is not None:
            self.short_name = short_name
        if name_en is not None:
            self.name_en = name_en
        if name_jp is not None:
            self.name_jp = name_jp
        if name_fr is not None:
            self.name_fr = name_fr
        if name_de is not None:
            self.name_de = name_de
        if name_it is not None:
            self.name_it = name_it
        if name_pt is not None:
            self.name_pt = name_pt
        if name_zh is not None:
            self.name_zh = name_zh
        if name_es is not None:
            self.name_es = name_es
        if name_ko is not None:
            self.name_ko = name_ko

    @property
    def dial_code(self):
        """Gets the dial_code of this XiqCountry.  # noqa: E501

        The dialing code for international calls, typically prefixed by the '+' key for mobile.  # noqa: E501

        :return: The dial_code of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._dial_code

    @dial_code.setter
    def dial_code(self, dial_code):
        """Sets the dial_code of this XiqCountry.

        The dialing code for international calls, typically prefixed by the '+' key for mobile.  # noqa: E501

        :param dial_code: The dial_code of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._dial_code = dial_code

    @property
    def alpha2_code(self):
        """Gets the alpha2_code of this XiqCountry.  # noqa: E501

        The country ISO 2-letter code.  # noqa: E501

        :return: The alpha2_code of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._alpha2_code

    @alpha2_code.setter
    def alpha2_code(self, alpha2_code):
        """Sets the alpha2_code of this XiqCountry.

        The country ISO 2-letter code.  # noqa: E501

        :param alpha2_code: The alpha2_code of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._alpha2_code = alpha2_code

    @property
    def country_code(self):
        """Gets the country_code of this XiqCountry.  # noqa: E501

        The country ISO numeric code.  # noqa: E501

        :return: The country_code of this XiqCountry.  # noqa: E501
        :rtype: int
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this XiqCountry.

        The country ISO numeric code.  # noqa: E501

        :param country_code: The country_code of this XiqCountry.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                country_code is not None and country_code > 999):  # noqa: E501
            raise ValueError("Invalid value for `country_code`, must be a value less than or equal to `999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country_code is not None and country_code < 1):  # noqa: E501
            raise ValueError("Invalid value for `country_code`, must be a value greater than or equal to `1`")  # noqa: E501

        self._country_code = country_code

    @property
    def internal_country_codes(self):
        """Gets the internal_country_codes of this XiqCountry.  # noqa: E501

        Extreme IQ internal country codes.  # noqa: E501

        :return: The internal_country_codes of this XiqCountry.  # noqa: E501
        :rtype: list[int]
        """
        return self._internal_country_codes

    @internal_country_codes.setter
    def internal_country_codes(self, internal_country_codes):
        """Sets the internal_country_codes of this XiqCountry.

        Extreme IQ internal country codes.  # noqa: E501

        :param internal_country_codes: The internal_country_codes of this XiqCountry.  # noqa: E501
        :type: list[int]
        """

        self._internal_country_codes = internal_country_codes

    @property
    def short_name(self):
        """Gets the short_name of this XiqCountry.  # noqa: E501

        The country short name.  # noqa: E501

        :return: The short_name of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this XiqCountry.

        The country short name.  # noqa: E501

        :param short_name: The short_name of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def name_en(self):
        """Gets the name_en of this XiqCountry.  # noqa: E501

        The country official name in English.  # noqa: E501

        :return: The name_en of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this XiqCountry.

        The country official name in English.  # noqa: E501

        :param name_en: The name_en of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_en = name_en

    @property
    def name_jp(self):
        """Gets the name_jp of this XiqCountry.  # noqa: E501

        The country official name in Japanese.  # noqa: E501

        :return: The name_jp of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_jp

    @name_jp.setter
    def name_jp(self, name_jp):
        """Sets the name_jp of this XiqCountry.

        The country official name in Japanese.  # noqa: E501

        :param name_jp: The name_jp of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_jp = name_jp

    @property
    def name_fr(self):
        """Gets the name_fr of this XiqCountry.  # noqa: E501

        The country official name in French.  # noqa: E501

        :return: The name_fr of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_fr

    @name_fr.setter
    def name_fr(self, name_fr):
        """Sets the name_fr of this XiqCountry.

        The country official name in French.  # noqa: E501

        :param name_fr: The name_fr of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_fr = name_fr

    @property
    def name_de(self):
        """Gets the name_de of this XiqCountry.  # noqa: E501

        The country official name in German.  # noqa: E501

        :return: The name_de of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_de

    @name_de.setter
    def name_de(self, name_de):
        """Sets the name_de of this XiqCountry.

        The country official name in German.  # noqa: E501

        :param name_de: The name_de of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_de = name_de

    @property
    def name_it(self):
        """Gets the name_it of this XiqCountry.  # noqa: E501

        The country official name in Italian.  # noqa: E501

        :return: The name_it of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_it

    @name_it.setter
    def name_it(self, name_it):
        """Sets the name_it of this XiqCountry.

        The country official name in Italian.  # noqa: E501

        :param name_it: The name_it of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_it = name_it

    @property
    def name_pt(self):
        """Gets the name_pt of this XiqCountry.  # noqa: E501

        The country official name in Portuguese.  # noqa: E501

        :return: The name_pt of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_pt

    @name_pt.setter
    def name_pt(self, name_pt):
        """Sets the name_pt of this XiqCountry.

        The country official name in Portuguese.  # noqa: E501

        :param name_pt: The name_pt of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_pt = name_pt

    @property
    def name_zh(self):
        """Gets the name_zh of this XiqCountry.  # noqa: E501

        The country official name in Chinese.  # noqa: E501

        :return: The name_zh of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        """Sets the name_zh of this XiqCountry.

        The country official name in Chinese.  # noqa: E501

        :param name_zh: The name_zh of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_zh = name_zh

    @property
    def name_es(self):
        """Gets the name_es of this XiqCountry.  # noqa: E501

        The country official name in Spanish.  # noqa: E501

        :return: The name_es of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_es

    @name_es.setter
    def name_es(self, name_es):
        """Sets the name_es of this XiqCountry.

        The country official name in Spanish.  # noqa: E501

        :param name_es: The name_es of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_es = name_es

    @property
    def name_ko(self):
        """Gets the name_ko of this XiqCountry.  # noqa: E501

        The country official name in Korean.  # noqa: E501

        :return: The name_ko of this XiqCountry.  # noqa: E501
        :rtype: str
        """
        return self._name_ko

    @name_ko.setter
    def name_ko(self, name_ko):
        """Sets the name_ko of this XiqCountry.

        The country official name in Korean.  # noqa: E501

        :param name_ko: The name_ko of this XiqCountry.  # noqa: E501
        :type: str
        """

        self._name_ko = name_ko

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
        if not isinstance(other, XiqCountry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCountry):
            return True

        return self.to_dict() != other.to_dict()
