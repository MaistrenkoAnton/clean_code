import mock
calculate_commissioned_pay = mock.Mock()
calculate_hourly_pay = mock.Mock()
calculate_salaried_pay = mock.Mock()
InvalidEmployeeType = mock.Mock()
NotImplementedError = mock.Mock()
CommissionedEmployee = mock.Mock()
HourlyEmployee = mock.Mock()
SalariedEmployee = mock.Mock()


def calculate_pay(e):
    match e.type:
        case 'COMMISSIONED':
            return calculate_commissioned_pay(e)
        case 'HOURLY':
            return calculate_hourly_pay(e)
        case 'SALARIED':
            return calculate_salaried_pay(e)
        case _:
            raise InvalidEmployeeType(e.type)


###################################################3


class Employee:

    def is_payday(self):
        raise NotImplementedError

    def calculate_pay(self):
        raise NotImplementedError

    def deliver_pay(self, pay):
        raise NotImplementedError


class EmployeeFactory:
    def makeEmployee(self, r):
        raise NotImplementedError


class EmployeeFactoryImpl(EmployeeFactory):
    def makeEmployee(self, r):
        match r.type:
            case 'COMMISSIONED':
                return CommissionedEmployee(r)
            case 'HOURLY':
                return HourlyEmployee(r)
            case 'SALARIED':
                return SalariedEmployee(r)
            case _:
                raise InvalidEmployeeType(r.type)