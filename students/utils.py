
def format_method_students(students):
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Birthday</th></tr><thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.birthday}</td></td>'
    string += '</tbody></table>'
    return string


def format_list_students(students):
    # string = '<br>'.join(str(student) for student in students)
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First name</th>' \
             '<th>Last name</th>' \
             '<th>Email</th>' \
             '<th>Phone</th>' \
             '<th>Birthday</th>' \
             '<th>City</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for st in students:
        string += f'<tr>' \
                  f'<td>{st.first_name}</td>' \
                  f'<td>{st.last_name}</td>' \
                  f'<td>{st.email}</td>' \
                  f'<td>{st.phone}</td>' \
                  f'<td>{st.birthday}</td>' \
                  f'<td>{st.city if st.city else ""}</td>' \
                  f'<td><a href="/students/update/{st.pk}/">Edit</a></td>' \
                  f'</tr>'

    string += '</tbody></table>'
    return