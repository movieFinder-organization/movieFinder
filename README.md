# Movie Finder Web App 🎬

Welcome to the Movie Finder web app! This application helps you find a random movie based on your preferences (like genre and year) and gives you detailed information about it. Let’s break down how everything works step by step.

# Table of Contents
[What Does This App Do?](##What-Does-This-App-Do?-🤔)

[How Does It Work?](##How-Does-It-Work?-🛠️)

[Project Structure](##Project-Structure-📂)

[How to Set Up the App](##How-to-Set-Up-the-App-🚀)

[How to Run the App](##How-to-Run-the-App-▶️)

[How to Use the App](##How-to-Use-the-App-🖱️)

[How the Code Works](##How-the-Code-Works-💻)

[Docker and CircleCI](##Docker-and-CircleCI-🐳)

[FAQs](##FAQs-❓)


## What Does This App Do? 🤔

Imagine you’re bored and want to watch a movie, but you don’t know what to watch. This app helps you:

1. Find a random movie based on your favorite genre and year.

2. Get detailed information about the movie, like its plot, rating, and release year.

## How Does It Work? 🛠️

The app uses two main APIs (Application Programming Interfaces) to do its magic:

1. TMDB API: This API helps us find a random movie based on your preferences (like genre and year).

2. OMDB API: This API gives us detailed information about the movie, like its plot and rating.

Here’s how the app works step by step:

1. You open the app in your browser.

2. You type in your favorite genre (e.g., "Action") and year (e.g., "2020").

3. The app sends your preferences to the TMDB API to find a random movie.

4. Once the movie is found, the app sends the movie’s title to the OMDB API to get more details.

5. The app shows you the movie’s details on the screen.

## Project Structure 📂

Here’s what the project folder looks like:

```bash
movie-finder/
├── app/                  # Contains the main app code
│   ├── __init__.py       # Initializes the Flask app
│   ├── routes.py         # Handles the website routes (like the homepage)
│   ├── templates/        # Contains HTML files
│   │   └── index.html    # The main webpage
│   └── static/           # Contains static files like CSS
│       └── style.css     # Styles the webpage
├── scripts/              # Contains helper scripts
│   └── fetch_movie.py    # Fetches movie data from APIs
├── requirements.txt      # Lists Python dependencies
├── Dockerfile            # Instructions to build the Docker container
├── .circleci/            # Contains CircleCI configuration
│   └── config.yml        # Configures the CI/CD pipeline
└── README.md             # This file!
```

## How to Set Up the App 🚀

### Step 1: Install Python

Make sure you have Python installed. You can download it from [python.org](python.org).

### Step 2: Get API Keys

1. Sign up for a free account at [TMDB](https://www.themoviedb.org/) and get your API key.

2. Sign up for a free account at [OMDB](http://www.omdbapi.com/) and get your API key.

### Step 3: Set Up the Project

1. Download or clone this project to your computer.

2. Open the project folder in a code editor (like VS Code).

### Step 4: Install Dependencies

1. Open a terminal in the project folder.

2. Run the following command to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 5: Add API Keys

1. Create a file named .env in the project folder.

2. Add your API keys to the .env file like this:
```bash
TMDB_API_KEY=your_tmdb_api_key
OMDB_API_KEY=your_omdb_api_key
```

## How to Run the App ▶️
### Option 1: Run Locally
1. Open a terminal in the project folder.

2. Run the following command:
```bash
flask run
```
3. Open your browser and go to http://127.0.0.1:5000.

### Option 2: Run with Docker
1. Build the Docker image:
```bash
docker build -t movie-finder .
```
2. Run the Docker container:
```bash
docker run -p 5000:5000 movie-finder
```
3. Open your browser and go to http://127.0.0.1:5000.

## How to Use the App 🖱️
1. Open the app in your browser.

2. Enter your favorite genre (e.g., "Action") and year (e.g., "2020").

3. Click the "Find Movie" button.

4. Wait a few seconds, and the app will show you a random movie with its details.

### Open the app in your browser.

Enter your favorite genre (e.g., "Action") and year (e.g., "2020").

Click the "Find Movie" button.

Wait a few seconds, and the app will show you a random movie with its details.

## How the Code Works 💻
### 1. app/routes.py
This file handles the website’s routes (like the homepage). When you click the "Find Movie" button, it:

1. Gets your input (genre and year).

2. Calls the fetch_random_movie function to find a random movie.

3. Calls the fetch_movie_details function to get more details about the movie.

4. Displays the movie details on the webpage.

### scripts/fetch_movie.py
This file contains the functions that talk to the TMDB and OMDB APIs:

1. fetch_random_movie: Finds a random movie based on your preferences.

2. fetch_movie_details: Gets detailed information about the movie.

### app/templates/index.html
This is the webpage you see in your browser. It has:

1. A form where you type your preferences.

2. A section to display the movie details.

### app/static/style.css
This file makes the webpage look nice by adding colors, spacing, and other styles.

## Docker and CircleCI 🐳

### Docker
Docker is a tool that packages the app into a container so it can run anywhere. The Dockerfile contains instructions to build the container.

### CircleCI
CircleCI is a tool that automatically tests and deploys the app whenever you make changes to the code. The .circleci/config.yml file tells CircleCI what to do.

## FAQs ❓

### 1. What if I don’t have an API key?
You need API keys from TMDB and OMDB to use this app. Sign up for free accounts on their websites to get your keys.

### 2. Why is the app not working?
Make sure:

1. You added your API keys to the .env file.

2. You installed all the dependencies using pip install -r requirements.txt.

3. The Flask server is running (flask run).

### 3. Can I change the app’s design?

Yes! You can edit the style.css file to change how the app looks.

## Illustrations 🖼️

### 1. How the App Works

```bash
User Input (Genre, Year) → TMDB API → Random Movie → OMDB API → Movie Details → Display on Webpage
```
