from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.subject}' 

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE) # 게시판을 외래키로 참조하며, 연쇄삭제 기능 추가
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # like = models.IntegerField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f'[{self.board.id}:{self.board.subject} ] {self.content}'