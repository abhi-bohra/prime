#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Incometax:
    def __init__(self, gross_income, deduction):
        self.gross_income = gross_income
        self.deduction = deduction
        
    def tax_income(self):
        taxable_income = self.gross_income - self.deduction
        if taxable_income < 0:
            print("You must enter a valid amount. Please try again.")
        
        elif taxable_income <= 250000:
            print('Taxpay has to pay nothing')
            
        elif taxable_income >= 250001 & taxable_income <= 500000:
            taxable_income = taxable_income * 0.05
            print('Taxpayer has to pay:', taxable_income)
            
        elif taxable_income >= 500001 & taxable_income <= 750000:
            taxable_income = taxable_income * 0.1
            print('Taxpayer has to pay:', taxable_income)
            
        elif taxable_income >= 750001 & taxable_income <= 1000000:
            taxable_income = taxable_income * 0.15
            print('Taxpayer has to pay:', taxable_income)
            
        elif taxable_income >= 1000001 & taxable_income <= 1250000:
            taxable_income = taxable_income * 0.2
            print('Taxpayer has to pay:', taxable_income)
            
        elif taxable_income >= 1250001 & taxable_income <= 1500000:
            taxable_income = taxable_income * 0.25
            print('Taxpayer has to pay:', taxable_income)
            
        else:
            taxable_income = taxable_income * 0.3
            print('Taxpayer has to pay:', taxable_income)
            
p1 = Incometax(int(input('Enter Your Gross Salary:')), int(input('Enter Your Deduction:')))
p1.tax_income()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




