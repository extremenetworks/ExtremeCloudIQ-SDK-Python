# extremecloudiq.model.xiq_deployment_by_id_status_response.XiqDeploymentByIdStatusResponse

The deployment details status response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The deployment details status response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schedule_status** | [**XiqScheduleStatus**](XiqScheduleStatus.md) | [**XiqScheduleStatus**](XiqScheduleStatus.md) |  | [optional] 
**schedule_time** | decimal.Decimal, int,  | decimal.Decimal,  | The scheduled time | [optional] value must be a 64 bit integer
**created_time** | decimal.Decimal, int,  | decimal.Decimal,  | The created time | [optional] value must be a 64 bit integer
**updated_time** | decimal.Decimal, int,  | decimal.Decimal,  | The updated time | [optional] value must be a 64 bit integer
**[site_info](#site_info)** | list, tuple,  | tuple,  | The site information tagged to devices | [optional] 
**[deployment_status](#deployment_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The deployment status | [optional] 
**overview** | [**XiqDeploymentOverviewDetails**](XiqDeploymentOverviewDetails.md) | [**XiqDeploymentOverviewDetails**](XiqDeploymentOverviewDetails.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_info

The site information tagged to devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The site information tagged to devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqSiteInfo**](XiqSiteInfo.md) | [**XiqSiteInfo**](XiqSiteInfo.md) | [**XiqSiteInfo**](XiqSiteInfo.md) |  | 

# deployment_status

The deployment status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The deployment status | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**XiqDeploymentStatus**](XiqDeploymentStatus.md) | [**XiqDeploymentStatus**](XiqDeploymentStatus.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

