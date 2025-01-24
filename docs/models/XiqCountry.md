# extremecloudiq.model.xiq_country.XiqCountry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dial_code** | str,  | str,  | The dialing code for international calls, typically prefixed by the &#x27;+&#x27; key for mobile. | [optional] 
**alpha2_code** | str,  | str,  | The country ISO 2-letter code. | [optional] 
**country_code** | decimal.Decimal, int,  | decimal.Decimal,  | The country ISO numeric code. | [optional] value must be a 32 bit integer
**[internal_country_codes](#internal_country_codes)** | list, tuple,  | tuple,  | Extreme IQ internal country codes. | [optional] 
**short_name** | str,  | str,  | The country short name. | [optional] 
**name_en** | str,  | str,  | The country official name in English. | [optional] 
**name_jp** | str,  | str,  | The country official name in Japanese. | [optional] 
**name_fr** | str,  | str,  | The country official name in French. | [optional] 
**name_de** | str,  | str,  | The country official name in German. | [optional] 
**name_it** | str,  | str,  | The country official name in Italian. | [optional] 
**name_pt** | str,  | str,  | The country official name in Portuguese. | [optional] 
**name_zh** | str,  | str,  | The country official name in Chinese. | [optional] 
**name_es** | str,  | str,  | The country official name in Spanish. | [optional] 
**name_ko** | str,  | str,  | The country official name in Korean. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# internal_country_codes

Extreme IQ internal country codes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Extreme IQ internal country codes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | Extreme IQ internal country codes. | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

