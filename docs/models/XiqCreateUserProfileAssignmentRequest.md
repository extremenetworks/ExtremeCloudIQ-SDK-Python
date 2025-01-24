# extremecloudiq.model.xiq_create_user_profile_assignment_request.XiqCreateUserProfileAssignmentRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The user profile name | [optional] 
**description** | str,  | str,  | The user profile assignment description | [optional] 
**[folder_ids](#folder_ids)** | list, tuple,  | tuple,  | The location folder Id list | [optional] 
**assignment_radius_attribute** | [**XiqUserProfileAssignmentRadiusAttribute**](XiqUserProfileAssignmentRadiusAttribute.md) | [**XiqUserProfileAssignmentRadiusAttribute**](XiqUserProfileAssignmentRadiusAttribute.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# folder_ids

The location folder Id list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The location folder Id list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The location folder Id list | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

