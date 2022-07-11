from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Camisa",
        "Approve",
        "22/03/2021",
        "22/03/2027",
        154789,
        "Manter em local arejado"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Camisa"
    assert product.nome_da_empresa == "Approve"
    assert product.data_de_fabricacao == "22/03/2021"
    assert product.data_de_validade == "22/03/2027"
    assert product.numero_de_serie == 154789
    assert product.instrucoes_de_armazenamento == "Manter em local arejado"
