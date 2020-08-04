class FilterModule(object):

    def filters(self):
        return {
            'wan_health_cleanup_brief': self.wan_health_cleanup_brief,
        }

    def wan_health_cleanup_brief(self, value):
        interface_report = {}

        interface_report['name'] = value['name'][0]['data']
        interface_report['oper_status'] = value['oper-status'][0]['data']
        interface_report['last_flap'] = value['interface-flapped'][0]['data']
        # vdsl info
        interface_report['vdsl_info'] = {}
        interface_report['vdsl_info']['line_status'] = value['vdsl-information'][0]['vdsl-line-status'][0]['data']
        interface_report['vdsl_info']['line_profile'] = value['vdsl-information'][0]['vdsl-line-profile-type'][0]['data']
        interface_report['vdsl_info']['seconds_in_showtime'] = value['vdsl-information'][0]['vdsl-seconds-in-showtime'][0]['data']
        # vdsl statistics
        interface_report['vdsl_statistics'] = {}
        interface_report['vdsl_statistics']['far_end_attenuation'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-far-end-attenuation'][0]['data']
        interface_report['vdsl_statistics']['near_end_attenuation'] = value['vdsl-information'][0]['vdsl-statistics'][0]['vdsl-near-end-attenuation'][0]['data']
        # logical interface
        interface_report['logical_interface'] = {}
        interface_report['logical_interface']['encapsulation'] = value['logical-interface'][0]['encapsulation'][0]['data']

        return interface_report