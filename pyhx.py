import sys
import os
from importlib import invalidate_caches
from importlib.abc import SourceLoader
from importlib.machinery import FileFinder
import subprocess

class HaxeLoader(SourceLoader):
    haxe_bin = 'haxe'

    def __init__(self, fullname, path):
        self.fullname = fullname
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, filename):
        """exec_module is already defined for us, we just have to provide a way
        of getting the source code of the module"""
        pyfile = filename + '.py'
        if not os.path.exists(pyfile) or os.path.getmtime(pyfile) < os.path.getmtime(filename):
            # recompile the Haxe file
            status = subprocess.call([self.haxe_bin, '-cp', os.path.dirname(filename), os.path.basename(filename), '-python', pyfile])
            if status:
                raise ImportError("Haxe compilation of {} failed with status {}".format(filename, status))
        with open(pyfile) as f:
            data = f.read()
        return data

def install(haxe_bin='haxe'):
    HaxeLoader.haxe_bin = haxe_bin
    loader_details = HaxeLoader, [".hx"]

    # insert the path hook ahead of other path hooks
    sys.path_hooks.insert(0, FileFinder.path_hook(loader_details))
    # clear any loaders that might already be in use by the FileFinder
    sys.path_importer_cache.clear()
    invalidate_caches()
