from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("jaxmuitoop", "2")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)

    assert encrypt_message("jaxmuitoop", 10) == "axmuitoopj"

    assert encrypt_message("jaxmuitoop", 3) == "xaj_muipoot"

    assert encrypt_message("jaxmuitoop", 4) == "mutoop_axji"
