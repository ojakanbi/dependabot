import json

from lambda_function import handler


def test_handler_returns_200():
    response = handler({}, None)
    assert response["statusCode"] == 200


def test_handler_returns_message():
    response = handler({}, None)
    body = json.loads(response["body"])
    assert body["message"] == "hello from sample-lambda"
