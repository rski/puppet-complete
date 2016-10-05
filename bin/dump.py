from __future__ import print_function
from puppet_complete.lib import modulepath

path = modulepath.Modulepath("/etc/puppet/modules:/does/not/exist")
print(path.load_modules())
