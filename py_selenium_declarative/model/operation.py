class Operation:
    name: str = ""
    xpath: str = ""
    action: str = ""
    value: str = ""
    iFrameSelector: str = ""
    isInIFrame: bool = None
    verify: bool = None

    def __init__(
        self,
        name="",
        xpath=None,
        action=None,
        value=None,
        iFrameSelector=None,
        isInIFrame=False,
        verify=False,
    ) -> None:
        self.name = name
        self.xpath = xpath
        self.action = action
        self.value = value
        self.iFrameSelector = iFrameSelector
        self.isInIFrame = isInIFrame
        self.verify = verify

    def __str__(self) -> str:
        return str(
            {
                "name": self.name,
                "xpath": self.xpath,
                "action": self.action,
                "value": self.value,
                "iFrameSelector": self.iFrameSelector,
                "isInIFrame": self.isInIFrame,
            }
        )
