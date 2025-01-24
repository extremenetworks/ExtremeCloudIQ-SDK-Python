# extremecloudiq.model.xiq_create_user_group_request.XiqCreateUserGroupRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password_settings** | [**XiqPasswordSettings**](XiqPasswordSettings.md) | [**XiqPasswordSettings**](XiqPasswordSettings.md) |  | 
**password_type** | [**XiqPasswordType**](XiqPasswordType.md) | [**XiqPasswordType**](XiqPasswordType.md) |  | 
**name** | str,  | str,  | The user group name | 
**expiration_settings** | [**XiqExpirationSettings**](XiqExpirationSettings.md) | [**XiqExpirationSettings**](XiqExpirationSettings.md) |  | 
**password_db_location** | [**XiqPasswordDbLocation**](XiqPasswordDbLocation.md) | [**XiqPasswordDbLocation**](XiqPasswordDbLocation.md) |  | 
**delivery_settings** | [**XiqDeliverySettings**](XiqDeliverySettings.md) | [**XiqDeliverySettings**](XiqDeliverySettings.md) |  | 
**description** | str,  | str,  | The user group description | [optional] 
**ppsk_use_only** | bool,  | BoolClass,  | Whether it&#x27;s for PPSK use only | [optional] 
**enable_max_clients_per_ppsk** | bool,  | BoolClass,  | The enablement for the maximum number of clients per private PSK | [optional] 
**max_clients_per_ppsk** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of clients per private PSK | [optional] value must be a 32 bit integer
**pcg_use_only** | bool,  | BoolClass,  | Whether it&#x27;s for PCG use only | [optional] 
**pcg_type** | [**XiqPcgType**](XiqPcgType.md) | [**XiqPcgType**](XiqPcgType.md) |  | [optional] 
**enable_cwp_reg** | bool,  | BoolClass,  | Whether to enable CWP registration setting | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

