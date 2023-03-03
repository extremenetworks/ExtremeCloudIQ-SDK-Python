# XiqFloor

The Floor information on the floorplan.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**parent_id** | **int** | The parent building ID | 
**name** | **str** | The floor name | 
**unique_name** | **str** | The floor unique name | 
**environment** | [**XiqRfEnvironmentType**](XiqRfEnvironmentType.md) |  | 
**db_attenuation** | **float** | The floor attenuation in dBs | 
**measurement_unit** | [**XiqMeasurementUnit**](XiqMeasurementUnit.md) |  | 
**installation_height** | **float** | The installation height | 
**map_size_width** | **float** | The floormap width | [optional] 
**map_size_height** | **float** | The floormap height | [optional] 
**map_name** | **str** | The floormap name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


