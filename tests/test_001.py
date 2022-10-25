from model.group import Group


def test_edit_patient_surname(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="Артур", secondname="Артурович", birthday="12081980",
                  phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")
