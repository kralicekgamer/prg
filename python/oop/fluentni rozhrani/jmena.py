class Query:
    def __init__(self, data):
        self.original_data = data
        self.operations = []

    def filter(self, field, operator, value):
        allowed_ops = ['>=', '<=', '!=']
        if operator not in allowed_ops:
            raise ValueError("Operator neni povolen")

        def op(record):
            # kdyz neexistuje uzivatel ma smulu
            if field not in record:
                return False
            if operator == ">=":
                return record[field] >= value
            if operator == "<=":
                return record[field] <= value
            if operator == "!=":
                return record[field] != value

        self.operations.append(("filter", op))
        return self


    def sort_by(self, field, descending=False):
        # idk kazdy ma rad trideni
        def op(data):
            # pokud field neexistuje pad, linej impementovat
            return sorted(data, key=lambda x: x[field], reverse=descending)

        self.operations.append(("sort", op))
        return self


    def limit(self, count):
        # vezmes n zbytek dej pryc
        def op(data):
            return data[:count]

        self.operations.append(("limit", op))
        return self


    def distinct(self, field):
        # deduplikace pokud vidime stejny mazeme
        def op(data):
            seen = set()
            result = []
            for item in data:
                val = item.get(field)
                if val not in seen:
                    seen.add(val)
                    result.append(item)
            return result

        self.operations.append(("distinct", op))
        return self


    def execute(self):
        result = list(self.original_data)
        for name, operation in self.operations:
            if name == "filter":
                result = list(filter(operation, result))
            else:
                result = operation(result)
        return result


students = [
    {'name': 'Anna', 'age': 19, 'score': 85},
    {'name': 'Petr', 'age': 17, 'score': 60},
    {'name': 'Eva', 'age': 21, 'score': 92},
    {'name': 'Jan', 'age': 18, 'score': 70},
    {'name': 'Lucie', 'age': 20, 'score': 88}
]


result = (
    Query(students)
    .filter("age", ">=", 18)
    .distinct("age")
    .sort_by("score", descending=True)
    .limit(3)
    .execute()
)

print(result)
