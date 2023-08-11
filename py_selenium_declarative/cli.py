import logging
from json import loads
from pathlib import Path
from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from typer import Typer, echo, Exit, Option, style, colors

from py_selenium_declarative import __app_name__, __version__
from py_selenium_declarative.model.suite import Suite
from py_selenium_declarative.runner import Runner
from py_selenium_declarative.validator import Validator

logging.basicConfig(level=logging.INFO)
logging.StreamHandler()

app = Typer()


@app.command()
def run(
    filename: Path = Option(
        "suite.json",
        "--filename",
        "-f",
        help="File to run",
        exists=True,
        readable=True,
        prompt="Filename",
    ),
    timeout: int = Option(10, "--timeout", "-t", help="timeout(in secs) for wait"),
) -> None:
    data = loads(filename.read_text())
    try:
        Validator.validate_with_json_schema(data)
        suite = Suite(**data)
        Validator.validate_suite(suite)
        service = Service()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

        runner = Runner(driver, timeout)
        echo(style("Starting test suite run", fg=colors.GREEN, bold=True))
        runner.run(suite)
        echo(style("Completed test suite run", fg=colors.GREEN, bold=True))
    except Exception as e:
        echo(style(str(e), fg=colors.RED))


def _version_callback(value: bool) -> None:
    if value:
        echo(f"{__app_name__} v{__version__}")
        raise Exit()


@app.callback()
def main(
    version: Optional[bool] = Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
