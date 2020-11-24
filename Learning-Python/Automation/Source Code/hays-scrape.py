from bs4 import BeautifulSoup
import requests
import json
import datetime
import pandas as pd


def get_result(soup):
    results = soup.find_all('div', class_='search__results')
    for result in results:
        headers = result.find_all('h3')
        new_result = str(headers[0])
        return new_result


def create_url(count):
    return f'https://www.hays.de/jobsuche/stellenangebote-jobs/i/Banks-saving-banks-financial-service-providers/6E7A1D11-89E8-DE11-BAE0-0007E92E2CEA/p/{count}/?q=&e=false'


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')


def get_job_urls(soup):
    jobs_dict = dict()
    items = soup.find_all('a', class_='search__result__header__a')
    for item in items:
        url = item['href']
        job = item.find('span').text.strip('\n')
        job = job.lstrip()
        jobs_dict[url] = job
    return jobs_dict


def clean_json(input_string):
    temp_string = input_string
    temp_string = temp_string.replace('\n', '')
    temp_string = temp_string.replace('\r', '')
    return_string = temp_string[:temp_string.find('"description"')]
    return_string += temp_string[temp_string.find('",', temp_string.find(
        '"description"')) + 2: temp_string.find('"jobBenefits"')]
    return_string += temp_string[temp_string.find(
        '",', temp_string.find('"jobBenefits')) + 2:]
    return return_string


def convert_json_data(soup, json_data, result):
    for item in json_data:
        item = str(item)
        item = item[item.find('{'): item.rfind('}') + 1]
        item = clean_json(item)
        job_details = json.loads(item)
        for key, value in job_details.items():
            if key == 'datePosted':
                result.append(value)
            elif key == 'employmentType':
                result.insert(1, value)
                if value == 'CONTRACTING':
                    meta_details = soup.find_all(
                        'div', class_='row hays__job__details__job__meta__item')
                    meta_detail = clean_meta_details(meta_details)
                    result.append(meta_detail)
                else:
                    result.append('')
            elif key == 'jobLocation':
                result.append(value)
            elif key == 'identifier':
                result.insert(0, value)
    return result


def write_details(soup, key, value, file_name):
    result = list()
    result.append(value)
    result.append(key)
    desc = soup.find_all('div', class_='hays__job__detail__accordion__body')
    json_data = soup.find_all('script', type='application/ld+json')
    if len(json_data) > 1:
        json_data = json_data[1]
    convert_json_data(soup, json_data, result)
    for count, item in enumerate(desc, 0):
        list_items = item.find_all('li')
        contact_details = item.find_all('span')
        if count == 0:
            aufgaben = clean_list_items(list_items)
            result.append(aufgaben)
        elif count == 1:
            qualifikationen = clean_list_items(list_items)
            result.append(qualifikationen)
        elif count == 2:
            vorteile = clean_list_items(list_items)
            result.append(vorteile)
        elif count == 3:
            arbeitgeber = clean_employer_details(item)
            result.append(arbeitgeber)
        elif count == len(desc) - 1:
            kontakt = clean_contact_details(contact_details)
            result.append(kontakt)
    file = open(file_name, 'a')
    for item in result:
        file.write(f'{item}|')
    file.write('\n')
    file.close()


def clean_list_items(list_items):
    result = list()
    for item in list_items:
        result.append(item.get_text(strip=True))
    return result


def clean_employer_details(item):
    result = item.get_text(strip=True)
    result = result.strip()
    return result


def clean_contact_details(contact_details):
    contact_list = clean_list_items(contact_details)
    result = contact_list[0]
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    result = result.replace(' ', '')
    result = result.lower()
    result = result.replace('e-mail', ':e-mail')
    result = result.split(':')
    return result


def clean_meta_details(meta_details):
    result = ''
    temp_list = clean_list_items(meta_details)
    for detail in temp_list:
        if detail.find('Projektdauer') != -1:
            result = detail
            result = result.replace('\n', '')
            result = result.replace('\r', '')
            result = result.replace(' ', '')
            result = result.replace('Projektdauer', 'Projektdauer:')
            result = result.replace('Project duration', 'Projektdauer:')
            result = result.split(':')
    return result


def get_substring(input_string, start_string, end_string):
    return input_string[input_string.find(start_string) + len(start_string): (input_string.find(end_string))]


def write_jobs_dict_to_file(jobs_dict):
    file_name = generate_file_name('jobs', 'json')
    with open(file_name, 'w') as json_file:
        json.dump(jobs_dict, json_file)


def generate_file_name(name, extension):
    timestamp = datetime.datetime.utcnow()
    timestamp_string = str(timestamp.strftime("%Y")) + '-' + str(timestamp.strftime("%m")) + '-' + str(timestamp.strftime(
        "%d")) + '_' + str(timestamp.strftime("%H")) + str(timestamp.strftime("%M")) + str(timestamp.strftime("%S"))
    result = f'{name}_{timestamp_string}.{extension}'
    return result


def create_csv_file(file_name):
    file = open(file_name, 'w')
    file.write(
        'Referenz|Titel|Art|URL|Erstellungsdatum|Dauer|Ort|Aufgaben|Qualifikationen|Vorteile|Arbeitgeber|Kontakt\n')
    file.close()


def clean_file(file_name):
    text = open(file_name, 'r')
    text = ''.join([i for i in text]).replace('\\xa0', ' ')
    text = ''.join([i for i in text]).replace('\\xad', '')
    file_name = f'Hays-{file_name}'
    output = open(file_name, 'w')
    output.writelines(text)
    output.close


def convert_csv_to_excel(file_name):
    file_name = f'Hays-{file_name}'
    df = pd.read_csv(file_name, delimiter='|', encoding='ANSI')
    df.reset_index(inplace=True)
    cols = df.columns[1:]
    df = df.drop('Kontakt', 1)
    df.columns = cols
    file_name = file_name.replace('csv', 'xlsx')
    df.to_excel(
        f'{file_name}', sheet_name='Hays', index=False)


def write_all_job_listings(jobs_dict, file_name):
    for key, value in jobs_dict.items():
        print(value, key)
        soup = get_soup(key)
        write_details(soup, key, value, file_name)


def main():
    count = 1
    url = create_url(count)
    soup = get_soup(url)
    jobs_dict = dict()

    while get_result(soup) != "<h3>0 Ergebnisse</h3>":
        url = create_url(count)
        soup = get_soup(url)
        jobs_dict.update(get_job_urls(soup))
        count += 1
    write_jobs_dict_to_file(jobs_dict)
    file_name = generate_file_name('Job-Listings', 'csv')
    create_csv_file(file_name)
    write_all_job_listings(jobs_dict, file_name)
    clean_file(file_name)
    convert_csv_to_excel(file_name)


main()
