![logo](resources/images/logo.png)

_**» Raspberry Pi Point of Sale on the Fly.**_

[![raspberry-badge](https://img.shields.io/badge/run%20on-Rasberry%20Pi%203-red.svg)](https://www.raspberrypi.org/)
[![Powered by docker](https://img.shields.io/badge/powered%20by-docker-blue.svg)](https://www.docker.com/)
[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)
[![License](https://img.shields.io/badge/license-GPLv3-yellow.svg)][LICENSE.md]

-----

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [Presentation](#presentation)
- [Documentation](#documentation)
- [Version numbers](#version-numbers)
- [Contributing](#contributing)
- [License](#license)
- [Legal](#legal)

<!-- markdown-toc end -->

-----

# Presentation

This project provides an on-the-fly point of sale that can be deployed anywhere
where a power plug is available. It targets small events such as village fairs
that happen to run once a year. The initial focus is to sell food and drinks
through tickets that will then be exchanged at the different desks.

The project is build on top of the _Raspberry Pi 3_ and support all printers
that are supported by the [`python-escpos`][python-escpos] library.

[python-escpos]:   https://github.com/python-escpos/python-escpos


# Documentation

- [Installation][installation]
- [Milestones][milestones]

[installation]:    doc/installation.rst
[milestones]:      doc/milestones.rst


# Version numbers

This software uses [Semantic Versioning v2.0.0][semver]. Version numbers are of
the form:

    MAJOR.MINOR.PATCH

- `MAJOR` increases with backwards-incompatible API changes.
- `MINOR` increases with functionality added in a backwards-compatible manner.
- `PATCH` increases with backwards-compatible bug fixes.

Any part may also be incremented freely at any time for any reason.

*Note*: `MAJOR` version `0` is for initial development and does not follow the
`MINOR` and `PATCH` schema. Do not expect any stability during this period.

[semver]:          http://semver.org/spec/v2.0.0.html


# Contributing

**Branching**

The development of this project follows Vincent Driessen's
[git branching model][git-branching].

*Note*: Initial development (`MAJOR` version `0`) does not follow this
branching model. Only the `master` branch is used.

**Commit messages**

Git commit messages are better if they follow Tim Pope's
[recommendations][git-messages].

**Pull requests**

Simple changes must be squashed in one commit. Bigger changes may be split over
more than one commit, but this kind of changes should be discussed beforehand
anyway.

Contributions will be reviewed by the maintainer, who will decide to include it
or not, and who may ask for changes in order to keep the project consistent.

Commit messages may be reworded before being merged. Original author's name will
be kept and commit will be signed-off. The author name will be added to the list
of contributors.

[git-branching]:   http://nvie.com/posts/a-successful-git-branching-model/
[git-messages]:    http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html


# License

This software is licensed under the term of the [GPL v3.0][] license:

    raposfly, a Raspberry Pi Point of Sale on the Fly.
    Copyright (C) 2016 Fabien Dubosson <fabien.dubosson@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

See [LICENSE.md][] for the complete license.

[GPL v3.0]:        https://www.gnu.org/licenses/gpl-3.0.html
[LICENSE.md]:      LICENSE.md


# Legal

- _Raspberry Pi_ is a trademark of the Raspberry Pi Foundation:
  http://www.raspberrypi.org
