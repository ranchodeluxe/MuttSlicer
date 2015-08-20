from setuptools import setup, find_packages

setup(
    name='MuttSlicer',
    version='0.0.1',
    description='for the love absurd Python data structures',
    url='https://github.com/thebigspoon/MuttSlicer',
    author='junkmob',
    author_email='gregcorradini+junkmob@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='experimental whynot',
    packages=find_packages(exclude=['docs',]),
    install_requires=['mock>=1.0.1','nose>=1.3.7'],
    # pip install -e .['dev','test]
    extras_require={
        'dev': ['mock>=1.0.1','nose>=1.3.7'],
        'test': ['mock>=1.0.1','nose>=1.3.7'],
    },
    scripts=['bin/kickoff-muttslicer-tests.py']
)
