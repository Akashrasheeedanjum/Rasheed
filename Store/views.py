# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib.auth import authenticate, login,logout
from datetime import date
from decimal import Decimal
from django.db.models import Sum
def index(request):
    # Your view logic here
    return render(request, 'base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        print(username,password)
        print("/////")
        print(user)

        if user is not None:
            login(request, user)
            if user.user_type == 'manager':
                print("i am manager")
                return redirect('manager_dashbord')
            elif request.user.is_staff:
                print("i am Admin")
                return redirect('manager_dashbord')

            elif user.user_type == 'customer':
                return redirect('customer_dashboard')  # Redirect customers to their dashboard
        else:
            # Handle invalid login credentials
            # You can render a template with an error message or redirect to the login page again
            pass
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST['user_type']
        phone = request.POST.get('phone', '')  # Optional field
        address = request.POST.get('address', '')  # Optional field
        date_of_birth = request.POST.get('date_of_birth', '')  # Optional field

        # Process and save the data (e.g., create a user object)
        CustomUser.objects.create_user(username=username,password=password,user_type=user_type,phone_number=phone,address=address,date_of_birth=date_of_birth)
        print("saved")

        return redirect('user_login')
    # Your view logic here
    return render(request, 'signup.html')

def signout(request):
    print("logout")
    logout(request)
    # messages.success(request,"Logout Successfully")
    return redirect("/")

# delect Functions 

def deleteCenterMilk(request,id,pid):
    print('rining')
    print(id)
    
    inf = MilkPurchase.objects.get(id=id)
    inf.delete()
    return redirect(f'/view_center/{pid}')

def deleteCenter(request,id):
    print('rining')
    print(id)
    
    inf = MilkCenter.objects.get(id=id)
    inf.delete()
    return redirect('center_details')

def deleteCenterPayment(request,id,pid):
    print('rining')
    print(id)
    
    inf = MakePayment.objects.get(id=id)
    inf.delete()
    return redirect(f'/view_center/{pid}')

def deleteCustomer(request,id):
    print('rining')
    print(id)
    
    inf = Customer.objects.get(id=id)
    inf.delete()
    return redirect('customer_details')

def deleteCustomerPayment(request,id,pid):
    print('rining')
    print(id)
    
    inf = ReceivedPayment.objects.get(id=id)
    inf.delete()
    return redirect(f'/view_customer/{pid}')

def deleteExpence(request,id,pid):
    print('rining')
    print(id)
    
    inf = CustomerExpence.objects.get(id=id)
    inf.delete()
    return redirect(f'/view_customer/{pid}')

def deleteSalePayment(request,id,pid):
    print('rining')
    print(id)
    
    inf = sale_milk.objects.get(id=id)
    inf.delete()
    return redirect(f'/view_customer/{pid}')


# Edit Functions
# 
def editCenterMilk(request,id,pid):

    edit_milk=MilkPurchase.objects.get(id=id)

    dd=str(edit_milk.purchase_date)




    if request.method == 'POST':
        # center_name = request.POST.get('milk_center', '')
        date_str = request.POST.get('date', '')
        print(date_str)
        volume = request.POST.get('volume', '')
        price = request.POST.get('price', '')
        lr = request.POST.get('LR', '')  # Corrected variable name
        fat = request.POST.get('Fat', '')  # Corrected variable name
        snf = request.POST.get('SNF', '') # Corrected variable name
        ts = request.POST.get('TS', '')  # Corrected variable name
        TsVolume = request.POST.get('TsVolume', '')
        total_price = request.POST.get('total_price', '')
        date = datetime.strptime(date_str, '%Y-%m-%d')
        print(date)

        # date=str(date)
        edit_milk=MilkPurchase.objects.get(id=id)

        # edit_milk.milk_center=milk_center,
        edit_milk.purchase_date=date,
        edit_milk.volume=volume,
        edit_milk.price_per_liter=price,
        edit_milk.LR=lr,
        edit_milk.Fat=fat,
        edit_milk.SNF=snf,
        edit_milk.price_on_TS=TsVolume,
        edit_milk.total_price=total_price

        edit_milk.save()

        



        return redirect(f'/view_center/{pid}') 
    
    context={
        'edit_milk':edit_milk,
        'dd':dd
    }


    return render(request, 'manager/edit_purchase_milk.html',context)


def add_center(request):
    if request.method == 'POST':
        print("start")
        name = request.POST.get('name', '')  # Use the 'name' attribute of the input element
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        price = request.POST.get('price', '')


        MilkCenter(name=name,phone_number=phone,address=address,price_of_milk=price).save()
        print("saved")
        return redirect('/manager_dashbord/')

    

    return render(request, 'manager/add_center.html')

def add_customer(request):
    if request.method == 'POST':
        print("start")
        name = request.POST.get('name', '')  # Use the 'name' attribute of the input element
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        


        Customer(name=name,phone_number=phone,address=address).save()
        print("saved")
        return redirect('/manager_dashbord/')
    return render(request, 'manager/add_customer.html')


def purchase_milk(request):

    from datetime import date
    today = date.today()
    centers = MilkCenter.objects.all()
    purchase=MilkPurchase.objects.filter(purchase_date=today)
    
    
    if request.method == 'POST':
        center_name = request.POST.get('milk_center', '')
        date = request.POST.get('date', '')
        print(date)
        volume = request.POST.get('volume', '')
        price = request.POST.get('price', '')
        lr = request.POST.get('LR', '')  # Corrected variable name
        fat = request.POST.get('Fat', '')  # Corrected variable name
        snf = request.POST.get('SNF', '') # Corrected variable name
        ts = request.POST.get('TS', '')  # Corrected variable name
        TsVolume = request.POST.get('TsVolume', '')
        total_price = request.POST.get('total_price', '')

        # Basic validation, you should add more robust validation
        if center_name and date and volume and price and lr and fat and snf and ts and total_price:
            # Get the MilkCenter instance
            try:
                milk_center = MilkCenter.objects.get(name=center_name)
            except MilkCenter.DoesNotExist:
                milk_center = None

            if milk_center:
                # Create a MilkPurchase instance and save it
                MilkPurchase(
                    milk_center=milk_center,
                    purchase_date=date,
                    volume=volume,
                    price_per_liter=price,
                    LR=lr,
                    Fat=fat,
                    SNF=snf,
                    price_on_TS=TsVolume,
                    total_price=total_price
                ).save()
                print("Saved")
                stor, created = Stor.objects.get_or_create(id=1)
           
                if created:
                    stor.milk_storage = Decimal('0.0')  # Set an initial value for 'milk_storage'
                volume_decimal = Decimal(volume)
                X = stor.milk_storage
                print(X)
                X += volume_decimal
                print(X)
                stor.milk_storage = X
                stor.save()
                purchase=MilkPurchase.objects.filter(purchase_date=today)
                return redirect('/purchase_milk/')
                # Redirect to a success page or do something else
                # return redirect('success_page')  # Replace 'success_page' with your actual success page URL
            else:
                # Handle the case where the MilkCenter with the given name doesn't exist
                error_message = "Milk Center not found."
                print("Milk Center not found.")
        else:
            # Handle the case where some fields are missing
            error_message = "Please fill in all fields."
            print("Please fill in all fields")

    # If it's not a POST request or there was an error, render the form page
    return render(request, 'manager/purchase.html', {'milk_center': centers,'purchase':purchase})


def sale_milk (request):
    from datetime import date
    today = date.today()
    customers = Customer.objects.all()
    sales=MilkSale.objects.filter(purchase_date=today)
    
    
    if request.method == 'POST':
        customer = request.POST.get('customer_name', '')
        date2 = request.POST.get('date', '')
        volume = request.POST.get('volume', '')
        price = request.POST.get('price', '')
        lr = request.POST.get('LR', '')  # Corrected variable name
        fat = request.POST.get('Fat', '')  # Corrected variable name
        snf = request.POST.get('SNF', '') # Corrected variable name
        ts = request.POST.get('TS', '')  # Corrected variable name
        total_price = request.POST.get('total_price', '')
        print(customer,date2,date2,price,lr,fat,snf,ts,total_price)

        # Basic validation, you should add more robust validation
        if customer and date2 and volume and price and lr and fat and snf and ts and total_price:
            # Get the MilkCenter instance
            try:
                milk_center = Customer.objects.get(name=customer)
            except Customer.DoesNotExist:
                milk_center = None

            if milk_center:
                # Create a MilkPurchase instance and save it
                MilkSale(
                    customer=milk_center,
                    purchase_date=date2,
                    volume=volume,
                    price_per_liter=price,
                    LR=lr,
                    Fat=fat,
                    SNF=snf,
                    price_on_TS=ts,
                    total_price=total_price
                ).save()
                print("Saved")
                stor, created = Stor.objects.get_or_create(id=1)
           
                if created:
                    stor.milk_storage = Decimal('0.0')  # Set an initial value for 'milk_storage'
                volume_decimal = Decimal(volume)
                X = stor.milk_storage
                print(X)
                X -= volume_decimal
                print(X)
                stor.milk_storage = X
                stor.save()
                sales=MilkSale.objects.filter(purchase_date=today)
                return redirect('/sale_milk/')
                # Redirect to a success page or do something else
                # return redirect('success_page')  # Replace 'success_page' with your actual success page URL
            else:
                # Handle the case where the MilkCenter with the given name doesn't exist
                error_message = "Milk Center not found."
                print("Milk Center not found.")
        else:
            # Handle the case where some fields are missing
            error_message = "Please fill in all fields."
            print("Please fill in all fields")

    # If it's not a POST request or there was an error, render the form page
    return render(request, 'manager/sale_milk.html', {'customers': customers, 'sales': sales})


def make_payment (request):
    from datetime import date
    today = date.today()
    centers=MilkCenter.objects.all()

    if request.method == 'POST':
        center_name = request.POST.get('center_name', '')
        amount = request.POST.get('amount', '')
        payment_date = request.POST.get('date', '')
        payment_method = 'Cash or ATM'
        notes= request.POST.get('node', '')
        print(center_name,amount,payment_date,payment_method,notes)

        if center_name and amount and payment_date and payment_method and notes:
            # Get the MilkCenter instance
            try:
                milk_center = MilkCenter.objects.get(name=center_name)
            except MilkCenter.DoesNotExist:
                milk_center = None

            if milk_center:
                # Create a MilkPurchase instance and save it
                MakePayment(milk_center=milk_center,amount=amount,payment_date=payment_date,payment_method=payment_method,notes=notes).save()
                print("Saved")
                # purchase=MilkPurchase.objects.filter(purchase_date=today)
                return redirect('/make_payment/')
                # Redirect to a success page or do something else
                # return redirect('success_page')  # Replace 'success_page' with your actual success page URL
            else:
                # Handle the case where the MilkCenter with the given name doesn't exist
                error_message = "Milk Center not found."
                print("Milk Center not found.")
        else:
            # Handle the case where some fields are missing
            error_message = "Please fill in all fields."
            print("Please fill in all fields")



        

    # Your view logic here
    return render(request, 'manager/Make_payment.html',{'center_name':centers})

def recive_payment (request):
    from datetime import date
    today = date.today()
    customers=Customer.objects.all()

    if request.method == 'POST':
        customer = request.POST.get('customer_name', '')
        amount_received = request.POST.get('amount', '')
        payment_date = request.POST.get('date', '')
        payment_method = 'Cash or ATM'
        notes= request.POST.get('node', '')
        print(customer,amount_received,payment_date,payment_method,notes)

        if customer and amount_received and payment_date and payment_method and notes:
            # Get the MilkCenter instance
            try:
                milk_center = Customer.objects.get(name=customer)
            except Customer.DoesNotExist:
                milk_center = None

            if milk_center:
                # Create a MilkPurchase instance and save it
                ReceivedPayment(customer=milk_center,amount_received=amount_received,payment_date=payment_date,payment_method=payment_method,notes=notes).save()
                print("Saved")
                # purchase=MilkPurchase.objects.filter(purchase_date=today)
                return redirect('/make_payment/')
                # Redirect to a success page or do something else
                # return redirect('success_page')  # Replace 'success_page' with your actual success page URL
            else:
                # Handle the case where the MilkCenter with the given name doesn't exist
                error_message = "Milk Center not found."
                print("Milk Center not found.")
        else:
            # Handle the case where some fields are missing
            error_message = "Please fill in all fields."
            print("Please fill in all fields")



        

    # Your view logic here
    return render(request, 'manager/recive_payment.html',{"customers":customers})

def manager_dashbord (request):
    from datetime import date
    today = date.today()
    from datetime import datetime
    customers=Customer.objects.all().count()
    centers=MilkCenter.objects.all().count()
    total_volume = MilkPurchase.objects.filter(purchase_date=today).aggregate(Sum('volume'))['volume__sum']
    total_price = MilkPurchase.objects.filter(purchase_date=today).aggregate(Sum('total_price'))['total_price__sum']
    sale_volume= MilkSale.objects.filter(purchase_date=today).aggregate(Sum('volume'))['volume__sum']
    sale_price=MilkSale.objects.filter(purchase_date=today).aggregate(Sum('total_price'))['total_price__sum']
    storage=Stor.objects.get(id=1)
    if request.method == 'POST':
        selected_date=request.POST.get('date', '')
        # Parse the selected_date string to a datetime object
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
        today=selected_date
        # Query the database to get the total volume and total price for the selected date
        total_volume = MilkPurchase.objects.filter(purchase_date=selected_date).aggregate(Sum('volume'))['volume__sum']
        total_price = MilkPurchase.objects.filter(purchase_date=selected_date).aggregate(Sum('total_price'))['total_price__sum']
        sale_volume= MilkSale.objects.filter(purchase_date=selected_date).aggregate(Sum('volume'))['volume__sum']
        sale_price=MilkSale.objects.filter(purchase_date=selected_date).aggregate(Sum('total_price'))['total_price__sum']


    # Your view logic here
    context={
        'today':today,
        "sale_price":sale_price,
        "sale_volume":sale_volume,
        'customers':customers,
        "centers":centers,
        'storage':storage,
        'total_volume': total_volume,
            'total_price': total_price,

    }
    return render(request, 'manager/manager_content.html',context)

def customer_details (request):
    customers=Customer.objects.all()
    # Your view logic here
    return render(request, 'manager/customer_details.html',{'customers':customers})

def center_details (request):
    centers=MilkCenter.objects.all()
    # Your view logic here
    return render(request, 'manager/center_details.html',{'centers':centers})

def view_center(request, pid):
    # Get the customer based on the provided username
    customer = get_object_or_404(MilkCenter, id=pid)

    # Filter MilkPurchase and MakePayment records for the specific customer
    # Filter MilkPurchase records for the specific customer based on username
    milk_purchases = MilkPurchase.objects.filter(milk_center__id=pid)

    # Filter MakePayment records for the specific customer based on username
    payments = MakePayment.objects.filter(milk_center__id=pid)

    # Add a field to each query to identify the source (MilkPurchase or MakePayment)
    milk_purchases = milk_purchases.annotate(source=models.Value('MilkPurchase', output_field=models.CharField()))
    payments = payments.annotate(source=models.Value('MakePayment', output_field=models.CharField()))

    # Combine and order the two querysets by datetime
    combined_data = list(milk_purchases) + list(payments)
    combined_data.sort(key=lambda x: x.purchase_date if x.source == 'MilkPurchase' else x.payment_date)

    # Calculate the balance
    balance = 0
    for entry in combined_data:
        if entry.source == 'MilkPurchase':
            balance += entry.total_price
        else:
            balance -= entry.amount

        # Add a 'balance' attribute to each entry
        entry.balance = balance

    context = {
        'pid':pid,
        'combined_data': combined_data,
        'customer': customer,  # Pass the customer object to the template
    }

    return render(request, 'manager/view_center.html', context)


def view_customer(request, pid):
    # Get the customer based on the provided username
    customer = get_object_or_404(Customer, id=pid)

    # Filter MilkPurchase and MakePayment records for the specific customer
    # Filter MilkPurchase records for the specific customer based on username
    milk_sale = MilkSale.objects.filter(customer__id=pid)

    # Filter MakePayment records for the specific customer based on username
    payments = ReceivedPayment.objects.filter(customer__id=pid)

    expences = CustomerExpence.objects.filter(customer__id=pid)

    # Add a field to each query to identify the source (MilkPurchase or MakePayment)
    milk_sale = milk_sale.annotate(source=models.Value('MilkPurchase', output_field=models.CharField()))
    expences = expences.annotate(source=models.Value('Expences', output_field=models.CharField()))
    payments = payments.annotate(source=models.Value('MakePayment', output_field=models.CharField()))
    

    # Combine and order the two querysets by datetime
    combined_data = list(milk_sale)+ list(expences) + list(payments) 
    # combined_data.sort(key=lambda x: x.purchase_date if x.source == 'MilkPurchase' else x.payment_date)
    def get_record_date(record):
        if record.source == 'MilkPurchase':
            return record.purchase_date
        elif record.source == 'MakePayment':
            return record.payment_date
        elif record.source == 'Expences':
            return record.date  # Assuming there is an 'expense_date' field in the Expenses model

# Sort the combined_data list based on the date using the get_record_date function
    combined_data.sort(key=get_record_date)

    # Calculate the balance
    balance = 0
    for entry in combined_data:
        if entry.source == 'MilkPurchase':
            balance += entry.total_price
        elif entry.source=='Expences':
            balance+=entry.expence_amount
        else:
            balance -= entry.amount_received

        # Add a 'balance' attribute to each entry
        entry.balance = balance

    context = {
        'pid':pid,
        'combined_data': combined_data,
        'customer': customer,  # Pass the customer object to the template
    }

    return render(request, 'manager/view_customer.html', context)
   

def register_customer_ex (request):
    if request.method=='POST':
        expence_name=request.POST.get('expence_name', '')

        Expence(expence_name=expence_name).save()
        print("expence saved")

    # Your view logic here
    return render(request, 'manager/register_customer_ex.html')


def add_customer_ex (request):
    expences=Expence.objects.all()
    customers=Customer.objects.all()
    print(customers)

    if request.method=='POST':
        date=request.POST.get('date', '')
        customer_name=request.POST.get('customer_name', '')
        expence_type=request.POST.get('expence_type', '')
        expence_amount=request.POST.get('expence_amount', '')


        name = Customer.objects.get(name=customer_name)
        CustomerExpence(customer=name,date=date,expence_type=expence_type,expence_amount=expence_amount).save()
        print("expence saved")

    context={
        'expences':expences,
        'customers':customers
    }
    # Your view logic here
    return render(request, 'manager/add_customer_ex.html',context)




from decimal import Decimal  # Import Decimal

from django.db.models import Sum
from datetime import date, datetime


def PNL(request):
    # Get the current date
    today = date.today()

    # Initialize selected_date to None
    selected_date = None

    # Process form input if the request method is POST
    if request.method == 'POST':
        selected_date_str = request.POST.get('date', '')
        try:
            # Parse the selected_date string to a datetime object
            selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d')
        except ValueError:
            # Handle invalid date format gracefully
            selected_date = None

    # If selected_date is still None, default it to today
    if selected_date is None:
        selected_date = today

    # Query the database to get total volume and total price for purchases and sales
    total_volume_purchase = MilkPurchase.objects.filter(purchase_date=selected_date).aggregate(Sum('volume'))['volume__sum'] or 0

    # Convert total_price_purchase to a Decimal if it's a string
    total_price_purchase = Decimal(MilkPurchase.objects.filter(purchase_date=selected_date).aggregate(Sum('total_price'))['total_price__sum'] or 0)
    formatted_total_price_purchase = "{:.2f}".format(total_price_purchase)

    total_volume_sale = MilkSale.objects.filter(purchase_date=selected_date).aggregate(Sum('volume'))['volume__sum'] or 0

    # Convert total_price_sale to a Decimal if it's a string
    total_price_sale = Decimal(MilkSale.objects.filter(purchase_date=selected_date).aggregate(Sum('total_price'))['total_price__sum'] or 0)
    formatted_total_price_sale = "{:.2f}".format(total_price_sale)
    # Calculate remaining milk, average price, estimated price, and other metrics
    remaining_milk = total_volume_purchase - total_volume_sale
    average_price = int(total_price_purchase / total_volume_purchase if total_volume_purchase != 0 else Decimal('0'))
    # average_price = "{:.2f}".format(average_price)
    estimated_price = remaining_milk * average_price
    total_purchase_price = total_price_purchase
    total_purchase_price = round(total_purchase_price, 2)
    total_expense = 0  # Adjust this if you have expenses to consider
    total_sale_price = total_price_sale + estimated_price
    profit = total_sale_price - total_purchase_price - total_expense
    profit = round(profit, 2)

    # Prepare the context dictionary
    context = {
        'today': today,
        'selected_date': selected_date,
        'remaining_milk': remaining_milk,
        'average_price': average_price,
        'estimated_price': estimated_price,
        'total_purchase_price': total_purchase_price,
        'total_expense': total_expense,
        'total_sale_price': total_sale_price,
        'profit': profit,
        'total_volume_purchase': total_volume_purchase,
        'total_price_purchase': formatted_total_price_purchase,
        'total_volume_sale': total_volume_sale,
        'total_price_sale': formatted_total_price_sale,
    }

    # Render the HTML template and return it as an HTTP response
    return render(request, 'manager/PNL.html', context)




from datetime import datetime
from decimal import Decimal


def BetweenPNL(request):
    # Initialize default values for variables
    total_volume_purchase = 0
    total_price_purchase = 0
    total_volume_sale = 0
    total_price_sale = 0

    # Set a default value for total_price_sale
    total_price_sale = 0

    # Process form input if the request method is POST
    if request.method == 'POST':
        selecting_date = request.POST.get('selecting_date', '')
        ending_date = request.POST.get('ending_date', '')
        print(selecting_date)
        print("111")
        
        
        # Parse the selected_date and ending_date strings to datetime objects
        selecting_date = datetime.strptime(selecting_date, '%Y-%m-%d')
        ending_date = datetime.strptime(ending_date, '%Y-%m-%d')

        # Query the database to get total volume and total price for purchases and sales
        purchase_query = MilkPurchase.objects.filter(purchase_date__range=[selecting_date, ending_date])
        sale_query = MilkSale.objects.filter(purchase_date__range=[selecting_date, ending_date])

        total_volume_purchase = purchase_query.aggregate(Sum('volume'))['volume__sum'] or 0
        print(total_volume_purchase)
        total_volume_sale = sale_query.aggregate(Sum('volume'))['volume__sum'] or 0
        print(total_volume_sale)
        # Convert total_price_purchase and total_price_sale to Decimals if they're strings
        total_price_purchase = Decimal(purchase_query.aggregate(Sum('total_price'))['total_price__sum'] or 0)
        total_price_sale = Decimal(sale_query.aggregate(Sum('total_price'))['total_price__sum'] or 0)

        # total_price_purchase = "{:.2f}".format(total_price_purchase)
        # total_price_sale = "{:.2f}".format(total_price_sale)
        print("total_price_purchase")

        

    # Calculate remaining milk, average price, estimated price, and other metrics
    remaining_milk = total_volume_purchase - total_volume_sale
    average_price = int(total_price_purchase / total_volume_purchase) if total_volume_purchase != 0 else Decimal('0')
    estimated_price = remaining_milk * average_price
    total_purchase_price = total_price_purchase 
    total_expense = 0  # Adjust this if you have expenses to consider
    total_sale_price = total_price_sale + estimated_price
    profit = round(total_sale_price - total_purchase_price - total_expense, 2)

    # Prepare the context dictionary
    context = {
        'remaining_milk': remaining_milk,
        'average_price': average_price,
        'estimated_price': estimated_price,
        'total_purchase_price': total_purchase_price,
        'total_expense': total_expense,
        'total_sale_price': total_sale_price,
        'profit': profit,
        'total_volume_purchase': total_volume_purchase,
        'total_price_purchase': total_price_purchase,
        'total_volume_sale': total_volume_sale,
        'total_price_sale': total_price_sale,
    }

    # Render the HTML template and return it as an HTTP response
    return render(request, 'manager/BetweenPNL.html', context)

