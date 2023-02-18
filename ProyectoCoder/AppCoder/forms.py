from django import forms

class AddProduct(forms.Form):
 title = forms.CharField()
 code = forms.IntegerField()
 stock = forms.IntegerField()
 price = forms.IntegerField()



class AddStores(forms.Form):
    name = forms.IntegerField()
    phone= forms.CharField(max_length=40)
    address = forms.CharField(max_length=40)
    online = forms.BooleanField()


class AddOrder(forms.Form):
    number = forms.IntegerField()
    products = forms.CharField(max_length=40)
    address = forms.CharField(max_length=40)



class FindProduct(forms.Form):
 title = forms.CharField()
 