# extremecloudiq.model.xiq_neighbor_ap.XiqNeighborAp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**hostname** | str,  | str,  |  | [optional] 
**ip_address** | str,  | str,  |  | [optional] 
**mac_address** | str,  | str,  |  | [optional] 
**rssi** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**connection_failure_reason** | str,  | str,  |  | [optional] must be one of ["OTHER", "ABORT_FROM_OS", "DEASSOC_FROM_AP", "DEAUTH_FROM_AP", "INTERNAL_TERMINATION", "INVALID_CAPABILITIES", "ASSOC_FAILURE_802_11", "AUTH_FAILURE_802_11", "TX_RX_FAILURE_REASON", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

