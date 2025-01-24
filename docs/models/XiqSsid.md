# extremecloudiq.model.xiq_ssid.XiqSsid

The SSID

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The SSID | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The SSID profile name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**broadcast_name** | str,  | str,  | The SSID broadcast name | 
**predefined** | bool,  | BoolClass,  | Whether it is predefined | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The SSID description | [optional] 
**advanced_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The SSID advanced settings ID. | [optional] value must be a 64 bit integer
**enable_user_profile_assignment** | bool,  | BoolClass,  | The flag to enable User Profile Assignment. | [optional] 
**enable_radius_attribute_user_profile_assignment** | bool,  | BoolClass,  | The flag to enable Radius Attribute User Profile Assignment. | [optional] 
**attribute_type** | [**XiqAttributeType**](XiqAttributeType.md) | [**XiqAttributeType**](XiqAttributeType.md) |  | [optional] 
**attribute_key** | decimal.Decimal, int,  | decimal.Decimal,  | The SSID attribute key. | [optional] value must be a 32 bit integer
**access_security** | [**XiqSsidAccessSecurity**](XiqSsidAccessSecurity.md) | [**XiqSsidAccessSecurity**](XiqSsidAccessSecurity.md) |  | [optional] 
**radius_client_profile** | [**XiqRadiusClientProfile**](XiqRadiusClientProfile.md) | [**XiqRadiusClientProfile**](XiqRadiusClientProfile.md) |  | [optional] 
**default_user_profile** | decimal.Decimal, int,  | decimal.Decimal,  | The default User Profile ID. | [optional] value must be a 64 bit integer
**vendor_id** | decimal.Decimal, int,  | decimal.Decimal,  | The vendor id, when the Attribute type is CUSTOM. | [optional] value must be a 64 bit integer
**[user_profile_assignment_rules](#user_profile_assignment_rules)** | list, tuple,  | tuple,  | The SSID user profile assignment rules. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_profile_assignment_rules

The SSID user profile assignment rules.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The SSID user profile assignment rules. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUserProfileAssignmentRule**](XiqUserProfileAssignmentRule.md) | [**XiqUserProfileAssignmentRule**](XiqUserProfileAssignmentRule.md) | [**XiqUserProfileAssignmentRule**](XiqUserProfileAssignmentRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

