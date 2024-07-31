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
city_name: str = capital_list[random.randint(0, size - 1)].lower();
city_name_display: str = ''.join(['-' if char == ' ' else '_' for char in city_name]);
counter: int = 0;

while True:

    if city_name_display.lower() == city_name.replace(" ", "-"):
        print("WINNER");
        break;

    letter: str = input("Please guess a letter of the city name: ").lower();
    city_name_list: list[str] = list(city_name_display);
    last_letter: any = len(city_name) - 1 - city_name[::-1].index(letter) if letter in city_name else 0;

    if letter in city_name:
        for i in range(len(city_name)):
            if city_name[i] == letter:
                city_name_list[i] = letter.upper() if city_name[i - 1] == " " or i == 0 else letter;
                city_name_display = "".join(city_name_list);
                if i == last_letter:
                    print(city_name_display);
                else:
                    continue;

    else:
        print("letter does not exist in capital");
    counter += 1
print(f"The number of guess attempts are: {counter}");                    
