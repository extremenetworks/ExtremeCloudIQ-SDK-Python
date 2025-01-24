# extremecloudiq.model.xiq_viq.XiqViq

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**devices** | decimal.Decimal, int,  | decimal.Decimal,  | Total # of all licensed devices | [optional] value must be a 32 bit integer
**standalone** | bool,  | BoolClass,  | Returns true if HIQ is not enabled, otherwise returns false | [optional] 
**expired** | bool,  | BoolClass,  | Whether VIQ is expired | [optional] 
**customer_id** | str,  | str,  | The customer ID, also known as Salesforce customer ID | [optional] 
**vhm_id** | str,  | str,  | The VIQ ID | [optional] 
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner account ID | [optional] value must be a 64 bit integer
**[licenses](#licenses)** | list, tuple,  | tuple,  | The license list | [optional] 
**partner_id** | str,  | str,  | The partner ID | [optional] 
**partner_email** | str,  | str,  | The partner email | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# licenses

The license list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The license list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqViqLicense**](XiqViqLicense.md) | [**XiqViqLicense**](XiqViqLicense.md) | [**XiqViqLicense**](XiqViqLicense.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

