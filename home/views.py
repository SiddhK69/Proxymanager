import datetime
import pyautogui
from PIL import Image
import keyboard
import pytesseract as pyt
import pyperclip
import cv2
import xlwt

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView
from django.forms.models import model_to_dict
from django.http import HttpResponse

from home.forms import *
from home.models import *

from django.http import JsonResponse


# Create your views here.
def Index(request):
    PRX_data = Data_PRX.objects.all()
    TT_Data = TimeTable.objects.all()
    Sts_Data = stats.objects.all()
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'Design.html', {'PRX_Data': PRX_data, 'TT_Data': TT_Data, "Sts_Data": Sts_Data})


def Design_NA(request):
    PRX_Data = Data_PRX.objects.all()
    print(request.user)
    return render(request, 'Design_NA.html', {'PRXData': PRX_Data})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user.is_superuser:
            login(request, user)
            return redirect("/")
        elif user.is_authenticated:
            return redirect("user/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")


class Add_TimeTable(CreateView):
    def get(self, request):
        fm = AddTimeTable
        return render(request, 'Add_TT.html', {'form': fm})

    def post(self, request):
        fm = AddTimeTable(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'Add_TT.html', {'form': fm})


class Edit_TimeTable(UpdateView):
    def get(self, request, id):
        data = TimeTable.objects.get(Acronym=id)
        fm = EditTimeTable(instance=data)
        return render(request, 'Add_TT.html', {'form': fm})

    def post(self, request, id):
        data = TimeTable.objects.get(Acronym=id)
        fm = EditTimeTable(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'Add_TT.html', {'form': fm})


def delete_tt(request, id):

    data = TimeTable.objects.get(Acronym=id)
    data.delete()
    return redirect('/')


