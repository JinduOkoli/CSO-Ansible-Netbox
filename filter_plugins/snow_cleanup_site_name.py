class FilterModule(object):

    def filters(self):
        return {
            'snow_cleanup_site_name': self.snow_cleanup_site_name,
        }

    def snow_cleanup_site_name(self, value):
        # cpe = {}
        site_name = value.replace(" ", "-")
        site_name = site_name.lower()
        return site_name