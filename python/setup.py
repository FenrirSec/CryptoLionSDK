from setuptools import setup, find_packages

setup(
    name='cryptolion-sdk',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'cryptolion.libs': ['*.so', '*.dylib', '*.dll'],
    },
    install_requires=[],
    author='CryptoLion Team',
    author_email='support@cryptolion.com',
    description='Official SDK for CryptoLion License Management System',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cryptolion/sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
