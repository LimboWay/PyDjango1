from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Group
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from groups.forms import CreateGroupForm, UpdateGroupForm
from django.urls import reverse_lazy
from students.models import Student


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = "groups"


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups/create.html'
    form_class = CreateGroupForm
    success_url = reverse_lazy("groups:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        new_group = form.save()
        students = form.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()

        return response


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'groups_detail'


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups/update.html'
    context_object_name = 'group'
    form_class = UpdateGroupForm
    success_url = reverse_lazy('groups:list')

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        students = form.cleaned_data['students']
        for student in students:
            student.group = self.object
            if hasattr(student, 'headman_group'):
                group = student.headman_group
                group.headman = None
            student.save()
        headman_id = int(form.cleaned_data.get('headman_field'))
        if headman_id:
            form.instance.headman = Student.objects.get(id=headman_id)
        else:
            form.instance.headman = None
        form.save()
        return response


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/delete.html'
    context_object_name = 'group'
    success_url = reverse_lazy('groups:list')
