# Streamlit Merge App

This project is a Streamlit application designed to merge data from three different Excel files. It provides a user-friendly interface for uploading the files and displays the merged data.

## Project Structure

```
streamlit-merge-app
├── src
│   ├── app.py          # Entry point of the Streamlit application
│   └── utils
│       └── merge.py    # Contains functions for merging Excel data
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Requirements

To run this application, you need to install the following dependencies:

- Streamlit
- pandas
- openpyxl

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:

   ```
   cd streamlit-merge-app
   ```

2. Run the Streamlit application:

   ```
   streamlit run src/app.py
   ```

3. Open the provided local URL in your web browser to access the application.

## Usage

- Upload three Excel files using the interface.
- Click the "Merge" button to combine the data from the uploaded files.
- The merged data will be displayed on the screen.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.