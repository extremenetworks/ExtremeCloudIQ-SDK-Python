# extremecloudiq.model.xiq_subnet_address_profile.XiqSubnetAddressProfile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**address_type** | [**XiqL3AddressType**](XiqL3AddressType.md) | [**XiqL3AddressType**](XiqL3AddressType.md) |  | 
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | Address profile name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**predefined** | bool,  | BoolClass,  | Flag to describe whether the application is predefined or customised | [optional] 
**description** | str,  | str,  | Address profile description | [optional] 
**value** | str,  | str,  | Address profile value | [optional] 
**enable_classification** | bool,  | BoolClass,  | The flag to enable classification on L3 address profile | [optional] 
**[classified_entries](#classified_entries)** | list, tuple,  | tuple,  | The address profile classified entries | [optional] 
**netmask** | str,  | str,  | The Subnet address netmask. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classified_entries

The address profile classified entries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The address profile classified entries | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAddressProfileClassifiedEntry**](XiqAddressProfileClassifiedEntry.md) | [**XiqAddressProfileClassifiedEntry**](XiqAddressProfileClassifiedEntry.md) | [**XiqAddressProfileClassifiedEntry**](XiqAddressProfileClassifiedEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

