from distutils.core import setup

setup(
    name='hide_my_ass',
    version='0.1',
    packages=['axh', 'axh.proxy'],
    namespace_packages=['axh'],
    url='https://github.com/axle-h/hide-my-ass',
    license='',
    author='Alex Haslehurst',
    author_email='alex.haslehurst@gmail.com',
    description='Scraper for http://proxylist.hidemyass.com/',
    requires=['beautifulsoup4', 'cssutils', 'html5lib'],
    install_requires=['beautifulsoup4', 'cssutils', 'html5lib']
)