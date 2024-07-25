# Ansible Collection - calaviaorg.setup

This Ansbile collection is intended to be used in order to setup:

* git
* vim
* tmux

## Supported platforms

* MacOS
* Ubuntu / Debian

## Development

### Usefull commands

* tox -e unit-py3.12-2.17 --ansible --conf tox-ansible.ini -- junit-xml=tests/output/junit/unit.xml
* tox -e integration-py3.12-2.17 --ansible --conf tox-ansible.ini -- junit-xml=tests/output/junit/integration.xml
