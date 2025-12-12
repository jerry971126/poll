from django.shortcuts import render
from .models import Poll,Option     #從models引用
from django.views.generic import ListView,DetailView , RedirectView,CreateView,UpdateView
from django.urls import reverse, reverse_lazy

# Create your views here.
def poll_list(req):
    polls=Poll.objects.all()    #從後面拿取資料給前面的變數
    return render (req,"default/list.html",{'poll_list':polls,'msg':'Hello'})

class PollList(ListView):
    model = Poll

    #應用程式名稱/資料模型_list.html
    #default/poll_list.html
class PollView(DetailView):
    model = Poll
    #default/poll_detail.html
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['option_list']=option_list = Option.objects.filter(poll_id=self.object.id)
        return ctx
class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id = self.kwargs['oid'])
        option.votes += 1 #option.votes = options.vote +1
        option.save()
        #return "/poll/{}/".format(option.poll_id)
        #return f"/poll/{option.poll_id}"
        return reverse("poll_view",args=[option.poll_id])
        #return reverse("poll_view",kwargs=['pk':option.poll_id])
class PollCreate(CreateView):
    model = Poll
    fields = "__all__"#["subject",'desc']
    success_url =reverse_lazy('poll_list')
class PollEdit(UpdateView):
    model = Poll
    fields = "__all__"#["subject",'desc']
    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk':self.object.id})
    #
class OptionCreate(CreateView):
    model = Option
    fields = ['title']
    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk':self.kwargs['pid']})