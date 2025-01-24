# extremecloudiq.model.xiq_deployment_status.XiqDeploymentStatus

The configuration deployment status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration deployment status | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_finished** | bool,  | BoolClass,  | Indicates whether the last deployment is finished | 
**current_progress** | decimal.Decimal, int,  | decimal.Decimal,  | The current deploy progress if not finished, range from 0 to 100 | [optional] value must be a 32 bit integer
**current_step_code** | str,  | str,  | The code of the current deploy step if not finished | [optional] 
**current_step_message** | str,  | str,  | The readable message of the current deploy step if not finished | [optional] 
**is_finished_successful** | bool,  | BoolClass,  | Indicates whether the last deployment is successful if finished | [optional] 
**last_deploy_time** | decimal.Decimal, int,  | decimal.Decimal,  | The last deployed time (Only valid when in_progress &#x3D; false) | [optional] value must be a 64 bit integer
**status_message** | str,  | str,  | The status message | [optional] 
**is_pending_config** | bool,  | BoolClass,  | Indicates whether is pending config status or not | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

