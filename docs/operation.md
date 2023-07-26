# Operation
An operation is a entity that does a single unit of a task. The task type is defined by <b>action</b>.
An operation is defined by the following fields:

- [Name](./operation.md#name)
- [XPath](./operation.md#xpath)
- [Value](./operation.md#value)
- [Action](./operation.md#action)
- [IsInIFrame](./operation.md#isiniframe)
- [IFrameSelector](./operation.md#iframeselector)

## Name
Field Name: `name`<br/>
This field is used to specify the operation name.

## XPath
Field Name: `xpath`<br/>
This field is used to specify the xpath of the element to interact with.

## Value
Field Name: `value` <br/>
This field is used to specify the value to select or set the text field with.

## Action
Field Name : `action`<br/>
Action can be of type:

- get: Go to the webpage
- click : Wait for the element to be visible and then click on it.
- select: Wait for the element to be visible and then select a value specified in the field `value`.
- text: Wait for the element to be visible, then set the value to the specified contents in the field `value` 
and then click enter.
- screenshot: Takes a screenshot of the current screen. (Filename is `screenshot_{operation_name}.png` if operation_name is not present the epoch is added)
- sleep: Sleep for specified(via `value`) amount of seconds


## IsInIFrame
Field Name: `isInIFrame`<br/>
A boolean flag which indicates if the element to interact is inside an iframe.<br/>
If the element is inside an iframe, we specify an iframe CSS Selector.

## IFrameSelector
Field Name: `iFrameSelector` <br/>
This field is used to specify the CSS selector to fetch the iframe inside which the element to interact is present. 