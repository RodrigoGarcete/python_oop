from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DICストア")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("メモリー", 13880, seller)
    Item("マザーボード", 28980, seller)
    Item("電源ユニット", 8980, seller)
    Item("PCケース", 8727, seller)
    Item("3.5インチHDD", 10980, seller)
    Item("2.5インチSSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPUクーラー", 13400, seller)
    Item("グラフィックボード", 23800, seller)

print("🤖 あなたの名前を教えてください 'Por favor, dime tu nombre'")
customer = Customer(input())

print("🏧 ウォレットにチャージする金額を入力にしてください 'Por favor, introduce el monto que deseas cargar en tu billetera.'")
customer.wallet.deposit(int(input()))

print("🛍️ ショッピングを開始します 'Voy a comenzar a comprar.'")
end_shopping = False
while not end_shopping:
    print("📜 商品リスト 'Lista de productos'")
    seller.show_items()

    print("️️⛏ 商品番号を入力してください 'Por favor, ingresa el número del producto.'")
    number = int(input())

    print("⛏ 商品数量を入力してください 'Por favor, ingresa la cantidad del producto.'")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 カートの中身")
    customer.cart.show_items()
    print(f"🤑 合計金額: {customer.cart.total_amount()}")

    print("😭 買い物を終了しますか？(yes/no)")
    end_shopping = input() == "yes"

print("💸 購入を確定しますか？(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈結果┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}の所有物")
customer.show_items()
print(f"😱👛 {customer.name}のウォレット残高: {customer.wallet.balance}")

print(f"📦 {seller.name}の在庫状況")
seller.show_items()
print(f"😻👛 {seller.name}のウォレット残高: {seller.wallet.balance}")

print("🛒 カートの中身")
customer.cart.show_items()
print(f"🌚 合計金額: {customer.cart.total_amount()}")

print("🎉 終了")
