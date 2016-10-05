from os import path, listdir, walk
import subprocess

class Modulepath(object):

    def __init__(self, modulepath):
        self.paths = self._get_existing_paths(modulepath)

    def _get_existing_paths(self, modulepath):
        """Return a list of the forders in the modulepath that exist"""
        path_strings = modulepath.split(":")
        return [x for x in path_strings if path.exists(x)]

    def load_modules(self):
        """Read all the modules in the modulepath in a hash

        {
         "module1": {"class1": [parameters]}
                    {"class11": [parameters]}
         "module2": {"class2": [parameters]}
        }
        Basically a hash structured like a tree.

        """
        puppet_env = {}
        for module_dir in self.paths:
            pp_files = self._get_pp_files(module_dir)

        self.parse_files(pp_files)


    def _get_pp_files(self, module_dir):
        """Get all the .pp files under the manifests/ folders of all modules in a dir"""
        pp_files = []
        modules = [path.join(module_dir, x) for x in listdir(module_dir)]
        for module in modules:
            for root, dirs, files in walk(path.join(module, "manifests")):
                for file in files:
                    if file.endswith(".pp"):
                        pp_files.append(path.join(root, file))

        return pp_files


    def parse_files(self, pp_files):
        for file in pp_files:
            dump = "puppet parser dump %s " % file
            subprocess.call(dump.split())
