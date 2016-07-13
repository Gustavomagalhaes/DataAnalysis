import csv_reader as cs
import clean_data as cl

if __name__ == "__main__":
     print "Main"

enrollments = cs.read_csv('data/enrollments.csv')
daily_engagement = cs.read_csv('data/daily_engagement.csv')
project_submissions = cs.read_csv('data/project_submissions.csv')

print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])

# CLEAN UP THE DATA TYPE
for enrollment in enrollments:
    enrollment['cancel_date'] = cl.parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = cl.parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = cl.parse_date(enrollment['join_date'])
    
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = cl.parse_date(engagement_record['utc_date'])
    
for submission in project_submissions:
    submission['completion_date'] = cl.parse_date(submission['completion_date'])
    submission['creation_date'] = cl.parse_date(submission['creation_date'])
    
print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])