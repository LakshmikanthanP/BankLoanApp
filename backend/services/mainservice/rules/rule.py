import json
from abc import ABC, abstractmethod
from unicodedata import decimal


class PreAssessmentRule(ABC):
    @abstractmethod
    def shouldprocess(self, balancesheetInfo):
        pass

    @abstractmethod
    def calculatepreAssessment(self):
        pass

class AverageAssesmentRule(PreAssessmentRule):

    def shouldprocess(self, balancesheetInfo):
        print("Inside AverageAssesmentRule")
        print(balancesheetInfo.ProfitLastYear)
        return int(balancesheetInfo.ProfitLastYear) > 0

    def calculatepreAssessment(self):
            return 60

class HighAssesmentRule(PreAssessmentRule):

    def shouldprocess(self, balancesheetInfo):
        return balancesheetInfo.AverageAsset > balancesheetInfo.LoanAmount

    def calculatepreAssessment(self):
            return 100

class RuleEngine:
    rulescollection = list()
    def __init__(self):
        self.rulescollection.append(AverageAssesmentRule)
        self.rulescollection.append(HighAssesmentRule)

    def calculatePreAssesment(self,balancesheetInfo)-> decimal:
        for rule in self.rulescollection:
            if rule.shouldprocess(self,balancesheetInfo):
                print(f"inside rule-engine for rule {rule} ")
                return rule.calculatepreAssessment(self)



