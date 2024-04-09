from django.shortcuts import render
from .models import CaptainLogs

# Create your views here.
def create_log(request):
  all_logs = CaptainLogs.objects.all().order_by("-date_created")  # Get all logs for sidebar
  if request.method == 'POST':
    log_text = request.POST['log']
    new_log = CaptainLogs.objects.create(Log=log_text)
    # Handle success, e.g., redirect or confirmation message
    return render(request, 'Crud/create_log.html', {'all_logs': all_logs})  # Replace with your success template
  else:
    return render(request, 'Crud/create_log.html', {'all_logs': all_logs})
