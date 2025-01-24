# extremecloudiq.model.xiq_email_template.XiqEmailTemplate

The password or ppsk notification template for user groups.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The password or ppsk notification template for user groups. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**password_type** | [**XiqPasswordType**](XiqPasswordType.md) | [**XiqPasswordType**](XiqPasswordType.md) |  | 
**name** | str,  | str,  | The email template name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**predefined** | bool,  | BoolClass,  | Wheter or not it is a system prefined template | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The email template description | [optional] 
**content** | str,  | str,  | The email template form. | [optional] 
**enable_preview** | bool,  | BoolClass,  | The setting to enable preview | [optional] 
**logo_url** | str,  | str,  | The logo url | [optional] 
**icon_url** | str,  | str,  | The icon url | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

