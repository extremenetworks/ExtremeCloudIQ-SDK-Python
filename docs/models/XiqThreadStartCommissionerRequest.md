# extremecloudiq.model.xiq_thread_start_commissioner_request.XiqThreadStartCommissionerRequest

The request to start the thread commissioner on an iot interface of a device.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request to start the thread commissioner on an iot interface of a device. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device id | value must be a 64 bit integer
**comm_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | After this timeout the Commissioner will shutdown. The default is 120 sec. but the max is approximately 23 days. | [optional] value must be a 32 bit integer
**interface_name** | str,  | str,  | The IoT interface on which to start the Commissioner. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

