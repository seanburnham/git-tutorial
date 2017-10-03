from django.db import models


class Candidate(models.Model):
    '''A political candidate.'''
    POLITICAL_PARTIES = (
        ('republican', 'Republican'),
        ('democratic', 'Democratic'),
        ('independent', 'Independent'),
    )

    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    party = models.CharField(max_length=25, choices=POLITICAL_PARTIES)
    photo_url = models.URLField()
    votes = models.PositiveIntegerField(default=0)

    def full_name(self):
        '''Return the candidate's full name.'''
        return '{} {}. {}'.format(
            self.first_name,
            self.middle_initial,
            self.last_name)