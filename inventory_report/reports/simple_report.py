from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, report):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in report]
        )

        expiration_date = min(
            [
                product["data_de_validade"]
                for product in report
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()
            ]
        )

        stocked = max(product["nome_da_empresa"] for product in report)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {stocked}\n"
        )
