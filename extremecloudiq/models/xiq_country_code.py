# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCountryCode(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AFGHANISTAN_4 = "AFGHANISTAN_4"
    ALGERIA_12 = "ALGERIA_12"
    ARGENTINA_32 = "ARGENTINA_32"
    ARUBA_533 = "ARUBA_533"
    AUSTRALIA_36 = "AUSTRALIA_36"
    AUSTRIA_40 = "AUSTRIA_40"
    AZERBAIJAN_31 = "AZERBAIJAN_31"
    BAHAMAS_44 = "BAHAMAS_44"
    BAHRAIN_48 = "BAHRAIN_48"
    BANGLADESH_50 = "BANGLADESH_50"
    BARBADOS_52 = "BARBADOS_52"
    BELARUS_112 = "BELARUS_112"
    BELGIUM_56 = "BELGIUM_56"
    BERMUDA_60 = "BERMUDA_60"
    BHUTAN_64 = "BHUTAN_64"
    BOLIVIA_68 = "BOLIVIA_68"
    BRAZIL_76 = "BRAZIL_76"
    BULGARIA_100 = "BULGARIA_100"
    CAMBODIA_116 = "CAMBODIA_116"
    CAMEROON_120 = "CAMEROON_120"
    CANADA_124 = "CANADA_124"
    CAYMAN_ISLANDS_136 = "CAYMAN_ISLANDS_136"
    CHILE_152 = "CHILE_152"
    COLOMBIA_170 = "COLOMBIA_170"
    COSTA_RICA_188 = "COSTA_RICA_188"
    CROATIA_191 = "CROATIA_191"
    CYPRUS_196 = "CYPRUS_196"
    CZECH_REPUBLIC_203 = "CZECH_REPUBLIC_203"
    DENMARK_208 = "DENMARK_208"
    DOMINICAN_REPUBLIC_214 = "DOMINICAN_REPUBLIC_214"
    ECUADOR_218 = "ECUADOR_218"
    EGYPT_818 = "EGYPT_818"
    EL_SALVADOR_222 = "EL_SALVADOR_222"
    ESTONIA_233 = "ESTONIA_233"
    FINLAND_246 = "FINLAND_246"
    FRANCE_250 = "FRANCE_250"
    FRENCH_GUIANA_254 = "FRENCH_GUIANA_254"
    GEORGIA_268 = "GEORGIA_268"
    GERMANY_276 = "GERMANY_276"
    GHANA_288 = "GHANA_288"
    GREECE_300 = "GREECE_300"
    GUAM_316 = "GUAM_316"
    GUATEMALA_320 = "GUATEMALA_320"
    GUYANA_328 = "GUYANA_328"
    HAITI_332 = "HAITI_332"
    HONDURAS_340 = "HONDURAS_340"
    HONG_KONG_344 = "HONG_KONG_344"
    HUNGARY_348 = "HUNGARY_348"
    ICELAND_352 = "ICELAND_352"
    INDIA_356 = "INDIA_356"
    INDONESIA_360 = "INDONESIA_360"
    IRELAND_372 = "IRELAND_372"
    PAKISTAN_586 = "PAKISTAN_586"
    ISRAEL_376 = "ISRAEL_376"
    ITALY_380 = "ITALY_380"
    JAMAICA_388 = "JAMAICA_388"
    JAPAN_4014 = "JAPAN_4014"
    JORDAN_400 = "JORDAN_400"
    KAZAKHSTAN_398 = "KAZAKHSTAN_398"
    KENYA_404 = "KENYA_404"
    KOREA_410 = "KOREA_410"
    KUWAIT_414 = "KUWAIT_414"
    KYRGYZSTAN_417 = "KYRGYZSTAN_417"
    LATVIA_428 = "LATVIA_428"
    LEBANON_422 = "LEBANON_422"
    LIECHTENSTEIN_438 = "LIECHTENSTEIN_438"
    LITHUANIA_440 = "LITHUANIA_440"
    LUXEMBOURG_442 = "LUXEMBOURG_442"
    MACAO_446 = "MACAO_446"
    MALAWI_454 = "MALAWI_454"
    MALAYSIA_458 = "MALAYSIA_458"
    MALTA_470 = "MALTA_470"
    MAURITIUS_480 = "MAURITIUS_480"
    MEXICO_484 = "MEXICO_484"
    MOLDOVA_498 = "MOLDOVA_498"
    MOROCCO_504 = "MOROCCO_504"
    MOZAMBIQUE_508 = "MOZAMBIQUE_508"
    NEPAL_524 = "NEPAL_524"
    NETHERLANDS_528 = "NETHERLANDS_528"
    NEW_CALEDONIA_540 = "NEW_CALEDONIA_540"
    NEW_ZEALAND_554 = "NEW_ZEALAND_554"
    NICARAGUA_558 = "NICARAGUA_558"
    NIGERIA_566 = "NIGERIA_566"
    NORWAY_578 = "NORWAY_578"
    OMAN_512 = "OMAN_512"
    PALAU_585 = "PALAU_585"
    PANAMA_591 = "PANAMA_591"
    PAPUA_NEW_GUINEA_598 = "PAPUA_NEW_GUINEA_598"
    PARAGUAY_600 = "PARAGUAY_600"
    CHINA_156 = "CHINA_156"
    PERU_604 = "PERU_604"
    POLAND_616 = "POLAND_616"
    PORTUGAL_620 = "PORTUGAL_620"
    PUERTO_RICO_630 = "PUERTO_RICO_630"
    QATAR_634 = "QATAR_634"
    PHILIPPINES_608 = "PHILIPPINES_608"
    ROMANIA_642 = "ROMANIA_642"
    RUSSIA_643 = "RUSSIA_643"
    SAUDI_ARABIA_682 = "SAUDI_ARABIA_682"
    SERBIA_688 = "SERBIA_688"
    SINGAPORE_702 = "SINGAPORE_702"
    SLOVAK_REPUBLIC_703 = "SLOVAK_REPUBLIC_703"
    SLOVENIA_705 = "SLOVENIA_705"
    SOUTH_AFRICA_710 = "SOUTH_AFRICA_710"
    SPAIN_724 = "SPAIN_724"
    SRI_LANKA_144 = "SRI_LANKA_144"
    SURINAME_740 = "SURINAME_740"
    SWEDEN_752 = "SWEDEN_752"
    SWITZERLAND_756 = "SWITZERLAND_756"
    TAIWAN_158 = "TAIWAN_158"
    TANZANIA_834 = "TANZANIA_834"
    THAILAND_764 = "THAILAND_764"
    REPUBLIC_OF_MACEDONIA_807 = "REPUBLIC_OF_MACEDONIA_807"
    TOGO_768 = "TOGO_768"
    TRINIDAD_Y_TOBAGO_780 = "TRINIDAD_Y_TOBAGO_780"
    TUNISIA_788 = "TUNISIA_788"
    TURKEY_792 = "TURKEY_792"
    TURKS_AND_CAICOS_ISLANDS_796 = "TURKS_AND_CAICOS_ISLANDS_796"
    U_A_E_784 = "U_A_E_784"
    US_VIRGIN_ISLANDS_850 = "US_VIRGIN_ISLANDS_850"
    UKRAINE_804 = "UKRAINE_804"
    UNITED_KINGDOM_826 = "UNITED_KINGDOM_826"
    UNITED_STATES_840 = "UNITED_STATES_840"
    URUGUAY_858 = "URUGUAY_858"
    VANUATU_548 = "VANUATU_548"
    VENEZUELA_862 = "VENEZUELA_862"
    VIETNAM_704 = "VIETNAM_704"

    allowable_values = [AFGHANISTAN_4, ALGERIA_12, ARGENTINA_32, ARUBA_533, AUSTRALIA_36, AUSTRIA_40, AZERBAIJAN_31, BAHAMAS_44, BAHRAIN_48, BANGLADESH_50, BARBADOS_52, BELARUS_112, BELGIUM_56, BERMUDA_60, BHUTAN_64, BOLIVIA_68, BRAZIL_76, BULGARIA_100, CAMBODIA_116, CAMEROON_120, CANADA_124, CAYMAN_ISLANDS_136, CHILE_152, COLOMBIA_170, COSTA_RICA_188, CROATIA_191, CYPRUS_196, CZECH_REPUBLIC_203, DENMARK_208, DOMINICAN_REPUBLIC_214, ECUADOR_218, EGYPT_818, EL_SALVADOR_222, ESTONIA_233, FINLAND_246, FRANCE_250, FRENCH_GUIANA_254, GEORGIA_268, GERMANY_276, GHANA_288, GREECE_300, GUAM_316, GUATEMALA_320, GUYANA_328, HAITI_332, HONDURAS_340, HONG_KONG_344, HUNGARY_348, ICELAND_352, INDIA_356, INDONESIA_360, IRELAND_372, PAKISTAN_586, ISRAEL_376, ITALY_380, JAMAICA_388, JAPAN_4014, JORDAN_400, KAZAKHSTAN_398, KENYA_404, KOREA_410, KUWAIT_414, KYRGYZSTAN_417, LATVIA_428, LEBANON_422, LIECHTENSTEIN_438, LITHUANIA_440, LUXEMBOURG_442, MACAO_446, MALAWI_454, MALAYSIA_458, MALTA_470, MAURITIUS_480, MEXICO_484, MOLDOVA_498, MOROCCO_504, MOZAMBIQUE_508, NEPAL_524, NETHERLANDS_528, NEW_CALEDONIA_540, NEW_ZEALAND_554, NICARAGUA_558, NIGERIA_566, NORWAY_578, OMAN_512, PALAU_585, PANAMA_591, PAPUA_NEW_GUINEA_598, PARAGUAY_600, CHINA_156, PERU_604, POLAND_616, PORTUGAL_620, PUERTO_RICO_630, QATAR_634, PHILIPPINES_608, ROMANIA_642, RUSSIA_643, SAUDI_ARABIA_682, SERBIA_688, SINGAPORE_702, SLOVAK_REPUBLIC_703, SLOVENIA_705, SOUTH_AFRICA_710, SPAIN_724, SRI_LANKA_144, SURINAME_740, SWEDEN_752, SWITZERLAND_756, TAIWAN_158, TANZANIA_834, THAILAND_764, REPUBLIC_OF_MACEDONIA_807, TOGO_768, TRINIDAD_Y_TOBAGO_780, TUNISIA_788, TURKEY_792, TURKS_AND_CAICOS_ISLANDS_796, U_A_E_784, US_VIRGIN_ISLANDS_850, UKRAINE_804, UNITED_KINGDOM_826, UNITED_STATES_840, URUGUAY_858, VANUATU_548, VENEZUELA_862, VIETNAM_704]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """XiqCountryCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, XiqCountryCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCountryCode):
            return True

        return self.to_dict() != other.to_dict()
