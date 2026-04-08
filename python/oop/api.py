# třída pro práci s daty a dotazy

class Query:
    def __init__(self, data):
        self.data = data
    
    # Filtrování dat podle zadaného klíče a hodnoty
    def filter_by(self, field, value):
        filtered = []
        for item in self.data:
            if item.get(field) == value:
                filtered.append(item)

        self.data = filtered

        return self

    # Seřazení dat podle zadaného klíče
    def sort_by(self, field):
        def get_item(item):
            return item.get(field)

        self.data.sort(key=get_item)

        return self

    # Omezení počtu výsledků na n
    def limit(self, n):
        filtered = []
        for item in self.data:
            if len(filtered) != n:
                filtered.append(item)
            else:
                break

        self.data = filtered

        return self

    # Vrácení výsledků dotazu
    def execute(self):
        return self.data

# Vzorová testovací data
data = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 17},
    {"name": "Emily", "age": 18},
    {"name": "John", "age": 21},
    {"name": "Jack", "age": 22},
    {"name": "Kevin", "age": 18},
    {"name": "Annie", "age": 20},
    {"name": "Charlotte", "age": 17},
    {"name": "Wanda", "age": 18},
    {"name": "Adam", "age": 16},
    {"name": "Fiona", "age": 17},
    {"name": "Charlie", "age": 18},
    {"name": "Charlie", "age": 29}
]

# Původní API bez fluentního rozhraní
q = Query(data)
q.filter_by("age", 18)
q.sort_by("name")
q.limit(10)
result = q.execute()

# Příklad cílového řešení s fluent API, otestování nového API
result = Query(data).filter_by("age", 18).execute()
print(result)
