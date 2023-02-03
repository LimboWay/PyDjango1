
def format_list_teachers(teachers):
    # string = '<br>'.join(str(teachers) for teacher in teachers)
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First name</th>' \
             '<th>Last name</th>' \
             '<th>Email</th>' \
             '<th>Birthday</th>' \
             '<th>Salary</th>' \
             '<th>City</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for tch in teachers:
        string += f'<tr>' \
                  f'<td>{tch.first_name}</td>' \
                  f'<td>{tch.last_name}</td>' \
                  f'<td>{tch.email}</td>' \
                  f'<td>{tch.birthday}</td>' \
                  f'<td>{tch.salary if tch.salary else ""}</td>' \
                  f'<td>{tch.city if tch.city else ""}</td>' \
                  f'<td><a href="/teachers/update/{tch.pk}/">Edit</a></td>' \
                  f'</tr>'

    string += '</tbody></table>'
    return string
