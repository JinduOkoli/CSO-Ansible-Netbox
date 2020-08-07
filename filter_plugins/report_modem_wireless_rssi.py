class FilterModule(object):

    def filters(self):
        return {
            'report_modem_wireless_rssi': self.report_modem_wireless_rssi,
        }

    def report_modem_wireless_rssi(self, value):
        report_rssi = {}

        # connection time
        report_rssi['rssi'] = value['parsed_output']['wwand-modem-wireless-interface-rssi'][0]['rssi'][0]['data']

        return report_rssi
