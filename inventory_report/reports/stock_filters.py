from abc import ABC, abstractmethod
import datetime


class Stock(ABC):
    @classmethod
    @abstractmethod
    def company_bigger_stock(cls, products):
        company = [product["nome_da_empresa"] for product in products]

        return max(company, key=company.count)

    @classmethod
    @abstractmethod
    def nearest_expiration_date(cls, products):
        next_date = [
            product["data_de_validade"]
            for product in products
            if product["data_de_validade"] >= str(datetime.date.today())
        ]

        return min(next_date)

    @classmethod
    @abstractmethod
    def earliest_manufacturing_date(cls, products):
        last_date = [product["data_de_fabricacao"] for product in products]

        return min(last_date)
