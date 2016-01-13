from model.group import Group
import random


def test_edit_group_name(app,db,check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1"))
    old_groups = db.get_group_list()
    groups = random.choice(old_groups)
    group = Group(name="11111")
    app.group.edit_group_by_id(groups.id,group)
    new_groups = db.get_group_list()
    assert len(old_groups)== len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
  #  if app.group.count() == 0:
   #     app.group.create(Group(header="Header1"))
    #old_groups = app.group.get_group_list()
    #app.group.edit_group(Group(header="22222"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups)== len(new_groups)




