class Course:
    """Moels the iea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prere: str) -> bool:
        """Check whether the course is desirable."""
        if prere in self.prerequisites and self.level > 400:
            return True
        return False


def find_courses(input: list[Course], input1: str) -> list[str]:
    """Return a list of names of desirable courses."""
    list_r: list[str] = []
    for elem in input:
        if input1 in elem.prerequisites and elem.level > 400:
            list_r.append(elem.name)
    return list_r