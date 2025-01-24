# extremecloudiq.model.xiq_iotp_tg_white_list_entry.XiqIotpTgWhiteListEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pskd** | str,  | str,  | The PSKd (Pre-Shared-Key for the Device) is the Joining Device Credential encoded using base32-thread.  A Joining Device Credential is encoded as uppercase, alphanumeric characters (base32-thread: 0-9,A-Y excluding I,O,Q, and Z for readability)  with a minimum length of 6 such characters and a maximum length of 32 such characters. | 
**long_eui** | str,  | str,  | The factory-assigned IEEE EUI-64. (16 hex digits) or * to match any joiner. FFFFFFFFFFFFFFFF is reserved. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

