# extremecloudiq.model.xiq_attach_up_assignment_request.XiqAttachUPAssignmentRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[user_profile_assignment_rules](#user_profile_assignment_rules)** | list, tuple,  | tuple,  | The User Profile Assignment and User Profile Id&#x27;s to attach to SSID | [optional] 
**enable_user_profile_assignment** | bool,  | BoolClass,  | The flag to enable User Profile Assignment | [optional] 
**enable_radius_attribute_user_profile_assignment** | bool,  | BoolClass,  | The flag to enable Radius Attribute User Profile Assignment | [optional] 
**attribute_type** | [**XiqAttributeType**](XiqAttributeType.md) | [**XiqAttributeType**](XiqAttributeType.md) |  | [optional] 
**attribute_key** | decimal.Decimal, int,  | decimal.Decimal,  | The SSID attribute key | [optional] value must be a 32 bit integer
**default_radius_client_object_id** | decimal.Decimal, int,  | decimal.Decimal,  | The default RADIUS client object ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_profile_assignment_rules

The User Profile Assignment and User Profile Id's to attach to SSID

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The User Profile Assignment and User Profile Id&#x27;s to attach to SSID | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAttachUPAssignmentEntry**](XiqAttachUPAssignmentEntry.md) | [**XiqAttachUPAssignmentEntry**](XiqAttachUPAssignmentEntry.md) | [**XiqAttachUPAssignmentEntry**](XiqAttachUPAssignmentEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

