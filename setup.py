from setuptools import setup, find_packages

import pyclasher


with open('requirements.txt') as requirements_txt:
    requirements = requirements_txt.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as readme_md:
    readme = readme_md.read()

packages = find_packages(where="pyclasher")

setup(
    name='pyclasher',
    version=pyclasher.__version__,
    author='201st-Luka',
    description='pyclasher - an object-oriented wrapper client for Python that provides easy access to the requested data',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=packages,
    install_requires=requirements,
    tests_require=[
        'pytest',
    ],
    url='https://github.com/your-username/your-repo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Topic :: Games/Entertainment',
    ],
    keywords='python async clashofclans api wrapper',
    python_requires='>=3.11',
    package_data={package: ['*.pyi'] for package in packages}
)
