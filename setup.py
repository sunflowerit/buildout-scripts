import os
import sys
from setuptools import setup, find_packages

version = '0.1'

if sys.version_info < (2, 6):
    sys.stderr.write("This package requires Python 2.6 or newer. "
                     "Yours is " + sys.version + os.linesep)
    sys.exit(1)

# a sufficient version of pip is needed to parse Odoo requirement file
# version 1.4.1 is the one required by reportlab anyway
requires = [
  'anybox.recipe.odoo',
  'pylint==1.6.4',
  'pylint_odoo'
]

if sys.version_info < (2, 7):
    requires.append('ordereddict')
    requires.append('argparse')

setup(
    name="therp.scripts.odoo",
    version=version,
    author="Sunflower IT",
    author_email="info@sunflowerweb.nl",
    description="Buildout scripts for use with Odoo",
    license="AGPLv3+",
    url="https://github.com/sunflowerit",
    packages=find_packages(),
    namespace_packages=['therp','therp.scripts'],
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
    tests_require=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Buildout :: Recipe',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Affero General Public License v3 or '
        'later (AGPLv3+)',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
             'pylint = therp.scripts.odoo.linter:do_pylint',
        ]
    }
)
