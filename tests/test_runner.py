from time import time
from unittest.mock import MagicMock

import pytest

from py_selenium_declarative.model.operation import Operation
from py_selenium_declarative.model.suite import Suite
from py_selenium_declarative.runner import Runner


def test_runner_for_get():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)

    operation = Operation(value="www.google.com", action="get")
    suite = Suite(operations=[{"value": "www.google.com", "action": "get"}])
    runner.driver_utils = MagicMock()
    runner.run(suite)

    runner.driver_utils.get_page.assert_called_with(operation.value)


def test_runner_for_click():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()
    xpath = "//somepath"
    suite = Suite(operations=[{"xpath": xpath, "action": "click"}])
    runner.run(suite)

    runner.driver_utils.wait_for_element_then_click.assert_called_with(xpath)


def test_runner_for_set_text():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()
    xpath = "//somepath"
    value = "settext"
    suite = Suite(operations=[{"xpath": xpath, "value": value, "action": "text"}])

    runner.run(suite)

    runner.driver_utils.wait_for_element_then_set_text_and_click_enter.assert_called_with(
        xpath, value, False, None
    )


def test_runner_for_verify_text():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()
    xpath = "//somepath"
    value = "settext"

    suite = Suite(
        operations=[{"xpath": xpath, "value": value, "action": "text", "verify": True}]
    )
    runner.driver_utils.wait_until_element_is_visible.return_value = None
    from types import SimpleNamespace

    runner.driver_utils.find_element_by_xpath.return_value = SimpleNamespace(text=value)

    runner.run(suite)

    runner.driver_utils.wait_until_element_is_visible.assert_called_with(xpath)
    runner.driver_utils.find_element_by_xpath.assert_called_with(xpath)


def test_runner_for_verify_text_invalid_case():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()
    xpath = "//somepath"
    value = "settext"

    suite = Suite(
        operations=[{"xpath": xpath, "value": value, "action": "text", "verify": True}]
    )
    runner.driver_utils.wait_until_element_is_visible.return_value = None
    from types import SimpleNamespace

    runner.driver_utils.find_element_by_xpath.return_value = SimpleNamespace(
        text=value + "invalid"
    )

    with pytest.raises(Exception) as context:
        runner.run(suite)

    runner.driver_utils.wait_until_element_is_visible.assert_called_with(xpath)
    runner.driver_utils.find_element_by_xpath.assert_called_with(xpath)
    assert context.value.args[0] == "Expected: [settext] Found [settextinvalid] "


def test_runner_for_select():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()
    runner.driver_utils.wait_for_element_then_select_value.return_value = None

    runner.run(
        Suite(operations=[{"action": "select", "value": "val", "xpath": "//somepath"}])
    )

    runner.driver_utils.wait_for_element_then_select_value.assert_called_with(
        "//somepath", "val"
    )


def test_runner_for_take_screenshot():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()
    runner.driver_utils.save_screenshot.return_value = None
    suite = Suite(operations=[{"action": "screenshot", "name": "SS"}])

    runner.run(suite)
    runner.driver_utils.save_screenshot.assert_called_with("screenshot_SS.png")


def test_runner_for_sleep():
    mock1 = MagicMock()
    runner = Runner(mock1, 10)
    runner.driver_utils = MagicMock()

    suite = Suite(operations=[{"action": "sleep", "value": "1"}])
    start = time()
    runner.run(suite)
    end = time()
    assert int(end - start) >= 1
