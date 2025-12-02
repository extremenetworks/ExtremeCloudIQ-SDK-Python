# extremecloudiq.model.xiq_airrm_get_device_regulatory_config_afc_spectrum_response.XIQAirrmGetDeviceRegulatoryConfigAfcSpectrumResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ap_mode** | str,  | str,  |  | [optional] 
**country_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**antenna_info** | str,  | str,  |  | [optional] must be one of ["INDOOR", "OUTDOOR", "UNDERSEAT", ] 
**[regulatory_configurations](#regulatory_configurations)** | list, tuple,  | tuple,  |  | [optional] 
**afc_spectrum** | [**XIQAirrmAfcSpectrum**](XIQAirrmAfcSpectrum.md) | [**XIQAirrmAfcSpectrum**](XIQAirrmAfcSpectrum.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# regulatory_configurations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XIQAirrmRegulatoryConfiguration**](XIQAirrmRegulatoryConfiguration.md) | [**XIQAirrmRegulatoryConfiguration**](XIQAirrmRegulatoryConfiguration.md) | [**XIQAirrmRegulatoryConfiguration**](XIQAirrmRegulatoryConfiguration.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

