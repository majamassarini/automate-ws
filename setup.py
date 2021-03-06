from os import path
from glob import glob
from setuptools import setup, find_packages

with open(path.join(".", "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="automate-ws",
    version="0.9.1",
    url="https://github.com/majamassarini/automate-home",
    description="A simple web server to interact with automate-home projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Maja Massarini",
    author_email="maja.massarini@gmail.com",
    data_files=[
        ("etc/automate-home/templates", glob("ws/templates/*.html")),
        ("etc/automate-home/templates/light", glob("ws/templates/light/*.html")),
        (
            "etc/automate-home/templates/light/event/",
            glob("ws/templates/light/event/*.html"),
        ),
        ("etc/automate-home/templates/event", glob("ws/templates/event/*.html")),
        ("etc/automate-home/templates/event", glob("ws/templates/event/*.html")),
        ("etc/automate-home/static", glob("ws/static/*.css")),
        ("etc/automate-home/static", glob("ws/static/*.js")),
        ("etc/automate-home/static", glob("ws/static/*.png")),
        ("etc/automate-home/static", glob("ws/static/*.svg")),
        ("etc/automate-home/static/block", glob("ws/static/block/*.js")),
        ("etc/automate-home/static/generator", glob("ws/static/generator/*.js")),
        ("etc/automate-home/static/media", glob("ws/static/generator/*")),
        ("etc/automate-home/static/msg/js", glob("ws/static/msg/js/*.js")),
        ("etc/automate-home/static/msg/json", glob("ws/static/msg/json/*.js")),
    ],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Intended Audience :: Developers",
    ],
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=[
        "aiohttp_security==0.4.0",
        "aiohttp_session==2.9.0",
        "aiohttp-jinja2==1.5",
        "aiohttp==3.8.1",
        "automate-graphite-feeder",
        "automate-home-assistant-plugin",
        "automate-home",
        "automate-knx-plugin",
        "automate-lifx-plugin",
        "automate-sonos-plugin",
        "colour",
        "multidict==4.7.6",
    ],
)
