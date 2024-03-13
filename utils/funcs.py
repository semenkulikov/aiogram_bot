from database.models import Product


def get_text_for_product(product: Product) -> str:
    result_text = (f"Вот информация по товару с артикулом {product.article}:\n"
                   f"Название: {product.name}\n"
                   f"Артикул: {product.article}\n"
                   f"Цена: {product.price}\n"
                   f"Рейтинг товара: {product.rating}\n"
                   f"Количество товара на всех складах: {product.count}")
    return result_text
