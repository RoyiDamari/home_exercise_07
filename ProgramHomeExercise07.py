# Exercise 1
name_city: str = "roYi damAri haIfa";
print(len(name_city));
print(name_city.upper());
print(name_city.lower());
print(name_city.startswith("roYi"));
print(name_city.endswith("haIfa"));
print(name_city.split());
new_name_city: str = name_city.replace(" ", "*");
print(new_name_city);
print(new_name_city.split("*"));
print(new_name_city.center(50, '='));
print(new_name_city[3:]);
print(new_name_city[:4]);
print(new_name_city[::2]);
print(new_name_city.title());

# Exercise 2
print("  fun-day  ".strip());
print("hello".isalpha());
print("777".isdigit());
print("   ".isspace());
print("".join(['N','I','N','J','A']));
print("*".join(['N','I','N','J','A']));
print("e" in "hELLo".lower());
word: str = input("Please enter a word: ");
word_list: list[str] = [c.upper() for c in word if c.isalpha()];
print(word_list);

# Exercise 4
capital_list: list[str] = [
    'Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Saint John\'s', 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto-Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasília', 'Bandar Seri Begawan', 'Sofia',
    'Ouagadougou', 'Gitega', 'Praia', 'Phnom Penh', 'Yaoundé', 'Ottawa', 'Bangui', 'Santiago',
    'Beijing', 'Bogotá', 'Moroni', 'Brazzaville', 'Kinshasa', 'San José', 'Zagreb', 'Havana', 'Nicosia',
    'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Quito', 'Cairo', 'San Salvador', 'Malabo',
    'Asmara', 'Tallinn', 'Mbabane', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville',
    'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', 'Saint George\'s', 'Guatemala City', 'Conakry', 'Bissau',
    'Georgetown', 'Port-au-Prince', 'Tegucigalpa', 'Budapest', 'Reykjavík', 'New Delhi', 'Jakarta',
    'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa',
    'Pyongyang', 'Seoul', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli',
    'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Malé', 'Bamako', 'Valletta',
    'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City', 'Palau', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica',
    'Rabat', 'Maputo', 'Windhoek', 'Yaren', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
    'Niamey', 'Abuja', 'Skopje', 'Oslo', 'Muscat', 'Islamabad', 'Panama City', 'Port Moresby',
    'Asunción', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre',
    'Castries', 'Kingstown', 'Apia', 'San Marino', 'São Tomé', 'Riyadh', 'Dakar', 'Belgrade', 'Victoria',
    'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria', 'Juba', 'Madrid',
    'Colombo', 'Khartoum', 'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma',
    'Bangkok', 'Lomé', 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala',
    'Kyiv', 'Abu Dhabi', 'London', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City',
    'Caracas', 'Hanoi', 'Sanaa', 'Lusaka', 'Harare'
]

import random
size: int = len(capital_list);
city_name: str = capital_list[random.randint(0, size)];
city_name_display: str = ''.join(['-' if char == ' ' else '_' for char in city_name]);
print(city_name);

while True:
    if city_name_display == city_name.replace(" ", "-"):
        print("WINNER");
        break;

    temp: str = city_name.lower();
    letter: str = input("Please guess a letter of the city name: ").lower();
    city_name_list: list[str] = list(city_name_display);
    count_letter: int = temp.count(letter);
    count: int = 0;

    if letter in temp:
        for i in range(len(temp)):
            if temp[i] == letter:
                city_name_list[i] = letter.upper() if temp[i - 1] == " " or i == 0 else letter;
                city_name_display = "".join(city_name_list);
                count += 1;
                if count == count_letter:
                    print(city_name_display);
                else:
                    continue;

    else:
        print("letter does not exist in capital");
