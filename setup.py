from distutils.core import setup
import setuptools

setup(
    name='finsymbols',
    version='1.1.1',
    packages=['finsymbols'],
    package_dir={'finsymbols': 'finsymbols'},
    package_data={'finsymbols': ['exchanges/*.csv']},
    include_package_data=True,
    author='Dwayne V Campbell',
    author_email='dwaynecampbell13 _at_ gmail.com',
    description='Retrieves list of all symbols present in SP500, NASDAQ ,AMEX and NYSE',
    long_description=open('README.md').read(),
    url='http://skillachie.github.io/finsymbols/',
    download_url='http://pypi.python.org/pypi/finsymbols',
    keywords='stocks stockmarket yahoo finance SP500 NASDAQ AMEX NYSE'.split(),
    license='GNU LGPLv2+',
    install_requires=[
        "beautifulsoup4 >= 4.2.1"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Investment',
    ]
)
