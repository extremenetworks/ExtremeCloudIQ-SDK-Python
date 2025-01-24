# extremecloudiq.model.xiq_copilot_anomalies_by_category.XiqCopilotAnomaliesByCategory

Copilot Anomalies Data by Category

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomalies Data by Category | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[anomalies_by_location](#anomalies_by_location)** | list, tuple,  | tuple,  | The total anomalies by location | [optional] 
**anomalies_by_severity** | [**XiqAnomaliesSeverityEntity**](XiqAnomaliesSeverityEntity.md) | [**XiqAnomaliesSeverityEntity**](XiqAnomaliesSeverityEntity.md) |  | [optional] 
**[anomalies_by_type](#anomalies_by_type)** | list, tuple,  | tuple,  | The total anomalies by type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# anomalies_by_location

The total anomalies by location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The total anomalies by location | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAnomaliesSiteEntity**](XiqAnomaliesSiteEntity.md) | [**XiqAnomaliesSiteEntity**](XiqAnomaliesSiteEntity.md) | [**XiqAnomaliesSiteEntity**](XiqAnomaliesSiteEntity.md) |  | 

# anomalies_by_type

The total anomalies by type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The total anomalies by type | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAnomaliesTypeEntity**](XiqAnomaliesTypeEntity.md) | [**XiqAnomaliesTypeEntity**](XiqAnomaliesTypeEntity.md) | [**XiqAnomaliesTypeEntity**](XiqAnomaliesTypeEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

