#!/usr/bin/env python
# Copyright: (c) 2018, Network to Code, Calvin Remsburg <calvin.remsburg@networktocode.com>


ANSIBLE_METADATA = {
  "metadata_version": "1.0",
  "status": ["preview"],
  "supported_by": "community"
}

DOCUMENTATION = '''
  ---
  module: cso_create_site
  version_added: "2.8.9"
  short_description: Create a SD-WAN site in CSO
  description:
    - This module is used to create SD-WAN sites in CSO
    - Module is idempotent
  author: Calvin Remsburg (@packetferret)
  options:
    username:
      description:
        - The username used to authenticate with the CSO.
      required: False
      type: str
    password:
      description:
        - The password used to authenticate with the CSO.
      required: False
      type: str
    provider:
      description:
        - Dictionary which acts as a collection of arguments used to define the
          characteristics of how to connect to the device.
        - Arguments username, and password must be specified in either
          provider or local param.
        - Local params take precedence, e.g. username is preferred to
          provider["username"] when both are specified.
      required: False
      type: dict
    site_name:
      description:
        - Name of the site being created/deleted
      required: True
      type: str
    config:
      description:
        - configuration file of the site being created/deleted
      required: True
      type: str
    state:
      description:
        - Control if site is absent / present in the CSO.
      required: True
      type: str
      choices: ["absent", "present"]
    token:
      description:
        - token 
'''

EXAMPLES = '''
  tasks:
    - name: Create a SD-WAN site
      cso_create_site:
        site_name: "{{ inventory_hostname }}"
        config: "{{ config }}"
        state: present
        token: "{{ token }}"
'''
import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import env_fallback
# from ansible.module_utils.basic import return_values
from cso_ansible_sdk.api import CSO


def main():
    argument_spec = dict(
      site_name=dict(required=True, type="str"),
      config=dict(required=True, type="dict"),
      state=dict(required=True,  choices=['present', 'absent'], type="str"),
      token=dict(required=True, type="str"),
    )

    changed = False
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    site_name = module.params["site_name"]
    config = module.params["config"]
    state = module.params["state"]
    token = module.params["token"]

    cso = CSO(api_token=token)

    try:
      create_payload = json.dumps(config)
      delete_payload = json.dumps(
        {
          "input": {
            "tenant_name": "AcmeCorp",
            "remove_tenant": False,
            "forced": True,
            "sites": [
              {
                "site_name": site_name
              }
            ]
          }
        }
      )
    except Exception as e:
      module.fail_json(msg=str(e))

    if state == 'absent':
      value_found = True
      if value_found:
        changed = True
        if not module.check_mode:
          try:
            cso.delete_site(delete_payload)
          except Exception as e:
            module.fail_json(msg=str(e))
    elif state == 'present':
      value_found = False
      if not value_found:
        changed = True
        if not module.check_mode:
          try:
            cso.create_site(create_payload)
          except Exception as e:
            module.fail_json(msg=str(e))

    module.exit_json(**{'changed': changed})


if __name__ == '__main__':
    main()
