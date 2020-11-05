# The Turing Index Flask API [![Build Status](https://travis-ci.com/the-turing-index/flask-api.svg?branch=main)](https://travis-ci.com/the-turing-index/flask-api)

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
- Activate a virtual environment `python -m venv ./venv && source bench/bin/activate`
- Install the dependencies `pip install -r requirements.txt`
- Start the server: `gunicorn app:app`
- The API will run at `localhost:8000`

When you are done
- Shut down the server `ctrl+C`
- Deactivate your virtual environment `deactivate`

<!-- USAGE EXAMPLES -->
## Usage

### GET 'api/v1/calendars'

#### [Click to see it live](https://fast-depths-29900.herokuapp.com/api/v1/calendars)


### GET 'api/v1/demo'

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
