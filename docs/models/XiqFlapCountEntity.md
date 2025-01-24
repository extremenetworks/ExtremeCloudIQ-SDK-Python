# extremecloudiq.model.xiq_flap_count_entity.XiqFlapCountEntity

ExtremeCloud IQ FlapCount Point

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ FlapCount Point | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp | value must be a 64 bit integer
**flap_count** | decimal.Decimal, int, float,  | decimal.Decimal,  | The flap count | [optional] 
**sub_optimal_count** | decimal.Decimal, int,  | decimal.Decimal,  | The sub-optimal count | [optional] value must be a 32 bit integer
**optimal_time_spent** | decimal.Decimal, int, float,  | decimal.Decimal,  | The time spent | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

