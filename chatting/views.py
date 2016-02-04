from django.shortcuts import render, redirect, get_object_or_404, render_to_response, RequestContext
from django.http import HttpResponse
from .models import User, ChattingRoom
import templates 

# Create your views here.
def main_view(request):
	# 메인 화면 출력
	return render(request, 'main_view.html')

def login_check(request):
	# 아이디, 비밀번호 체크 뷰
	if 'username' in request.POST:
		if len(request.POST['username']) == 0:
			# 아무 글자도 입력 안되었을 때
			return HttpResponse('글자를 입력하세요.')
		else:
			username = request.POST['username']
	else: 
		return HttpResponse('False in Post')

	try:
		if User.objects.get(username=username):
			return HttpResponse('ID 중복')
	except:
		user = User(username=username)
		user.save()

	return redirect('/%s/chat/' %username)


def chat_view(request, username):

	chattingRoom = ChattingRoom.objects.all()

	return render(request, "chat_view.html", 
		{
			"username": username,
			"chattingRoom": chattingRoom,
		}
	)
	