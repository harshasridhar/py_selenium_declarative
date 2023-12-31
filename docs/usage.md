# Usage
## Help
```shell
python -m py_selenium_declarative --help
```
OR
```shell
psd --help
```
OUTPUT:<br/>
```text
Usage: py_selenium_declarative [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  run
```
## Run
Run a test suite.
### Help
```shell
python -m py_selenium_declarative run --help
```
OR
```shell
psd run --help
```
OUTPUT:<br/>
```text
Usage: py_selenium_declarative run [OPTIONS]

Options:
  -f, --filename PATH  File to run  [default: suite.json]
  --help               Show this message and exit.
```

### With prompt
```shell
python -m py_selenium_declarative run
```
OR
```shell
psd run
```
OUTPUT:<br/>
A prompt as follows is shown where the file path needs to be entered
```text
Filename [suite.json]: 
```

### Without prompt
```shell
python -m py_selenium_declarative run -f suite.json
```
OR
```shell
psd run -f suite.json
```