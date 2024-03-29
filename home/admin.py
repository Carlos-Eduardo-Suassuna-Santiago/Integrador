from django.contrib import admin
from .models import AddBook,IssueBook,ReturnBook,AddStudent

# Extendendo o modelo de usuário padrão do Django (AbstractUser), adicionando campos personalizados. / Registrado no admin para que possa ser gerenciado por meio da interface de administração.
from django.contrib.sessions.models import Session
admin.site.register(Session)
from .models import UserExtend
admin.site.register(UserExtend)
class AddBook_Admin(admin.ModelAdmin):
    list_display=("user","bookid","bookname","subject","category")
admin.site.register(AddBook,AddBook_Admin)
class IssueBookAdmin(admin.ModelAdmin):
    list_display=("user","book1","studentid")
admin.site.register(IssueBook,IssueBookAdmin)
class ReturnBookAdmin(admin.ModelAdmin):
    list_display=("user","bookid2")
admin.site.register(ReturnBook,ReturnBookAdmin)
class AddStudentAdmin(admin.ModelAdmin):
    list_display=("user","sname","studentid")
admin.site.register(AddStudent,AddStudentAdmin)

