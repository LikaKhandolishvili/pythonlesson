# სავარჯიშო 7. შეიყვანეთ სამი სტრიქონი რომელიც წარმოადგენს სხვადასხვა ხილის დასახელებას (მაგ. Banana,
# Watermelon, Apple). დაბეჭდეთ ისინი ალფაბეტის ზრდადობის მიხედვით (თავდაპირველად
# წაიკითხეთ სლაიდი “შედარების ოპერაციები სტრიქონებზე”).

text_1 = "Banana"
text_2 = "Watermelon"
text_3 = "Apple"
if text_1>text_2 and text_2>text_3:
    print(text_2, "is first alphabetically")
elif text_2<text_1 and text_1<text_3:
    print(text_1, "is first alphabetically")
else:
    print(text_3, "is first alphabetically")

