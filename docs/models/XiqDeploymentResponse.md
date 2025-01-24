# extremecloudiq.model.xiq_deployment_response.XiqDeploymentResponse

The configuration deployment response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration deployment response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deployment_id** | decimal.Decimal, int,  | decimal.Decimal,  | The scheduled deployment ID | [optional] value must be a 64 bit integer
**[deployment_status](#deployment_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Devices config deployment status map  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# deployment_status

Devices config deployment status map 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Devices config deployment status map  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**XiqDeploymentStatus**](XiqDeploymentStatus.md) | [**XiqDeploymentStatus**](XiqDeploymentStatus.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

