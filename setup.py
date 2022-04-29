from setuptools import find_packages, setup

setup(
    name="test",
    description="",
    use_scm_version={
        "version_scheme": "post-release",
        "relative_to": __file__,
        "root": "..",
    },
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
)
