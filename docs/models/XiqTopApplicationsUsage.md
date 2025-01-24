# extremecloudiq.model.xiq_top_applications_usage.XiqTopApplicationsUsage

The Top N Applications Usage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Top N Applications Usage | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The application ID | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The application name | [optional] 
**clients** | decimal.Decimal, int,  | decimal.Decimal,  | The associated unique client count | [optional] value must be a 64 bit integer
**users** | decimal.Decimal, int,  | decimal.Decimal,  | The associated unique user count | [optional] value must be a 64 bit integer
**usage** | decimal.Decimal, int,  | decimal.Decimal,  | The application usage | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

