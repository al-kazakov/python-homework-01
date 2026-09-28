import argparse
import getpass
import hashlib
import os
import smtplib
import ssl
from email.message import EmailMessage


STUDENT_NAME = "Казаков Алексей Алексеевич"


def calculate_hashes(text: str) -> tuple[str, str]:
    data = text.encode("utf-8")
    md5_hash = hashlib.md5(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()
    return md5_hash, sha256_hash


def make_report(name: str) -> str:
    values = [
        42,
        3.14,
        True,
        "Python",
        [1, 2, 3],
        (1, 2, 3),
        {1, 2, 3},
        {"language": "Python"},
    ]

    lines = [f"ФИО: {name}"]
    for value in values:
        lines.append(f"{value!r} {type(value)}")
    return "\n".join(lines)


def send_email(name: str, report: str, md5_hash: str, sha256_hash: str) -> None:
    required = ("SMTP_HOST", "SMTP_PORT", "SMTP_USER", "EMAIL_TO")
    missing = [key for key in required if not os.environ.get(key)]
    if missing:
        raise ValueError(
            "Не заданы переменные окружения: " + ", ".join(missing)
        )

    host = os.environ["SMTP_HOST"]
    port = int(os.environ["SMTP_PORT"])
    sender = os.environ["SMTP_USER"]
    recipient = os.environ["EMAIL_TO"]
    password = getpass.getpass("Пароль приложения для SMTP: ")

    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "Домашнее задание 1 — хеши отчёта"
    message.set_content(
        f"ФИО: {name}\n\n"
        f"Данные и их типы:\n{report}\n\n"
        f"MD5:\n{md5_hash}\n\n"
        f"SHA-256:\n{sha256_hash}\n"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context, timeout=20) as server:
        server.login(sender, password)
        server.send_message(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--send",
        action="store_true",
        help="Отправить письмо с хешами",
    )
    args = parser.parse_args()

    report = make_report(STUDENT_NAME)
    md5_hash, sha256_hash = calculate_hashes(report)

    print(report)
    print(f"\nMD5: {md5_hash}")
    print(f"SHA-256: {sha256_hash}")

    if args.send:
        send_email(STUDENT_NAME, report, md5_hash, sha256_hash)
        print("Письмо отправлено.")


if __name__ == "__main__":
    main()

