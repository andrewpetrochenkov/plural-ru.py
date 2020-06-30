import setuptools

setuptools.setup(
    name='plural-ru',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/plural']
)
