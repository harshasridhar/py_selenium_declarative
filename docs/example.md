# Examples

## 1. Run a Google search for 'Hello World'

### Prepare the test suite json file
This file can be downloaded/viewed from examples section in the repository.
```json
{
  "operations": [
    {
      "action": "get",
      "value": "https://www.google.com"
    },
    {
      "xpath": "//*[@id='APjFqb']",
      "value": "Hello World",
      "action": "text"
    },
    {
      "action": "sleep",
      "value": "10"
    }
  ]
}
```

### Run the test suite
```shell
python -m py_selenium_declarative run -f example.json
```
