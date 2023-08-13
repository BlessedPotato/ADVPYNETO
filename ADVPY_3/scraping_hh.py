import requests
import bs4
from fake_headers import Headers
import json

return_list = []

def headers_gen():
    return Headers(browser='opera', os='win').generate()


url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

params = {
    'text': 'python django flask',
    'area': (1, 2),
    'page': 0
}


try:
    while True:

        site_html = requests.get(url=url, params=params, headers=headers_gen()).text
        site_soup = bs4.BeautifulSoup(site_html, 'lxml')
        params['page'] += 1
        tag_content = site_soup.find('div', id='a11y-main-content')
        div_item_tags = tag_content.find_all('div', class_='serp-item')

        for div_item_tag in div_item_tags:
            vacancy = div_item_tag.find('h3')
            link = vacancy.find('a').get('href')
            try:
                salary = div_item_tag.find('span', class_='bloko-header-section-3').text.replace('\u202f', '')
            except:
                salary = 'З/П не указана'
            company = div_item_tag.find('a', class_='bloko-link bloko-link_kind-tertiary').text.replace('\xa0', '')
            city = div_item_tag.find('div', class_='vacancy-serp-item__info').contents[1].contents[0]
            return_list.append(
                {
                    "вакансия": vacancy.text,
                    "ссылка": link,
                    "компания": company,
                    "зарплата": salary,
                    "город": city
                }

            )

except:
    pass

if __name__ == '__main__':

    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(return_list, f, ensure_ascii=False, indent=5)


