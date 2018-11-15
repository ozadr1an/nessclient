import os

from setuptools import setup


def get_version():
    version_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'VERSION')
    v = open(version_path).read()
    if type(v) == str:
        return v.strip()
    return v.decode('UTF-8').strip()


readme_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)),
    'README.md',
)
long_description = open(readme_path).read()

try:
    version = get_version()
except Exception as e:
    version = '0.0.0-dev'

setup(
    name='py-ness-232',
    version=version,
    packages=['py_ness_232'],
    author="Nick Whyte",
    author_email='nick@nickwhyte.com',
    description="Implementation/abstraction of the Ness D8x / D16x Serial Interface ASCII protocol",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nickw444/py-ness-232',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    test_suite="py_ness_232_tests",
    install_requires=[
        'justbackoff',
        'dataclasses;python_version<"3.7"'
    ],
    extras_require={
        'cli': ['click']
    },
)
