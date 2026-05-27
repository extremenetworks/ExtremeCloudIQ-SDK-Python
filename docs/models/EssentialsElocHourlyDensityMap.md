# extremecloudiq.model.essentials_eloc_hourly_density_map.EssentialsElocHourlyDensityMap

Density map for a specific hour

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Density map for a specific hour | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[cells](#cells)** | list, tuple,  | tuple,  | Density map cells for this hour | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cells

Density map cells for this hour

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Density map cells for this hour | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EssentialsElocDensityMapCell**](EssentialsElocDensityMapCell.md) | [**EssentialsElocDensityMapCell**](EssentialsElocDensityMapCell.md) | [**EssentialsElocDensityMapCell**](EssentialsElocDensityMapCell.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

