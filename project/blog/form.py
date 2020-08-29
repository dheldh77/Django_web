from django import forms
from .models import Patient

# form 형식을 지정해주는 클래스
class PatientForm(forms.ModelForm):
    # form 형식을 지정할 클래스의 메타데이터
    class Meta:
        # form 형식을 지정해줄 클래스를 Model에서 가져온다.
        model = Patient
        # 지정해줄 필드명을 리스트에 명시한다.
        fields = ['name', 'age', 'height', 'weight', 'blood', 'description']