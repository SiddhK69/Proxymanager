from django import forms

from home.models import *





class AddData_PRX(forms.ModelForm):
    class Meta:
        model = Data_PRX
        fields = ("Teacher","Acronym")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            'Acronym':forms.TextInput(attrs={'class':'form-control','placeholder':'Acronym'}),
        }


# Proxy Placing Forms
class place_PRX1(forms.ModelForm):
    class Meta:
        model = Psub1
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    
    
class place_PRX2(forms.ModelForm):
    class Meta:
        model = Psub2
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    
class place_PRX3(forms.ModelForm):
    class Meta:
        model = Psub3
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
        
    

class place_PRX4(forms.ModelForm):
    class Meta:
        model = Psub4
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    

class place_PRX5(forms.ModelForm):
    class Meta:
        model = Psub5
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }


class place_PRX6(forms.ModelForm):
    class Meta:
        model = Psub6
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    

class place_PRX7(forms.ModelForm):
    class Meta:
        model = Psub7
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    

class place_PRX8(forms.ModelForm):
    class Meta:
        model = Psub8
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    

class place_PRX9(forms.ModelForm):
    class Meta:
        model = Psub9
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    

class place_PRX10(forms.ModelForm):
    class Meta:
        model = Psub10
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    

class place_PRX11(forms.ModelForm):
    class Meta:
        model = Psub11
        fields = ("FIRST_proxy","SECOND_proxy","THIRD_proxy","FOURTH_proxy","FIFTH_proxy","SIXTH_proxy","SEVENTH_proxy","EIGHTH_proxy","NINETH_proxy")
        widgets = {
            'FIRST_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SECOND_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'THIRD_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FOURTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'FIFTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SIXTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'SEVENTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'EIGHTH_proxy':forms.TextInput(attrs={'class':'form-control'}),
            'NINETH_proxy':forms.TextInput(attrs={'class':'form-control'}),
                }
    


# Confirmation Proxy Forms
class ConfirmData_PRX1(forms.ModelForm):
    class Meta:
        model = Psub1
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            "Teacher":forms.TextInput(attrs={"class":"form-control",'placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX2(forms.ModelForm):
    class Meta:
        model = Psub2
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }
        

class ConfirmData_PRX3(forms.ModelForm):
    class Meta:
        model = Psub3
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX4(forms.ModelForm):
    class Meta:
        model = Psub4
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX5(forms.ModelForm):
    class Meta:
        model = Psub5
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX6(forms.ModelForm):
    class Meta:
        model = Psub6
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX7(forms.ModelForm):
    class Meta:
        model = Psub7
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX8(forms.ModelForm):
    class Meta:
        model = Psub8
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX9(forms.ModelForm):
    class Meta:
        model = Psub9
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX10(forms.ModelForm):
    class Meta:
        model = Psub10
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }

class ConfirmData_PRX11(forms.ModelForm):
    class Meta:
        model = Psub11
        fields = ("Teacher","FIRST_period","SECOND_period","THIRD_period","FOURTH_period","FIFTH_period","SIXTH_period","SEVENTH_period","EIGHTH_period","NINETH_period")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            "FIRST_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'First Period'}),
            "SECOND_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Second Period'}),
            "THIRD_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Third Period'}),
            "FOURTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fourth Period'}),
            "FIFTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Fifth Period'}),
            "SIXTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Sixth Period'}),
            "SEVENTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Seventh Period'}),
            "EIGHTH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Eighth Period'}),
            "NINETH_period":forms.TextInput(attrs={"class":"form-control",'placeholder':'Nineth Period'}),
        }


class EditData_PRX(forms.ModelForm):
    class Meta:
        model = Data_PRX
        fields = ("Teacher",)
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
        }

class AddTimeTable(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ("Teacher","Acronym")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            'Acronym':forms.TextInput(attrs={'class':'form-control','placeholder':'Acronym'}),
        }


class EditTimeTable(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ("Teacher",)
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
        }

class Add_stats(forms.ModelForm):
    class Meta:
        model = stats
        fields = ("Teacher","Acronym")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            'Acronym':forms.TextInput(attrs={'class':'form-control','placeholder':'Acronym'}),
        }

class EditStats(forms.ModelForm):
    class Meta:
        model = stats
        fields = ("Teacher","Proxy")
        widgets = {
            'Teacher':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher'}),
            'Proxy':forms.TextInput(attrs={'class':'form-control','placeholder':'Proxy Count'}),
        }