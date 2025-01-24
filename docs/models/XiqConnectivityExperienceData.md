# extremecloudiq.model.xiq_connectivity_experience_data.XiqConnectivityExperienceData

ExtremeCloud IQ Connectivity Experience data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Connectivity Experience data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**trend_indicator** | [**XiqTrendIndicator**](XiqTrendIndicator.md) | [**XiqTrendIndicator**](XiqTrendIndicator.md) |  | 
**[quality_index_graph](#quality_index_graph)** | list, tuple,  | tuple,  | the quality index graph | 
**quality_index_value** | [**XiqQualityIndex**](XiqQualityIndex.md) | [**XiqQualityIndex**](XiqQualityIndex.md) |  | 
**name** | str,  | str,  | the location/ssid/os-name based on view type | 
**client_type** | [**XiqClientType**](XiqClientType.md) | [**XiqClientType**](XiqClientType.md) |  | 
**quality_index** | decimal.Decimal, int,  | decimal.Decimal,  | the quality index | value must be a 32 bit integer
**id** | str,  | str,  | the unique identifier | [optional] 
**info** | str,  | str,  | the info related to connectivity experience view type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# quality_index_graph

the quality index graph

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the quality index graph | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDataPoint**](XiqDataPoint.md) | [**XiqDataPoint**](XiqDataPoint.md) | [**XiqDataPoint**](XiqDataPoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

