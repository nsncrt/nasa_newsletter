# NASA Newsletter 🪐 📷

This project sends a daily email with NASA's Astronomy Picture of the Day (APOD) to a list of recipients. The email includes the image, its title, description, and other metadata.

## Project Structure

- `nasa/`
  - `servermail.py`: Handles the email server connection and sending emails.
  - `nasafile.py`: Fetches and processes data from the NASA API.
  - `emailwriting.py`: Composes the email content.
- `data/`
  - `mailing_list.example.csv`: Example CSV file for the mailing list.
- `main.py`: Main script to run the project.
- `config.example.json`: Configuration file for API keys and SMTP server details.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd nasa_newsletter
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure the project:**
    - Create a `config.json` file in the root directory with the given structure
    - Create a `data/mailing_list.csv` file with the given structure


## Usage

1. **Run the main script:**
    ```sh
    python main.py
    ```

2. The script will:
    - Fetch the APOD data from NASA's API.
    - Compose an email with the image and its metadata.
    - Send the email to each recipient in the mailing list.

## Notes

- Ensure that the `img/` directory exists in the root folder if you want to save images locally.
- The `config.json` file and `mailing_list.csv` file should be properly configured before running the script.
- Configure a **Cron Job** to deploy the script and ensure daily newsletter.

## Links
- [NASA API](https://api.nasa.gov/)
- [NASA Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html)