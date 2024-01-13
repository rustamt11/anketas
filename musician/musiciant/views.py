from django.shortcuts import render
from .models import Student


def check_profile(request):


    return render(request, 'check.html', context={'profiles': Student.objects.all()})








def update_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        # Обработка данных формы после отправки
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.tools = request.POST.get('tools')
        student.academic_performance = request.POST.get('academic_performance')
        student.status = bool(request.POST.get('status'))
        student.save()
    return render(request, 'update_student.html', {'student': student})




def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        course = request.POST.get('course')
        tools = request.POST.get('tools')
        academic_performance = request.POST.get('academic_performance')
        status = request.POST.get('status') == 'on'

        student = Student.objects.create(
            name=name,
            surname=surname,
            age=age,
            course=course,
            tools=tools,
            academic_performance=academic_performance,
            status=status
        )
        student.save()


    return render(request, 'register.html')