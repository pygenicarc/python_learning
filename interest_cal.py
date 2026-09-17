def ramu():
    loan_data = {
        "loan_amount": 50000,
        "interest_rate": 5.5,
        "loan_term": 10
    }
    return loan_data

def raju():
    loan_data = {
            "loan_amount": 150000,
            "interest_rate": 8.5,
            "loan_term": 10
        }
    return loan_data

def reddy():
    ramu_loan_data = ramu()
    raju_loan_data = raju()

    # Calculate total loan amounts
    total_loan_amount = ramu_loan_data["loan_amount"] + raju_loan_data["loan_amount"]
    print(f"Total Loan Amount: {total_loan_amount}")

    avg_interest_rate = (ramu_loan_data["interest_rate"] + raju_loan_data["interest_rate"]) / 2
    print(f"Average Interest Rate: {avg_interest_rate}%")

    total_loan_term = ramu_loan_data["loan_term"] + raju_loan_data["loan_term"]
    print(f"Total Loan Term: {total_loan_term} months")


print("This is a simple Python script with three functions.")
reddy() # main function call to start the chain of function calls
