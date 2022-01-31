from django.contrib import messages
from django.shortcuts import redirect, render
from task.forms import CreateTaskForm
from task.models import Task
from random import randint

def task_view(request):
    if "salam" not in request.session:
        request.session["salam"] = str(randint(1, 100000000000000000000)) + "NaCl"
        return redirect("task")
    else:
        if request.method == "POST":
            if request.POST.get("delete" , False):
                Task.objects.get(pk = request.POST['pk']).delete()
                return redirect("task")
            elif request.POST.get("done" , False):                
                tsk = Task.objects.get(pk = request.POST["done"])
                if str(tsk.pk) in request.session:
                    request.session.pop(f"{tsk.pk}")
                    tsk.done = True
                    tsk.save()
                    return redirect("task")
                else:
                    request.session[f"{tsk.pk}"] = "True"
                    tsk.done = False
                    tsk.save()
                    return redirect("task")
            
            else:
                form = CreateTaskForm(request.POST or None)
                if form.is_valid():
                    tsk = form.save(commit=False)
                    tsk.session_id = request.session["salam"]
                    tsk.save()
                    request.session[f"{tsk.pk}"] = "True"
                    return redirect("task")
                else:
                    
                    messages.error(request , "haji hack nakon")
                    return redirect("task")
        else:
            context = {
                "form" : CreateTaskForm(),
                "tasks" : Task.objects.filter(session_id= request.session["salam"]),

                "background" : "https://media.discordapp.net/attachments/801740253336698939/914012410522796103/manteghie.gif"
            }
            return render(request , "task.html" , context)


        


