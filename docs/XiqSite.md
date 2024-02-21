# XiqSite

The site location information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**parent_id** | **int** | The parent site group ID | [optional] 
**name** | **str** | The site name | 
**unique_name** | **str** | The site unique name | 
**type** | **str** | The location type | 
**address** | [**XiqAddress**](XiqAddress.md) |  | [optional] 
**country_code** | **int** | The country code for the site | 
**created_by** | **int** | The user ID used to create the site | [optional] 
**latitude** | **float** | The latitude coordinate for the site | [optional] 
**longitude** | **float** | The longitude coordinate for the site | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


