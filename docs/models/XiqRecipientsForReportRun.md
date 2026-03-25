# extremecloudiq.model.xiq_recipients_for_report_run.XiqRecipientsForReportRun

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**report_run_id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique ID of the report run | [optional] value must be a 64 bit integer
**report_id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique ID of the report | [optional] value must be a 64 bit integer
**report_name** | str,  | str,  | The report name | [optional] 
**[recipients](#recipients)** | list, tuple,  | tuple,  | The list of report recipients | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# recipients

The list of report recipients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of report recipients | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqReportRecipientInfo**](XiqReportRecipientInfo.md) | [**XiqReportRecipientInfo**](XiqReportRecipientInfo.md) | [**XiqReportRecipientInfo**](XiqReportRecipientInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

