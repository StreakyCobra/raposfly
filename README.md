![logo][]

_**» Raspberry Pi Point of Sale on the Fly.**_

![raspberry_logo][]
[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)][LICENSE.md]



-----

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->

**Table of Contents**

- [Presentation](#presentation)
- [Licensing](#licensing)
- [License](#license)

<!-- markdown-toc end -->

# Presentation

This project provides a temporary, on the fly point of sale that can be deployed
anywhere where a power plug is available. It targets small events such as
village fairs that happen to run once a year. The main focus is to sell food and
drinks through tickets that will then be exchanged at the different desks.

The project is build on top of the _Raspberry Pi_ and support printers that are
supported by
the [`python-escpos`](https://github.com/python-escpos/python-escpos) library.


# Legal

- _Raspberry Pi_ is a trademark of the Raspberry Pi Foundation:
  http://www.raspberrypi.org

# License

This software is licensed under the term of the [GPL v3.0][] license:

    rapostfly, a Raspberry Pi Point of Sale on the Fly.
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

[logo]:           resources/images/logo.png
[raspberry_logo]: resources/images/raspberry_logo.png
[semver]:         http://semver.org/spec/v2.0.0.html
[LICENSE.md]:     LICENSE.md
[GPL v3.0]:       https://www.gnu.org/licenses/gpl-3.0.html
