from setuptools import setup

setup(
    name='awsume-bitwarden-plugin',
    version='1.1.0',
    description='Automates awsume MFA entry via bitwarden CLI.',
    entry_points={
        'awsume': [
            'bitwarden = bitwarden'
        ]
    },
    author='Daniel Jensen',
)
