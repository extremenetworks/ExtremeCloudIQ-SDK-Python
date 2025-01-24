# extremecloudiq.model.xiq_hotspot_wan_metrics.XiqHotspotWanMetrics

Hotspot WAN (Wide Area Network) metrics.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Hotspot WAN (Wide Area Network) metrics. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uplink_speed** | decimal.Decimal, int,  | decimal.Decimal,  | The downlink speed for the WAN network, in kbps (where 0 is unknown). | value must be a 32 bit integer
**downlink_speed** | decimal.Decimal, int,  | decimal.Decimal,  | The downlink speed for the WAN network, in kbps (where 0 is unknown). | value must be a 32 bit integer
**status** | [**XiqHotspotWanLinkStatus**](XiqHotspotWanLinkStatus.md) | [**XiqHotspotWanLinkStatus**](XiqHotspotWanLinkStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

