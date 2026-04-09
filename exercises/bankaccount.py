from __future__ import annotations


class BankAccount:
    """A simple bank account with a few attributes."""

    owner: str
    balance: float
    currency: str

    def __init__(self, owner: str, balance: float, currency: str):
        """Initialize a BankAccount instance."""
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def __str__(self) -> str:
        """Return a human-readable string representation of the account."""
        return f"{self.owner}'s account: ${self.balance} {self.currency}"

    def __repr__(self) -> str:
        return f"{repr(self.owner)}, ${repr(self.balance)}, {repr(self.currency)}"

    def __add__(self, amount: float) -> BankAccount:
        """Return a new BankAccount with 'amount' deposited into it."""
        return BankAccount(self.owner, self.balance + amount, self.currency)

    def __mul__(self, factor: float) -> BankAccount:
        """Return a new BankAccount with 'factor' multiplied on balance"""
        return BankAccount(self.owner, self.balance * factor, self.currency)


account: BankAccount = BankAccount("Colby", 6000.0, "USD")

print(account)
print(repr(account))
richer = account + 10000.0
print(richer)
with_interest = richer * 1.50
print(with_interest)
