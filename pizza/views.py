from django.shortcuts import render
from django.conf import settings
from .forms import PizzaForm,MultipleForm
from django.forms import formset_factory
from .models import Pizza


def home(request):

    return render(request,'home.html')
def order(request):
    multiple_form=MultipleForm()
    if (request.method=='POST') :
        filled_form=PizzaForm(request.POST)
        if(filled_form.is_valid()):
            created_pizza=filled_form.save()
            created_pizza_pk=created_pizza.id
            note='thanks for ordering pizza with us!your %s pizza with %s and %s is ready' %(
            filled_form.cleaned_data['size'],
            filled_form.cleaned_data['toppping1'],
            filled_form.cleaned_data['toppping2'],)

        return render(request,'order.html',{'created_pizza_pk':created_pizza_pk,'pizzaform':filled_form,'note':note,'multiple_form':multiple_form})


    else:
        given_form=PizzaForm()
        return render(request,'order.html',{'pizzaform':given_form,'multiple_form':multiple_form})
def pizzas(request):
    number_of_pizza=2
    filled_multiple_form=MultipleForm(request.GET)
    if filled_multiple_form.is_valid():
        number_of_pizza=filled_multiple_form.cleaned_data['number']
    PizzaFormSet=formset_factory(PizzaForm,extra=number_of_pizza)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_form_set=PizzaFormSet(request.POST)
        if(filled_form_set.is_valid()):
            for form in filled_form_set:
                note1="your multiple pizza have been ordered "
        else:
            note1="ordered not created"
        return render(request,'pizza.html',{'formset':formset,'note':note1})
    else:
        return render(request,'pizza.html',{'formset':formset})
def edit_order(request,pk):
    pizza=Pizza.objects.get(pk=pk)
    form=PizzaForm(instance=pizza)
    if request.method=='POST':
        filled_form=PizzaForm(request.POST,instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form=filled_form
            note="order has been edited"
            return render(request,'edit_order.html',{'note':note,'pizzaform':form,'pizza':pizza})
    return render(request,'edit_order.html',{'pizzaform':form,'pizza':pizza})
