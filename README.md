WhatsApp Chat Analyzer(A Python Project)

This Streamlit application allows you to analyze your WhatsApp chat data and gain insights into your conversations.

Features:

* Upload a WhatsApp chat export file.
* View a summary of chat statistics for a selected user or the entire group.
* Analyze message activity over time (daily, monthly, and weekly).
* Identify the most active days and months for a user.
* Generate a word cloud to visualize frequently used words.
* Explore the most common words used in chats.
* Analyze emoji usage within conversations.


Requirements:

* Python 3.x
* Streamlit
* pandas
* matplotlib
* seaborn
* emoji
* Other dependencies mentioned in helper.py and preprocessor.py (assuming these files contain helper functions and the pre-processing logic)
Instructions:

Clone this repository or download the project files.

Install the required libraries using pip install -r requirements.txt (assuming you have a requirements.txt file listing the dependencies).
Place your WhatsApp chat export file in the same directory as this README file.
Run the application using streamlit run app.py.


Code Structure:

* app.py: This file contains the main application logic using Streamlit components.
* preprocessor.py: This file defines functions for pre-processing the WhatsApp chat data.
* helper.py: This file contains helper functions used for various visualizations and analysis tasks.

Note: Ensure you have replaced helper.py and preprocessor.py with the actual file names containing your helper functions and pre-processing logic.
This README provides a general overview. Refer to the code for detailed implementation.
