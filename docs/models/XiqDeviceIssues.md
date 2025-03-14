# extremecloudiq.model.xiq_device_issues.XiqDeviceIssues

The device details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**authentication_failures** | decimal.Decimal, int,  | decimal.Decimal,  | The count of authentication failures | [optional] value must be a 64 bit integer
**association_failures** | decimal.Decimal, int,  | decimal.Decimal,  | The count of association issues | [optional] value must be a 64 bit integer
**ip_address_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The count of IP address issues | [optional] value must be a 64 bit integer
**excessive_packet_loss_ap_count** | decimal.Decimal, int,  | decimal.Decimal,  | The total count of number of packets lost | [optional] value must be a 64 bit integer
**excessive_packet_loss_ap_count_5g** | decimal.Decimal, int,  | decimal.Decimal,  | The total count of number of packets lost (in 5g band) | [optional] value must be a 64 bit integer
**excessive_packet_loss_ap_count_6g** | decimal.Decimal, int,  | decimal.Decimal,  | The total count of number of packets lost (in 6g band) | [optional] value must be a 64 bit integer
**total_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The total clients of the device | [optional] value must be a 64 bit integer
**excessive_packet_loss_ap_count_2dot4g** | decimal.Decimal, int,  | decimal.Decimal,  | The count of number of packets lost (in 2.4g band) | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

