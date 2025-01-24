# extremecloudiq.model.xiq_deployment_request.XiqDeploymentRequest

The configuration/firmware update deployment request to devices.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration/firmware update deployment request to devices. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schedule** | [**XiqScheduleDetails**](XiqScheduleDetails.md) | [**XiqScheduleDetails**](XiqScheduleDetails.md) |  | [optional] 
**devices** | [**XiqDeployDeviceFilter**](XiqDeployDeviceFilter.md) | [**XiqDeployDeviceFilter**](XiqDeployDeviceFilter.md) |  | [optional] 
**policy** | [**XiqDeploymentPolicy**](XiqDeploymentPolicy.md) | [**XiqDeploymentPolicy**](XiqDeploymentPolicy.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

