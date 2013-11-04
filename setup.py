from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='oeis',
    version='0.1',
    description='OEIS utilities and sequence generation',
    long_description=readme(),
      classifiers=[
          'Programming Language :: Python :: 2.7.3',
          ],
      keywords='oeis',
    url='https://github.com/GuySrinivasan/oeis',
    author='Guy Srinivasan',
    author_email='srinivgp@gmail.com',
    license='MIT',
    packages=['oeis'],
    install_requires=[
        'markdown',
    ],
    zip_safe=False)


