"""
Package config for selfie bot
"""
import setuptools

setuptools.setup(
    name='trans_girls_rule_the_world',
    version='2.0.0',
    description='A tumblr bot to reblog trans girl\'s selfies',
    url='https://github.com/Deafjams/trans_girls_rule_the_world',
    author='Emma Foster',
    license='Public Domain',
    install_requires=[
        'pymongo',
        'pytumblr',
        'emoji',
        'plan'
    ],
    package_dir={
        'trans_girls_rule_the_world': 'trans_girls_rule_the_world'
    },
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 5 - Production",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7"
    )
)