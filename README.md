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

## Peg Solitaire Game: 

[Peg Solitaire Repo](https://github.com/sigreipel/PegSolitaireGame)

Peg Solitaire Game is a Python-based implementation of the puzzle Peg Solitaire. The program simulates a board created in the `square.txt`, rules are defined in `Rules.txt`, and manages game progression and victory conditions in `EliminationGame.py`.

<ins>Features:</ins>

- Board Initialization and Configuration
- Reads and constructs the board layout from a text file (square.txt).
- Supports flexible board shapes or layouts through text-based configuration.

Game Rule Enforcement

- Encapsulates movement logic in Rules.py, ensuring that only valid peg jumps (over adjacent pegs into empty spaces) are allowed.
- Validates game state transitions—jump moves update board state correctly and enforce game rules.

Gameplay Management

- EliminationGame.py handles turn progression, move application, and detects game-over conditions (i.e., only one peg remains or no valid moves remain).
- Provides core logic for peg elimination and board updates.

<ins>TechStack:</ins>

Language: Python

Input: square.txt for board layout

Modules:

- Rules.py – movement validation
- EliminationGame.py – game state management
- square.txt – defines initial board setup

<ins>Future Improvements</ins>

- Implement a graphical interface (e.g., using Tkinter or Pygame) to make interaction more intuitive and engaging.
- Add move history and undo/redo functionality to enable exploration and backtracking.
- Integrate automatic solving algorithms, such as depth-first search or heuristic-driven methods, to allow users to request hints or complete the puzzle automatically.
- Extend board flexibility, including triangular or European variants, enabling comparative analysis of board types.
- Incorporate performance optimizations, such as memoization of board states or pruning techniques, to enhance solver efficiency.

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
