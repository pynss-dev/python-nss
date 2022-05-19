"""Manage C dependencies."""

import os
import platform

from conans import ConanFile, CMake

version = platform.python_version_tuple()
base_dir = (
    '/usr/local/Cellar/python@3.9/3.9.12/Frameworks/Python.framework/Versions/3.9'
)
os.path.join(base_dir, 'include', 'python3.9')


class ConanInstall(ConanFile):
    """Manage Conan specfile."""

    name = 'python-nss'
    version = '2.0.0.dev2'
    requires = 'nss/3.77', 'pybind11/2.3.0@conan/stable'
    settings = 'os', 'compiler', 'arch', 'build_type'
    exports = '*'
    generators = 'cmake'
    build_policy = 'missing'

    def build(self) -> None:
        """Proform build."""
        cmake = CMake(self)
        pythonpaths = (
            '-DPYTHON_INCLUDE_DIR=C:/Python27/include'
            + '-DPYTHON_LIBRARY=C:/Python27/libs/python27.lib'
        )
        self.run(
            'cmake %s %s -DEXAMPLE_PYTHON_VERSION=2.7'
            % (cmake.command_line, pythonpaths)
        )
        self.run('cmake --build . %s' % cmake.build_config)

    def package(self):
        """Package dependencies."""
        self.copy('*.py*')
        self.copy('*.so')

    def package_info(self):
        """Prepare package info."""
        self.env_info.PYTHONPATH.append(self.package_folder)
