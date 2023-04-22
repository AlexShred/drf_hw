from app.models import *

c1 = Category.objects.create(name="Продукты")
c2 = Category.objects.create(name="Мыломойка")

p1 = Product.objects.create(name="хлеб", price="20с", category=c1)
p2 = Product.objects.create(name="вода", price="45с", category=c1)
p3 = Product.objects.create(name="моющее средство для посуды", price="150с", category=c2)
p4 = Product.objects.create(name="порошок", price="320с", category=c2)
p5 = Product.objects.create(name="шампунь ", price="500с", category=c2)