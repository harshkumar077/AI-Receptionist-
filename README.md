# AI Receptionist for a Doctor's Office:  This project is an AI-based receptionist built using Flask, designed to assist a doctor's office in handling emergency and non-emergency cases via a text-based interface. The application guides the user through a series of questions and provides immediate steps for emergencies while ensuring the doctor is notified.
## Features  - 
**Emergency Handling**: Guides the user to provide details about an emergency and responds with immediate steps to take. 
**Message Handling**: Allows users to leave a message for the doctor. 
**Simulated Delay for Emergency Response**: Implements a delay to simulate querying a vector database (like Qdrant) for emergency instructions. 
**Location-Based ETA**: Provides an estimated time of arrival for the doctor based on the user's location. 
**Dynamic User Interaction**: Continuously engages the user by asking follow-up questions.
## Technologies Used:  
**Flask**: A lightweight WSGI web application framework in Python.
**HTML/CSS**: For rendering basic forms and interactions on the front end. 
**Python**: The main programming language used. 
**Threading**: To simulate a delay in database response without blocking the main thread.
