import pytest
from jsonschema.exceptions import ValidationError

from py_selenium_declarative.validator import Validator
from py_selenium_declarative.model.suite import Suite


def test_validate_with_json_schema():
    instance = {"operations": []}
    Validator.validate_with_json_schema(instance)


@pytest.mark.parametrize(
    "operation, expected_message",
    [({"action": 1}, "1 is not of type 'null', 'string'")],
)
@pytest.mark.validator_tests
def test_validate_with_json_schema_with_error(operation, expected_message):
    instance = {"operations": [operation]}
    with pytest.raises(ValidationError) as context:
        Validator.validate_with_json_schema(instance)

    exception = context.value
    assert exception.message == expected_message


@pytest.mark.parametrize(
    "operations, expected_message",
    [
        ([{"value": "10"}], "Operation[1] invalid: Action missing"),
        ([{"action": "invalid"}], "Operation[1] invalid: Invalid action: invalid"),
        ([{"action": "get"}], "Operation[1] invalid: Value missing"),
        ([{"action": "click"}], "Operation[1] invalid: XPATH missing"),
        ([{"action": "text"}], "Operation[1] invalid: XPATH missing"),
        (
            [{"action": "text", "xpath": "//somepath"}],
            "Operation[1] invalid: Value missing",
        ),
        (
            [{"action": "text", "xpath": "somepath"}],
            "Operation[1] invalid: Invalid XPATH",
        ),
    ],
)
def test_validate_suite(operations, expected_message):
    suite = Suite(operations=operations)
    with pytest.raises(Exception) as context:
        Validator.validate_suite(suite)

    exception = context.value
    assert exception.args[0] == expected_message
