class FilterModule(object):

    def filters(self):
        return {
            'cleanup_switch_mac': self.cleanup_switch_mac,
        }

    def cleanup_switch_mac(self, value):
        macs = []
        for each in value:
            for mac in each["mac"]:
                macs.append(mac)
        return macs
