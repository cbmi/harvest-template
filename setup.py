from setuptools import setup, find_packages

PACKAGE = 'harvest_project'
VERSION = __import__(PACKAGE).get_version()

kwargs = {
    'name': PACKAGE,
    'version': VERSION,
    'packages': find_packages(),
    'test_suite': 'test_suite',
    'author': '',
    'author_email': '',
    'description': '',
    'license': '',
    'keywords': '',
    'url': '',
    'classifiers': [],
}

setup(**kwargs)
