from __future__ import annotations
from typing import Optional, Dict


class Node:
    def __init__(self, data: Dict[str, str]):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __repr__(self) -> str:
        return f"DATA: {self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.start: Optional[Node] = None

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = ["START"]

        for node in self:
            nodes.append(node.data["name"])

        nodes.append("NIL")

        return "\n" + " --> ".join(nodes)

    def insert_at_end(self, element: Node) -> None:
        if self.start is None:
            self.start = element
            return

        current = self.start

        while current.next is not None:
            current = current.next

        current.next = element
        element.prev = current