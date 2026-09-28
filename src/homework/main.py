import hashlib


#  ФИО.
STUDENT_NAME = "Казаков Алексей Алексеевич"


def calculate_hashes(text: str) -> tuple[str, str]:
    """Вернуть MD5 и SHA-256 от одних и тех же UTF-8 байтов."""
    data = text.encode("utf-8")
    md5_hash = hashlib.md5(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()
    return md5_hash, sha256_hash


def make_report(name: str) -> str:
    values = [
        42,                         # int
        3.14,                       # float
        True,                       # bool
        "Python",                   # str
        [1, 2, 3],                  # list
        (1, 2, 3),                  # tuple
        {1, 2, 3},                  # set
        {"language": "Python"},     # dict
    ]

    lines = [f"ФИО: {name}"]
    for value in values:
        lines.append(f"{value!r} {type(value)}")

    return "\n".join(lines)


def main() -> None:
    report = make_report(STUDENT_NAME)
    md5_hash, sha256_hash = calculate_hashes(report)

    print(report)
    print(f"\nMD5: {md5_hash}")
    print(f"SHA-256: {sha256_hash}")


if __name__ == "__main__":
    main()
