# extremecloudiq.model.xiq_device_installation_report.XiqDeviceInstallationReport

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**onboarded** | bool,  | BoolClass,  |  | [optional] 
**location_name** | str,  | str,  |  | [optional] 
**network_policy_name** | str,  | str,  |  | [optional] 
**device_template_name** | str,  | str,  |  | [optional] 
**ip_address** | str,  | str,  |  | [optional] 
**default_gateway** | str,  | str,  |  | [optional] 
**ntp_server** | str,  | str,  |  | [optional] 
**dns_server** | str,  | str,  |  | [optional] 
**enable_poe** | bool,  | BoolClass,  |  | [optional] 
**xiq_connectivity** | bool,  | BoolClass,  |  | [optional] 
**image_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[image_names](#image_names)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# image_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

