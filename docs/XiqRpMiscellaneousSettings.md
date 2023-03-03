# XiqRpMiscellaneousSettings

The payload of config for the radio profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**sla_throughput_level** | **str** | The Client SLA options -- \&quot;NORMAL_DENSITY\&quot;, \&quot;HIGH_DENSITY\&quot; (performance-oriented), or \&quot;LOW_DENSITY\&quot; (coverage-oriented) | [optional] 
**radio_range** | **int** | The Outdoor Deployment for signal distance from 300 to 10000 meters | [optional] 
**wmm_qos_settings** | [**list[XiqRpWmmQosSettings]**](XiqRpWmmQosSettings.md) | The WMM QoS settings for various media types | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


