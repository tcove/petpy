from setuptools import setup

setup(name='petpy',
      version='0.3',
      description='Petrophysics utilities',
      utl='https://www.shell.com/',
      author='Shell',
      author_email='thomas.ovestad@shell.com',
      license='Apache 2',
      packages=['petpy'],  # this refers to the name of the package, i.e. the petpy dir with code and __init__. It will import whatever is stated in __init__
      install_requires=['numpy'],
      tests_require=['pytest', 'pytest-cov'],
      entry_points={
          'console_scripts': ['gardner=petpy.__main__:main']
      }
      )
