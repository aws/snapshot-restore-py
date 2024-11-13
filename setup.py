from setuptools import setup
import snapshot_restore_py

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="snapshot-restore-py",
    version=snapshot_restore_py.__version__,
    author=snapshot_restore_py.__author__,
    description="Runtime Hooks for AWS Lambda SnapStart - Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    keywords="serverless aws lambda python snapstart runtime hooks",
    url="https://github.com/aws/snapshot-restore-py",
    py_modules=["snapshot_restore_py"],
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    test_suite="tests",
)


