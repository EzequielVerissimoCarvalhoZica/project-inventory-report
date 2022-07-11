from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Camisa",
        "Approve",
        "22/03/2021",
        "22/03/2027",
        154789,
        "Manter em local arejado"
    )

    assert str(product) == (
        "O produto Camisa fabricado em 22/03/2021 "
        "por Approve com validade até "
        "22/03/2027 precisa ser armazenado "
        "Manter em local arejado."
        )
