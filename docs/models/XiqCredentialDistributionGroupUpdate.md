# extremecloudiq.model.xiq_credential_distribution_group_update.XiqCredentialDistributionGroupUpdate

 The Credential Distribution Group 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  The Credential Distribution Group  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner ID of the Credential Distribution group | [optional] value must be a 64 bit integer
**group_type** | str,  | str,  | The Group type | [optional] 
**enable_email_approval** | bool,  | BoolClass,  | Whether email approval is enabled | [optional] 
**enable_user_limitation** | bool,  | BoolClass,  | Whether user limitation is enabled | [optional] 
**employee_group_type** | [**XiqEmployeeGroupType**](XiqEmployeeGroupType.md) | [**XiqEmployeeGroupType**](XiqEmployeeGroupType.md) |  | [optional] 
**[employee_groups](#employee_groups)** | list, tuple,  | tuple,  | The member employee groups | [optional] 
**name** | str,  | str,  | The name of the credential distribution group | [optional] 
**restrict_number** | str,  | str,  | Restriction on number of credentials per employee | [optional] 
**[user_groups](#user_groups)** | list, tuple,  | tuple,  | The UserGroups | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# employee_groups

The member employee groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The member employee groups | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqEmployeeGroupUpdate**](XiqEmployeeGroupUpdate.md) | [**XiqEmployeeGroupUpdate**](XiqEmployeeGroupUpdate.md) | [**XiqEmployeeGroupUpdate**](XiqEmployeeGroupUpdate.md) |  | 

# user_groups

The UserGroups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The UserGroups | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCdgUserGroups**](XiqCdgUserGroups.md) | [**XiqCdgUserGroups**](XiqCdgUserGroups.md) | [**XiqCdgUserGroups**](XiqCdgUserGroups.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

