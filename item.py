class Item:
    from ownable import set_owner
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Itemインスタンスの生成時、そのItemインスタンス(self)は、insntancesというクラス変数に格納されます。
        # Durante la creación de una instancia de Item, dicha instancia de Item (self) se almacena en una variable de clase llamada 'instances'.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # instancesを返します ==> Item.item_all()でこれまでに生成されたItemインスタンスを全て返すということです
        # Devuelve las instancias ==> Con Item.item_all(), se devuelven todas las instancias de Item que se han creado hasta el momento.
        return Item.instances
