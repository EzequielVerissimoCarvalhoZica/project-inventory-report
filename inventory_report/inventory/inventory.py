import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):

        report = []
        if path.endswith(".csv"):
            with open(path, mode="r") as file:
                reader = csv.DictReader(file)
            for row in reader:
                report.append(row)
        else:
            raise ValueError("File type not supported")

        print(report, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        if report_type == "simples":
            return SimpleReport.generate(report)
        elif report_type == "completo":
            return CompleteReport.generate(report)
        else:
            raise ValueError("Invalid report type")
