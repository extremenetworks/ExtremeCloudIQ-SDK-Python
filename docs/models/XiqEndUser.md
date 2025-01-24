# extremecloudiq.model.xiq_end_user.XiqEndUser

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**email_address** | str,  | str,  | The user email address | 
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**approval_type** | str,  | str,  | The approval type | 
**user_name** | str,  | str,  | The user identifiable name or the same one from common name, emailAddress or phoneNumber | 
**name** | str,  | str,  | The user common name | 
**expired_time** | decimal.Decimal, int,  | decimal.Decimal,  | The password expired time | value must be a 64 bit integer
**phone_number** | str,  | str,  | The user phone number | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**user_group_name** | str,  | str,  | The user group name | 
**user_group_id** | decimal.Decimal, int,  | decimal.Decimal,  | The user group ID | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The user description | [optional] 
**password** | str,  | str,  | The user password | [optional] 
**organization** | str,  | str,  | The organization name | [optional] 
**visit_purpose** | str,  | str,  | The purpose of visit | [optional] 
**email_password_delivery** | str,  | str,  | The email address for password delivery | [optional] 
**sms_password_delivery** | str,  | str,  | The sms number for password delivery | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

