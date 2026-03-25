# extremecloudiq.model.xiq_update_custom_report_request.XiqUpdateCustomReportRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[recipients](#recipients)** | list, tuple,  | tuple,  | List of recipient email to send the report. | 
**[schedules](#schedules)** | list, tuple,  | tuple,  | List of schedules (e.g., daily, weekly, etc.). | 
**[metrics](#metrics)** | list, tuple,  | tuple,  | List of metrics to include in the report (e.g., MAX_CONCURRENT_CLIENTS). | 
**report_name** | str,  | str,  | The name of the report. | 
**[file_format](#file_format)** | list, tuple,  | tuple,  | The file format(s) of the report (e.g., PDF, CSV). | 
**report_description** | str,  | str,  | A short description of the report. | [optional] 
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | List of site IDs the report will cover. | [optional] 
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | List of building IDs the report will cover. | [optional] 
**[floor_ids](#floor_ids)** | list, tuple,  | tuple,  | List of floor IDs the report will cover. | [optional] 
**[ssids](#ssids)** | list, tuple,  | tuple,  | List of SSIDs to be included in the report. | [optional] 
**[bands](#bands)** | list, tuple,  | tuple,  | List of bands (e.g., 2.4GHz, 5GHz) to be covered in the report. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metrics

List of metrics to include in the report (e.g., MAX_CONCURRENT_CLIENTS).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of metrics to include in the report (e.g., MAX_CONCURRENT_CLIENTS). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) |  | 

# recipients

List of recipient email to send the report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of recipient email to send the report. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRecipientCnsInfo**](XiqRecipientCnsInfo.md) | [**XiqRecipientCnsInfo**](XiqRecipientCnsInfo.md) | [**XiqRecipientCnsInfo**](XiqRecipientCnsInfo.md) |  | 

# schedules

List of schedules (e.g., daily, weekly, etc.).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of schedules (e.g., daily, weekly, etc.). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUpdateReportScheduleRequest**](XiqUpdateReportScheduleRequest.md) | [**XiqUpdateReportScheduleRequest**](XiqUpdateReportScheduleRequest.md) | [**XiqUpdateReportScheduleRequest**](XiqUpdateReportScheduleRequest.md) |  | 

# file_format

The file format(s) of the report (e.g., PDF, CSV).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The file format(s) of the report (e.g., PDF, CSV). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqReportFileFormat**](XiqReportFileFormat.md) | [**XiqReportFileFormat**](XiqReportFileFormat.md) | [**XiqReportFileFormat**](XiqReportFileFormat.md) |  | 

# site_ids

List of site IDs the report will cover.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of site IDs the report will cover. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of site IDs the report will cover. | value must be a 64 bit integer

# building_ids

List of building IDs the report will cover.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of building IDs the report will cover. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of building IDs the report will cover. | value must be a 64 bit integer

# floor_ids

List of floor IDs the report will cover.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of floor IDs the report will cover. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of floor IDs the report will cover. | value must be a 64 bit integer

# ssids

List of SSIDs to be included in the report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of SSIDs to be included in the report. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of SSIDs to be included in the report. | 

# bands

List of bands (e.g., 2.4GHz, 5GHz) to be covered in the report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of bands (e.g., 2.4GHz, 5GHz) to be covered in the report. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

