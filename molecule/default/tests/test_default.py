import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('f',
                         ['python-apt', 'apt-transport-https', 'ca-certificates'])
def test_packages_installed(host, f):
    pkg = host.package(f)
    assert pkg.is_installed

# @pytest.mark.parametrize('f',
#                          ['/etc/ansible/facts.d/timezone.fact',
#                           '/etc/ansible/facts.d/resolver.fact',
#                           '/etc/ansible/facts.d/init.fact',
#                           '/etc/ansible/facts.d/cap12s.fact',
#                           '/etc/ansible/facts.d/core.fact',
#                           '/etc/ansible/facts.d/uuid.fact',
#                           '/etc/ansible/facts.d/tags.fact',
#                           '/etc/ansible/facts.d/root.fact'])
# def test_all_ansible_facts_created(host, f):
#     file = host.file(f)

#     assert file.exists
