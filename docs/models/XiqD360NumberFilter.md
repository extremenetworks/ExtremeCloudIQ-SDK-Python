# extremecloudiq.model.xiq_d360_number_filter.XiqD360NumberFilter

Number Filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number Filter | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**column_name** | str,  | str,  | The column name | [optional] 
**filter_type** | [**XiqD360FilterType**](XiqD360FilterType.md) | [**XiqD360FilterType**](XiqD360FilterType.md) |  | [optional] 
**value** | decimal.Decimal, int,  | decimal.Decimal,  | The value | [optional] value must be a 64 bit integer
**min** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum value | [optional] value must be a 64 bit integer
**max** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum value | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

