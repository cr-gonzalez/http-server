from setuptools import setup

setup(
    name="http-server",
    description="This package runs an http server and client",
    version=0.1,
    license='MIT',
    author="Alex German, Crystal Lessor",
    author_email="alexgerman11233@gmail.com, lessor88@gmail.com",
    py_modules=['server', 'client'],
    package_dir={' ': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']}
    # entry_points={
    #     'console_scripts': [
    #         'client=src.client:client'
    #     ]
    # }
)