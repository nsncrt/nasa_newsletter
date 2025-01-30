# NASA Newsletter

This project sends a daily email with NASA's Astronomy Picture of the Day (APOD) to a list of recipients. The email includes the image, its title, description, and other metadata.

## Project Structure

- `nasa/`
  - `servermail.py`: Handles the email server connection and sending emails.
  - `nasafile.py`: Fetches and processes data from the NASA API.
  - `emailwriting.py`: Composes the email content.
- `data/`
  - `mailing_list.example.csv`: Example CSV file for the mailing list.
- `main.py`: Main script to run the project.
- `config.json`: Configuration file for API keys and SMTP server details.

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
    - Create a `config.json` file in the root directory with the following structure:
      ```json
      {
        "api": {
          "url": "https://api.nasa.gov/planetary/apod",
          "key": "YOUR_NASA_API_KEY"
        },
        "smtp": {
          "server": "your_smtp_server",
          "port": 465
        },
        "sender": {
          "email": "your_email@example.com",
          "pwd": "your_email_password"
        }
      }
      ```

4. **Prepare the mailing list:**
    - Create a `data/mailing_list.csv` file with the following structure:
      ```csv
      name,email
      John Doe,johndoe@example.com
      Jane Smith,janesmith@example.com
      ```

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
