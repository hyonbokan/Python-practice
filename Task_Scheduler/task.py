from typing import Callable, Any, Tuple

class Task:
    def __init__(
        self,
        name: str,
        priority: int,
        func: Callable[..., Any],
        args: Tuple[Any, ...] = (),
        retries: int = 0
    ):
        self.name = name
        self.priority = priority
        self.func = func
        self.args = args
        self.retries = retries
        
    def __lt__(self, other: "Task") -> bool:
        return self.priority < other.priority
    
    def run(self) -> Any:
        return self.func(*self.args)
    
    def __repr__(self) -> str:
        return f"<Task name:'{self.name}; Priority: {self.priority} Retries: {self.retries}"