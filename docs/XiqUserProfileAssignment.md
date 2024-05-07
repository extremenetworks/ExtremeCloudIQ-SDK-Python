# XiqUserProfileAssignment

The payload of User Profile Assignment
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The user profile name | [optional] 
**description** | **str** | The user profile assignment description | [optional] 
**authorisation_policy** | **str** | The Authorization policy name | [optional] 
**folder_ids** | **list[int]** | The location folder Id list | [optional] 
**assignment_radius_attribute** | [**XiqUserProfileAssignmentRadiusAttribute**](XiqUserProfileAssignmentRadiusAttribute.md) |  | [optional] 
**user_group** | [**list[XiqUserGroup]**](XiqUserGroup.md) | The set of User groups. | [optional] 
**mac_object_profiles** | [**list[XiqMacObject]**](XiqMacObject.md) | The set of Mac object profiles. | [optional] 
**os_object_dhcp** | [**list[XiqOsObject]**](XiqOsObject.md) | The set of OS DHCP objects. | [optional] 
**os_object_https** | [**list[XiqOsObject]**](XiqOsObject.md) | The set of OS HTTP objects. | [optional] 
**schedules** | [**list[XiqSchedule]**](XiqSchedule.md) | The set of OS HTTP objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


