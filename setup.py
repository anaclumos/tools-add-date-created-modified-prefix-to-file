from setuptools import setup

setup(
    name='dateprefix',
    version='1.0.0',
    summary="Add Date Created Prefix to Files",
    home_page="https://github.com/anaclumos/tools-add-date-created-modified-prefix-to-file",
    author="anaclumos",
    license="MIT",
    description="Add Date Created Prefix to Files",
    entry_points={
        'console_scripts': [
            'dateprefix=dateprefix:run'
        ]
    },

)
