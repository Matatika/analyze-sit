from setuptools import setup, find_packages

setup(
    name="files-matatika-sit-datasets",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for Matatika SIT",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/*.yaml",
            "analyze/datasets/*.yml"
        ]
    }
)
