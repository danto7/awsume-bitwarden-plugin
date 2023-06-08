from setuptools import setup

setup(
    name="awsume-bitwarden-plugin",
    version="0.0.1",
    description="Automates awsume MFA entry via bitwarden CLI.",
    entry_points={"awsume": ["bitwarden = bitwarden"]},
    author="Daniel Jensen",
    py_modules=["bitwarden"],
)
