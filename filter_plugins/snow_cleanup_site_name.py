class FilterModule(object):

    def filters(self):
        return {
            'find_cpe': self.snow_cleanup_site_name,
        }

    def snow_cleanup_site_name(self, value):
        # cpe = {}
        site_name = value.replace(" ", "-")
        site_name = site_name.lower()
        return site_name