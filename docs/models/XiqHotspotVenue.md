# extremecloudiq.model.xiq_hotspot_venue.XiqHotspotVenue

Venue information helps client devices understand the type and nature of the location where the Wi-Fi network is deployed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Venue information helps client devices understand the type and nature of the location where the Wi-Fi network is deployed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**venue_group** | [**XiqHotspotVenueGroup**](XiqHotspotVenueGroup.md) | [**XiqHotspotVenueGroup**](XiqHotspotVenueGroup.md) |  | [optional] 
**venue_type** | [**XiqHotspotVenueType**](XiqHotspotVenueType.md) | [**XiqHotspotVenueType**](XiqHotspotVenueType.md) |  | [optional] 
**[names](#names)** | list, tuple,  | tuple,  | Localized names for the venue. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# names

Localized names for the venue.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Localized names for the venue. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

