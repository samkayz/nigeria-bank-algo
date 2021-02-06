# NUBAN (Nigerian Uniform Bank Account Number) Algorithm

This library is an algorithm for generating and validating a NUBAN (Nigeria Uniform Bank Account Number) in python. The algorithm is based on CBN specification for the 10-digit NUBAN.

A common application of this algorithm in Nigeria today is to cut down the list of banks on USSD interfaces from about 23 to less than 5 after the user enters their bank account number (NUBAN). This comes in handy because a USSD screen can display at most, 160 characters at a time.

## How to use it 

pip install nigeria-bank-algo

## API Endpoints

from banks.getbanks import *

bnk = GetBank()

likely = bnk.GetLikeBank(accountNumber='your-account-number')
print(likely)

[
    {'code': '044', 'name': 'ACCESS BANK'}, 
    {'code': '070', 'name': 'FIDELITY BANK'}, 
    {'code': '011', 'name': 'FIRST BANK OF NIGERIA'}, 
    {'code': '058', 'name': 'GUARANTY TRUST BANK'}, 
    {'code': '033', 'name': 'UNITED BANK FOR AFRICA'}
    ]

A list of banks where the account number may likely domiciled will be return.
