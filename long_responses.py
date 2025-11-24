import random

R_LOCATION = "VIT Bhopal is located in Kotri Kalan, Astha, Sehore"
R_FEES = "Contact this email id for your fees related problems- feescollection@vitbopal.ac.in "
R_CTS = "Contact this email id for cts office- cts@vitbhopal.ac.in"
R_LADIES_HOSTEL = "This is the email id of girls hostel chief warden- cw.lh@vitbhopal.ac.in"
R_BOYS_HOSTEL = "This is the email id of boys hstel chief warden- cw@vitbhopal.ac.in"
R_ADMISSION = "For admission into vitb you must clear VITEEE"
R_PLACEMENTS = "90% if students from vitb get placed"
R_CHANCELLOR = "The chancellor of vitb is Dr. G. Viswanathan"
R_AGE = "Vitb is 10 years old"
def unknown():
    response = ["Could you please re-phrase that? ",
                "I'm sorry, I don't understand",
                "I couldn't quite process that",
                "What do you mean by that?"][
        random.randrange(4)]
    return response
