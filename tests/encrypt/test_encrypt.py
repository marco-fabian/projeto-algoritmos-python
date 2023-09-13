from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, "key")
    with pytest.raises(TypeError):
        encrypt_message('humm', 'humm')
    assert encrypt_message("hello", 6) == "olleh"
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("hello", 4) == "o_lleh"
