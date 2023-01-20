from django import forms




class Matriz2(forms.Form):
    CHOICES = [
        ('l0c0', ''),
        ('l0c1', ''),
        ('l0c2', ''),
        ('l0c3', ''),
        ('l0c4', ''),
        ('l0c5', ''),
        ('l1c0', ''),
        ('l1c1', ''),
        ('l1c2', ''),
        ('l1c3', ''),
        ('l1c4', ''),
        ('l1c5', ''),
        ('l2c0', ''),
        ('l2c1', ''),
        ('l2c2', ''),
        ('l2c3', ''),
        ('l2c4', ''),
        ('l2c5', ''),
        ('l3c0', ''),
        ('l3c1', ''),
        ('l3c2', ''),
        ('l3c3', ''),
        ('l3c4', ''),
        ('l3c5', ''),
        ('l4c0', ''),
        ('l4c1', ''),
        ('l4c2', ''),
        ('l4c3', ''),
        ('l4c4', ''),
        ('l4c5', ''),
        ('l5c0', ''),
        ('l5c1', ''),
        ('l5c2', ''),
        ('l5c3', ''),
        ('l5c4', ''),
        ('l5c5', ''),

    ]
    object = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
