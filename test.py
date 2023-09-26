import openpyxl


# функция выберет сайт, на котором есть нужный артикул
def choice_site(links):
    pass
    return 0


# def main(row):
#     actions = {
#         'example1': parser_for_site_1,
#         'example2': parser_for_site_2,
#         'example3': parser_for_site_3,
#         'example4': parser_for_site_4,
#         'example5': parser_for_site_5
#     }
#
#     site = choice_site
#     if site in actions:
#         specifications = actions[site]()
#         save_in_xl(specifications, row)
#
#
# def save_in_xl(specifications, row):


def import_xl(table):
    catalog = openpyxl.open(table)
    sheet = catalog.active

    cnt = 1
    for row in range(1, sheet.max_row + 1):
        links = sheet[row][3].value
        site = choice_site(links)

        actions = {
            'example1': parser_for_site_1,
            'example2': parser_for_site_2,
            'example3': parser_for_site_3,
            'example4': parser_for_site_4,
            'example5': parser_for_site_5
        }

        site = choice_site
        if site in actions:
            specifications = actions[site]()
            save_in_xl(specifications, row)




def parser_for_site_1():
    pass


def parser_for_site_2():
    pass


def parser_for_site_3():
    pass


def parser_for_site_4():
    pass


def parser_for_site_5():
    pass
