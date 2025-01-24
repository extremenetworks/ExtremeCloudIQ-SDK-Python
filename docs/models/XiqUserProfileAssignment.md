# extremecloudiq.model.xiq_user_profile_assignment.XiqUserProfileAssignment

The payload of User Profile Assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of User Profile Assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The user profile name | [optional] 
**description** | str,  | str,  | The user profile assignment description | [optional] 
**authorisation_policy** | str,  | str,  | The Authorization policy name | [optional] 
**[folder_ids](#folder_ids)** | list, tuple,  | tuple,  | The location folder Id list | [optional] 
**assignment_radius_attribute** | [**XiqUserProfileAssignmentRadiusAttribute**](XiqUserProfileAssignmentRadiusAttribute.md) | [**XiqUserProfileAssignmentRadiusAttribute**](XiqUserProfileAssignmentRadiusAttribute.md) |  | [optional] 
**[user_group](#user_group)** | list, tuple,  | tuple,  | The set of User groups. | [optional] 
**[mac_object_profiles](#mac_object_profiles)** | list, tuple,  | tuple,  | The set of Mac object profiles. | [optional] 
**[os_object_dhcp](#os_object_dhcp)** | list, tuple,  | tuple,  | The set of OS DHCP objects. | [optional] 
**[os_object_https](#os_object_https)** | list, tuple,  | tuple,  | The set of OS HTTP objects. | [optional] 
**[schedules](#schedules)** | list, tuple,  | tuple,  | The set of OS HTTP objects. | [optional] 
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

# user_group

The set of User groups.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of User groups. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUserGroup**](XiqUserGroup.md) | [**XiqUserGroup**](XiqUserGroup.md) | [**XiqUserGroup**](XiqUserGroup.md) |  | 

# mac_object_profiles

The set of Mac object profiles.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of Mac object profiles. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqMacObject**](XiqMacObject.md) | [**XiqMacObject**](XiqMacObject.md) | [**XiqMacObject**](XiqMacObject.md) |  | 

# os_object_dhcp

The set of OS DHCP objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of OS DHCP objects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqOsObject**](XiqOsObject.md) | [**XiqOsObject**](XiqOsObject.md) | [**XiqOsObject**](XiqOsObject.md) |  | 

# os_object_https

The set of OS HTTP objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of OS HTTP objects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqOsObject**](XiqOsObject.md) | [**XiqOsObject**](XiqOsObject.md) | [**XiqOsObject**](XiqOsObject.md) |  | 

# schedules

The set of OS HTTP objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of OS HTTP objects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqSchedule**](XiqSchedule.md) | [**XiqSchedule**](XiqSchedule.md) | [**XiqSchedule**](XiqSchedule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

