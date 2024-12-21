import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="co2_reduction_project",
    version="0.0.1",
    author="Your Name",
    author_email="you@example.com",
    description="A project to optimize transport routes and reduce CO2 emissions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "pulp",
        "scikit-learn",
        "pandas",
        "joblib"
    ],
    python_requires='>=3.7',
)
