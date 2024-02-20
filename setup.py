#!/usr/bin/env python


import os
from os.path import isfile
import subprocess
from setuptools import setup
from distutils.core import Extension, Command
from distutils.command.build_ext import build_ext

class BuildConfigure(Command):
    def initialize_options(self):
        pass
      
    def finalize_options(self):
        pass

    def run(self):
        os.chdir("pymitlm/mitlm")
        if not isfile('configure'):
            subprocess.call([
              "autoreconf",
              "--install"        
              ])
        if not isfile('Makefile'):
            subprocess.call([
              "./configure",
              "--enable-shared",
              "--disable-maintainer-mode",
              '--with-pic'
              ])
        subprocess.call(["make"])
        os.chdir("../..")

class BuildExtension(build_ext):
    def run(self):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        build_ext.run(self)
    sub_commands = [("build_configure", None)] + build_ext.sub_commands

setup(
    name = "pymitlm",
    packages = ['pymitlm'],
    cmdclass = {"build_configure": BuildConfigure, "build_ext": BuildExtension},
    ext_modules=[Extension('pymitlm._pymitlm',
                           [
                             'pymitlm/pymitlm.i',
                           ],
                           extra_objects=[
                             'pymitlm/mitlm/.libs/libmitlm.a',
                           ],
                           include_dirs=['pymitlm/mitlm/src'],
                           libraries=['gfortran'],
                           swig_opts=['-c++'],
                           extra_compile_args=['-std=gnu++11', '-fPIC']
                          )],
    py_modules=['pymitlm.pymitlm'],
)
