# extremecloudiq.model.xiq_create_l3_address_profile_request.XiqCreateL3AddressProfileRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address_type** | [**XiqL3AddressType**](XiqL3AddressType.md) | [**XiqL3AddressType**](XiqL3AddressType.md) |  | 
**name** | str,  | str,  | The L3 Address profile name | 
**value** | str,  | str,  | The L3 Address profile value | 
**description** | str,  | str,  | The L3 Address profile description | [optional] 
**enable_classification** | bool,  | BoolClass,  | The flag to enable classification entries on host name address profile | [optional] 
**[classified_entries](#classified_entries)** | list, tuple,  | tuple,  | The host name address profile classified entries | [optional] 
**ip_address_end** | str,  | str,  | The classified entry IP address end, only available for \&quot;IP_RANGE\&quot; address type | [optional] 
**netmask** | str,  | str,  | The classified entry IP address end, only available for \&quot;IP_SUBNET\&quot; address type | [optional] 
**wildcard_mask** | str,  | str,  | The wildcard address profile mask value, only available for \&quot;WILDCARD\&quot; address type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classified_entries

The host name address profile classified entries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The host name address profile classified entries | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAddressProfileClassifiedEntry**](XiqAddressProfileClassifiedEntry.md) | [**XiqAddressProfileClassifiedEntry**](XiqAddressProfileClassifiedEntry.md) | [**XiqAddressProfileClassifiedEntry**](XiqAddressProfileClassifiedEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

