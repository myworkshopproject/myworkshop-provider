# myworkshop-provider
OAuth provider and document sharing server for a network of _MyWorkshop_ clients.

## Features
 * OAuth provider to share a _Maker_ community;
 * Web REST API to share documents between _MyWorkshop_ clients.

## Getting started

### Requirements
 * python 3.6.9 or higher (package _python3_);

### Install
Install all the required tools in a virtualenv:
```
$ make install
```

### Serve

#### Development environment
To run the application locally in a development environment:
```
$ make serve
```

#### Production environment
Create a new file named `production.py` in `provider/settings` and write your production settings in it.

Edit `provider/settings/__init__.py`:
```
from .production import *
```

## Tech/framework used

### Backend
 * [Django 3.0](https://www.djangoproject.com/) : High-level Python Web framework.

### Frontend
 * [Bootstrap 4.4.1](https://getbootstrap.com/) : A responsive web toolkit.
 * [Boostwatch 4.4.1](https://bootswatch.com/) : Free themes for Bootstrap.
 * [Font Awesome 5.11.2](https://fontawesome.com/) : Icon set and toolkit.
 * [jQuery 3.4.1](https://jquery.com/) : A feature-rich JavaScript library for dynamic web pages.

## Versioning
We use [SemVer](http://semver.org/) for versioning. See the [CHANGELOG.md](CHANGELOG.md) file for details.

## Technical details
To know more about the development guidelines of this project, see the [TECHNICAL_DETAILS.md](TECHNICAL_DETAILS.md) file.

## Contributing
If you'd like to contribute, please raise an issue or fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contributors
 * **Julien Lebunetel** - [jlebunetel](https://github.com/jlebunetel)
