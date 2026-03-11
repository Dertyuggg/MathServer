# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
bill.html

<html>
<head>
<title>GST Bill Calculator</title>

<style>

body{
margin:0;
background:black;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}

.container{
background:white;
padding:35px;
width:320px;
border-radius:10px;
text-align:center;
}

h2{
margin-bottom:20px;
}

label{
display:block;
margin-top:10px;
}

input{
width:90%;
padding:8px;
margin-top:5px;
}

button{
margin-top:20px;
padding:10px 20px;
background:blue;
color:white;
border:none;
border-radius:5px;
cursor:pointer;
}

.result{
margin-top:20px;
font-weight:bold;
color:black;
}

</style>

</head>

<body>

<div class="container">

<h2>GST Bill Calculator</h2>

<form method="post">
{% csrf_token %}

<label>Price (₹)</label>
<input type="number" name="price" required>

<label>GST (%)</label>
<input type="number" name="gst" required>

<button type="submit">Calculate</button>

</form>

{% if total %}
<div class="result">
Total Bill Amount: ₹{{ total }}
</div>
{% endif %}

</div>

</body>
</html>

views.py
from django.shortcuts import render

def bill(request):
    total = None

    if request.method == "POST":
        price = float(request.POST.get("price"))
        gst = float(request.POST.get("gst"))

        total = price + (price * gst / 100)

    return render(request, "bill.html", {"total": total})

urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill, name='bill'),
]
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (34).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (33).png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
