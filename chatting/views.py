from django.shortcuts import render
import templates 

# Create your views here.
def main_view(request):
	# 메인 화면 출력
	return render(request, 'main_view.html')