from setuptools import setup, find_packages

with open('./docs/README.md') as f:
    long_description = f.read()
setup(
    name='WebNavigator-AI',
    version='0.1.0',
    description='The WebNavigator-AI is designed to automate the process of gathering information from the internet, such as to navigate websites, perform searches, and retrieve data.',
    author='Jaysurya046',
    url='https://github.com/Jaysurya046/WebNavigator-AI',
    packages=find_packages(),
    install_requires=[
        'langgraph',
        'tenacity',
        'requests',
        'playwright',
        'termcolor',
        'python-dotenv',
        'httpx',
        'nest_asyncio',
        'MainContentExtractor'
    ],
    entry_points={
        'console_scripts': [
            'WebNavigator-AI=main:main'
        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT'
)