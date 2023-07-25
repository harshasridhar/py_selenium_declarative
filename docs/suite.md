# Suite
A suite has a list of [operations](./operation.md).
## Format
Suite should be a json file in the format:
```json
{
  "operations": [
    {
      "xpath": "<xpath of the element>",
      "value": "<value to be selected or set>",
      "action": "<action on selected element>",
      "isInIFrame": false,
      "iFrameSelector": "<css selector for iframe>"
    },
  ]
}
```