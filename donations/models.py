from django.db import models

# Create your models here.
#roomNum could be made as a table by itself
# SerNo roomName(unique) grade teacher num_students
class RoomDetails(models.Model):
    name  = models.CharField(max_length=100, unique=True, verbose_name="Class Name")
    grade = models.PositiveIntegerField() # must be made not null
    teacher = models.CharField(max_length=200, verbose_name="Name of the teacher during first period")
    num_students = models.PositiveIntegerField(default=40, verbose_name="Number of students during first period")

    def __unicode__(self):
        return u'%s %s' % (self.name, self.teacher)

    def __str__(self):
        return '%s %s' % (self.name, self.teacher)

    class Meta:
        ordering = ['grade']
        verbose_name_plural = "room details"

# SerNo Week1 roomNum numPenny numNickel numDime numQuaters numDollars
# 1 08/13/2015 4A 5 10 2 1 0
# 2 08/13/2015 80 5 10 8 0 2
# 3 08/20/2015 4A 2 1  3 9 2
class CoinsDonated(models.Model):
    # serial number will be added automatically; that will be the primary key
    week =  models.DateField(verbose_name="Start of the week Monday when donations were made")
    room = models.ForeignKey(RoomDetails)
    numPenny = models.PositiveIntegerField(verbose_name="number of pennies collected")
    numNickel = models.PositiveIntegerField(verbose_name="number of nickels collected")
    numDime = models.PositiveIntegerField(verbose_name="number of dimes collected")
    numQuaters = models.PositiveIntegerField(verbose_name="number of quarters collected")
    numDollars = models.PositiveIntegerField(verbose_name="number of dollars collected")

    def __unicode__(self):
        return u'For %s' % (self.week.__str__())

    def __str__(self):
        return 'For %s' % (self.week.__str__())

    class Meta:
        ordering = ['week']
        verbose_name_plural = "coins donated"
