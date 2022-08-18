<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[contributors-shield]: https://img.shields.io/github/contributors/kiran-karandikar/env-file-for-github-actions?style=for-the-badge

[contributors-url]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Kiran-Karandikar/env-file-for-github-actions?style=for-the-badge

[forks-url]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/network

[stars-shield]: https://img.shields.io/github/stars/Kiran-Karandikar/env-file-for-github-actions?style=for-the-badge

[stars-url]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/stargazers

[issues-shield]: https://img.shields.io/github/issues/Kiran-Karandikar/env-file-for-github-actions?style=for-the-badge

[issues-url]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/issues

[license-shield]: https://img.shields.io/github/license/Kiran-Karandikar/env-file-for-github-actions?style=for-the-badge

[license-url]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/kiran-karandikar

[ci-shield]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/actions/workflows/ci.yml/badge.svg

[ci-url]: https://github.com/Kiran-Karandikar/env-file-for-github-actions/actions/workflows/ci.yml

[doc-shield]: https://readthedocs.org/projects/env-file-for-github-actions/badge/?version=latest

[doc-url]: https://env-file-for-github-actions.readthedocs.io/en/latest/?badge=latest

---------

[![CI][ci-shield]][ci-url]
[![Documentation Status][doc-shield]][doc-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">env-file-for-github-actions</h3>
  <p align="center">
    Update Github Action Secrets from local <code>.env</code> file
    <br />
    <a href="https://env-file-for-github-actions.readthedocs.io/en/latest/?"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kiran-karandikar/env-file-for-github-actions">View Demo</a>
    ·
    <a href="https://github.com/kiran-karandikar/env-file-for-github-actions/issues">Report Bug</a>
    ·
    <a href="https://github.com/kiran-karandikar/env-file-for-github-actions/issues">Request Feature</a>
  </p>
</div>

<!-- BADGES.MD Finish -->



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is a sample project to update the github action secrets from local `.env` file.
When using github actions, many times the jobs in `ci` needs access to environment variables.
Using GitHub Api and pre-commit hook, the github action secrets will be updated on every `push` action from local `.env` file/s.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Github API](https://github.com/mailhog/MailHog).
- [AIOHTTP](https://docs.aiohttp.org/en/latest/index.html#aiohttp-installation) Asynchronous HTTP Client/Server for asyncio and Python.
- [PyNaCl](https://pynacl.readthedocs.io/en/latest/) for public key encryption.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Optional:
    - [Dokcer](https://www.docker.com/get-started/)
      and [Docker dependencies](https://docs.docker.com/desktop/install/windows-install/)
      installed if using dokcer based setup.
    - Use [ruby installer](https://rubyinstaller.org/) if
      using [pre-commit hook](https://pre-commit.com/) : [Search and Replace](https://github.com/mattlqx/pre-commit-search-and-replace)

### Installation

1. Clone the repository
   ```sh
    $ git clone https://github.com/kiran-karandikar/env-file-for-github-actions.git
   ```
2. For local development, see the following:
   - [Workflow](./base/docs/source/workflow.rst)

<!-- USAGE EXAMPLES -->

## Usage

- Add `GH_ACCESS_TOKEN`, `OWNER`, `Repository` in  details in `.envs\.local\.gh_credentials`
    - Refer to `envs-example` for creating `.env` files.
- Setup docker containers using:

  ```shell
  docker build .
  docker compose -f local.yml build
  docker compose -f local.yml up
  docker compose -f local.yml down
  ```

_For more examples, please refer to
the [Documentation](https://env-file-for-github-actions.readthedocs.io/en/latest/?)_ built using `Sphinx`

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->

## Roadmap

- [ ] Use bash script in to export variables in ``ci.yml``.

See the [open issues](https://github.com/kiran-karandikar/env-file-for-github-actions/issues) for a
full list of proposed features (and known issues).


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the `MIT License`. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

<!-- CONTACT -->

## Contact

- [Kiran Karandikar](mailto:hkarandikar@gmail.com)

Project
Link: [https://github.com/kiran-karandikar/env-file-for-github-actions](https://github.com/kiran-karandikar/env-file-for-github-actions)

<p align="right">(<a href="#top">back to top</a>)</p>
