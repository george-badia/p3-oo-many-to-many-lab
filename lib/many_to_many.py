# many_to_many.py

class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        """Return all contracts related to the author."""
        return self._contracts

    def books(self):
        """Return all books related to the author."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Sign a new contract and add it to the list of contracts."""
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        """Calculate the total royalties from all contracts."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        """Return all contracts related to the book."""
        return self._contracts

    def authors(self):
        """Return all authors related to the book."""
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate types
        if not isinstance(author, Author):
            raise Exception("Invalid author type.")
        if not isinstance(book, Book):
            raise Exception("Invalid book type.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        # Initialize the contract attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add contract to author's and book's lists
        author._contracts.append(self)
        book._contracts.append(self)

        # Add to the global list of contracts
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, target_date):
        """Return contracts sorted by date that match the target date."""
        return [contract for contract in cls.all if contract.date == target_date]
