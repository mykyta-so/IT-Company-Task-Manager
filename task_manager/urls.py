from django.urls import path

from task_manager.views import (
    index,
    WorkerListView,
    TaskListView,
    TaskTypeListView,
    PositionListView, WorkerDetailView, TaskDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("task_types/", TaskTypeListView.as_view(), name="tasktype-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
]

app_name = "task_manager"
