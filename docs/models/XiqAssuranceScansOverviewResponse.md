# extremecloudiq.model.xiq_assurance_scans_overview_response.XiqAssuranceScansOverviewResponse

Copilot AssuranceScans Overview

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot AssuranceScans Overview | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**aggregated_scans_count** | decimal.Decimal, int,  | decimal.Decimal,  | The aggregated scans count | [optional] value must be a 64 bit integer
**[anomalies_count_vos](#anomalies_count_vos)** | list, tuple,  | tuple,  | the channel stats data | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# anomalies_count_vos

the channel stats data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the channel stats data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAnomaliesCountVoEntity**](XiqAnomaliesCountVoEntity.md) | [**XiqAnomaliesCountVoEntity**](XiqAnomaliesCountVoEntity.md) | [**XiqAnomaliesCountVoEntity**](XiqAnomaliesCountVoEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

