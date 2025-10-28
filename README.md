🗺️ NTU Map Portal

A Python-based interactive campus navigation program built using folium. It allows students to find buildings on NTU Clifton campus, validate student identity, and generate a dynamic map with marked start and destination points.

📌 Features

Name and Student ID validation before map access

Auto-suggestion of building names for incorrect entries

Interactive map pop-up in the default browser

Displays two marked points with a connecting line

Stores validated users in an external text file

Works offline after installation

🧰 Tech Stack

Language: Python 3

Library: folium

Browser: Default system browser (via Python Standard Library webbrowser module)

🧭 How It Works

User enters Name and Student ID.

Name must not contain digits.

ID must start with N or T and contain 8 characters.

On successful validation, user enters:

Current location

Destination building

If both buildings are valid:

A map is generated and opened in the browser.

If input is incorrect:

Program suggests buildings or lists all names.

User can retry or exit.

🏛️ Buildings Covered

Includes major Clifton Campus buildings such as:

DH Lawrence

Clifton Library

John Clare Lecture Theatre

ISTEC

Erasmus Darwin
…and more (full list in NTU_map_portal.py).

🗂️ File Handling

A Student ID.txt file is created automatically.

Stores Name and Student ID of each user who passes validation.

🧪 Installation
# clone the repository
git clone https://github.com/<your-username>/NTU-Map-Portal.git
cd NTU-Map-Portal

# install dependencies
pip install folium

▶️ Usage
python NTU_map_portal.py


Follow on-screen prompts:

Enter your Name and Student ID

Enter current and destination building names

View generated map in your default browser.

🧭 Example
Enter your Name: LAVAN
Enter your student ID: N1234567
Hi LAVAN, you are eligible to access this site.
Where are you now? DH LAWRENCE
Where you wanted to go? ISTEC


👉 A map with two marked points opens automatically.

⚡ Future Improvements

Real-time location tracking

Actual route mapping

NTU database integration for authentication

GUI implementation

Multi-campus support

📝 Reference

Coordinates: [Nottingham Trent University Clifton Campus on Google Maps]

Building names: MazeMap NTU
