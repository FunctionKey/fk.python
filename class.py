# Define invoice class
class invoice:
    def __init__(self, source, amount, account, agent):
        self.client = "fnkguy"
        self.source = source
        self.amount = amount
        self.payment_account = account
        self.agent = agent  # empty variable to be filled later in the script

# Request input from user
source = input("source: \n")
amount = input("amount: \n")
account = input("payment account: \n")

# Evaluate source to define agent
if source == "azure":
    agent = "smith"
else:
    agent = "laura"
    # add properties to class
    #print("azure requests should be handled by agent smith")   # here so the code doesn't return error

# Create the object (Instantiate)
bill = invoice(source, amount, account, agent)
print("Please inform agent ", bill.agent, " that payment is required from ", bill.source, " with the amount: ", bill.amount)
