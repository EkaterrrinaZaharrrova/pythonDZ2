from unittest.mock import patch

from src.external_api import get_convert_currency


@patch("requests.get")
def test_get_convert_currency(mock_get):

    mock_get.return_value.json.return_value = {"result": 1234}
    assert get_convert_currency(mock_get, "o") == 1234
