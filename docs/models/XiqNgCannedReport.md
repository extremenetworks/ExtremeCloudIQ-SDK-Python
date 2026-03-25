# extremecloudiq.model.xiq_ng_canned_report.XiqNgCannedReport

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**report_id** | decimal.Decimal, int,  | decimal.Decimal,  | Report Id | [optional] value must be a 64 bit integer
**report_schedule_id** | decimal.Decimal, int,  | decimal.Decimal,  | Report Schedule Id | [optional] value must be a 64 bit integer
**enable_schedule** | bool,  | BoolClass,  | Status of report Schedule | [optional] 
**[report_runs](#report_runs)** | list, tuple,  | tuple,  | List of report runs | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# report_runs

List of report runs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of report runs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqNgCannedReportRuns**](XiqNgCannedReportRuns.md) | [**XiqNgCannedReportRuns**](XiqNgCannedReportRuns.md) | [**XiqNgCannedReportRuns**](XiqNgCannedReportRuns.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

