def estimate_hause_value(size_in_sqft, number_of_bedrooms):

    # her evin en az $50.000 olduğunu varsayalım
    value = 50000

    # evin büyklüğüne göre fiyat ayarlaması yapalım
    value = value + (size_in_sqft * 92)

    # yatak odası sayısına göre fiyat ayarlamsı yapalım
    value = value + (number_of_bedrooms * 10000)

    return value

value = estimate_hause_value(3800, 5)

print("Estimated valued:")
print(value)