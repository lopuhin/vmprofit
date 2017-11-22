from setuptools import setup


def get_long_description():
    readme = open('README.rst').read()
    changelog = open('CHANGES.rst').read()
    return '\n\n'.join([readme, changelog])


setup(
    name='vmprofit',
    version='0.1.1',
    packages=['vmprofit'],
    install_requires=[
        'vmprof',
    ],
    url='https://github.com/lopuhin/vmprofit',
    description='vmprof helpers',
    long_description=get_long_description(),
    license='MIT license',
    author='Konstantin Lopuhin',
    author_email='kostia.lopuhin@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
