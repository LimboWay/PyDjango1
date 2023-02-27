
def format_list_students(students):
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First name</th>' \
             '<th>Last name</th>' \
             '<th>Email</th>' \
             '<th>Birthday</th>' \
             '<th>City</th>' \
             '<th>Phone</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody> '
    for student in students:
        string += f'<tr>' \
                  f'<td>{student.first_name}</td>' \
                  f'<td>{student.last_name}</td>' \
                  f'<td>{student.email}</td>' \
                  f'<td>{student.birthday}</td>' \
                  f'<td>{student.city if student.city else ""}</td>' \
                  f'<td>{student.phone if student.phone else ""}</td>' \
                  f'<td><a href="/students/update/{student.id}/">Edit</td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return string
