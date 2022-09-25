import datetime
import decimal



class BusinessDetails:
    def __init__(self, name: str, yearEstablished: datetime, summary:{} ):
        self.Name = name
        self.YearEstablished = yearEstablished
        self.Summary = summary

class LoanRequestInfo:
    def __init__(self, businessdetails: BusinessDetails, preassesment: decimal):
        self.businessdetails = businessdetails
        self.preassesment = preassesment

class BalanceSheetSummary:
    def __init__(self, businessDetails: BusinessDetails, profitlastyear: decimal, averageasset: decimal, loanamount: decimal):
        self.BusinessDetails = businessDetails
        self.ProfitLastYear = profitlastyear
        self.AverageAsset = averageasset
        self.LoanAmount = loanamount