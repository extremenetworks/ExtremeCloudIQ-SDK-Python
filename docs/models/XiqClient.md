# extremecloudiq.model.xiq_client.XiqClient

The Client associate to ExtremeCloud IQ device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Client associate to ExtremeCloud IQ device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**hostname** | str,  | str,  | The hostname of the client | [optional] 
**mac_address** | str,  | str,  | The MAC address of the client | [optional] 
**ip_address** | str,  | str,  | The IP address of the client | [optional] 
**ipv6_address** | str,  | str,  | The IPv6 address of the client | [optional] 
**os_type** | str,  | str,  | The OS type of the client | [optional] 
**username** | str,  | str,  | The username of the client. | [optional] 
**user_profile_name** | str,  | str,  | The user profile name of the client | [optional] 
**connected** | bool,  | BoolClass,  | Client is connected or not | [optional] 
**online_time** | str, datetime,  | str,  | The online time for the client | [optional] value must conform to RFC-3339 date-time
**offline_time** | str, datetime,  | str,  | The offline time for the client | [optional] value must conform to RFC-3339 date-time
**vlan** | decimal.Decimal, int,  | decimal.Decimal,  | The associate VLAN | [optional] value must be a 32 bit integer
**connection_type** | decimal.Decimal, int,  | decimal.Decimal,  | The connection type | [optional] value must be a 32 bit integer
**ssid** | str,  | str,  | The SSID | [optional] 
**port** | str,  | str,  | The associate device port | [optional] 
**org_name** | str,  | str,  | The organization name | [optional] 
**device_function** | decimal.Decimal, int,  | decimal.Decimal,  | The associated device function | [optional] value must be a 32 bit integer
**device_mac_address** | str,  | str,  | The associated device mac address | [optional] 
**device_name** | str,  | str,  | The associated device name | [optional] 
**auth** | decimal.Decimal, int,  | decimal.Decimal,  | The authentication type | [optional] value must be a 32 bit integer
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | The channel value | [optional] value must be a 32 bit integer
**client_health** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of client | [optional] value must be a 32 bit integer
**application_health** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of application | [optional] value must be a 32 bit integer
**radio_health** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of radio | [optional] value must be a 32 bit integer
**network_health** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of network | [optional] value must be a 32 bit integer
**radio_type** | decimal.Decimal, int,  | decimal.Decimal,  | The radio type. Represented by an integer code for each standard:&lt;br&gt; 1 - 2.4G&lt;br&gt; 2 - 5G&lt;br&gt; 3 - WIRED&lt;br&gt; 4 - 6G&lt;br&gt; 5 - THREAD | [optional] value must be a 32 bit integer
**encryption_method** | decimal.Decimal, int,  | decimal.Decimal,  | The encryption method, represented by an integer code for each encryption type:&lt;br&gt;-1 - N/A (Not applicable)&lt;br&gt;0 - AES (Advanced Encryption Standard)&lt;br&gt;1 - TKIP (Temporal Key Integrity Protocol)&lt;br&gt;2 - WEP (Wired Equivalent Privacy)&lt;br&gt;3 - NON (No encryption)&lt;br&gt;4 - CCMP (Counter Mode with Cipher Block Chaining Message Authentication Code Protocol)&lt;br&gt;5 - KEYGUARD (Keyguard encryption)&lt;br&gt;6 - WEP128 (128-bit WEP encryption)&lt;br&gt;7 - WEP64 (64-bit WEP encryption)&lt;br&gt;8 - WAPI (WLAN Authentication and Privacy Infrastructure)&lt;br&gt;9 - GCMP256 (256-bit Galois/Counter Mode Protocol)&lt;br&gt;10 - NONE (No encryption)&lt;br&gt;11 - PAP (Password Authentication Protocol)&lt;br&gt;12 - MsCHAP (Microsoft Challenge Handshake Authentication Protocol)&lt;br&gt;13 - EAP-MD5 (Extensible Authentication Protocol - MD5)&lt;br&gt;14 - EAP-TLS (Extensible Authentication Protocol - Transport Layer Security)&lt;br&gt;15 - PEAP (Protected Extensible Authentication Protocol)&lt;br&gt;16 - TTLS (Tunneled Transport Layer Security)&lt;br&gt;17 - TTLS-INNER-TUNNEL (Inner tunnel for TTLS)&lt;br&gt;18 - PEAP-INNER-TUNNEL (Inner tunnel for PEAP)&lt;br&gt;19 - EAP-FAST (Extensible Authentication Protocol - Flexible Authentication via Secure Tunneling)&lt;br&gt;20 - EAP-LEAP (Lightweight Extensible Authentication Protocol)&lt;br&gt;21 - EAP-RSA (Extensible Authentication Protocol - RSA)&lt;br&gt;22 - EAP-SIM (Extensible Authentication Protocol - SIM)&lt;br&gt;23 - EAP-AKA (Extensible Authentication Protocol - AKA)&lt;br&gt;24 - EAP-TEAP (Extensible Authentication Protocol - Tunneled EAP) | [optional] value must be a 32 bit integer
**mac_protocol** | str,  | str,  | The MAC protocol of the client:&lt;br&gt;&#x27;N/A&#x27;&lt;br&gt;&#x27;802.11a&#x27;&lt;br&gt;&#x27;802.11b&#x27;&lt;br&gt;&#x27;802.11g&#x27;&lt;br&gt;&#x27;802.11na&#x27;&lt;br&gt;&#x27;802.11ng&#x27;&lt;br&gt;&#x27;802.11ac&#x27;&lt;br&gt;&#x27;802.11ax-2.4g&#x27;&lt;br&gt;&#x27;802.11ax-5g&#x27;&lt;br&gt;&#x27;802.3&#x27;&lt;br&gt;&#x27;802.11ax-6g&#x27;&lt;br&gt;&#x27;802.15.4&#x27;&lt;br&gt;&#x27;802.11be-2g&#x27;&lt;br&gt;&#x27;802.11be-5g&#x27;&lt;br&gt;&#x27;802.11be-6g&#x27; | [optional] 
**interface_name** | str,  | str,  | The interface name | [optional] 
**bssid** | str,  | str,  | The bssid | [optional] 
**rssi** | decimal.Decimal, int,  | decimal.Decimal,  | The RSSI | [optional] value must be a 32 bit integer
**snr** | decimal.Decimal, int,  | decimal.Decimal,  | The SNR | [optional] value must be a 32 bit integer
**description** | str,  | str,  | The description of client | [optional] 
**category** | str,  | str,  | The category of client | [optional] 
**mobility** | str,  | str,  | The client mobility | [optional] 
**port_type_name** | str,  | str,  | The client port type name | [optional] 
**wing_ap** | bool,  | BoolClass,  | Wing ap flag | [optional] 
**vendor** | str,  | str,  | The vendor of client | [optional] 
**[locations](#locations)** | list, tuple,  | tuple,  | The detailed location | [optional] 
**product_type** | str,  | str,  | The Category which describes the Extreme device types(For example:For example:SR_2208P, AP_4000, AP_5010) | [optional] 
**alias** | str,  | str,  | The alias of the client | [optional] 
**th_rloc16** | str,  | str,  | The thread client Rloc16 | [optional] 
**th_child_id** | decimal.Decimal, int,  | decimal.Decimal,  | The thread client child ID | [optional] value must be a 32 bit integer
**th_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | The thread client timeout | [optional] value must be a 64 bit integer
**th_supervision_interval** | decimal.Decimal, int,  | decimal.Decimal,  | The thread client Super vision interval | [optional] value must be a 32 bit integer
**th_netdata_version** | decimal.Decimal, int,  | decimal.Decimal,  | The thread client netdata version | [optional] value must be a 32 bit integer
**th_csl_synced** | bool,  | BoolClass,  | The thread client CSL synced | [optional] 
**[th_ip_addresses](#th_ip_addresses)** | list, tuple,  | tuple,  | The thread client IP addresses | [optional] 
**th_router_last_reported** | str, datetime,  | str,  | The last reported datetime by thread router | [optional] value must conform to RFC-3339 date-time
**thread_connected** | bool,  | BoolClass,  | Is client connected to thread network | [optional] 
**make** | str,  | str,  | The Manufacturer of the client associated device | [optional] 
**os_version** | str,  | str,  | The OS version of the client associated device | [optional] 
**connected_to** | str,  | str,  | The device name which client is connected to | [optional] 
**connection_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The client&#x27;s connection duration | [optional] value must be a 64 bit integer
**captive_web_portal** | str,  | str,  | Captive Web Portal | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

The detailed location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The detailed location | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqLocationLegend**](XiqLocationLegend.md) | [**XiqLocationLegend**](XiqLocationLegend.md) | [**XiqLocationLegend**](XiqLocationLegend.md) |  | 

# th_ip_addresses

The thread client IP addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The thread client IP addresses | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadIpv6Setting**](XiqThreadIpv6Setting.md) | [**XiqThreadIpv6Setting**](XiqThreadIpv6Setting.md) | [**XiqThreadIpv6Setting**](XiqThreadIpv6Setting.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

