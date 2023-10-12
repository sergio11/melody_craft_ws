from setuptools import setup, find_packages

setup(
    name='SongCraftSEE',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.1.1',
        'Flask-SSE==0.2.1',
        'audiocraft==1.0.0',
    ],
    author='Sergio Sánchez Sánchez',
    author_email='dreamsoftware92@gmail.com',
    description='A Python package for generating melodies from text and sending SSE notifications.',
    url='https://github.com/sergio11/songcraftsee',
    keywords=['music', 'text', 'SSE', 'melody'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7, <4',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'songcraftsee = songcraftsee:app.run',
        ],
    }
)


"""
SongCraftSEE Setup

This setup script configures the installation of the SongCraftSEE package. SongCraftSEE is a Python package designed for generating melodies from textual content and providing real-time Server-Sent Events (SSE) notifications to clients. The package integrates Flask and other dependencies to achieve this functionality.

Project Details:
- Name: SongCraftSEE
- Version: 0.1
- Author: Sergio Sánchez Sánchez
- Email: dreamsoftware92@gmail.com
- Description: SongCraftSEE is a package that enables the generation of music from text input and the communication of progress and results to clients using SSE. It is intended for developers and enthusiasts interested in text-to-melody conversion and real-time event streaming.
- Repository: https://github.com/sergio11/songcraftsee
- Keywords: music, text, SSE, melody

Requirements:
- Flask 2.1.1
- Flask-SSE 0.2.1
- audiocraft 1.0.0

Development Status: Beta

License: MIT License

Python Version Compatibility: 3.7, 3.8, 3.9, 3.10

For more details, refer to the project's README.md file.
"""