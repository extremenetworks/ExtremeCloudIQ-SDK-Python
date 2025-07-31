# extremecloudiq.model.xiq_vhm_setting.XiqVhmSetting

The VHM Setting.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The VHM Setting. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**enable_copilot** | bool,  | BoolClass,  | Flag indicating whether Co-Pilot should be enabled (true) or disabled (false). | [optional] 
**enable_ssh** | bool,  | BoolClass,  | Flag indicating Ssh Availability. | [optional] 
**enable_supplemental_cli** | bool,  | BoolClass,  | Flag indicating Supplemental CLI. | [optional] 
**enable_wireless_onboarding** | bool,  | BoolClass,  | Flag indicating AP Out-of-the-box Wireless Onboarding. | [optional] 
**enable_password_for_exos_voss** | bool,  | BoolClass,  | Flag to enable device management settings for Switch Engine (EXOS) / Fabric Engine (VOSS) switches. | [optional] 
**enable_auto_config_push** | bool,  | BoolClass,  | Flag to enable auto config push. | [optional] 
**enable_site_isolation** | bool,  | BoolClass,  | Flag to enable site isolation. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

