from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result


# nornir_napalm需要用到的platform: huawei_vrp

nr = InitNornir(config_file="nornir.yaml", dry_run=True)
results = nr.run(task=napalm_get, getters=["get_interfaces_ip", "get_interfaces"])
print_result(results)