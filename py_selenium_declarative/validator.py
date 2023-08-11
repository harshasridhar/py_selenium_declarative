from json import loads
from logging import getLogger

from jsonschema import validate
from pkg_resources import resource_string

from py_selenium_declarative.constants import Constants
from py_selenium_declarative.model.operation import Operation
from py_selenium_declarative.model.suite import Suite

logger = getLogger(__name__)


class Validator:
    @staticmethod
    def validate_with_json_schema(instance: dict) -> None:
        schema = loads(resource_string("py_selenium_declarative", "files/suite.json"))
        validate(instance, schema)

    @staticmethod
    def validate_suite(instance: Suite) -> None:
        for index, operation in enumerate(instance.operations):
            try:
                Validator.validate_operation_object(operation)
            except Exception as e:
                raise Exception("Operation[{}] invalid: {}".format(index + 1, e))

    @staticmethod
    def validate_operation_object(instance: Operation) -> None:
        Validator.__validate_by_action(instance)

    @staticmethod
    def __validate_by_action(instance: Operation) -> None:
        if instance.action is None or instance.action == "":
            raise Exception("Action missing")
        if instance.action not in Constants.AVAILABLE_ACTIONS:
            raise Exception("Invalid action: " + instance.action)
        if instance.action in ["get", "sleep"]:
            Validator.__validate_value(instance.value)
        elif instance.action == "click":
            Validator.__validate_xpath(instance.xpath)
        elif instance.action in ["text", "select"]:
            Validator.__validate_xpath(instance.xpath)
            Validator.__validate_value(instance.value)

    @staticmethod
    def __validate_xpath(xpath: [str, None]) -> None:
        if not xpath:
            raise Exception("XPATH missing")
        if not xpath.startswith("//"):
            raise Exception("Invalid XPATH")

    @staticmethod
    def __validate_value(value: [str, None]) -> None:
        if not value:
            raise Exception("Value missing")
