[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

This is the Backend API for The Turing Index. It is a RESTful API that serves JSON.

### Built With

- Python 3.8.6
- Flask 1.1.2
- Continuous Integration with Travis CI
- Continuous Deployment to Heroku

## Getting Started

You can consume the set the API up locally for your development environment by following the instructions below.

### Prerequisites

- Get Python Version 3.8.6
  - TIP: Use `pyenv` to manage versionings

### Installation

- Clone down this repo and `cd` into it
- Activate a virtual environment `python -m venv ./venv`
- Install the dependencies `pip install -r requirements.txt`
- Start the server: `gunicorn app:app`
- The API will run at `localhost:8000`

When you are done
- Shut down the server `ctrl+C`
- Deactivate your virtual environment `deactivate`

<!-- USAGE EXAMPLES -->
## Usage

### GET '/calendars'

#### [Click to see it live](https://fast-depths-29900.herokuapp.com/api/v1/calendars)


### GET '/demo'

#### [Click to see it live](https://fast-depths-29900.herokuapp.com/api/v1/demo)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/the-turing-index/api/issues) for a list of proposed features (and known issues).


### Known Issues

The JSON response for `/calendars` currently does not serve live links to any meetings.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


Project Link: [https://github.com/the-turing-index/flask-api](https://github.com/the-turing-index/flask-api)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/the-turing-index/api.svg?style=flat-square
[contributors-url]: https://github.com/the-turing-index/api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/the-turing-index/api.svg?style=flat-square
[forks-url]: https://github.com/the-turing-index/api/network/members
[stars-shield]: https://img.shields.io/github/stars/the-turing-index/api.svg?style=flat-square
[stars-url]: https://github.com/the-turing-index/api/stargazers
[issues-shield]: https://img.shields.io/github/issues/the-turing-index/api.svg?style=flat-square
[issues-url]: https://github.com/the-turing-index/api/issues
[license-shield]: https://img.shields.io/github/license/the-turing-index/api.svg?style=flat-square
[license-url]: https://github.com/the-turing-index/api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[product-screenshot]: images/screenshot.png
