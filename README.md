# Introduction:

Hello, my name is Svetlana. I am a college graduate from Drake University. 
I graduated with a major in Computer Science and a minor in Data Analytics and AI.

I am a computer science graduate seeking a full-time job opportunity in software development, data engineering, entry-level IT, or another related field that allows me to apply the skills and knowledge acquired through my college courses, experience, and background.

# My Projects:
## Studio Ghibli Movie Explorer: 

[Data Structures FP Repo](https://github.com/sigreipel/DataStructures-Final-Project)

_Studio Ghibli Movie Explorer_ is an interactive program designed to retrieve and display information about Studio Ghibli films. The JSON data is obtained from the [Studio Ghibli API](https://ghibliapi.vercel.app/#), parsed into python data structures, sorted the films alphabetically using the insertion sort algorithm, and presented through a GUI built with Tkinter.

<ins>Features:</ins>
  API Integration
  
  - Retrieves live movie data from the Studio Ghibli API.
  - Parses JSON into Python data structures (lists and dictionaries).
  
  Sorting Algorithm
  
  - Implements a custom insertion sort for ordering movies alphabetically by title.
  - Reinforces understanding of algorithm design and efficiency trade-offs.
  
  Graphical User Interface
  
  - Tkinter-based interface to display film details including title, director, release date, and description.
  - Provides structured and user-friendly movie browsing.
  
  Data Structures
  
  - Lists used for managing collections of movie objects.
  - Dictionaries used for storing individual movie attributes.
  
  <ins>TechStack:</ins>
  
  Language: Python
  
  Libraries: Tkinter, Requests (for API calls), JSON
  
  Algorithm: Insertion Sort
  
  <ins>Future Improvements</ins>
  
  - Replace with a more efficient algorithm (e.g., merge sort or quicksort) for scalability.
  - Add filtering or searching functionality by director, release year, or rating.
  - Expand the GUI with images, better layout, and improved interactivity.
  - Cache or locally store API results to improve performance and usability offline.
    
## Roman Numerals:

[Roman Numerals Repo](https://github.com/sigreipel/RomanNumerals)

A small project that helps demonstrate my Python skills. 
Takes in an input value and converts the value to either a Roman numeral or an integer.
I have added additional unit tests in another folder called `Tests`.

## Peg Elimination Game: 

[Peg Solitaire Repo](https://github.com/sigreipel/PegSolitaireGame)

A current personal project to simulate the Peg Solitaire game. It is also known as the Crackerbarrel Peg Game. 
All of the rules are implemented and the game works; however, the UI is not friendly, and my next step for this project.

## Game Recommendation Platform:

[Game Recommendation Platform Repo](https://github.com/sigreipel/GameAggregatorCapstone/tree/main)

Game Recommendation Platform is a Django-based web application that aggregates and recommends video game news, updates, and developer information. It allows users to personalize their experience by following or blocking specific games or developers. The platform also includes a custom authentication system and a structured database design.

<ins>__Features:__</ins>
  Custom Authentication System
    
  - Using Django's `AbstractUser` and email as a login field.
  - Personalized user features (Following/Blocking games or developers)
    
  Game & Developer Database
  
  - Populated custom `placeholder_db.py` for script testing and UI prototyping.
  - Stores structured data on users, games, and developers.
    
  Game News Aggregation
  
  - Fetches and organizes data from multiple sources.
  - Filtering and displays relevant information based on user preferences.
    
  Scalable Backend
  
  - Built with Django, allowing SQLite for development.
  - Designed with other databases and cloud implementation in mind (AWS)
    
<ins>__TechStack:__</ins>

  Backend: Django (Python)
  
  Database: SQLite
  
  Frontend: Django templates, HTML, CSS
  
  Cloud Deployment: AWS (future integration)
    
<ins>__Future Improvements__</ins>
  
  - Full integration of real-time news API feeds
  - Advancing recommendations using filtering or ML personalization.
  - Deployment with Docker, Lambda, and AWS
