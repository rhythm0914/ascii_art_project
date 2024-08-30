# ASCII Art Flask Application

This is a simple web application built with Flask that uses `pyfiglet` to generate and display ASCII art. The application serves a webpage that renders ASCII art in a web browser.

## Project Structure


- **`app.py`**: The main Flask application script. It generates ASCII art using `pyfiglet` and serves it through a web page.
- **`templates/index.html`**: The HTML template that displays the ASCII art in a web browser.
- **`README.md`**: This file, providing an overview and instructions for the project.

## Features

- Generates ASCII art using `pyfiglet`.
- Serves the ASCII art on a web page using Flask.
- Uses basic HTML and CSS to render and style the ASCII art.

## Prerequisites

Before running the application, you need to have Python installed on your machine. You also need to install the required Python packages.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/ascii_art_project.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd ascii_art_project
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the required packages:**

    ```bash
    pip install Flask pyfiglet
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://localhost:5000
    ```

    You should see the ASCII art rendered on the web page.

## How It Works

- **`app.py`**:
  - Uses `pyfiglet` to generate ASCII art from the text "RYAN JOSEPH".
  - Passes the generated ASCII art to the `index.html` template.
  - The application runs a Flask server that serves the HTML page.

- **`index.html`**:
  - Uses the `<pre>` tag to preserve the formatting of the ASCII art.
  - Styles the ASCII art with CSS to ensure proper display in the browser.

## Contributing

If you want to contribute to this project, please fork the repository and make a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- `pyfiglet`: A Python library used to generate ASCII art.
- Flask: A lightweight WSGI web application framework in Python.

