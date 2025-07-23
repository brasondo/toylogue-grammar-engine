<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/brasondo/toylogue-grammar-engine">
    <img src="images/logo.webp" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Toylogue</h3>

  <p align="center">
    A modular, constraint-driven grammar engine for expressive toy dialogue.
    <br />
    <a href="https://github.com/brasondo/toylogue-grammar-engine"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/brasondo/toylogue-grammar-engine">View Demo</a>
    &middot;
    <a href="https://github.com/brasondo/toylogue-grammar-engine/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/brasondo/toylogue-grammar-engine/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Toylogue][product-screenshot]](https://github.com/brasondo/toylogue-grammar-engine)

Toylogue is a modular, grammar-driven NLP engine for generating expressive, role-specific dialogue for toys, characters, and games.  
It combines structured grammar (YAML) with syntactic introspection (spaCy), logical role constraints (Prolog), CFG modeling (NLTK), and optional LLM surface realization (e.g. Ollama).  
Designed to demonstrate linguistic engineering skills for narrative design, Toylogue outputs contextualized, emotionally resonant dialogue grounded in generative syntax.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python 3.12+
* YAML (grammar definition)
* JSON (grammar export)
* spaCy (syntactic analysis)
* NLTK (generative grammar modeling)
* Prolog (role-tone logic validation)
* Visual Studio Code
* Git
* Optional: Ollama or OpenAI (LLM surface realization)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.10+  
* pip (Python package manager)  
* [SWI-Prolog](https://www.swi-prolog.org/) (required for logic validation via Prolog)  
* [Ollama](https://ollama.com/) (optional, for LLM-based surface realization)

> Python dependencies such as `pyyaml`, `spacy`, `nltk`, and `pyswip` will be installed during setup.

### Installation

1. Clone the repo  
   ```sh
   
   git clone https://github.com/brasondo/toylogue-grammar-engine.git
   cd toylogue-grammar-engine/Toylogue
   ```

2. Set up virtual environment
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```


3. Run demo
    ```sh
    python demo.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The grammar engine loads rules from `phrases.yaml`, recursively generates symbolic phrases, and can optionally enhance them using an LLM for expressive surface realization.

### Role-Based Example with LLM Realization

```python
structure = recursive_generate(rules, symbol="S_VILLAIN")
print("Raw:", structure)

refined = surface_realize_with_ollama(structure, role="villain")
print("Ollama:", refined)
```
> Note: This example uses Ollama (`llama3`) running locally. You must install and start Ollama separately.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


Sample Output:
Raw: Hello — I'm Voidmaster and ruler of all you see.  
Ollama: (cackling) "Yes! I am VOIDMASTER, ruler of all you see and destroyer of hope!"


<!-- ROADMAP -->
## Roadmap

- [x] Modular grammar engine using YAML rules
- [x] Role- and tone-aware dialogue construction
- [x] Recursive grammar expansion via `S -> NP VP`-style rules
- [x] Prolog logic for tone-role constraint validation
- [x] NLTK CFG tree generation (generative syntax demo)
- [x] spaCy POS + dependency introspection
- [x] LLM-based expressive surface realization via Ollama
- [ ] Interactive authoring tool for character grammars
- [ ] Dialogue chaining with context persistence

See the [open issues](https://github.com/brasondo/toylogue-grammar-engine/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/brasondo/toylogue-grammar-engine/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brasondo/toylogue-grammar-engine" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brason Dobson - braleee@outlook.com 
🔗 [LinkedIn](https://linkedin.com/in/brasondo)


Project Link: [https://github.com/brasondo/toylogue-grammar-engine](https://github.com/brasondo/toylogue-grammar-engine)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Machler Labs](http://www.machlerlabs.com) — for inspiring this project’s focus on modular, expressive language systems for toys


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/brasondo/toylogue-grammar-engine.svg?style=for-the-badge
[contributors-url]: https://github.com/brasondo/toylogue-grammar-engine/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/brasondo/toylogue-grammar-engine.svg?style=for-the-badge
[forks-url]: https://github.com/brasondo/toylogue-grammar-engine/network/members
[stars-shield]: https://img.shields.io/github/stars/brasondo/toylogue-grammar-engine.svg?style=for-the-badge
[stars-url]: https://github.com/brasondo/toylogue-grammar-engine/stargazers
[issues-shield]: https://img.shields.io/github/issues/brasondo/toylogue-grammar-engine.svg?style=for-the-badge
[issues-url]: https://github.com/brasondo/toylogue-grammar-engine/issues
[license-shield]: https://img.shields.io/github/license/brasondo/toylogue-grammar-engine.svg?style=for-the-badge
[license-url]: https://github.com/brasondo/toylogue-grammar-engine/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/brasondo
[product-screenshot]: images/product-screenshot.png