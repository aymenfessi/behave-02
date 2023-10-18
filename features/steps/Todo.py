class Todo:
    user_id: int
    id: int
    title: str
    completed: bool

    def __init__(self, user_id: int, id: int, title: str, completed: bool) -> None:
        self.user_id = user_id
        self.id = id
        self.title = title
        self.completed = completed