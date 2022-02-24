from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)
        companies_list = Counter(
            product["nome_da_empresa"] for product in report
        )
        stocked = "Produtos estocados por empresa: \n"
        for company in companies_list:
            stocked += f"- {company}: {companies_list[company]}\n"

        return f"{simple_report}\n" f"{stocked}"
