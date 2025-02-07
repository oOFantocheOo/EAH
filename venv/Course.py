import Timetable as tt
import operations_gui as og


class Course:
    def __init__(self, course_id, title, course_type='', major=' ', week_start='', week_end='', class_list=[], taught_by_profs=[],
                 period_required=tt.Timetable(), location='', scheduled_manually=False, should_be_scheduled=False):
        self.course_type = course_type
        self.course_id = str(course_id)
        self.title = title
        self.class_list = class_list
        self.week_start = week_start
        self.week_end = week_end
        self.location = location
        self.taught_by_profs = taught_by_profs
        for prof in taught_by_profs:
            self.taught_by_profs.append(prof)
        self.period_required = period_required
        self.period_allocated = []
        self.scheduled_manually = scheduled_manually
        self.should_be_scheduled = should_be_scheduled
        self.major = major
        self.groups = []
        self.weeks = ['0' for _ in range(30)]

    def __str__(self):
        profs_names = ''
        status = ''
        if self.should_be_scheduled:
            status += 'Should be scheduled in the school timetable\n'
        else:
            status += 'Should NOT be scheduled in the school timetable\n'

        if self.scheduled_manually:
            status += 'Scheduled manually'
        else:
            status += 'To be scheduled by the program'
        for prof in self.taught_by_profs:
            profs_names = profs_names + prof.name
        return str(self.course_id) + '\n' + str(self.title) + '\n' + str(profs_names) + '\n' + str(
            *self.class_list) + '\n' + status

    def complete_info(self):
        time = self.period_allocated if self.period_allocated else 'Not Allocated Yet!'
        return self.__str__() + '\n' + str(self.period_required) + '\n' + str(self.location) + '\n' + str(time)

    def set_scheduled_manually(self):
        self.scheduled_manually = True

    def set_not_scheduled_manually(self):
        self.scheduled_manually = False

    def set_should_be_scheduled(self):
        self.should_be_scheduled = True

    def set_should_not_be_scheduled(self):
        self.should_be_scheduled = False

    def clear_classes(self):
        self.class_list = []

    def add_class(self, class_a):
        self.class_list.append(class_a.classId)

    def clear_profs(self):
        self.taught_by_profs = []

    def add_prof(self, prof):
        self.taught_by_profs.append(prof.prof_id)

    def add_prof_to_group(self, group, prof):
        if prof.prof_id in group[1]:
            og.show_error_message(prof.name + ' already added to this group')
            return
        group[1].append(prof.prof_id)
        og.show_succeed_message()

    def add_class_to_group(self, group, class_a):
        if class_a.classId in group[0]:
            og.show_error_message(class_a.classId + 'already added to this group')
            return
        group[0].append(class_a.classId)
        og.show_succeed_message()

    def remove_group(self, group):
        self.groups.remove(group)

    def add_group(self):
        self.groups.append([[], []])

