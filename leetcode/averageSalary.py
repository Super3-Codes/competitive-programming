  def average(self, salary: List[int]) -> float:
        salary.sort()
        salary[0], salary[-1] = 0, 0
        return float((sum(salary)*1.0) / (len(salary) - 2))
