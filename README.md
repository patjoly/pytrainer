# Pytrainer (Fork of)
This repository is a fork of the original Pytrainer project.

Main goals of this fork:
- SQLAlchemy 2.0 modernization
- Python compatibility updates
- dependency cleanup
- maintenance and bug fixes

The original Pytrainer project can be found here: https://github.com/pytrainer/pytrainer

This fork aims to preserve the application's architecture and behaviour while updating the codebase for current Python ecosystem and applying functional updates to features like maps and charts.

# pytrainer - Free your sports
pytrainer is a desktop application for logging and graphing sporting
activities such as running or cycling sessions. Data can be imported from GPS
devices, files or input manually. Currently pytrainer supports GPX, TCX, and
FIT files.

## Installation
Most popular Linux distributions (Debian, Ubuntu, Fedora and so on) already
contain a pytrainer package, use that if available. If a package is not
available for your system you can install from source, see below.

### Installation from source tarball
Copy tarball file to a location where you have write and execution rights (e.g. your `$HOME` directory).

```shell
tar -xzf pytrainer-X.Y.Z.tar.gz
cd pytrainer-X.Y.Z
pip install ."[gui]"
pytrainer
```

### Installation into a venv (for development)
This installation method is very similar to the basic source install above.
For development it makes more sense to start from a git clone instead of a
tarball, and also makes more sense to install into a virtual Python
environment.

```shell
git clone https://github.com/pytrainer/pytrainer.git
cd pytrainer
python3 -m venv .venv
.venv/bin/pip install -e ".[gui]"
.venv/bin/pytrainer
```

### Additional packages
For map functionality the GIR bindings for WebKit2 need to be installed.

Certain plugins and extensions also need additional software:

| Package       | Plugin or extension                                                               |
|---------------|-----------------------------------------------------------------------------------|
| GPSBabel      | Garmin via GPSBabel and Google Earth plugins (aka garmin-hr)                      |
| garmintools   | Import from Garmin GPS device (Garmin via garmintools plugin aka garmintools_full)|
| Perl          | Garmin FIT plugin                                                                 |
| wordpresslib  | Wordpress extension, already distributed within pytrainer tarball                 |
| httplib2      | Wordpress extension                                                               |
| SOAPpy        | Dotclear extension                                                                |
| GDAL          | Elevation correction extension, via gdal-python or python-gdal                    |

## Further Resources
* FAQ [https://github.com/pytrainer/pytrainer/wiki/FAQ](https://github.com/pytrainer/pytrainer/wiki/FAQ)
* Distribution list: pytrainer-devel@lists.sourceforge.net
* Development guide: [https://github.com/pytrainer/pytrainer/wiki/Development-guide](https://github.com/pytrainer/pytrainer/wiki/Development-guide)
* Localization guide: [https://github.com/pytrainer/pytrainer/wiki/Localization-guide](https://github.com/pytrainer/pytrainer/wiki/Localization-guide)
* Report an Issue: [https://github.com/pytrainer/pytrainer/issues](https://github.com/pytrainer/pytrainer/issues)

## Relationship to upstream

This fork started as a compatibility and modernization effort for the original Pytrainer project.

The intent is to keep the original application's functionality while updating dependencies and infrastructure for modern Python environments. Updates to upstream will be continuously applied.
