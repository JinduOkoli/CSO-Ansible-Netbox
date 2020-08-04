class FilterModule(object):

    def filters(self):
        return {
            'wan_health_cleanup': self.wan_health_cleanup,
        }

    def wan_health_cleanup(self, value):
        interface_report = {}

        interface_report['name'] = value['name'][0]['data']
        interface_report['status'] = value['admin-status'][0]['data']
        interface_report['oper_status'] = value['oper-status'][0]['data']
        interface_report['description'] = value['description'][0]['data']
        interface_report['mtu'] = value['mtu'][0]['data']
        interface_report['physical_mode'] = value['physical-mode'][0]['data']
        interface_report['speed'] = value['speed'][0]['data']
        interface_report['mac_address'] = value['current-physical-address'][0]['data']
        interface_report['last_flap'] = value['interface-flapped'][0]['data']
        interface_report['traffic_stats'] = {}
        interface_report['traffic_stats']['input_bps'] = value['traffic-statistics'][0]['input-bps'][0]['data']
        interface_report['traffic_stats']['input_pps'] = value['traffic-statistics'][0]['input-pps'][0]['data']
        interface_report['traffic_stats']['output_bps'] = value['traffic-statistics'][0]['output-bps'][0]['data']
        interface_report['traffic_stats']['output_pps'] = value['traffic-statistics'][0]['output-pps'][0]['data']
        interface_report['active_alarms'] = value['active-alarms'][0]['interface-alarms'][0]
        interface_report['active_defects'] = value['active-defects'][0]['interface-alarms'][0]
        # vdsl info
        interface_report['vdsl_info'] = {}
        interface_report['vdsl_info']['line_status'] = value['vdsl-information'][0]['vdsl-line-status'][0]['data']
        interface_report['vdsl_info']['line_profile'] = value['vdsl-information'][0]['vdsl-line-profile-type'][0]['data']
        interface_report['vdsl_info']['annex'] = value['vdsl-information'][0]['vdsl-annex-type'][0]['data']
        interface_report['vdsl_info']['seconds_in_showtime'] = value['vdsl-information'][0]['vdsl-seconds-in-showtime'][0]['data']
        # vdsl statistics
        interface_report['vdsl_statistics'] = {}
        interface_report['vdsl_statistics']['far_end_attenuation'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-attenuation'][0]['data']
        interface_report['vdsl_statistics']['far_end_capacity_used'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-capacity-used'][0]['data']
        interface_report['vdsl_statistics']['far_end_fast_crc'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-fast-crc'][0]['data']
        interface_report['vdsl_statistics']['far_end_fast_fec'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-fast-fec'][0]['data']
        interface_report['vdsl_statistics']['far_end_fast_hec'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-fast-hec'][0]['data']
        interface_report['vdsl_statistics']['far_end_noise_margin'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-noise-margin'][0]['data']
        interface_report['vdsl_statistics']['far_end_output_power'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-output-power'][0]['data']
        interface_report['vdsl_statistics']['near_end_attenuation'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-near-end-attenuation'][0]['data']
        interface_report['vdsl_statistics']['near_end_capacity_used'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-near-end-capacity-used'][0]['data']
        # logical interface
        interface_report['logical_interface'] = {}
        interface_report['logical_interface']['encapsulation'] = value['logical-interface'][0]['encapsulation'][0]['data']
        interface_report['logical_interface']['bandwidth'] = value['logical-interface'][0]['logical-interface-bandwidth'][0]['data']
        interface_report['logical_interface']['traffic_stats'] = {}
        interface_report['logical_interface']['traffic_stats']['input_packets'] = value['logical-interface'][0]['traffic-statistics'][0]['input-packets'][0]['data']
        interface_report['logical_interface']['traffic_stats']['output_packets'] = value['logical-interface'][0]['traffic-statistics'][0]['output-packets'][0]['data']
        # output-error-list
        interface_report['output_error_list'] = {}
        interface_report['output_error_list']['carrier_transitions'] = value['output-error-list'][0]['carrier-transitions'][0]['data']
        interface_report['output_error_list']['mtu_errors'] = value['output-error-list'][0]['mtu-errors'][0]['data']
        interface_report['output_error_list']['output_drops'] = value['output-error-list'][0]['output-drops'][0]['data']
        interface_report['output_error_list']['output_errors'] = value['output-error-list'][0]['output-errors'][0]['data']

        return interface_report