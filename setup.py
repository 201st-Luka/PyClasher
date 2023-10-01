from setuptools import setup, find_packages

import pyclasher


with open('requirements.txt') as requirements_txt:
    requirements = requirements_txt.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as readme_md:
    readme = readme_md.read()

packages = find_packages(exclude=["testing*", "tests*"])
print(packages)

setup(
    name='pyclasher',
    version=pyclasher.__version__,
    author='201st-Luka',
    author_email='201stLuka@gmail.com',
    description='PyClasher - an object-oriented wrapper client for Python '
                'that provides easy access to the requested data',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=packages,
    install_requires=requirements,
    # tests_require=[
    #     'pytest',
    # ],
    url='https://github.com/201st-Luka/PyClasher',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        'Topic :: Games/Entertainment',
    ],
    keywords='python async clashofclans api wrapper',
    python_requires='>=3.10',
    package_data={package: ['*.pyi'] for package in packages}
)
