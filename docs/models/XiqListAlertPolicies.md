# extremecloudiq.model.xiq_list_alert_policies.XiqListAlertPolicies

The List Alert Policy Response Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The List Alert Policy Response Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**global_policy** | [**XiqAlertPolicy**](XiqAlertPolicy.md) | [**XiqAlertPolicy**](XiqAlertPolicy.md) |  | [optional] 
**[site_policies](#site_policies)** | list, tuple,  | tuple,  | The site alert policy List | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_policies

The site alert policy List

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The site alert policy List | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertPolicy**](XiqAlertPolicy.md) | [**XiqAlertPolicy**](XiqAlertPolicy.md) | [**XiqAlertPolicy**](XiqAlertPolicy.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

