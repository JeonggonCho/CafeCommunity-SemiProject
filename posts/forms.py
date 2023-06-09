from django import forms
from .models import Post, Comment, Review, ReComment
from taggit.forms import TagField, TagWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='카페명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '카페이름을 입력해주세요',
            },
        ),
    )


    address = forms.CharField(
        label='주소',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '주소를 입력해주세요',
            },
        ),
    )


    phone_number = forms.CharField(
        label='전화번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '전화번호를 입력해주세요',
            },
        ),
    )


    menu = forms.CharField(
        label='메뉴',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '카페의 대표메뉴를 입력해주세요',
            },
        ),
    )


    hours = forms.CharField(
        label='영업시간',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영업시간 및 휴무일을 입력해주세요',
            },
        ),
    )

    
    information = forms.CharField(
        label='편의시설 정보',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '방문객을 위한 편의시설 정보를 입력해주세요',
            },
        ),
    )

    CHOICES=[('카공 모각코', '카공/모각코'), ('펫 카페', '펫 카페'), ('북 카페', '북 카페')]
    category = forms.ChoiceField(
        label='카테고리',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ),
        choices=CHOICES,
    )

    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            },
        )
    )

    tags = forms.CharField(
        label='태그',
        widget=TagWidget(
            attrs={
                'class': 'form-control',
                'placeholder': '태그는 콤마(,)로 구분하여 작성해주세요' 
            }
        )
    )


    class Meta:
        model = Post
        fields = ('title', 'address', 'phone_number', 'menu', 'hours', 'information', 'category', 'image', 'tags',)


class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
            },
        ),
    )


    rating = forms.FloatField(
        label='평점',
        widget=forms.Select(
            choices=[
                (1, '⭐' * 1 + '☆' * 4),
                (2, '⭐' * 2 + '☆' * 3),
                (3, '⭐' * 3 + '☆' * 2),
                (4, '⭐' * 4 + '☆' * 1),
                (5, '⭐' * 5),
            ],
            attrs={
                'class': 'form-select',
            },
        ),
    )

    
    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
                'multiple': 'True',
            },
        ),
        required=False,
    )
    class Meta:
        model = Review
        fields = ('content', 'rating','image',)


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', 'comment')
    


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='Comment',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control focus-ring focus-ring-danger',
            },
        ),
    )
    class Meta:
        model = Comment
        fields = ('content',)