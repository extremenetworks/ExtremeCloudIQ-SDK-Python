# extremecloudiq.model.xiq_hiq_context.XiqHiqContext

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[reading_org_ids](#reading_org_ids)** | list, tuple,  | tuple,  | The organization ID list for reading data (Empty means read data from all organizations in the HIQ) | 
**creating_org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization ID for creating new data | value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# reading_org_ids

The organization ID list for reading data (Empty means read data from all organizations in the HIQ)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The organization ID list for reading data (Empty means read data from all organizations in the HIQ) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The organization ID list for reading data (Empty means read data from all organizations in the HIQ) | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

