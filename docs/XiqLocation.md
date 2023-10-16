# XiqLocation

The hierarchical location for Site_Group/Site/Building/Floor
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**parent_id** | **int** | The parent location ID | [optional] 
**name** | **str** | The location name | 
**unique_name** | **str** | The unique location name | 
**type** | **str** | The location type | 
**address** | **str** | The address for the location | [optional] 
**children** | [**list[XiqLocation]**](XiqLocation.md) | The child locations | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


