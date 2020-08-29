from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Photo, Patient
from django.utils import timezone
from django.core.paginator import Paginator
from .form import PatientForm

# Create your views here.
def index(request):
    # Post 테이블의 모든 레코드를 불러온다.
    posts_all = Post.objects.all()
    # Post 테이블의 모든 레코드를 페이지네이터에서 5개씩 저장한다.
    paginator = Paginator(posts_all, 5)
    # request 된 page를 저장한다.
    page = request.GET.get('page')
    # reqeust된 page의 레코드를 저장한다.
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post' : post})

def delete(request, post_id):
    # 삭제할 레코드의 id 값을 get_object_or_404 메소드의 파라미터로 전달
    get_object_or_404(Post, pk=post_id).delete()

    # redirect 메소드로 삭제 후에 되돌아갈 페이지를 지정
    return redirect('/')

def update(request, post_id):
    if(request.method == 'POST'):
        post = get_object_or_404(Post, pk=post_id)
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()

        return redirect('/blog/detail/' + str(post.id))
    else:
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'edit.html', {'post' : post})


def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다 
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return redirect('/blog/detail/' + str(post.id))
    else:
        return render(request, 'new.html')

def regist(request):
    # POST 요청이 들어왔을 떄
    if(request.method == 'POST'):
        # form 객체에 POST 요청으로 전달된 PatientForm을 저장한다.
        form = PatientForm(request.POST)
        # form이 유효한 데이터일 경우
        if form.is_valid():
            # 데이터베이서에 저장ㅎ하지 않은 상태로 반환
            post = form.save(commit=False)
            # 데이터베이스에 저장
            post.save()
        return redirect('/')
    # GET 요청이 들어왔을 때
    else:
        # 데이터를 입력받을 빈 form 생성
        form = PatientForm()
        # 딕셔너리 형태로 template에 전달
        return render(request, 'regist.html', {'form' : form})