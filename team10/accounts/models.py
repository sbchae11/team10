from django.db import models
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.signals import user_logged_in

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30, blank = True, default = '')
    email = models.EmailField()
    
    def save(self, *args, **kwargs):
        #닉네임이 비어있으면 사용자의 이름으로 채운다
        if not self.nickname:
            self.nickname = self.user.username
        super().save(*args, **kwargs)

class UserSession(models.Model): #중복 로그인 방지 위해 사용자의 세션 정보 저장
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

#중복 로그인 방지
def block_duplicate_login(sender, request, user, **kwargs): #사용자 로그인시 호출되는 함수
    login_user_list = UserSession.objects.filter(user=user)
    for user_session in login_user_list: #동일한 사용자에 대해 기존에 저장된 모든 세션 기록 찾아서 삭제
        session = SessionStore(user_session.session_key)
        # session.delete()
        session['blocked'] = True
        session.save()
        
    session_key = request.session.session_key #ㅐ로운 세션 기록 생성
    UserSession.objects.create(user=user, session_key = session_key) #UserSession기록에 추가
user_logged_in.connect(block_duplicate_login) #사용자가 로그인할 때마다 함수 호출되도록 user_logged_in 신호에 함수 연결