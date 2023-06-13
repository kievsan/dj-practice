from rest_framework import serializers

from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description', ]


class ProductPositionSerializer(serializers.ModelSerializer):
    # сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # связанные данные для других таблиц
        # в validated_date - json запрос с полями 'address' и 'positions'

        # в positions сохраняем только поле 'positions'
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        # в validated_data осталось поле 'adress'
        stock = super().create(validated_data)

        # заполним связанные таблицы
        # StockProduct с помощью списка positions

        # перебираем все positions и создаем для каждой объект модели StockProduct,
        # где stock=stock - это ссылка на склад, созданный только что
        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position.get('product'),
                quantity=position.get('quantity'),
                price=position.get('price')
            )
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        # в validated_date - json запрос с 'address', 'positions'
        # в positions  - сохраняем только 'positions'

        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        # в instance - склад, передаем только поле positions (validated_data пусто)

        stock = super().update(instance, validated_data)

        # обновим связанные таблицы
        # StockProduct с помощью списка positions

        # метод update_or_create ищет в БД объект с полями stock и product,
        # нашел - обновляет остальные поля, указанные в defaults,
        # нет - создает новый объект

        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position.get('product'),
                defaults={
                    'quantity': position.get('quantity'),
                    'price': position.get('price'),
                }
            )

        return stock
