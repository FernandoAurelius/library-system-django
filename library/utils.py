from library.models import Loan

def delete_loans():
    loans = Loan.objects.all()
    for loan in loans:
        loan.delete()
