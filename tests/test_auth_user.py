
from routers.auth import get_password_hash, pwd_context


def test_get_password_hash():
    psw = get_password_hash('fulano123')
    assert pwd_context.verify('fulano123', psw)
