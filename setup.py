#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-ergopack',
    version='0.0.2',
    license='MIT',
    author='anki-code',
    author_email='no@no.no',
    description="Meta package that installs group of ergonomic xontribs in xonsh shell.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'xontrib-prompt-bar',
        'xontrib-argcomplete',
        'xontrib-onepath',
        'xontrib-output-search',
        'xontrib-pipeliner',
        'xontrib-sh',
        'xontrib-back2dir'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/anki-code/xontrib-ergopack',
    project_urls={
        "Documentation": "https://github.com/anki-code/xontrib-ergopack/blob/master/README.md",
        "Code": "https://github.com/anki-code/xontrib-ergopack",
        "Issue tracker": "https://github.com/anki-code/xontrib-ergopack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
