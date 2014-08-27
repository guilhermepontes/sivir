from setuptools import setup, find_packages

def read(file):
  return open(file, 'r+').read()


setup(
  name = 'sivir',
  version = read("version"),
  url = 'https://github.com/guilhermepontes/sivir/',
  license = 'GNU GPL',
  author = 'Guilherme Pontes',
  author_email='guilhermepontes@msn.com',
  tests_require = ['unittest'],
  install_requires = ['requests>=2.2.1'],
  description = 'SIVIR: League of Legends API Library',
  long_description = read("README.md"),
  packages=['sivir, tests'],
  platforms='any',
  classifiers = [
    'Programming Language :: Python',
    'Natural Language :: English',
    'Environment :: Web Environment',
    'Intended Audience :: Web Developers',
    'License :: OSI Approved :: GNU GPL',
    'Operating System :: OS Independent'
  ],
  extras_require={
    'testing': ['unittest']
  }
)