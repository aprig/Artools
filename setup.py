"""Setup Artools."""

from setuptools import setup

setup(name='Artools',
      description='Usefull scripts with Xarray',
      packages=['Artools'],
      package_dir={'Artools': 'Artools'},
      install_requires=['setuptools', ],
      zip_safe=False)
