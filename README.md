# Email Generator and Verifier

This project is an Email Generator and Verifier tool developed in Python. It allows for the automated generation and verification of email addresses, with the ability to use temporary emails and encrypt data if needed.

## Requirements

- Python 3.x
- Libraries: `requests`, `cryptography`, `tkinter`

## Project Structure

```
source/
│
├── config/
│   ├── settings.py
│
├── logs/
│   ├── app.log
│
├── styles/
│   ├── __init__.py
│   ├── main_window.py
│   ├── menu_style.py
│
├── tempmail/
│   ├── __init__.py
│   ├── tempmail.py
│
├── utils/
│   ├── __init__.py
│   ├── cryptografy/
│   │   ├── cryptography.py
│   │
│   ├── generate/
│   │   ├── gerador.py
│   │   ├── verificador.py
│   │
│   ├── utils.py
│
├── main.py
```

## How to Use

1. **Installing Dependencies**:
   Ensure that all the necessary libraries are installed by running the following command in the project's root directory:

   ```bash
   pip install -r requirements.txt
   ```

2. **Starting the Project**:

   To initiate the project, run the following command in the project's root directory:

   ```bash
   python main.py
   ```

   This will open a command-line interface where you can choose between the Graphical User Interface (GUI) or advanced email generation and verification.

3. **Graphical User Interface (GUI)**:

   - Choose the "Start the graphical interface (GUI)" option from the menu.
   - The graphical interface will allow you to generate and display random emails and passwords.
   - You can copy the generated passwords by clicking the "Copy" button and save them to a text file using the "Download Data" button.

4. **Advanced Email Generation and Verification**:

   - Choose the "Generate and verify emails (advanced option)" from the menu.
   - Follow the instructions to specify the number of emails to generate, whether to use temporary emails, and whether to encrypt the data.

## User Feedback

The project allows users to provide feedback on recommendations, contributing to continuous system improvement. Feedback is stored in a structured format in a database for future analysis.

## Final Thoughts

This project provides a solid and flexible foundation for developing high-quality recommendation systems. You can customize and expand the system by adding additional features and fine-tuning recommendation models as needed.

Enjoy email generation and verification with the Email Generator and Verifier!

## Notes: 

Ensure that the required data, such as CSV files and encryption models, are present in the appropriate folders before running the system. Additionally, make sure Python virtual environments (venv) are set up correctly to avoid dependency conflicts.

---