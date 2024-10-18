from django.db import models

# Модели
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    medical_type = models.CharField(max_length=50)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    c_gst = models.IntegerField()
    s_gst = models.IntegerField()
    batch_no = models.CharField(max_length=50)
    shelf_no = models.CharField(max_length=50)
    expire_date = models.DateTimeField()
    mfg_date = models.DateTimeField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    in_stock_total = models.IntegerField()
    qty_in_strip = models.IntegerField()
    objects = models.Manager()

class MedicalDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    salt_name = models.CharField(max_length=100)
    salt_qty = models.CharField(max_length=100)
    salt_qty_type = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    joining_date = models.DateTimeField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateTimeField()
    salary_amount = models.CharField(max_length=100)  # Указан тип данных
    added_on = models.DateTimeField()  # Добавлены скобки
    objects = models.Manager()

class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()  # Добавлены скобки
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class CustomerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    medicine_details = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    prescription = models.FileField(default="")
    objects = models.Manager()

class CompanyAccount(models.Model):
    choices = ((1, "Debit"), (2, "Credit"))

    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=choices, max_length=100)
    transaction_amt = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class CompanyBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=100)
    ifsc_no = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class EmployeeBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=100)
    ifsc_no = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
