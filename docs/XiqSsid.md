# XiqSsid

The SSID
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The SSID profile name | 
**broadcast_name** | **str** | The SSID broadcast name | 
**description** | **str** | The SSID description | [optional] 
**predefined** | **bool** | Whether it is predefined | 
**advanced_settings_id** | **int** | The SSID advanced settings ID. | [optional] 
**enable_user_profile_assignment** | **bool** | The flag to enable User Profile Assignment. | [optional] 
**enable_radius_attribute_user_profile_assignment** | **bool** | The flag to enable Radius Attribute User Profile Assignment. | [optional] 
**attribute_type** | [**XiqAttributeType**](XiqAttributeType.md) |  | [optional] 
**attribute_key** | **int** | The SSID attribute key. | [optional] 
**access_security** | [**XiqSsidAccessSecurity**](XiqSsidAccessSecurity.md) |  | [optional] 
**radius_client_profile** | [**XiqRadiusClientProfile**](XiqRadiusClientProfile.md) |  | [optional] 
**default_user_profile** | **int** | The default User Profile ID. | [optional] 
**vendor_id** | **int** | The vendor id, when the Attribute type is CUSTOM. | [optional] 
**user_profile_assignment_rules** | [**list[XiqUserProfileAssignmentRule]**](XiqUserProfileAssignmentRule.md) | The SSID user profile assignment rules. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


