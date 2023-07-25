class Operation:
    xpath: str = ''
    action: str = ''
    value: str = ''
    iFrameSelector: str = ''
    isInIFrame: bool = None

    def __init__(self, xpath=None, action=None, value=None, iFrameSelector=None, isInIFrame=False) -> None:
        self.xpath = xpath
        self.action = action
        self.value = value
        self.iFrameSelector = iFrameSelector
        self.isInIFrame = isInIFrame

    def __str__(self) -> str:
        return str({
            'xpath': self.xpath,
            'action': self.action,
            'value': self.value,
            'iFrameSelector': self.iFrameSelector,
            'isInIFrame': self.isInIFrame
        })
