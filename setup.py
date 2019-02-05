# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from setuptools import setup, find_packages

if sys.version_info[:2] < (3, 5):
    sys.exit('ZAP supports Python 3.5+ only')

# Read version.py
__version__ = None
__description__ = None
with open('zap/version.py') as f:
    exec(f.read())

# If the version is not stable, we can add a git hash to the __version__
if '.dev' in __version__:
    # Find hash for __githash__ and dev number for __version__ (can't use hash
    # as per PEP440)
    command_hash = 'git rev-list --max-count=1 --abbrev-commit HEAD'
    command_number = 'git rev-list --count HEAD'

    try:
        commit_hash = subprocess.check_output(command_hash, shell=True)\
            .decode('ascii').strip()
        commit_number = subprocess.check_output(command_number, shell=True)\
            .decode('ascii').strip()
    except Exception:
        pass
    else:
        # We write the git hash and value so that they gets frozen if installed
        with open(os.path.join('zap', '_githash.py'), 'w') as f:
            f.write("__githash__ = \"{}\"\n".format(commit_hash))
            f.write("__dev_value__ = \"{}\"\n".format(commit_number))

        # We modify __version__ here too for commands such as egg_info
        __version__ += commit_number

with open('README.rst') as f:
    README = f.read()

with open('CHANGELOG') as f:
    CHANGELOG = f.read()

setup(
    name='zap',
    version=__version__,
    description=__description__,
    long_description=README + '\n' + CHANGELOG,
    author='Kurt Soto, Simon Conseil',
    author_email='simon.conseil@univ-lyon1.fr',
    url='https://github.com/musevlt/zap',
    license='MIT',
    python_requires='>=3.5',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['numpy', 'scipy', 'astropy>=2.0', 'scikit-learn'],
    extras_require={'plot': ['matplotlib']},
    entry_points={
        'console_scripts': ['zap = zap.__main__:main']
    },
    keywords=['astronomy', 'astrophysics', 'science', 'muse', 'vlt',
              'sky subtraction'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics'
    ],
)
