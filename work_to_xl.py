import openpyxl

from search_in_ya import search_xml


def import_xl(table):
    catalog = openpyxl.open(table)
    sheet = catalog.active
    list_link = []
    cnt = 1
    for row in range(2550, 8000): #sheet.max_row + 1):
        article = sheet[row][1].value
        name = sheet[row][2].value
        print(cnt)
        cnt += 1

        if article and name:
            response = str(article) + ' ' + name
            links = ' '.join(search_xml(response))
            sheet[row][3].value = links if links else 'не найдено'

            catalog.save(table)


if __name__ == '__main__':
    import_xl('20958275d9484ca4a37ca4654e0c22a0.xlsx')
