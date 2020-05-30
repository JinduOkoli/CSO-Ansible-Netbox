# CSO Ansible Netbox

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/3/31/Juniper_Networks_logo.svg)](https://www.juniper.net/us/en/products-services/sdn/contrail/contrail-service-orchestration/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

`CSO-Ansible-Netbox` is an easier way to interact with Juniper's Contrail Service Orchestrator for building out SD-WAN sites.

- ease the authentication process with CSO for tokens
- build out new SD-WAN sites
- delete active SD-WAN sites
- retrieve statistics from your production SD-WAN environment

## New Features

> Native integration with Netbox for data collection

## Dependencies

A custom SDK written for this interaction, it's focus is to simplify the API interation

*[cso_ansible_sdk](https://pypi.org/project/cso_ansible_sdk/) - interact with CSO's REST API

## Installation

Python packages are installed with the pip command

```sh
$ pip install cso_ansible_sdk
```

## Very Important!

Please make sure to create your own `secrets.yml` file and store it in `group_vars/all` directory. This file hosts many variables necessary to complete the ansible playbook, without this file all of your plans for SD-WAN automation are destroyed. 

The `secrets_example.yml` file from the root directory of this project will get you started, simply update the variables with the values appropriate for your environment and move it to `group_vars/all` directory, overwriting the current file there.

This should do the trick nicely

```sh
$ mv secrets_example.yml ./group_vars/all/secrets.yml
```

### Optional:
> Leverage Ansible-Vault to encrypt the `secrets.yml` file before hosting on the public internet

> `ansible-vault encrypt secrets.yml`

## Development

Want to contribute? Great!

Submit a PR and let's work on this together :D
