# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


testpkgs = [

]
install_requires = [
    'redis',
    'aiohttp',
    'aiohttp_mako',
    'cryptography',
    'aiohttp_session'
]

setup(
    name='blog',
    version='0.1',
    description='',
    author='Amin Etesamian',
    author_email='aminetesamian1371@gmail.com',
    url='https://github.com/eteamin/blog',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    tests_require=testpkgs,
    include_package_data=True,
)
