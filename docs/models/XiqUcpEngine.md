# extremecloudiq.model.xiq_ucp_engine.XiqUcpEngine

The payload of UCP Engine

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of UCP Engine | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**image_name** | str,  | str,  | Name of the image for the engine | 
**upgradable** | bool,  | BoolClass,  | If the engine is upgradable | 
**name** | str,  | str,  | The name of the UCP engine | 
**description** | str,  | str,  | The description of the UCP engine | 
**max_instances** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of instances allowed for the engine | value must be a 32 bit integer
**instance_count** | decimal.Decimal, int,  | decimal.Decimal,  | Count of the number of instances for the engine | value must be a 32 bit integer
**[instances](#instances)** | list, tuple,  | tuple,  | List of instances installed | [optional] 
**type** | str,  | str,  | The type of engine image | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instances

List of instances installed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of instances installed | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUcpEngineInstance**](XiqUcpEngineInstance.md) | [**XiqUcpEngineInstance**](XiqUcpEngineInstance.md) | [**XiqUcpEngineInstance**](XiqUcpEngineInstance.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

