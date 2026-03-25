# extremecloudiq.model.xiq_thread_stop_commissioner_by_buildings_request.XiqThreadStopCommissionerByBuildingsRequest

The request to stop the thread commissioner on devices under buildings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request to stop the thread commissioner on devices under buildings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Owner ID | value must be a 64 bit integer
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | The building id list | 
**ext_pan_id** | str,  | str,  | The extPanID for IoT profile to filter out devices to stop the Commissioner. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# building_ids

The building id list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The building id list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The building id list | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

