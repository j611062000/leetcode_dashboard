from json import JSONEncoder
from datetime import date
from typing import Optional

Pattern = list[str]
DifficultyLevel = int
Status = int
Solved = 1
Unsolved = 0


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
    def __init__(
        self,
        id: int,
        title: str,
        slug: str,
        pattern: Pattern,
        difficulty: DifficultyLevel,
        is_premium: bool,
        companies: list[Company],
        status: int,
        last_updated:  Optional[date]
    ) -> None:
        self.id: int = id
        self.title: str = title
        self.slug: str = slug
        self.pattern: Pattern = pattern
        self.difficulty: DifficultyLevel = difficulty
        self.is_premium: bool = is_premium
        self.companies: list[Company] = companies
        self.status: Status = status
        self.last_updated: Optional[date] = last_updated

    def update_status(self, status: Status) -> None:
        self.status = status
        self.last_updated = date.today()

    def is_choosen(self, filter: Optional['ProblemFilter']) -> bool:
        is_no_filter = not filter or  filter.is_no_filter()
        if is_no_filter:
            return True
        else:
            if not filter:
                return True
            is_chosen_by_title = not filter.title or self.title == filter.title
            is_chosen_by_premuim = not filter.is_premium or self.is_premium == filter.is_premium
            is_chosen_by_status = not filter.statusSet or self.status in filter.statusSet

            return is_chosen_by_title and is_chosen_by_premuim and is_chosen_by_status


class ProblemEncoder(JSONEncoder):
    def default(self, o: Problem):
        return o.__dict__


class ProblemFilter:
    def __init__(self,
                 title: Optional[str] = None,
                 pattern: Optional[Pattern] = None,
                 statusSet: Optional[list[Status]] = None,
                 difficulty: Optional[list[str]] = None,
                 companies: Optional[list[str]] = None,
                 is_premium: Optional[bool] = None) -> None:
        self.title: Optional[str] = title
        self.pattern: Optional[Pattern] = pattern
        self.difficulty: Optional[list[str]] = difficulty
        self.is_premium: Optional[bool] = is_premium
        self.companies: Optional[list[str]] = companies
        self.statusSet: Optional[list[Status]] = statusSet

    def is_no_filter(self) -> bool:
        return self.title is None and self.pattern is None and self.difficulty is None and self.is_premium is None and self.companies is None and self.statusSet is None


class ProblemSet:
    def __init__(self, lastUpdated: str, problems: dict[int, Problem]) -> None:
        self.lastUpdated: str = lastUpdated
        self.problems: dict[int, Problem] = problems

    @staticmethod
    def getEmptyProblemSet() -> 'ProblemSet':
        return ProblemSet("", {})

    def get_sorted_problems(self) -> list[Problem]:
        return sorted(self.problems.values(), key=lambda p: p.id)

    def get_filtered_problems(self, problemFilter: Optional[ProblemFilter]) -> Optional[list[Problem]]:
        if problemFilter is None:
            return self.get_sorted_problems()
        else:
            problems = [p for p in self.problems.values(
            ) if p.is_choosen(problemFilter)]
            return sorted(problems, key=lambda p: p.id)

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

    # def get_filtered_problems(self, )


class Statistics:
    def __init__(self, solved: dict[int, int], total: int) -> None:
        self.solved_easy: int = solved[Difficulty.EASY]
        self.solved_medium: int = solved[Difficulty.MEDIUM]
        self.solved_hard: int = solved[Difficulty.HARD]
        self.total_solved: int = sum(solved.values())
        self.total: int = total
        self.progress_perct: float = round(
            self.total_solved / self.total * 100, 1)


class ProblemUpdateRequest:
    def __init__(self, problem_id: int, status: int) -> None:
        self.problem_id: int = problem_id
        self.status: int = status
