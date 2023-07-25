import logging
from json import loads
from typing import Optional
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from typer import Typer, echo, Exit, Option

from py_selenium_declarative import __app_name__, __version__
from py_selenium_declarative.model.suite import Suite
from py_selenium_declarative.runner import Runner

logging.basicConfig(level=logging.INFO)
logging.StreamHandler()

app = Typer()


@app.command()
def run(
        filename: Path = Option(
            'suite.json',
            '--filename',
            '-f',
            help='File to run',
            exists=True,
            readable=True,
            prompt='Filename'
        )
) -> None:
    data = loads(filename.read_text())
    suite = Suite(**data)
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    runner = Runner(driver)
    runner.run(suite)


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
