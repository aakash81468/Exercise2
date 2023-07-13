import requests
import logging
import schedule
import time
import random
import smtplib

api_url: str = "https://type.fit/api/quotes"

logging.basicConfig(
    level=logging.INFO,
    filename="./Assessment/main.log",
    filemode="w",
    format="%(asctime)s %(levelname)s: %(message)s",
)


def send_email(message: str):
    """
    Sends an email to the specified person about critical failures in the program
    """
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "aakashsoni9931@gmail.com"
        sender_password = "___________"
        receiver_email = "test@gmail.com"

        with smtplib.SMTP(smtp_server, smtp_port) as session:
            session.starttls()
            session.login(sender_email, sender_password)
            session.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        logging.critical(f"Error sending mail: {e}")


def display_wise_thoughts() -> None:
    """
    Displays random quotes from various perspectives of the world.
    """
    try:
        response = requests.get(api_url).json()
        random_index = random.randint(0, len(response))

        quote = f'{response[random_index]["text"]}\n by - {response[random_index]["author"]}'
        print(quote)
        logging.info(quote)
    except Exception as e:
        logging.critical(e)
        send_email(str(e))


schedule.every(1).seconds.do(display_wise_thoughts)

if __name__ == "__main__":
    counter: int = 0
    while True:
        schedule.run_pending()
        time.sleep(1)
        counter += 1
        print(counter)
        if counter == 10:
            break
