class Bankomat:
    def __init__(self, initial_balance_uzs=0):
        self.balance_uzs = initial_balance_uzs  # Balans so'mda
        self.usd_to_uzs = 11600  # Hozirgi dollar kursi

    def deposit(self, amount, currency='UZS'):
        """Pul qabul qilish."""
        if currency == 'USD':
            amount_in_uzs = amount * self.usd_to_uzs
        else:
            amount_in_uzs = amount

        self.balance_uzs += amount_in_uzs
        print(f"{amount} {currency} muvaffaqiyatli qabul qilindi. Yangi balans: {self.balance_uzs} UZS")

    def withdraw(self, amount, currency='UZS'):
        """Pul yechib olish (1% komissiya bilan)."""
        if currency == 'USD':
            amount_in_uzs = amount * self.usd_to_uzs
        else:
            amount_in_uzs = amount

        total_amount = amount_in_uzs * 1.01  # 1% komissiya hisobga olinadi
        if self.balance_uzs >= total_amount:
            self.balance_uzs -= total_amount
            print(f"{amount} {currency} muvaffaqiyatli yechildi. Qoldiq balans: {self.balance_uzs} UZS")
        else:
            print("Yetarli mablag' mavjud emas.")

    def show_balance(self):
        """Balansni ko'rsatish."""
        print(f"Joriy balans: {self.balance_uzs} UZS yoki {self.balance_uzs / self.usd_to_uzs:.2f} USD")

    def exchange_currency(self, amount, from_currency='UZS'):
        """Valyutani almashtirish."""
        if from_currency == 'USD':
            converted_amount = amount * self.usd_to_uzs
            print(f"{amount} USD to {converted_amount} UZS ga almashtirildi.")
        else:
            converted_amount = amount / self.usd_to_uzs
            print(f"{amount} UZS to {converted_amount:.2f} USD ga almashtirildi.")
        return converted_amount

# Dasturdan foydalanish:
bankomat = Bankomat()

# Pul qabul qilish
bankomat.deposit(500000)

# Pul yechish
bankomat.withdraw(100000)

# Balansni ko'rish
bankomat.show_balance()

# Valyutani almashtirish
bankomat.exchange_currency(100, 'USD')
