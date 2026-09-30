from unittest.mock import MagicMock

import app as app_module

def test_hello_returns_count(monkeypatch):
	fake_cache = MagicMock()
	fake_cache.incr.return_value = 5
	monkeypatch.setattr(app_module, "cache", fake_cache)

	client = app_module.app.test_client()
	response = client.get("/")

	assert response.status_code == 200
	assert b"visited 5 times" in response.data
	fake_cache.incr.assert_called_once_with("hits")

