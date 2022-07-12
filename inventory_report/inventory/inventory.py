import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def read_csv(cls, path):
        report = list()
        with open(path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                report.append(row)

        return report

    @classmethod
    def read_json(cls, path):
        report = list()
        with open(path, mode="r") as file:
            reader = json.load(file)
            for row in reader:
                report.append(row)
        return report

    @classmethod
    def read_xml(cls, path):
        report = list()
        with open(path, mode="r") as file:
            reader = xmltodict.parse(file.read())
            format_reader = reader["dataset"]["record"]
            for row in format_reader:
                report.append(row)
        return report

    @classmethod
    def handle_file(cls, path):
        if path.endswith(".csv"):
            return Inventory.read_csv(path)
        elif path.endswith(".json"):
            return Inventory.read_json(path)
        elif path.endswith(".xml"):
            return Inventory.read_xml(path)
        else:
            raise ValueError("File type not supported")

    @classmethod
    def import_data(cls, path, report_type):
        report = Inventory.handle_file(path)

        if report_type == "simples":
            return SimpleReport.generate(report)
        elif report_type == "completo":
            return CompleteReport.generate(report)
        else:
            raise ValueError("Invalid report type")
