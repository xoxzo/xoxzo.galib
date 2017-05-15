from setuptools import setup, find_packages

setup(
    name="xoxzo.galib",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={},
    test_suite = 'tests',
)
