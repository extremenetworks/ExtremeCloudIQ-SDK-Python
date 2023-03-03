# XiqDeploymentStatus

The configuration deployment status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_progress** | **int** | The current deploy progress if not finished, range from 0 to 100 | [optional] 
**current_step_code** | **str** | The code of the current deploy step if not finished | [optional] 
**current_step_message** | **str** | The readable message of the current deploy step if not finished | [optional] 
**is_finished_successful** | **bool** | Indicates whether the last deployment is successful if finished | [optional] 
**last_deploy_time** | **int** | The last deployed time (Only valid when in_progress &#x3D; false) | [optional] 
**finished** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


