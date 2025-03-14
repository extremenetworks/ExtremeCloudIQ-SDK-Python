# extremecloudiq.model.xiq_cdg_user_groups.XiqCdgUserGroups

 The User Group of Credential Distribution Group 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  The User Group of Credential Distribution Group  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner ID | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The User Group Name | [optional] 
**json_type** | str,  | str,  | JSON Type | [optional] 
**description** | str,  | str,  | The user group description | [optional] 
**password_rule_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The password rule settings id | [optional] value must be a 64 bit integer
**delivery_policy_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The delivery policy settings id | [optional] value must be a 64 bit integer
**time_expiration_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The time expiration settings id | [optional] value must be a 64 bit integer
**user_count** | decimal.Decimal, int,  | decimal.Decimal,  | The user count | [optional] value must be a 32 bit integer
**[ssids](#ssids)** | list, tuple,  | tuple,  | The list of SSIDs | [optional] 
**group_type** | str,  | str,  | The user group type | [optional] 
**pcg_use_only** | bool,  | BoolClass,  | Whether PCG use only is enabled | [optional] 
**ppsk_use_only** | bool,  | BoolClass,  | Whether PPSK use only is enabled | [optional] 
**enable_pcg_filter** | bool,  | BoolClass,  | Whether PCG filter is enabled | [optional] 
**enable_self_reg** | bool,  | BoolClass,  | Whether self reg is enabled | [optional] 
**enable_renew** | bool,  | BoolClass,  | Whether renew is enabled | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssids

The list of SSIDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of SSIDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The list of SSIDs | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

