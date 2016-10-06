import subprocess
import re


def describe_resource(resource_name):
    describe_cmd = "puppet describe %s --meta" % resource_name
    p = subprocess.Popen(describe_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (out, err) = p.communicate('stdout')
    out = out.decode('utf-8', 'replace')
    exit_code = p.returncode
    if exit_code != 0:
        raise Exception
    return out.strip()


def get_parameters(resource_name):
    description = describe_resource(resource_name)
    param_re = re.compile(r'- \*\*(.*)\*\*')
    res = param_re.findall(description)
    print(res)
