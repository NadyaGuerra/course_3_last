from datetime import datetime
class Operation():
    def __init__(self, date, operation_amount, description, where_from: str, to):
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.where_from = where_from
        self.to = to

    def date_format(self):
        date_format = datetime.fromisoformat(self.date)
        return date_format.strftime('%d.%m.%Y')

    def where_from_method(self):
        account = []
        name = []
        new = []
        if self.where_from is not None:
            for i in range(len(self.where_from)):
                if self.where_from[i].isdigit():
                    account.append(self.where_from[i])
                else:
                    name.append(self.where_from[i])
            for i in range(6, len(account) - 4):
                account[i] = "*"
            for i in range(len(account)):
                if i % 4 == 0 and i != 0:
                    new.append("")
                new.append(account[i])
            return ''.join(name + new)

    def hide_to(self):
        acc = []
        card = []
        for i in range(len(self.to)):
            if self.to[i].isdigit():
                acc.append(self.to[i])
            else:
                card.append(self.to[i])

        acc = acc[-6::]
        acc[0] = "*"
        acc[1] = "*"
        return ''.join(card + acc)

    def get_amount(self):
        return (self.operation_amount['amount'])

    def get_currency(self):
        return self.operation_amount["currency"]["name"]
    def get_description(self):
        return self.description