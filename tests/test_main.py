from homework.main import calculate_hashes


def test_calculate_hashes_for_abc():
    md5_hash, sha256_hash = calculate_hashes("abc")

    assert md5_hash == "900150983cd24fb0d6963f7d28e17f72"
    assert sha256_hash == (
        "ba7816bf8f01cfea414140de5dae2223"
        "b00361a396177a9cb410ff61f20015ad"
    )
