# extremecloudiq.model.xiq_credential_distribution_group_create_request.XiqCredentialDistributionGroupCreateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**employee_group_type** | [**XiqEmployeeGroupType**](XiqEmployeeGroupType.md) | [**XiqEmployeeGroupType**](XiqEmployeeGroupType.md) |  | 
**enable_email_approval** | bool,  | BoolClass,  | Flag indicating whether email approval is enabled (true) or disabled (false). | 
**name** | str,  | str,  | Name of the credential distribution group. | 
**enable_user_limitation** | bool,  | BoolClass,  | Flag indicating whether user limitation is enabled (true) or disabled (false). | 
**[employee_groups](#employee_groups)** | list, tuple,  | tuple,  | Array of member groups. | [optional] 
**restrict_number** | decimal.Decimal, int,  | decimal.Decimal,  | Number restriction. | [optional] value must be a 32 bit integer
**[user_group_ids](#user_group_ids)** | list, tuple,  | tuple,  | Array of user group IDs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# employee_groups

Array of member groups.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of member groups. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqEmployeeGroup**](XiqEmployeeGroup.md) | [**XiqEmployeeGroup**](XiqEmployeeGroup.md) | [**XiqEmployeeGroup**](XiqEmployeeGroup.md) |  | 

# user_group_ids

Array of user group IDs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of user group IDs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | Array of user group IDs. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

