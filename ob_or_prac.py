class customer :
    def __init__(self, name, membership_type) :
        self.name = name
        self.membership_type = membership_type

    def upgrad_membership(self, new_membership) :
        print('changing stuff')
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers) :
        for customer in customers :
            print(customer)

    def __eq__(self, other) :
        if self.name == other.name and self.membership_type == other.membership_type :
            return True

        return False

    __hash__ = None

    __repr__ = __str__

customers = [customer('Justin', 'KFC Club'),
            customer('Sherry', 'KFC Club')]

print(customers)