class Add_Data_PRX(CreateView):
    def get(self, request):
        fm = AddData_PRX
        return render(request, 'Add_PRX.html', {'form': fm})

    def post(self, request):
        fm = AddData_PRX(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/")
        else:
            return render(request, 'Add_PRX.html', {'form': fm})


def Confirm_PRX(request, id, pk):
    subTT_Data1 = Tsub1.objects.all()
    subTT_Data2 = Tsub2.objects.all()
    subTT_Data3 = Tsub3.objects.all()
    subTT_Data4 = Tsub4.objects.all()
    subTT_Data5 = Tsub5.objects.all()
    subTT_Data6 = Tsub6.objects.all()
    subTT_Data7 = Tsub7.objects.all()
    subTT_Data8 = Tsub8.objects.all()
    subTT_Data9 = Tsub9.objects.all()
    subTT_Data10 = Tsub10.objects.all()
    subTT_Data11 = Tsub11.objects.all()
    subTT_Data12 = Tsub12.objects.all()
    subTT_Data13 = Tsub13.objects.all()
    subTT_Data14 = Tsub14.objects.all()
    subTT_Data15 = Tsub15.objects.all()
    subTT_Data16 = Tsub16.objects.all()
    subTT_Data17 = Tsub17.objects.all()
    subTT_Data18 = Tsub18.objects.all()
    subTT_Data19 = Tsub19.objects.all()
    subTT_Data20 = Tsub20.objects.all()
    subTT_Data21 = Tsub21.objects.all()
    subTT_Data22 = Tsub22.objects.all()
    subTT_Data23 = Tsub23.objects.all()
    subTT_Data24 = Tsub24.objects.all()
    subTT_Data25 = Tsub25.objects.all()
    subTT_Data26 = Tsub26.objects.all()
    subTT_Data27 = Tsub27.objects.all()
    subTT_Data28 = Tsub28.objects.all()
    subTT_Data29 = Tsub29.objects.all()
    subTT_Data30 = Tsub30.objects.all()
    subTT_Data31 = Tsub31.objects.all()
    subTT_Data32 = Tsub32.objects.all()
    subTT_Data33 = Tsub33.objects.all()
    subTT_Data34 = Tsub34.objects.all()
    subTT_Data35 = Tsub35.objects.all()
    subTT_Data36 = Tsub36.objects.all()
    subTT_Data37 = Tsub37.objects.all()
    subTT_Data38 = Tsub38.objects.all()
    subTT_Data39 = Tsub39.objects.all()
    subTT_Data40 = Tsub40.objects.all()
    subTT_Data41 = Tsub41.objects.all()
    subTT_Data42 = Tsub42.objects.all()
    subTT_Data43 = Tsub43.objects.all()
    subTT_Data44 = Tsub44.objects.all()
    subTT_Data45 = Tsub45.objects.all()
    subTT_Data46 = Tsub46.objects.all()
    subTT_Data47 = Tsub47.objects.all()
    subTT_Data48 = Tsub48.objects.all()
    subTT_Data49 = Tsub49.objects.all()
    subTT_Data50 = Tsub50.objects.all()


    if id == 1:
        form = ConfirmData_PRX1(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 2:
        form = ConfirmData_PRX2(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 3:
        form = ConfirmData_PRX3(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 4:
        form = ConfirmData_PRX4(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 5:
        form = ConfirmData_PRX5(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 6:
        form = ConfirmData_PRX6(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 7:
        form = ConfirmData_PRX7(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 8:
        form = ConfirmData_PRX8(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 9:
        form = ConfirmData_PRX9(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 10:
        form = ConfirmData_PRX10(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    elif id == 11:
        form = ConfirmData_PRX11(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(f'show_prx/{id}/{pk}')
            else:
                return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
        return render(request, 'Confirm_PRX.html', {'form':form, 'subTT_Data1':subTT_Data1 ,'subTT_Data2':subTT_Data2 ,'subTT_Data3':subTT_Data3 ,'subTT_Data4':subTT_Data4 ,'subTT_Data5':subTT_Data5 ,'subTT_Data6':subTT_Data6 ,'subTT_Data7':subTT_Data7 ,'subTT_Data8':subTT_Data8 ,'subTT_Data9':subTT_Data9 ,'subTT_Data10':subTT_Data10 ,'subTT_Data11':subTT_Data11 ,'subTT_Data12':subTT_Data12 ,'subTT_Data13':subTT_Data13 ,'subTT_Data14':subTT_Data14 ,'subTT_Data15':subTT_Data15 ,'subTT_Data16':subTT_Data16 ,'subTT_Data17':subTT_Data17 ,'subTT_Data18':subTT_Data18 ,'subTT_Data19':subTT_Data19 ,'subTT_Data20':subTT_Data20 ,'subTT_Data21':subTT_Data21 ,'subTT_Data22':subTT_Data22 ,'subTT_Data23':subTT_Data23 ,'subTT_Data24':subTT_Data24 ,'subTT_Data25':subTT_Data25 ,'subTT_Data26':subTT_Data26 ,'subTT_Data27':subTT_Data27 ,'subTT_Data28':subTT_Data28 ,'subTT_Data29':subTT_Data29 ,'subTT_Data30':subTT_Data30 ,'subTT_Data31':subTT_Data31 ,'subTT_Data32':subTT_Data32 ,'subTT_Data33':subTT_Data33 ,'subTT_Data34':subTT_Data34 ,'subTT_Data35':subTT_Data35 ,'subTT_Data36':subTT_Data36 ,'subTT_Data37':subTT_Data37 ,'subTT_Data38':subTT_Data38 ,'subTT_Data39':subTT_Data39 ,'subTT_Data40':subTT_Data40 ,'subTT_Data41':subTT_Data41 ,'subTT_Data42':subTT_Data42 ,'subTT_Data43':subTT_Data43 ,'subTT_Data44':subTT_Data44 ,'subTT_Data45':subTT_Data45 ,'subTT_Data46':subTT_Data46 ,'subTT_Data47':subTT_Data47 ,'subTT_Data48':subTT_Data48 ,'subTT_Data49':subTT_Data49 ,'subTT_Data50':subTT_Data50})
    else:
        return redirect('/')


class Edit_Data_PRX(UpdateView):
    def get(self, request, pk):
        data = Data_PRX.objects.get(Acronym=id)
        fm = EditData_PRX(instance=data)
        return render(request, 'Add_PRX.html', {'form': fm})

    def post(self, request, pk):
        data = Data_PRX.objects.get(Acronym=id)
        fm = EditData_PRX(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'Add_PRX.html', {'form': fm})


def Place_PRX(request, pk, id):


# render
    if id == 1:
        data = Psub1.objects.get(Teacher=pk)
        subPRX_Data1 = Psub1.objects.all()
        form = place_PRX1(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data1':subPRX_Data1})
    elif id == 2:
        data = Psub2.objects.get(Teacher=pk)
        subPRX_Data2 = Psub2.objects.all()
        form = place_PRX2(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data2':subPRX_Data2})
    elif id == 3:
        data = Psub3.objects.get(Teacher=pk)
        subPRX_Data3 = Psub3.objects.all()
        form = place_PRX3(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data3':subPRX_Data3})
    elif id == 4:
        data = Psub4.objects.get(Teacher=pk)
        subPRX_Data4 = Psub4.objects.all()
        form = place_PRX4(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form,'subPRX_Data4':subPRX_Data4})
    elif id == 5:
        data = Psub5.objects.get(Teacher=pk)
        subPRX_Data5 = Psub5.objects.all()
        form = place_PRX5(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data5':subPRX_Data5})
    elif id == 6:
        data = Psub6.objects.get(Teacher=pk)
        subPRX_Data6 = Psub6.objects.all()
        form = place_PRX6(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data6':subPRX_Data6})
    elif id == 7:
        data = Psub7.objects.get(Teacher=pk)
        subPRX_Data7 = Psub7.objects.all()
        form = place_PRX7(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data7':subPRX_Data7})
    elif id == 8:
        data = Psub8.objects.get(Teacher=pk)
        subPRX_Data8 = Psub8.objects.all()
        form = place_PRX8(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data8':subPRX_Data8})
    elif id == 9:
        data = Psub9.objects.get(Teacher=pk)
        subPRX_Data9 = Psub9.objects.all()
        form = place_PRX9(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data9':subPRX_Data9})
    elif id == 10:
        data = Psub10.objects.get(Teacher=pk)
        subPRX_Data10 = Psub10.objects.all()
        form = place_PRX10(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data10':subPRX_Data10})
    elif id == 11:
        data = Psub11.objects.get(Teacher=pk)
        subPRX_Data11 = Psub11.objects.all()
        form = place_PRX11(request.POST, instance=data)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data
                try:
                    value_1 = stats.objects.get(Acronym=name['FIRST_proxy'])
                    value_1.Proxy += 1
                    value_1.save()
                except:
                    pass

                try:
                    value_2 = stats.objects.get(Acronym=name['SECOND_proxy'])
                    value_2.Proxy += 1
                    value_2.save()
                except:
                    pass

                try:
                    value_3 = stats.objects.get(Acronym=name['THIRD_proxy'])
                    value_3.Proxy += 1
                    value_3.save()
                except:
                    pass

                try:
                    value_4 = stats.objects.get(Acronym=name['FOURTH_proxy'])
                    value_4.Proxy += 1
                    value_4.save()
                except:
                    pass

                try:
                    value_5 = stats.objects.get(Acronym=name['FIFTH_proxy'])
                    value_5.Proxy += 1
                    value_5.save()
                except:
                    pass

                try:
                    value_6 = stats.objects.get(Acronym=name['SIXTH_proxy'])
                    value_6.Proxy += 1
                    value_6.save()
                except:
                    pass

                try:
                    value_7 = stats.objects.get(Acronym=name['SEVENTH_proxy'])
                    value_7.Proxy += 1
                    value_7.save()
                except:
                    pass

                try:
                    value_8 = stats.objects.get(Acronym=name['EIGHTH_proxy'])
                    value_8.Proxy += 1
                    value_8.save()
                except:
                    pass

                try:
                    value_9 = stats.objects.get(Acronym=name['NINETH_proxy'])
                    value_9.Proxy += 1
                    value_9.save()
                except:
                    pass

                form.save()
                return redirect('/')
        return render(request, 'Place_PRX.html', {'form': form, 'subPRX_Data11':subPRX_Data11})


def delete_prx(request, pk):
    data = Data_PRX.objects.get(Acronym=pk)
    data.delete()
    return redirect('/')


def get_proxys(request, idx ,id, pk):
    if id == 1:
        subPRX_Data1 = Psub1.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data1': subPRX_Data1})
    elif id == 2:
        subPRX_Data2 = Psub2.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data2': subPRX_Data2})
    elif id == 3:
        subPRX_Data3 = Psub3.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data3': subPRX_Data3})
    elif id == 4:
        subPRX_Data4 = Psub4.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data4': subPRX_Data4})
    elif id == 5:
        subPRX_Data5 = Psub5.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data5': subPRX_Data5})
    elif id == 6:
        subPRX_Data6 = Psub6.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data6': subPRX_Data6})
    elif id == 7:
        subPRX_Data7 = Psub7.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data7': subPRX_Data7})
    elif id == 8:
        subPRX_Data8 = Psub8.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data8': subPRX_Data8})
    elif id == 9:
        subPRX_Data9 = Psub9.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data9': subPRX_Data9})
    elif id == 10:
        subPRX_Data10 = Psub10.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data10': subPRX_Data10})
    elif id == 11:
        subPRX_Data11 = Psub11.objects.all()
        return render(request, 'Show_PRX.html', {'subPRX_Data11': subPRX_Data11})
    else:
        return redirect('/')


def get_subs(request, id):
    TabId = TimeTable.Table_Id = id
    if TabId =='1':
        subTT_Data1 = Tsub1.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data1':subTT_Data1})
    elif TabId =='2':
        subTT_Data2 = Tsub2.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data2':subTT_Data2})
    elif TabId =='3':    
        subTT_Data3 = Tsub3.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data3':subTT_Data3})
    elif TabId =='4':
        subTT_Data4 = Tsub4.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data4':subTT_Data4})
    elif TabId =='5':    
        subTT_Data5 = Tsub5.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data5':subTT_Data5})
    elif TabId =='6':
        subTT_Data6 = Tsub6.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data6':subTT_Data6})     
    elif TabId =='7':
        subTT_Data7 = Tsub7.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data7':subTT_Data7})
    elif TabId =='8':
        subTT_Data8 = Tsub8.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data8':subTT_Data8})
    elif TabId =='9':
        subTT_Data9 = Tsub9.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data9':subTT_Data9})
    elif TabId == '10':
        subTT_Data10 = Tsub10.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data10':subTT_Data10})
    elif TabId == '11':
        subTT_Data11 = Tsub11.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data11':subTT_Data11})     
    elif TabId == '12':
        subTT_Data12 = Tsub12.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data12':subTT_Data12})
    elif TabId == '13':
        subTT_Data13 = Tsub13.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data13':subTT_Data13})
    elif TabId == '14':
        subTT_Data14 = Tsub14.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data14':subTT_Data14})
    elif TabId == '15':
        subTT_Data15 = Tsub15.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data15':subTT_Data15})
    elif TabId == '16':
        subTT_Data16 = Tsub16.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data16':subTT_Data16})     
    elif TabId == '17':
        subTT_Data17 = Tsub17.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data17':subTT_Data17})
    elif TabId == '18':
        subTT_Data18 = Tsub18.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data18':subTT_Data18})
    elif TabId == '19':
        subTT_Data19 = Tsub19.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data19':subTT_Data19})
    elif TabId == '20':
        subTT_Data20 = Tsub20.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data20':subTT_Data20})
    elif TabId == '21':
        subTT_Data21 = Tsub21.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data21':subTT_Data21})     
    elif TabId == '22':
        subTT_Data22 = Tsub22.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data22':subTT_Data22})
    elif TabId == '23':
        subTT_Data23 = Tsub23.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data23':subTT_Data23})
    elif TabId == '24':
        subTT_Data24 = Tsub24.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data24':subTT_Data24})
    elif TabId == '25':
        subTT_Data25 = Tsub25.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data25':subTT_Data25})
    elif TabId == '26':
        subTT_Data26 = Tsub26.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data26':subTT_Data26})     
    elif TabId == '27':
        subTT_Data27 = Tsub27.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data27':subTT_Data27})
    elif TabId == '28':
        subTT_Data28 = Tsub28.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data28':subTT_Data28})
    elif TabId == '29':
        subTT_Data29 = Tsub29.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data29':subTT_Data29})
    elif TabId == '30':
        subTT_Data30 = Tsub30.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data30':subTT_Data30})
    elif TabId == '31':
        subTT_Data31 = Tsub31.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data31':subTT_Data31})     
    elif TabId == '32':
        subTT_Data32 = Tsub32.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data32':subTT_Data32})
    elif TabId == '33':
        subTT_Data33 = Tsub33.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data33':subTT_Data33})
    elif TabId == '34':
        subTT_Data34 = Tsub34.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data34':subTT_Data34})
    elif TabId == '35':
        subTT_Data35 = Tsub35.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data35':subTT_Data35})
    elif TabId == '36':
        subTT_Data36 = Tsub36.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data36':subTT_Data36})     
    elif TabId == '37':
        subTT_Data37 = Tsub37.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data37':subTT_Data37})
    elif TabId == '38':
        subTT_Data38 = Tsub38.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data38':subTT_Data38})
    elif TabId == '39':
        subTT_Data39 = Tsub39.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data39':subTT_Data39})
    elif TabId == '40':
        subTT_Data40 = Tsub40.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data40':subTT_Data40})
    elif TabId == '41':
        subTT_Data41 = Tsub41.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data41':subTT_Data41})     
    elif TabId == '42':
        subTT_Data42 = Tsub42.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data42':subTT_Data42})
    elif TabId == '43':
        subTT_Data43 = Tsub43.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data43':subTT_Data43})
    elif TabId == '44':
        subTT_Data44 = Tsub44.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data44':subTT_Data44})
    elif TabId == '45':
        subTT_Data45 = Tsub45.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data45':subTT_Data45})
    elif TabId == '46':
        subTT_Data46 = Tsub46.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data46':subTT_Data46})     
    elif TabId == '47':
        subTT_Data47 = Tsub47.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data47':subTT_Data47})
    elif TabId == '48':
        subTT_Data48 = Tsub48.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data48':subTT_Data48})
    elif TabId == '49':
        subTT_Data49 = Tsub49.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data49':subTT_Data49})
    elif TabId == '50':
        subTT_Data50 = Tsub50.objects.all()
        return render (request, 'Show_TT.html', {'subTT_Data50':subTT_Data50})
    else:
        return render (request, 'Design.html')


def All_Proxy(request):
    subPRX_Data1 = Psub1.objects.all()
    subPRX_Data2 = Psub2.objects.all()
    subPRX_Data3 = Psub3.objects.all()
    subPRX_Data4 = Psub4.objects.all()
    subPRX_Data5 = Psub5.objects.all()
    subPRX_Data6 = Psub6.objects.all()
    subPRX_Data7 = Psub7.objects.all()
    subPRX_Data8 = Psub8.objects.all()
    subPRX_Data9 = Psub9.objects.all()
    subPRX_Data10 = Psub10.objects.all()
    subPRX_Data11 = Psub11.objects.all()

    a = Tsub1.objects.filter(ZERO=0).values_list('FIRST_period_1', flat=True)
    b = Tsub1.objects.filter(ZERO=0).values_list('Teacher')
    print(a , b)

    return render(request, 'Show_All_PRX.html', {'subPRX_Data1': subPRX_Data1, 'subPRX_Data2': subPRX_Data2, 'subPRX_Data3': subPRX_Data3, 'subPRX_Data4': subPRX_Data4, 'subPRX_Data5': subPRX_Data5, 'subPRX_Data6': subPRX_Data6, 'subPRX_Data7': subPRX_Data7, 'subPRX_Data8': subPRX_Data8, 'subPRX_Data9': subPRX_Data9, 'subPRX_Data10': subPRX_Data10, 'subPRX_Data11': subPRX_Data11})


class add_stats(CreateView):
    def get(self, request):
        form = Add_stats
        return render(request, 'Add_TT.html', {'form': form})

    def post(self, request):
        form = Add_stats(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'Add_TT.html', {'form': form})


class Edit_stats(UpdateView):
    def get(self, request, pk):
        data = stats.objects.get(Acronym=pk)
        fm = EditStats(instance=data)
        return render(request, 'Add_PRX.html', {'form': fm})

    def post(self, request, pk):
        data = stats.objects.get(Acronym=pk)
        fm = EditStats(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'Add_PRX.html', {'form': fm})


def delete_stats(request, pk):
    data = stats.objects.get(Acronym=pk)
    data.delete()
    return redirect('/')


def delete_prx_all(request):
    Data_PRX.objects.all().delete()
    return redirect('/')


def reset_stats(request):
    Data = stats.objects.all()
    Data.update(Proxy=0)
    return redirect('/')


def locate_image(request):
     
    pyt.pytesseract.tesseract_cmd = ("C:\\Users\\LAB-22\\Desktop\\pyt\\tesseract.exe")
    one = cv2.imread("TT_Img\\1.PNG")
    x1,y1 = pyautogui.locateCenterOnScreen(one)

    two = cv2.imread("TT_Img\\2.PNG")
    x2,y2 = pyautogui.locateCenterOnScreen(two)

    three = cv2.imread("TT_Img\\3.PNG")
    x3,y3 = pyautogui.locateCenterOnScreen(three)

    four = cv2.imread("TT_Img\\4.PNG")
    x4,y4 = pyautogui.locateCenterOnScreen(four)

    five = cv2.imread("TT_Img\\5.PNG")
    x5,y5 = pyautogui.locateCenterOnScreen(five)

    six = cv2.imread("TT_Img\\6.PNG")
    x6,y6 = pyautogui.locateCenterOnScreen(six)

    seven = cv2.imread("TT_Img\\7.PNG")
    x7,y1 = pyautogui.locateCenterOnScreen(seven)

    eight = cv2.imread("TT_Img\\8.PNG")
    x8,y2 = pyautogui.locateCenterOnScreen(eight)

    nine = cv2.imread("TT_Img\\9.PNG")
    x9,y3 = pyautogui.locateCenterOnScreen(nine)

    Today = datetime.date.today()
    if Today.isoweekday() == 1:

        imgT = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-120,y1-25,60,50))
        data = pyt.image_to_string(imgT)
        print(data)
        pyperclip.copy(data.upper())
        fx1,fy1 = pyautogui.locateCenterOnScreen("TimeTable_Form\\First_period.png")
        pyautogui.moveTo(fx1,fy1-77)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        img1 = cv2.imread("TT_Img\\Monday.PNG")
        x,y = pyautogui.locateCenterOnScreen(img1)
        print(x,y)

        imgp1 = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-65,y-40,130,100))

        img = cv2.imread("Detect_Imgt.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1-40,fy1)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp2 = pyautogui.screenshot('Detect_Img.PNG', region=(x2-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+78)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp3 = pyautogui.screenshot('Detect_Img.PNG', region=(x3-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+156)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp4 = pyautogui.screenshot('Detect_Img.PNG', region=(x4-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+234)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp5 = pyautogui.screenshot('Detect_Img.PNG', region=(x5-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+311)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp6 = pyautogui.screenshot('Detect_Img.PNG', region=(x6-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+388)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp7 = pyautogui.screenshot('Detect_Img.PNG', region=(x7-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+465)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp8 = pyautogui.screenshot('Detect_Img.PNG', region=(x8-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+542)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp9 = pyautogui.screenshot('Detect_Img.PNG', region=(x9-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+619)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
   
    elif Today.isoweekday() == 2:

        imgT = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-120,y1-25,60,50))
        data = pyt.image_to_string(imgT)
        print(data)
        pyperclip.copy(data.upper())
        fx1,fy1 = pyautogui.locateCenterOnScreen("TimeTable_Form\\First_period.png")
        pyautogui.moveTo(fx1,fy1-77)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        img2 = cv2.imread("TT_Img\\Tuesday.PNG")
        x,y = pyautogui.locateCenterOnScreen(img2)
        print(x,y)

        imgp1 = pyautogui.screenshot('Detect_Img.PNG', region=(x1-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1-40,fy1)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp2 = pyautogui.screenshot('Detect_Img.PNG', region=(x2-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+78)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp3 = pyautogui.screenshot('Detect_Img.PNG', region=(x3-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+156)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp4 = pyautogui.screenshot('Detect_Img.PNG', region=(x4-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+234)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp5 = pyautogui.screenshot('Detect_Img.PNG', region=(x5-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+311)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp6 = pyautogui.screenshot('Detect_Img.PNG', region=(x6-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+388)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp7 = pyautogui.screenshot('Detect_Img.PNG', region=(x7-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+465)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp8 = pyautogui.screenshot('Detect_Img.PNG', region=(x8-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+542)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp9 = pyautogui.screenshot('Detect_Img.PNG', region=(x9-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+619)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

    elif Today.isoweekday() == 3:

        imgT = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-120,y1-25,60,50))
        data = pyt.image_to_string(imgT)
        print(data)
        pyperclip.copy(data.upper())
        fx1,fy1 = pyautogui.locateCenterOnScreen("TimeTable_Form\\First_period.png")
        pyautogui.moveTo(fx1,fy1-77)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        img3 = cv2.imread("TT_Img\\Wednesday.PNG")
        x,y = pyautogui.locateCenterOnScreen(img3)
        print(x,y)

        imgp1 = pyautogui.screenshot('Detect_Img.PNG', region=(x1-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1-40,fy1)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp2 = pyautogui.screenshot('Detect_Img.PNG', region=(x2-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+78)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp3 = pyautogui.screenshot('Detect_Img.PNG', region=(x3-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+120)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp4 = pyautogui.screenshot('Detect_Img.PNG', region=(x4-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+184)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp5 = pyautogui.screenshot('Detect_Img.PNG', region=(x5-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+251)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp6 = pyautogui.screenshot('Detect_Img.PNG', region=(x6-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+328)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp7 = pyautogui.screenshot('Detect_Img.PNG', region=(x7-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+395)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp8 = pyautogui.screenshot('Detect_Img.PNG', region=(x8-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+482)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp9 = pyautogui.screenshot('Detect_Img.PNG', region=(x9-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+482)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

    elif Today.isoweekday() == 4:

        imgT = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-120,y1-25,60,50))
        data = pyt.image_to_string(imgT)
        print(data)
        pyperclip.copy(data.upper())
        fx1,fy1 = pyautogui.locateCenterOnScreen("TimeTable_Form\\First_period.png")
        pyautogui.moveTo(fx1,fy1-77)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        img4 = cv2.imread("TT_Img\\Thursday.PNG")
        x,y = pyautogui.locateCenterOnScreen(img4)
        print(x,y)

        imgp1 = pyautogui.screenshot('Detect_Img.PNG', region=(x1-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1-40,fy1)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp2 = pyautogui.screenshot('Detect_Img.PNG', region=(x2-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+78)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp3 = pyautogui.screenshot('Detect_Img.PNG', region=(x3-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+156)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp4 = pyautogui.screenshot('Detect_Img.PNG', region=(x4-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+234)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp5 = pyautogui.screenshot('Detect_Img.PNG', region=(x5-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+311)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp6 = pyautogui.screenshot('Detect_Img.PNG', region=(x6-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+388)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp7 = pyautogui.screenshot('Detect_Img.PNG', region=(x7-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+465)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp8 = pyautogui.screenshot('Detect_Img.PNG', region=(x8-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+542)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp9 = pyautogui.screenshot('Detect_Img.PNG', region=(x9-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+619)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

    elif Today.isoweekday() == 5:

        imgT = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-120,y1-25,60,50))
        data = pyt.image_to_string(imgT)
        print(data)
        pyperclip.copy(data.upper())
        fx1,fy1 = pyautogui.locateCenterOnScreen("TimeTable_Form\\First_period.png")
        pyautogui.moveTo(fx1,fy1-77)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        img5 = cv2.imread("TT_Img\\Friday.PNG")
        x,y = pyautogui.locateCenterOnScreen(img5)
        print(x,y)

        imgp1 = pyautogui.screenshot('Detect_Img.PNG', region=(x1-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1-40,fy1)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp2 = pyautogui.screenshot('Detect_Img.PNG', region=(x2-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+78)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp3 = pyautogui.screenshot('Detect_Img.PNG', region=(x3-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+156)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp4 = pyautogui.screenshot('Detect_Img.PNG', region=(x4-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+234)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp5 = pyautogui.screenshot('Detect_Img.PNG', region=(x5-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+311)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp6 = pyautogui.screenshot('Detect_Img.PNG', region=(x6-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+388)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp7 = pyautogui.screenshot('Detect_Img.PNG', region=(x7-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+465)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp8 = pyautogui.screenshot('Detect_Img.PNG', region=(x8-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+542)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp9 = pyautogui.screenshot('Detect_Img.PNG', region=(x9-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+619)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

    elif Today.isoweekday() == 6:

        imgT = pyautogui.screenshot('Detect_Imgt.PNG', region=(x1-120,y1-25,60,50))
        data = pyt.image_to_string(imgT)
        print(data)
        pyperclip.copy(data.upper())
        fx1,fy1 = pyautogui.locateCenterOnScreen("TimeTable_Form\\First_period.png")
        pyautogui.moveTo(fx1,fy1-77)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        img6 = cv2.imread("TT_Img\\Saturday.PNG")
        x,y = pyautogui.locateCenterOnScreen(img6)
        print(x,y)

        imgp1 = pyautogui.screenshot('Detect_Img.PNG', region=(x1-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1-40,fy1)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp2 = pyautogui.screenshot('Detect_Img.PNG', region=(x2-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+78)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp3 = pyautogui.screenshot('Detect_Img.PNG', region=(x3-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+156)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

        imgp4 = pyautogui.screenshot('Detect_Img.PNG', region=(x4-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+234)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp5 = pyautogui.screenshot('Detect_Img.PNG', region=(x5-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+311)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp6 = pyautogui.screenshot('Detect_Img.PNG', region=(x6-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+388)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp7 = pyautogui.screenshot('Detect_Img.PNG', region=(x7-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+465)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp8 = pyautogui.screenshot('Detect_Img.PNG', region=(x8-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+542)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')
        
        imgp9 = pyautogui.screenshot('Detect_Img.PNG', region=(x9-65,y-40,130,100))

        img = cv2.imread("Detect_Img.png")

        data = pyt.image_to_string(img)
        print(data)
        pyperclip.copy(data.upper())
        pyautogui.moveTo(fx1,fy1+619)
        pyautogui.leftClick()
        keyboard.press_and_release('Ctrl + v')

    else:
        return redirect('/')


def download_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Statistics' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Statistics')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Teacher', 'Acronym', 'Proxy Count']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = stats.objects.filter().values_list('Teacher', 'Acronym', 'Proxy')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response) 

    return response   

