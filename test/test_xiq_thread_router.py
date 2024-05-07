# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_thread_router import XiqThreadRouter  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadRouter(unittest.TestCase):
    """XiqThreadRouter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadRouter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_router.XiqThreadRouter()  # noqa: E501
        if include_optional :
            return XiqThreadRouter(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                owner_id = 56, 
                device_id = 56, 
                serial_number = '0', 
                eui64 = '0', 
                ext_mac = '0', 
                rloc16 = '0', 
                global_ipv6 = '0', 
                tx_power = 56, 
                region = '0', 
                thread_platform = '0', 
                device_role = '0', 
                router_interface = extremecloudiq.models.xiq_thread_network_interface.XiqThreadNetworkInterface(
                    interface_name = '0', 
                    is_active = True, 
                    is_broadcast = True, 
                    is_loopback = True, 
                    is_point_to_point = True, 
                    is_running = True, 
                    is_arp = True, 
                    is_promisc = True, 
                    is_all_multi = True, 
                    is_multicast = True, 
                    is_dynamic = True, 
                    mtu = 56, 
                    hw_mac_address = '0', 
                    ipv4 = '0', 
                    ipv4_mask = '0', 
                    ipv4_broadcast = '0', 
                    ipv6_settings = [
                        extremecloudiq.models.xiq_thread_ipv6_setting.XiqThreadIpv6Setting(
                            address = '0', 
                            scope = '0', 
                            cast = '0', 
                            type = '0', )
                        ], ), 
                veth0 = extremecloudiq.models.xiq_thread_network_interface.XiqThreadNetworkInterface(
                    interface_name = '0', 
                    is_active = True, 
                    is_broadcast = True, 
                    is_loopback = True, 
                    is_point_to_point = True, 
                    is_running = True, 
                    is_arp = True, 
                    is_promisc = True, 
                    is_all_multi = True, 
                    is_multicast = True, 
                    is_dynamic = True, 
                    mtu = 56, 
                    hw_mac_address = '0', 
                    ipv4 = '0', 
                    ipv4_mask = '0', 
                    ipv4_broadcast = '0', 
                    ipv6_settings = [
                        extremecloudiq.models.xiq_thread_ipv6_setting.XiqThreadIpv6Setting(
                            address = '0', 
                            scope = '0', 
                            cast = '0', 
                            type = '0', )
                        ], ), 
                network_data = extremecloudiq.models.xiq_thread_network_data.XiqThreadNetworkData(
                    length = 56, 
                    max_length = 56, 
                    net_data_on_mesh_prefixes = [
                        extremecloudiq.models.xiq_thread_net_data_prefix.XiqThreadNetDataPrefix(
                            prefix = '0', 
                            route_preference = '0', 
                            added_by_rloc16 = '0', 
                            added_by_ext_mac = '0', 
                            preferred = True, 
                            slaac = True, 
                            dhcp = True, 
                            configure = True, 
                            default_route = True, 
                            on_mesh = '0', 
                            stable = True, 
                            nd_dns = True, 
                            dp = True, )
                        ], 
                    net_data_routes = [
                        extremecloudiq.models.xiq_thread_net_data_route.XiqThreadNetDataRoute(
                            prefix = '0', 
                            nat64 = True, 
                            stable = True, 
                            route_preference = '0', 
                            added_by_rloc16 = '0', 
                            added_by_ext_mac = '0', )
                        ], 
                    net_data_services = [
                        extremecloudiq.models.xiq_thread_net_data_service.XiqThreadNetDataService(
                            enterprise_number = 56, 
                            service_data = '0', 
                            server_data = '0', 
                            stable = True, 
                            added_by_rloc16 = '0', 
                            added_by_ext_mac = '0', )
                        ], ), 
                thread_mle_link_mode = extremecloudiq.models.xiq_thread_mle_link_mode.XiqThreadMleLinkMode(
                    rx_on_when_idle = True, 
                    full_thread_device = True, 
                    full_network_data = True, ), 
                thread_version = extremecloudiq.models.xiq_thread_version.XiqThreadVersion(
                    build_version = '0', 
                    api_version = '0', 
                    rcp_version = '0', ), 
                leader_service = extremecloudiq.models.xiq_thread_leader_service.XiqThreadLeaderService(
                    partition_id = 56, 
                    weighting = 56, 
                    full_network_data_version = 56, 
                    stable_network_data_version = 56, ), 
                border_router_service = extremecloudiq.models.xiq_thread_border_router_service.XiqThreadBorderRouterService(
                    state = '0', 
                    nat64_local_prefix = '0', 
                    nat64_favored_prefix = '0', 
                    nat64_favored_preference = '0', 
                    nat64_omr_local_prefix = '0', 
                    nat64_omr_favored_prefix = '0', 
                    nat64_omr_favored_preference = '0', 
                    nat64_onlink_local_prefix = '0', 
                    nat64_onlink_favored_prefix = '0', 
                    nat64_onlink_favored_preference = '0', ), 
                backbone_border_router_service = extremecloudiq.models.xiq_thread_backbone_border_router_service.XiqThreadBackboneBorderRouterService(
                    state = '0', ), 
                border_agent_service = extremecloudiq.models.xiq_thread_border_agent_service.XiqThreadBorderAgentService(
                    state = '0', 
                    udp_port = 56, ), 
                commissioner_service = extremecloudiq.models.xiq_thread_commissioner_service.XiqThreadCommissionerService(
                    state = '0', ), 
                nat64_service = extremecloudiq.models.xiq_thread_nat64_service.XiqThreadNat64Service(
                    prefix_manager_state = '0', 
                    translator_state = '0', 
                    translator_cidr = '0', ), 
                network_config = extremecloudiq.models.xiq_thread_network_config.XiqThreadNetworkConfig(
                    id = 56, 
                    channel = 56, 
                    channel_mask = '0', 
                    ext_pan_id = '0', 
                    mesh_local_prefix = '0', 
                    network_key = '0', 
                    network_name = '0', 
                    pan_id = '0', 
                    pskc = '0', 
                    obtain_network_key_enabled = True, 
                    native_commissioning_enabled = True, 
                    routers_enabled = True, 
                    external_commissioning_enabled = True, 
                    beacons_enabled = True, 
                    commercial_commissioning_enabled = True, 
                    autonomous_enrollment_enabled = True, 
                    network_key_provisioning_enabled = True, 
                    non_ccm_routers_enabled = True, 
                    active_timestamp = 56, ), 
                active_clients = 56, 
                hostname = '0', 
                last_reported = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                thread_connected = True
            )
        else :
            return XiqThreadRouter(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqThreadRouter(self):
        """Test XiqThreadRouter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()