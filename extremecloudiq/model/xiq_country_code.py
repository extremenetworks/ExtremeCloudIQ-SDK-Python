# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.2.0.123
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from extremecloudiq import schemas  # noqa: F401


class XiqCountryCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The organization country code.
    """


    class MetaOapg:
        enum_value_to_name = {
            "AFGHANISTAN_4": "AFGHANISTAN_4",
            "ALBANIA_8": "ALBANIA_8",
            "ALGERIA_12": "ALGERIA_12",
            "AMERICAN_SAMOA_16": "AMERICAN_SAMOA_16",
            "ANDORRA_20": "ANDORRA_20",
            "ANGOLA_24": "ANGOLA_24",
            "ANTARCTICA_10": "ANTARCTICA_10",
            "ANTIGUA_AND_BARBUDA_28": "ANTIGUA_AND_BARBUDA_28",
            "ARGENTINA_32": "ARGENTINA_32",
            "ARMENIA_51": "ARMENIA_51",
            "ARUBA_533": "ARUBA_533",
            "AUSTRALIA_36": "AUSTRALIA_36",
            "AUSTRIA_40": "AUSTRIA_40",
            "AZERBAIJAN_31": "AZERBAIJAN_31",
            "BAHAMAS_44": "BAHAMAS_44",
            "BAHRAIN_48": "BAHRAIN_48",
            "BANGLADESH_50": "BANGLADESH_50",
            "BARBADOS_52": "BARBADOS_52",
            "BELARUS_112": "BELARUS_112",
            "BELGIUM_56": "BELGIUM_56",
            "BELIZE_84": "BELIZE_84",
            "BENIN_204": "BENIN_204",
            "BERMUDA_60": "BERMUDA_60",
            "BHUTAN_64": "BHUTAN_64",
            "BOLIVIA_68": "BOLIVIA_68",
            "BOSNIA_AND_HERZEGOVINA_70": "BOSNIA_AND_HERZEGOVINA_70",
            "BOTSWANA_72": "BOTSWANA_72",
            "BRAZIL_76": "BRAZIL_76",
            "BRITISH_VIRGIN_ISLANDS_92": "BRITISH_VIRGIN_ISLANDS_92",
            "BRUNEI_96": "BRUNEI_96",
            "BULGARIA_100": "BULGARIA_100",
            "BURKINA_FASO_854": "BURKINA_FASO_854",
            "BURUNDI_108": "BURUNDI_108",
            "CAMBODIA_116": "CAMBODIA_116",
            "CAMEROON_120": "CAMEROON_120",
            "CANADA_124": "CANADA_124",
            "CAPE_VERDE_132": "CAPE_VERDE_132",
            "CAYMAN_ISLANDS_136": "CAYMAN_ISLANDS_136",
            "CENTRAL_AFRICAN_REPUBLIC_140": "CENTRAL_AFRICAN_REPUBLIC_140",
            "CHAD_148": "CHAD_148",
            "CHILE_152": "CHILE_152",
            "CHINA_156": "CHINA_156",
            "COLOMBIA_170": "COLOMBIA_170",
            "COMOROS_174": "COMOROS_174",
            "CONGO_178": "CONGO_178",
            "CONGO_THE_DEMOCRATIC_REPUBLIC_180": "CONGO_THE_DEMOCRATIC_REPUBLIC_180",
            "COOK_ISLANDS_184": "COOK_ISLANDS_184",
            "COSTA_RICA_188": "COSTA_RICA_188",
            "CROATIA_191": "CROATIA_191",
            "CYPRUS_196": "CYPRUS_196",
            "CZECH_REPUBLIC_203": "CZECH_REPUBLIC_203",
            "COTE_D_IVOIRE": "COTE_D_IVOIRE",
            "DENMARK_208": "DENMARK_208",
            "DJIBOUTI_262": "DJIBOUTI_262",
            "DOMINICA_212": "DOMINICA_212",
            "DOMINICAN_REPUBLIC_214": "DOMINICAN_REPUBLIC_214",
            "ECUADOR_218": "ECUADOR_218",
            "EGYPT_818": "EGYPT_818",
            "EL_SALVADOR_222": "EL_SALVADOR_222",
            "EQUATORIAL_GUINEA_226": "EQUATORIAL_GUINEA_226",
            "ERITREA_232": "ERITREA_232",
            "ESTONIA_233": "ESTONIA_233",
            "ETHIOPIA_231": "ETHIOPIA_231",
            "FALKLAND_ISLANDS_238": "FALKLAND_ISLANDS_238",
            "FAROE_ISLANDS_234": "FAROE_ISLANDS_234",
            "FIJI_242": "FIJI_242",
            "FINLAND_246": "FINLAND_246",
            "FRANCE_250": "FRANCE_250",
            "FRENCH_GUIANA_254": "FRENCH_GUIANA_254",
            "FRENCH_POLYNESIA_258": "FRENCH_POLYNESIA_258",
            "GABON_266": "GABON_266",
            "GAMBIA_270": "GAMBIA_270",
            "GEORGIA_268": "GEORGIA_268",
            "GERMANY_276": "GERMANY_276",
            "GHANA_288": "GHANA_288",
            "GIBRALTAR_292": "GIBRALTAR_292",
            "GREECE_300": "GREECE_300",
            "GREENLAND_304": "GREENLAND_304",
            "GRENADA_308": "GRENADA_308",
            "GUADELOUPE_312": "GUADELOUPE_312",
            "GUAM_316": "GUAM_316",
            "GUATEMALA_320": "GUATEMALA_320",
            "GUERNSEY_831": "GUERNSEY_831",
            "GUINEA_324": "GUINEA_324",
            "GUINEA_BISSAU_624": "GUINEA_BISSAU_624",
            "GUYANA_328": "GUYANA_328",
            "HAITI_332": "HAITI_332",
            "HOLY_SEE_336": "HOLY_SEE_336",
            "HONDURAS_340": "HONDURAS_340",
            "HONG_KONG_344": "HONG_KONG_344",
            "HUNGARY_348": "HUNGARY_348",
            "ICELAND_352": "ICELAND_352",
            "INDIA_356": "INDIA_356",
            "INDONESIA_360": "INDONESIA_360",
            "IRAN_364": "IRAN_364",
            "IRAQ_368": "IRAQ_368",
            "IRELAND_372": "IRELAND_372",
            "ISLE_OF_MAN_833": "ISLE_OF_MAN_833",
            "ISRAEL_376": "ISRAEL_376",
            "ITALY_380": "ITALY_380",
            "JAMAICA_388": "JAMAICA_388",
            "JAPAN_4014": "JAPAN_4014",
            "JERSEY_832": "JERSEY_832",
            "JORDAN_400": "JORDAN_400",
            "KAZAKHSTAN_398": "KAZAKHSTAN_398",
            "KENYA_404": "KENYA_404",
            "KIRIBATI_296": "KIRIBATI_296",
            "KOREA_410": "KOREA_410",
            "KUWAIT_414": "KUWAIT_414",
            "KYRGYZSTAN_417": "KYRGYZSTAN_417",
            "LAOS_418": "LAOS_418",
            "LATVIA_428": "LATVIA_428",
            "LEBANON_422": "LEBANON_422",
            "LESOTHO_426": "LESOTHO_426",
            "LIBERIA_430": "LIBERIA_430",
            "LIBYA_434": "LIBYA_434",
            "LIECHTENSTEIN_438": "LIECHTENSTEIN_438",
            "LITHUANIA_440": "LITHUANIA_440",
            "LUXEMBOURG_442": "LUXEMBOURG_442",
            "MACAO_446": "MACAO_446",
            "MADAGASCAR_450": "MADAGASCAR_450",
            "MALAWI_454": "MALAWI_454",
            "MALAYSIA_458": "MALAYSIA_458",
            "MALDIVES_462": "MALDIVES_462",
            "MALI_466": "MALI_466",
            "MALTA_470": "MALTA_470",
            "MARTINIQUE_474": "MARTINIQUE_474",
            "MAURITANIA_478": "MAURITANIA_478",
            "MAURITIUS_480": "MAURITIUS_480",
            "MEXICO_484": "MEXICO_484",
            "MICRONESIA_583": "MICRONESIA_583",
            "MOLDOVA_498": "MOLDOVA_498",
            "MONACO_492": "MONACO_492",
            "MONGOLIA_496": "MONGOLIA_496",
            "MONTENEGRO_499": "MONTENEGRO_499",
            "MOROCCO_504": "MOROCCO_504",
            "MOZAMBIQUE_508": "MOZAMBIQUE_508",
            "MYANMAR_104": "MYANMAR_104",
            "NAMIBIA_516": "NAMIBIA_516",
            "NEPAL_524": "NEPAL_524",
            "NETHERLANDS_528": "NETHERLANDS_528",
            "NEW_CALEDONIA_540": "NEW_CALEDONIA_540",
            "NEW_ZEALAND_554": "NEW_ZEALAND_554",
            "NICARAGUA_558": "NICARAGUA_558",
            "NIGER_562": "NIGER_562",
            "NIGERIA_566": "NIGERIA_566",
            "NORTH_KOREA_408_": "NORTH_KOREA_408_",
            "NORWAY_578": "NORWAY_578",
            "OMAN_512": "OMAN_512",
            "PAKISTAN_586": "PAKISTAN_586",
            "PALAU_585": "PALAU_585",
            "PALESTINE_275": "PALESTINE_275",
            "PANAMA_591": "PANAMA_591",
            "PAPUA_NEW_GUINEA_598": "PAPUA_NEW_GUINEA_598",
            "PARAGUAY_600": "PARAGUAY_600",
            "PERU_604": "PERU_604",
            "PHILIPPINES_608": "PHILIPPINES_608",
            "POLAND_616": "POLAND_616",
            "PORTUGAL_620": "PORTUGAL_620",
            "PUERTO_RICO_630": "PUERTO_RICO_630",
            "QATAR_634": "QATAR_634",
            "REPUBLIC_OF_MACEDONIA_807": "REPUBLIC_OF_MACEDONIA_807",
            "REUNION_638": "REUNION_638",
            "ROMANIA_642": "ROMANIA_642",
            "RUSSIA_643": "RUSSIA_643",
            "RWANDA_646": "RWANDA_646",
            "SAINT_KITTS_AND_NEVIS_659": "SAINT_KITTS_AND_NEVIS_659",
            "SAINT_LUCIA_662": "SAINT_LUCIA_662",
            "SAINT_VINCENT_AND_THE_GRENADINES_670": "SAINT_VINCENT_AND_THE_GRENADINES_670",
            "SAMOA_882": "SAMOA_882",
            "SAN_MARINO_674": "SAN_MARINO_674",
            "SAUDI_ARABIA_682": "SAUDI_ARABIA_682",
            "SENEGAL_686": "SENEGAL_686",
            "SERBIA_688": "SERBIA_688",
            "SEYCHELLES_690": "SEYCHELLES_690",
            "SIERRA_LEONE_694": "SIERRA_LEONE_694",
            "SINGAPORE_702": "SINGAPORE_702",
            "SLOVAK_REPUBLIC_703": "SLOVAK_REPUBLIC_703",
            "SLOVENIA_705": "SLOVENIA_705",
            "SOLOMON_ISLANDS_90": "SOLOMON_ISLANDS_90",
            "SOMALIA_706": "SOMALIA_706",
            "SOUTH_AFRICA_710": "SOUTH_AFRICA_710",
            "SPAIN_724": "SPAIN_724",
            "SRI_LANKA_144": "SRI_LANKA_144",
            "SUDAN_729": "SUDAN_729",
            "SURINAME_740": "SURINAME_740",
            "SWAZILAND_748": "SWAZILAND_748",
            "SWEDEN_752": "SWEDEN_752",
            "SWITZERLAND_756": "SWITZERLAND_756",
            "SYRIA_760": "SYRIA_760",
            "TAIWAN_158": "TAIWAN_158",
            "TAJIKISTAN_762": "TAJIKISTAN_762",
            "TANZANIA_834": "TANZANIA_834",
            "THAILAND_764": "THAILAND_764",
            "TIMOR_LESTE_626": "TIMOR_LESTE_626",
            "TOGO_768": "TOGO_768",
            "TONGA_776": "TONGA_776",
            "TRINIDAD_Y_TOBAGO_780": "TRINIDAD_Y_TOBAGO_780",
            "TUNISIA_788": "TUNISIA_788",
            "TURKEY_792": "TURKEY_792",
            "TURKMENISTAN_795": "TURKMENISTAN_795",
            "TURKS_AND_CAICOS_ISLANDS_796": "TURKS_AND_CAICOS_ISLANDS_796",
            "U_A_E_784": "U_A_E_784",
            "UGANDA_800": "UGANDA_800",
            "UKRAINE_804": "UKRAINE_804",
            "UNITED_KINGDOM_826": "UNITED_KINGDOM_826",
            "UNITED_STATES_840": "UNITED_STATES_840",
            "URUGUAY_858": "URUGUAY_858",
            "US_VIRGIN_ISLANDS_850": "US_VIRGIN_ISLANDS_850",
            "UZBEKISTAN_860": "UZBEKISTAN_860",
            "VANUATU_548": "VANUATU_548",
            "VENEZUELA_862": "VENEZUELA_862",
            "VIETNAM_704": "VIETNAM_704",
            "WALLIS_AND_FUTUNA_876": "WALLIS_AND_FUTUNA_876",
            "YEMEN_887": "YEMEN_887",
            "ZAMBIA_894": "ZAMBIA_894",
            "ZIMBABWE_716": "ZIMBABWE_716",
        }
    
    @schemas.classproperty
    def AFGHANISTAN_4(cls):
        return cls("AFGHANISTAN_4")
    
    @schemas.classproperty
    def ALBANIA_8(cls):
        return cls("ALBANIA_8")
    
    @schemas.classproperty
    def ALGERIA_12(cls):
        return cls("ALGERIA_12")
    
    @schemas.classproperty
    def AMERICAN_SAMOA_16(cls):
        return cls("AMERICAN_SAMOA_16")
    
    @schemas.classproperty
    def ANDORRA_20(cls):
        return cls("ANDORRA_20")
    
    @schemas.classproperty
    def ANGOLA_24(cls):
        return cls("ANGOLA_24")
    
    @schemas.classproperty
    def ANTARCTICA_10(cls):
        return cls("ANTARCTICA_10")
    
    @schemas.classproperty
    def ANTIGUA_AND_BARBUDA_28(cls):
        return cls("ANTIGUA_AND_BARBUDA_28")
    
    @schemas.classproperty
    def ARGENTINA_32(cls):
        return cls("ARGENTINA_32")
    
    @schemas.classproperty
    def ARMENIA_51(cls):
        return cls("ARMENIA_51")
    
    @schemas.classproperty
    def ARUBA_533(cls):
        return cls("ARUBA_533")
    
    @schemas.classproperty
    def AUSTRALIA_36(cls):
        return cls("AUSTRALIA_36")
    
    @schemas.classproperty
    def AUSTRIA_40(cls):
        return cls("AUSTRIA_40")
    
    @schemas.classproperty
    def AZERBAIJAN_31(cls):
        return cls("AZERBAIJAN_31")
    
    @schemas.classproperty
    def BAHAMAS_44(cls):
        return cls("BAHAMAS_44")
    
    @schemas.classproperty
    def BAHRAIN_48(cls):
        return cls("BAHRAIN_48")
    
    @schemas.classproperty
    def BANGLADESH_50(cls):
        return cls("BANGLADESH_50")
    
    @schemas.classproperty
    def BARBADOS_52(cls):
        return cls("BARBADOS_52")
    
    @schemas.classproperty
    def BELARUS_112(cls):
        return cls("BELARUS_112")
    
    @schemas.classproperty
    def BELGIUM_56(cls):
        return cls("BELGIUM_56")
    
    @schemas.classproperty
    def BELIZE_84(cls):
        return cls("BELIZE_84")
    
    @schemas.classproperty
    def BENIN_204(cls):
        return cls("BENIN_204")
    
    @schemas.classproperty
    def BERMUDA_60(cls):
        return cls("BERMUDA_60")
    
    @schemas.classproperty
    def BHUTAN_64(cls):
        return cls("BHUTAN_64")
    
    @schemas.classproperty
    def BOLIVIA_68(cls):
        return cls("BOLIVIA_68")
    
    @schemas.classproperty
    def BOSNIA_AND_HERZEGOVINA_70(cls):
        return cls("BOSNIA_AND_HERZEGOVINA_70")
    
    @schemas.classproperty
    def BOTSWANA_72(cls):
        return cls("BOTSWANA_72")
    
    @schemas.classproperty
    def BRAZIL_76(cls):
        return cls("BRAZIL_76")
    
    @schemas.classproperty
    def BRITISH_VIRGIN_ISLANDS_92(cls):
        return cls("BRITISH_VIRGIN_ISLANDS_92")
    
    @schemas.classproperty
    def BRUNEI_96(cls):
        return cls("BRUNEI_96")
    
    @schemas.classproperty
    def BULGARIA_100(cls):
        return cls("BULGARIA_100")
    
    @schemas.classproperty
    def BURKINA_FASO_854(cls):
        return cls("BURKINA_FASO_854")
    
    @schemas.classproperty
    def BURUNDI_108(cls):
        return cls("BURUNDI_108")
    
    @schemas.classproperty
    def CAMBODIA_116(cls):
        return cls("CAMBODIA_116")
    
    @schemas.classproperty
    def CAMEROON_120(cls):
        return cls("CAMEROON_120")
    
    @schemas.classproperty
    def CANADA_124(cls):
        return cls("CANADA_124")
    
    @schemas.classproperty
    def CAPE_VERDE_132(cls):
        return cls("CAPE_VERDE_132")
    
    @schemas.classproperty
    def CAYMAN_ISLANDS_136(cls):
        return cls("CAYMAN_ISLANDS_136")
    
    @schemas.classproperty
    def CENTRAL_AFRICAN_REPUBLIC_140(cls):
        return cls("CENTRAL_AFRICAN_REPUBLIC_140")
    
    @schemas.classproperty
    def CHAD_148(cls):
        return cls("CHAD_148")
    
    @schemas.classproperty
    def CHILE_152(cls):
        return cls("CHILE_152")
    
    @schemas.classproperty
    def CHINA_156(cls):
        return cls("CHINA_156")
    
    @schemas.classproperty
    def COLOMBIA_170(cls):
        return cls("COLOMBIA_170")
    
    @schemas.classproperty
    def COMOROS_174(cls):
        return cls("COMOROS_174")
    
    @schemas.classproperty
    def CONGO_178(cls):
        return cls("CONGO_178")
    
    @schemas.classproperty
    def CONGO_THE_DEMOCRATIC_REPUBLIC_180(cls):
        return cls("CONGO_THE_DEMOCRATIC_REPUBLIC_180")
    
    @schemas.classproperty
    def COOK_ISLANDS_184(cls):
        return cls("COOK_ISLANDS_184")
    
    @schemas.classproperty
    def COSTA_RICA_188(cls):
        return cls("COSTA_RICA_188")
    
    @schemas.classproperty
    def CROATIA_191(cls):
        return cls("CROATIA_191")
    
    @schemas.classproperty
    def CYPRUS_196(cls):
        return cls("CYPRUS_196")
    
    @schemas.classproperty
    def CZECH_REPUBLIC_203(cls):
        return cls("CZECH_REPUBLIC_203")
    
    @schemas.classproperty
    def COTE_D_IVOIRE(cls):
        return cls("COTE_D_IVOIRE")
    
    @schemas.classproperty
    def DENMARK_208(cls):
        return cls("DENMARK_208")
    
    @schemas.classproperty
    def DJIBOUTI_262(cls):
        return cls("DJIBOUTI_262")
    
    @schemas.classproperty
    def DOMINICA_212(cls):
        return cls("DOMINICA_212")
    
    @schemas.classproperty
    def DOMINICAN_REPUBLIC_214(cls):
        return cls("DOMINICAN_REPUBLIC_214")
    
    @schemas.classproperty
    def ECUADOR_218(cls):
        return cls("ECUADOR_218")
    
    @schemas.classproperty
    def EGYPT_818(cls):
        return cls("EGYPT_818")
    
    @schemas.classproperty
    def EL_SALVADOR_222(cls):
        return cls("EL_SALVADOR_222")
    
    @schemas.classproperty
    def EQUATORIAL_GUINEA_226(cls):
        return cls("EQUATORIAL_GUINEA_226")
    
    @schemas.classproperty
    def ERITREA_232(cls):
        return cls("ERITREA_232")
    
    @schemas.classproperty
    def ESTONIA_233(cls):
        return cls("ESTONIA_233")
    
    @schemas.classproperty
    def ETHIOPIA_231(cls):
        return cls("ETHIOPIA_231")
    
    @schemas.classproperty
    def FALKLAND_ISLANDS_238(cls):
        return cls("FALKLAND_ISLANDS_238")
    
    @schemas.classproperty
    def FAROE_ISLANDS_234(cls):
        return cls("FAROE_ISLANDS_234")
    
    @schemas.classproperty
    def FIJI_242(cls):
        return cls("FIJI_242")
    
    @schemas.classproperty
    def FINLAND_246(cls):
        return cls("FINLAND_246")
    
    @schemas.classproperty
    def FRANCE_250(cls):
        return cls("FRANCE_250")
    
    @schemas.classproperty
    def FRENCH_GUIANA_254(cls):
        return cls("FRENCH_GUIANA_254")
    
    @schemas.classproperty
    def FRENCH_POLYNESIA_258(cls):
        return cls("FRENCH_POLYNESIA_258")
    
    @schemas.classproperty
    def GABON_266(cls):
        return cls("GABON_266")
    
    @schemas.classproperty
    def GAMBIA_270(cls):
        return cls("GAMBIA_270")
    
    @schemas.classproperty
    def GEORGIA_268(cls):
        return cls("GEORGIA_268")
    
    @schemas.classproperty
    def GERMANY_276(cls):
        return cls("GERMANY_276")
    
    @schemas.classproperty
    def GHANA_288(cls):
        return cls("GHANA_288")
    
    @schemas.classproperty
    def GIBRALTAR_292(cls):
        return cls("GIBRALTAR_292")
    
    @schemas.classproperty
    def GREECE_300(cls):
        return cls("GREECE_300")
    
    @schemas.classproperty
    def GREENLAND_304(cls):
        return cls("GREENLAND_304")
    
    @schemas.classproperty
    def GRENADA_308(cls):
        return cls("GRENADA_308")
    
    @schemas.classproperty
    def GUADELOUPE_312(cls):
        return cls("GUADELOUPE_312")
    
    @schemas.classproperty
    def GUAM_316(cls):
        return cls("GUAM_316")
    
    @schemas.classproperty
    def GUATEMALA_320(cls):
        return cls("GUATEMALA_320")
    
    @schemas.classproperty
    def GUERNSEY_831(cls):
        return cls("GUERNSEY_831")
    
    @schemas.classproperty
    def GUINEA_324(cls):
        return cls("GUINEA_324")
    
    @schemas.classproperty
    def GUINEA_BISSAU_624(cls):
        return cls("GUINEA_BISSAU_624")
    
    @schemas.classproperty
    def GUYANA_328(cls):
        return cls("GUYANA_328")
    
    @schemas.classproperty
    def HAITI_332(cls):
        return cls("HAITI_332")
    
    @schemas.classproperty
    def HOLY_SEE_336(cls):
        return cls("HOLY_SEE_336")
    
    @schemas.classproperty
    def HONDURAS_340(cls):
        return cls("HONDURAS_340")
    
    @schemas.classproperty
    def HONG_KONG_344(cls):
        return cls("HONG_KONG_344")
    
    @schemas.classproperty
    def HUNGARY_348(cls):
        return cls("HUNGARY_348")
    
    @schemas.classproperty
    def ICELAND_352(cls):
        return cls("ICELAND_352")
    
    @schemas.classproperty
    def INDIA_356(cls):
        return cls("INDIA_356")
    
    @schemas.classproperty
    def INDONESIA_360(cls):
        return cls("INDONESIA_360")
    
    @schemas.classproperty
    def IRAN_364(cls):
        return cls("IRAN_364")
    
    @schemas.classproperty
    def IRAQ_368(cls):
        return cls("IRAQ_368")
    
    @schemas.classproperty
    def IRELAND_372(cls):
        return cls("IRELAND_372")
    
    @schemas.classproperty
    def ISLE_OF_MAN_833(cls):
        return cls("ISLE_OF_MAN_833")
    
    @schemas.classproperty
    def ISRAEL_376(cls):
        return cls("ISRAEL_376")
    
    @schemas.classproperty
    def ITALY_380(cls):
        return cls("ITALY_380")
    
    @schemas.classproperty
    def JAMAICA_388(cls):
        return cls("JAMAICA_388")
    
    @schemas.classproperty
    def JAPAN_4014(cls):
        return cls("JAPAN_4014")
    
    @schemas.classproperty
    def JERSEY_832(cls):
        return cls("JERSEY_832")
    
    @schemas.classproperty
    def JORDAN_400(cls):
        return cls("JORDAN_400")
    
    @schemas.classproperty
    def KAZAKHSTAN_398(cls):
        return cls("KAZAKHSTAN_398")
    
    @schemas.classproperty
    def KENYA_404(cls):
        return cls("KENYA_404")
    
    @schemas.classproperty
    def KIRIBATI_296(cls):
        return cls("KIRIBATI_296")
    
    @schemas.classproperty
    def KOREA_410(cls):
        return cls("KOREA_410")
    
    @schemas.classproperty
    def KUWAIT_414(cls):
        return cls("KUWAIT_414")
    
    @schemas.classproperty
    def KYRGYZSTAN_417(cls):
        return cls("KYRGYZSTAN_417")
    
    @schemas.classproperty
    def LAOS_418(cls):
        return cls("LAOS_418")
    
    @schemas.classproperty
    def LATVIA_428(cls):
        return cls("LATVIA_428")
    
    @schemas.classproperty
    def LEBANON_422(cls):
        return cls("LEBANON_422")
    
    @schemas.classproperty
    def LESOTHO_426(cls):
        return cls("LESOTHO_426")
    
    @schemas.classproperty
    def LIBERIA_430(cls):
        return cls("LIBERIA_430")
    
    @schemas.classproperty
    def LIBYA_434(cls):
        return cls("LIBYA_434")
    
    @schemas.classproperty
    def LIECHTENSTEIN_438(cls):
        return cls("LIECHTENSTEIN_438")
    
    @schemas.classproperty
    def LITHUANIA_440(cls):
        return cls("LITHUANIA_440")
    
    @schemas.classproperty
    def LUXEMBOURG_442(cls):
        return cls("LUXEMBOURG_442")
    
    @schemas.classproperty
    def MACAO_446(cls):
        return cls("MACAO_446")
    
    @schemas.classproperty
    def MADAGASCAR_450(cls):
        return cls("MADAGASCAR_450")
    
    @schemas.classproperty
    def MALAWI_454(cls):
        return cls("MALAWI_454")
    
    @schemas.classproperty
    def MALAYSIA_458(cls):
        return cls("MALAYSIA_458")
    
    @schemas.classproperty
    def MALDIVES_462(cls):
        return cls("MALDIVES_462")
    
    @schemas.classproperty
    def MALI_466(cls):
        return cls("MALI_466")
    
    @schemas.classproperty
    def MALTA_470(cls):
        return cls("MALTA_470")
    
    @schemas.classproperty
    def MARTINIQUE_474(cls):
        return cls("MARTINIQUE_474")
    
    @schemas.classproperty
    def MAURITANIA_478(cls):
        return cls("MAURITANIA_478")
    
    @schemas.classproperty
    def MAURITIUS_480(cls):
        return cls("MAURITIUS_480")
    
    @schemas.classproperty
    def MEXICO_484(cls):
        return cls("MEXICO_484")
    
    @schemas.classproperty
    def MICRONESIA_583(cls):
        return cls("MICRONESIA_583")
    
    @schemas.classproperty
    def MOLDOVA_498(cls):
        return cls("MOLDOVA_498")
    
    @schemas.classproperty
    def MONACO_492(cls):
        return cls("MONACO_492")
    
    @schemas.classproperty
    def MONGOLIA_496(cls):
        return cls("MONGOLIA_496")
    
    @schemas.classproperty
    def MONTENEGRO_499(cls):
        return cls("MONTENEGRO_499")
    
    @schemas.classproperty
    def MOROCCO_504(cls):
        return cls("MOROCCO_504")
    
    @schemas.classproperty
    def MOZAMBIQUE_508(cls):
        return cls("MOZAMBIQUE_508")
    
    @schemas.classproperty
    def MYANMAR_104(cls):
        return cls("MYANMAR_104")
    
    @schemas.classproperty
    def NAMIBIA_516(cls):
        return cls("NAMIBIA_516")
    
    @schemas.classproperty
    def NEPAL_524(cls):
        return cls("NEPAL_524")
    
    @schemas.classproperty
    def NETHERLANDS_528(cls):
        return cls("NETHERLANDS_528")
    
    @schemas.classproperty
    def NEW_CALEDONIA_540(cls):
        return cls("NEW_CALEDONIA_540")
    
    @schemas.classproperty
    def NEW_ZEALAND_554(cls):
        return cls("NEW_ZEALAND_554")
    
    @schemas.classproperty
    def NICARAGUA_558(cls):
        return cls("NICARAGUA_558")
    
    @schemas.classproperty
    def NIGER_562(cls):
        return cls("NIGER_562")
    
    @schemas.classproperty
    def NIGERIA_566(cls):
        return cls("NIGERIA_566")
    
    @schemas.classproperty
    def NORTH_KOREA_408_(cls):
        return cls("NORTH_KOREA_408_")
    
    @schemas.classproperty
    def NORWAY_578(cls):
        return cls("NORWAY_578")
    
    @schemas.classproperty
    def OMAN_512(cls):
        return cls("OMAN_512")
    
    @schemas.classproperty
    def PAKISTAN_586(cls):
        return cls("PAKISTAN_586")
    
    @schemas.classproperty
    def PALAU_585(cls):
        return cls("PALAU_585")
    
    @schemas.classproperty
    def PALESTINE_275(cls):
        return cls("PALESTINE_275")
    
    @schemas.classproperty
    def PANAMA_591(cls):
        return cls("PANAMA_591")
    
    @schemas.classproperty
    def PAPUA_NEW_GUINEA_598(cls):
        return cls("PAPUA_NEW_GUINEA_598")
    
    @schemas.classproperty
    def PARAGUAY_600(cls):
        return cls("PARAGUAY_600")
    
    @schemas.classproperty
    def PERU_604(cls):
        return cls("PERU_604")
    
    @schemas.classproperty
    def PHILIPPINES_608(cls):
        return cls("PHILIPPINES_608")
    
    @schemas.classproperty
    def POLAND_616(cls):
        return cls("POLAND_616")
    
    @schemas.classproperty
    def PORTUGAL_620(cls):
        return cls("PORTUGAL_620")
    
    @schemas.classproperty
    def PUERTO_RICO_630(cls):
        return cls("PUERTO_RICO_630")
    
    @schemas.classproperty
    def QATAR_634(cls):
        return cls("QATAR_634")
    
    @schemas.classproperty
    def REPUBLIC_OF_MACEDONIA_807(cls):
        return cls("REPUBLIC_OF_MACEDONIA_807")
    
    @schemas.classproperty
    def REUNION_638(cls):
        return cls("REUNION_638")
    
    @schemas.classproperty
    def ROMANIA_642(cls):
        return cls("ROMANIA_642")
    
    @schemas.classproperty
    def RUSSIA_643(cls):
        return cls("RUSSIA_643")
    
    @schemas.classproperty
    def RWANDA_646(cls):
        return cls("RWANDA_646")
    
    @schemas.classproperty
    def SAINT_KITTS_AND_NEVIS_659(cls):
        return cls("SAINT_KITTS_AND_NEVIS_659")
    
    @schemas.classproperty
    def SAINT_LUCIA_662(cls):
        return cls("SAINT_LUCIA_662")
    
    @schemas.classproperty
    def SAINT_VINCENT_AND_THE_GRENADINES_670(cls):
        return cls("SAINT_VINCENT_AND_THE_GRENADINES_670")
    
    @schemas.classproperty
    def SAMOA_882(cls):
        return cls("SAMOA_882")
    
    @schemas.classproperty
    def SAN_MARINO_674(cls):
        return cls("SAN_MARINO_674")
    
    @schemas.classproperty
    def SAUDI_ARABIA_682(cls):
        return cls("SAUDI_ARABIA_682")
    
    @schemas.classproperty
    def SENEGAL_686(cls):
        return cls("SENEGAL_686")
    
    @schemas.classproperty
    def SERBIA_688(cls):
        return cls("SERBIA_688")
    
    @schemas.classproperty
    def SEYCHELLES_690(cls):
        return cls("SEYCHELLES_690")
    
    @schemas.classproperty
    def SIERRA_LEONE_694(cls):
        return cls("SIERRA_LEONE_694")
    
    @schemas.classproperty
    def SINGAPORE_702(cls):
        return cls("SINGAPORE_702")
    
    @schemas.classproperty
    def SLOVAK_REPUBLIC_703(cls):
        return cls("SLOVAK_REPUBLIC_703")
    
    @schemas.classproperty
    def SLOVENIA_705(cls):
        return cls("SLOVENIA_705")
    
    @schemas.classproperty
    def SOLOMON_ISLANDS_90(cls):
        return cls("SOLOMON_ISLANDS_90")
    
    @schemas.classproperty
    def SOMALIA_706(cls):
        return cls("SOMALIA_706")
    
    @schemas.classproperty
    def SOUTH_AFRICA_710(cls):
        return cls("SOUTH_AFRICA_710")
    
    @schemas.classproperty
    def SPAIN_724(cls):
        return cls("SPAIN_724")
    
    @schemas.classproperty
    def SRI_LANKA_144(cls):
        return cls("SRI_LANKA_144")
    
    @schemas.classproperty
    def SUDAN_729(cls):
        return cls("SUDAN_729")
    
    @schemas.classproperty
    def SURINAME_740(cls):
        return cls("SURINAME_740")
    
    @schemas.classproperty
    def SWAZILAND_748(cls):
        return cls("SWAZILAND_748")
    
    @schemas.classproperty
    def SWEDEN_752(cls):
        return cls("SWEDEN_752")
    
    @schemas.classproperty
    def SWITZERLAND_756(cls):
        return cls("SWITZERLAND_756")
    
    @schemas.classproperty
    def SYRIA_760(cls):
        return cls("SYRIA_760")
    
    @schemas.classproperty
    def TAIWAN_158(cls):
        return cls("TAIWAN_158")
    
    @schemas.classproperty
    def TAJIKISTAN_762(cls):
        return cls("TAJIKISTAN_762")
    
    @schemas.classproperty
    def TANZANIA_834(cls):
        return cls("TANZANIA_834")
    
    @schemas.classproperty
    def THAILAND_764(cls):
        return cls("THAILAND_764")
    
    @schemas.classproperty
    def TIMOR_LESTE_626(cls):
        return cls("TIMOR_LESTE_626")
    
    @schemas.classproperty
    def TOGO_768(cls):
        return cls("TOGO_768")
    
    @schemas.classproperty
    def TONGA_776(cls):
        return cls("TONGA_776")
    
    @schemas.classproperty
    def TRINIDAD_Y_TOBAGO_780(cls):
        return cls("TRINIDAD_Y_TOBAGO_780")
    
    @schemas.classproperty
    def TUNISIA_788(cls):
        return cls("TUNISIA_788")
    
    @schemas.classproperty
    def TURKEY_792(cls):
        return cls("TURKEY_792")
    
    @schemas.classproperty
    def TURKMENISTAN_795(cls):
        return cls("TURKMENISTAN_795")
    
    @schemas.classproperty
    def TURKS_AND_CAICOS_ISLANDS_796(cls):
        return cls("TURKS_AND_CAICOS_ISLANDS_796")
    
    @schemas.classproperty
    def U_A_E_784(cls):
        return cls("U_A_E_784")
    
    @schemas.classproperty
    def UGANDA_800(cls):
        return cls("UGANDA_800")
    
    @schemas.classproperty
    def UKRAINE_804(cls):
        return cls("UKRAINE_804")
    
    @schemas.classproperty
    def UNITED_KINGDOM_826(cls):
        return cls("UNITED_KINGDOM_826")
    
    @schemas.classproperty
    def UNITED_STATES_840(cls):
        return cls("UNITED_STATES_840")
    
    @schemas.classproperty
    def URUGUAY_858(cls):
        return cls("URUGUAY_858")
    
    @schemas.classproperty
    def US_VIRGIN_ISLANDS_850(cls):
        return cls("US_VIRGIN_ISLANDS_850")
    
    @schemas.classproperty
    def UZBEKISTAN_860(cls):
        return cls("UZBEKISTAN_860")
    
    @schemas.classproperty
    def VANUATU_548(cls):
        return cls("VANUATU_548")
    
    @schemas.classproperty
    def VENEZUELA_862(cls):
        return cls("VENEZUELA_862")
    
    @schemas.classproperty
    def VIETNAM_704(cls):
        return cls("VIETNAM_704")
    
    @schemas.classproperty
    def WALLIS_AND_FUTUNA_876(cls):
        return cls("WALLIS_AND_FUTUNA_876")
    
    @schemas.classproperty
    def YEMEN_887(cls):
        return cls("YEMEN_887")
    
    @schemas.classproperty
    def ZAMBIA_894(cls):
        return cls("ZAMBIA_894")
    
    @schemas.classproperty
    def ZIMBABWE_716(cls):
        return cls("ZIMBABWE_716")
