from typing import List

from py_selenium_declarative.model.operation import Operation


class Suite:
    name: str = ''
    operations: List[Operation] = []

    def __init__(self, operations):
        self.operations = []
        for operation in operations:
            self.operations.append(Operation(**operation))
