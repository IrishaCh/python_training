__author__ = 'Irina.Chegodaeva'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create_edit(self, group, is_creating):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation/edition (is_created = 1/0)
        if is_creating == 1:
            wd.find_element_by_name("new").click()
            # redefining name of the group
            new_name = group.name
            submit_or_update = "submit"
        else:
            wd.find_element_by_name("selected[]").click()
            # click on edit button
            wd.find_element_by_name("edit").click()
            # redefining name of the group
            new_name = group.name + str(self.app.prefix.substring)
            submit_or_update = "update"
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(new_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation/edition
        wd.find_element_by_name(submit_or_update).click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
