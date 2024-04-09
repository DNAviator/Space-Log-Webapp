from django.shortcuts import render
from .models import CaptainLogs

# Create your views here.
def create_log(request):
  all_logs = CaptainLogs.objects.all().order_by("-date_created")  # Get all logs for sidebar
  if request.method == 'POST': # verify that the method is a post (note that unhandled errors may be caused by invalid post requests)
    success_message = "Log created successfully!"
    log_text = request.POST['log'] # get the log text from the post request
    new_log = CaptainLogs.objects.create(Log=log_text) # Create the log item
    return render(request, 'Crud/create_log.html', {'success_message': success_message, 'all_logs': all_logs})  # Replace with your success template
  else:
    return render(request, 'Crud/create_log.html', {'all_logs': all_logs})
