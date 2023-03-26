from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("abcdef", -10) == "fedcba"
    assert encrypt_message("abcdef", 3) == "cba_fed"
    assert encrypt_message("abcdef", 4) == "fe_dcba"
    assert encrypt_message("cba", 1) == "c_ab"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("test", "test")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)
    