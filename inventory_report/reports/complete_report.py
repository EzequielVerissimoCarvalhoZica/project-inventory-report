from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        simple_report = super().generate(stock)
        stock_by_company = Counter(
            [company["nome_da_empresa"] for company in stock]
        )
        text = "Produtos estocados por empresa:\n"
        for company in stock_by_company:
            text += f"- {company}: {stock_by_company[company]}\n"

        return f"{simple_report}\n" f"{text}"
