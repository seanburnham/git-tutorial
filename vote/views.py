from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from vote import models


class Vote(View):
    '''Vote view.'''

    def get(self, request):
        '''Show the voting page.'''
        candidates = models.Candidate.objects.all()
        user_vote = request.session.get('vote', None)

        return render(request, 'vote.html', {
            'candidates': candidates,
            'vote': user_vote,
            })

    def post(self, request):
        '''Get the user's vote.'''
        ballot = Ballot(request.POST)
        if ballot.is_valid():
            ballot.candidate.votes += 1
            ballot.candidate.save()
            request.session['vote'] = ballot.candidate.id
        return HttpResponseRedirect('/')


class Ballot(forms.Form):
    '''Voter ballot.'''
    candidate_id = forms.IntegerField(min_value=0)

    def clean(self):
        if len(self.errors) == 0:
            try:
                self.candidate = models.Candidate.objects.get(id=self.cleaned_data.get('candidate_id'))
            except models.Candidate.DoesNotExist:
                raise forms.ValidationError('Invalid candidate id.')
        return self.cleaned_data
