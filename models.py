class Difficulty():
    EASY = 1
    MEDIUM = 2
    HARD = 3

    @staticmethod
    def from_str(s: str) -> int:
        if s == 'Easy':
            return Difficulty.EASY
        elif s == 'Medium':
            return Difficulty.MEDIUM
        elif s == 'Hard':
            return Difficulty.HARD
        else:
            raise ValueError(f'Invalid difficulty string: {s}')


class Company:
    def __init__(self, name: str, slug: str, frequency: int) -> None:
        self.name: str = name
        self.slug: str = slug
        self.frequency: int = frequency


class Problem:
    def __init__(self, id: int, title: str, slug: str, pattern: list[str], difficulty: int, is_premium: bool, companies: list[Company], status: int) -> None:
        self.id: int = id
        self.title: str = title
        self.slug: str = slug
        self.pattern: list[str] = pattern
        self.difficulty: int = difficulty
        self.is_premium: bool = is_premium
        self.companies: list[Company] = companies
        self.status: int = status


class ProblemSet:
    def __init__(self, lastUpdated: str, problems: dict[int, Problem]) -> None:
        self.lastUpdated: str = lastUpdated
        self.problems: dict[int, Problem] = problems

    @staticmethod
    def getEmptyProblemSet() -> 'ProblemSet':
        return ProblemSet("", {})

    def get_sorted_problems(self) -> list[Problem]:
        return sorted(self.problems.values(), key=lambda p: p.id)

    def get_statistic(self) -> 'Statistics':
        solved = {Difficulty.EASY: 0, Difficulty.MEDIUM: 0, Difficulty.HARD: 0}

        for problem in self.problems.values():
            if problem.status == 1:
                if problem.difficulty == 1:
                    solved[Difficulty.EASY] += 1
                elif problem.difficulty == 2:
                    solved[Difficulty.MEDIUM] += 1
                elif problem.difficulty == 3:
                    solved[Difficulty.HARD] += 1
        return Statistics(solved, len(self.problems))

class Statistics:
    def __init__(self, solved: dict[int, int], total: int) -> None:
        self.solved_easy: int = solved[Difficulty.EASY]
        self.solved_medium: int = solved[Difficulty.MEDIUM]
        self.solved_hard: int = solved[Difficulty.HARD]
        self.total: int = total

class ProblemUpdateRequest:
    def __init__(self, problem_id: int, status: int) -> None:
        self.problem_id: int = problem_id
        self.status: int = status