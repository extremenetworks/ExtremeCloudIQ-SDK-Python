# extremecloudiq.model.xiq_user_group.XiqUserGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password_settings** | [**XiqPasswordSettings**](XiqPasswordSettings.md) | [**XiqPasswordSettings**](XiqPasswordSettings.md) |  | 
**[ssids](#ssids)** | list, tuple,  | tuple,  | The ssids | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**password_type** | [**XiqPasswordType**](XiqPasswordType.md) | [**XiqPasswordType**](XiqPasswordType.md) |  | 
**user_count** | decimal.Decimal, int,  | decimal.Decimal,  | The user count | value must be a 32 bit integer
**name** | str,  | str,  | The user group name | 
**expiration_settings** | [**XiqExpirationSettings**](XiqExpirationSettings.md) | [**XiqExpirationSettings**](XiqExpirationSettings.md) |  | 
**password_db_location** | [**XiqPasswordDbLocation**](XiqPasswordDbLocation.md) | [**XiqPasswordDbLocation**](XiqPasswordDbLocation.md) |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**predefined** | bool,  | BoolClass,  | Whether it is predefined | 
**delivery_settings** | [**XiqDeliverySettings**](XiqDeliverySettings.md) | [**XiqDeliverySettings**](XiqDeliverySettings.md) |  | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The user group description | [optional] 
**pcg_use_only** | bool,  | BoolClass,  |  Whether it&#x27;s for PCG use only | [optional] 
**pcg_type** | [**XiqPcgType**](XiqPcgType.md) | [**XiqPcgType**](XiqPcgType.md) |  | [optional] 
**ppsk_use_only** | bool,  | BoolClass,  | Whether it&#x27;s for PPSK use only | [optional] 
**enable_cwp_reg** | bool,  | BoolClass,  | Whether to enable CWP registration setting | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssids

The ssids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The ssids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The ssids | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

