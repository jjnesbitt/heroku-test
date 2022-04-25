from setuptools import find_packages, setup

setup(
    name="test",
    description="",
    python_requires=">=3.9",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
)
