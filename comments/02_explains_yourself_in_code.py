import mock
employee = mock.Mock()
HOURLY_FLAG = mock.Mock()


# Check to see if the employee is eligible for full benefits
if (employee.flags and HOURLY_FLAG) and (employee.age > 65):
    pass

if employee.isEligibleForFullBenefits():
    pass
