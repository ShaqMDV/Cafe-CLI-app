<a id="projecttop"></a>
A CLI application for managing the logs and tracking orders for a pop-up cafe

# Table of Contents

- [About the Project](#about-the-project)
    - [Built With](#built-with)
- [Getting Started](#getting-started)
    - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

# About the project

This project is a Command Line Interface (CLI) application created to assist a recently launched pop-up cafe. This involved:
    
    - A logical, clear and simple UI
    - Mainting a collection of products, couriers and orders
    - The functionality to create new products, couriers and orders
    - Being able to update the status of an order i.e: preparing, shipped, delivered
    - Persistting the data on exit i.e. save any new data to a file or database
    - Loading said data on start up of app
    - Finally, providi testing and ensuring the app works well

## Built with

- Python 3.13.0
- Docker

# Getting started

## Installation

How to get this project running locally.

1. Clone the repository:
```powershell
git clone https://github.com/ShaqMDV/Cafe-CLI-app.git
cd Cafe-CLI-app
```
2. Change git remote url to avoid accidental pushes to the original project
```powershell
git remote set-url origin github_username/repository_name
git remote -v # To confirm your changes
```

3. Build and run the Docker container:

```powershell
docker build -t cafe-cli-app .
docker run -it cafe-cli-app
```
# Usage
In your terminal, run the following line to start the app:

```powershell
>python main_menu.py
```
It should look like this if run correctly:
![Main Menu](./C:\Users\Me\OneDrive\Documents\Data-Engineering-Generation-UK-Course\DE-NAT3-MINI-SHAQ\MyRepository\ShaqM_Mini_Project\WEEK_4\Data\main_menu.jpeg)

# Contributing
Contributions are welcome! Please fork the repo and issue a pull request.

# License

# Contact

Shaquille Melbourne - shaquillemelbourne@gmail.com
Project link - https://github.com/generation-de-nat3/ShaqM_Mini_Project

<p align="right">(<a href="#projecttop">back to top</a>)</p>
