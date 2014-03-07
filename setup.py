from setuptools import setup, find_packages
import os

version = '0.1'

setup(
    name='slc.privateicalexport',
    version=version,
    description="Provide a random URL to expose a private iCal feed",
    long_description=open("README.rst").read() + "\n" +
    open(os.path.join("docs", "HISTORY.rst")).read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='icalendar',
    author='Cillian de Róiste',
    author_email='deroiste@syslab.com',
    url='https://github.com/syslabcom/slc.privateicalexport',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['slc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        'plone.app.dexterity',
        'plone.namedfile [blobs]',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    extras_require={
        'test': [
            'plone.app.testing',
        ],
    },
)
