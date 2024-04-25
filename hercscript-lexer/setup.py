#!/usr/bin/env python
"""Setup hercscript-lexers."""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
hercscript=hercscript_lexers:HercScriptLexer
'''

setup(
    name='hercscript-lexers',
    version='1.0.0',
    description='Pygments lexer package for hercscript.',
    author='Hercules Team',
    author_email='',
    url='',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ],
    zip_safe=True,
    license='MIT License',
    classifiers=[]
)