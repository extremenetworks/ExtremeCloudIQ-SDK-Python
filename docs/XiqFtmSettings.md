# XiqFtmSettings

The payload of FTM Settings
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**wgs84_override** | **bool** | World Geodetic System 1984 (WGS84) override | 
**wgs84** | [**XiqWgs84**](XiqWgs84.md) |  | [optional] 
**zsubelement_override** | **bool** | Z Subelement override. | 
**zsubelement** | [**XiqZsubelement**](XiqZsubelement.md) |  | [optional] 
**civic_address_override** | **bool** | Civic Address override. | 
**civic_address** | **str** | Civic Address as hex encoded RFC4776 formatted string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


