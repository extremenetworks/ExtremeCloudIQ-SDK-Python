# extremecloudiq.model.xiq_roaming_trial_detail.XiqRoamingTrialDetail

Get roaming trial details data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Get roaming trial details data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**channel_from** | decimal.Decimal, int,  | decimal.Decimal,  | The channel From | [optional] value must be a 32 bit integer
**channel_to** | decimal.Decimal, int,  | decimal.Decimal,  | The channel To | [optional] value must be a 32 bit integer
**rssi_from** | decimal.Decimal, int,  | decimal.Decimal,  | The RSSI From | [optional] value must be a 32 bit integer
**rssi_to** | decimal.Decimal, int,  | decimal.Decimal,  | The RSSI To | [optional] value must be a 32 bit integer
**snr_from** | decimal.Decimal, int,  | decimal.Decimal,  | The SNR From | [optional] value must be a 32 bit integer
**snr_to** | decimal.Decimal, int,  | decimal.Decimal,  | The SNR To | [optional] value must be a 32 bit integer
**status** | str,  | str,  | The operation progress | [optional] must be one of ["ASSOC_FAILED", "DHCP_FAILED", "GW_FAILED", "AUTH_FAILED", "DNS_FAILED", "ROAMING_STARTED", "ROAMING_COMPLETED", ] 
**reason** | str,  | str,  | Reason if operation failed | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

