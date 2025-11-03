# extremecloudiq.model.xiq_app_usage_summary_filter.XiqAppUsageSummaryFilter

Request body for Application Usage Summary Filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request body for Application Usage Summary Filter | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | Filter by Site Ids | [optional] 
**[application_name](#application_name)** | list, tuple,  | tuple,  | Filter by application name | [optional] 
**[category_name](#category_name)** | list, tuple,  | tuple,  | Filter by category (application group) name | [optional] 
**[number_filter](#number_filter)** | list, tuple,  | tuple,  | Filter by number filter | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_ids

Filter by Site Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter by Site Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | Filter by Site Ids | value must be a 64 bit integer

# application_name

Filter by application name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter by application name | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Filter by application name | 

# category_name

Filter by category (application group) name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter by category (application group) name | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Filter by category (application group) name | 

# number_filter

Filter by number filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter by number filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAppUsageSummaryNumberFilter**](XiqAppUsageSummaryNumberFilter.md) | [**XiqAppUsageSummaryNumberFilter**](XiqAppUsageSummaryNumberFilter.md) | [**XiqAppUsageSummaryNumberFilter**](XiqAppUsageSummaryNumberFilter.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

