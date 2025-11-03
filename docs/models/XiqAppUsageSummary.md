# extremecloudiq.model.xiq_app_usage_summary.XiqAppUsageSummary

The Application Usage Summary Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Application Usage Summary Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**application_name** | str,  | str,  | The application name | [optional] 
**category_name** | str,  | str,  | The category name of application | [optional] 
**usage** | decimal.Decimal, int,  | decimal.Decimal,  | The application summary usage | [optional] value must be a 64 bit integer
**percentage_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  | The application summary percentage usage | [optional] value must be a 32 bit float
**clients** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of clients | [optional] value must be a 64 bit integer
**users** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of users | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

