from abc import abstractmethod
from inventory_report.reports.stock_filters import Stock


class SimpleReport:
    @abstractmethod
    def generate(products):
        manufacturing_date = Stock.earliest_manufacturing_date(products)
        expiration_date = Stock.nearest_expiration_date(products)
        company = Stock.company_bigger_stock(products)

        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {company}"
        )
