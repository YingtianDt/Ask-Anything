from setuptools import find_packages, setup

# minimal setup for brainscore
setup(
    name='ask-anything',
    packages=find_packages(),
    include_package_data=True,
    package_data={'':['*.txt', '*.md', '*.json', '*.csv', '*.tsv']},
)