class ChoiceList():
    BRAND_CHOICE = {
    "Toyota": "Toyota",
    "Volkswagen": "Volkswagen",
    "Ford": "Ford",
    "Honda": "Honda",
    "Chevrolet": "Chevrolet",
    "Mercedes-Benz": "Mercedes-Benz",
    "BMW": "BMW",
    "Nissan": "Nissan",
    "Hyundai": "Hyundai",
    "Kia": "Kia",
    "Renault": "Renault",
    "Peugeot": "Peugeot",
    "Audi": "Audi",
    "Suzuki": "Suzuki",
    "Fiat": "Fiat",
    "Lexus": "Lexus",
    "Mazda": "Mazda",
    "Škoda": "Škoda",
    "Mitsubishi": "Mitsubishi",
    "Chery": "Chery",
    "Subaru": "Subaru",
    "Jeep": "Jeep",
    "Daihatsu": "Daihatsu",
    "Great Wall": "Great Wall",
    "Volvo": "Volvo",
    "Land Rover": "Land Rover",
    "Citroën": "Citroën",
    "Jaguar": "Jaguar",
    "Opel": "Opel",
    "Dacia": "Dacia",
    "Buick": "Buick",
    "Cadillac": "Cadillac",
    "Infiniti": "Infiniti",
    "Mini": "Mini",
    "Porsche": "Porsche",
    "Acura": "Acura",
    "Seat": "Seat",
    "BYD": "BYD",
    "Geely": "Geely",
    "Tesla": "Tesla",
    "Saab": "Saab",
    "Lada": "Lada",
    "Haval": "Haval",
    "Ram": "Ram",
    "Dongfeng": "Dongfeng",
    "Lincoln": "Lincoln",
    "GMC": "GMC",
    "Alfa Romeo": "Alfa Romeo",
    "Chrysler": "Chrysler",
    "Lotus": "Lotus",
    "Isuzu": "Isuzu",
    "Smart": "Smart",
    "FAW": "FAW",
    "DS": "DS",
    "Rover": "Rover",
    "Proton": "Proton",
    "Genesis": "Genesis",
    "Zotye": "Zotye",
    "Lancia": "Lancia",
    "Bugatti": "Bugatti",
    "Bentley": "Bentley",
    "Rolls-Royce": "Rolls-Royce",
    "Maserati": "Maserati",
    "Aston Martin": "Aston Martin",
    "Ferrari": "Ferrari",
    "Lamborghini": "Lamborghini",
    "Pagani": "Pagani",
    "McLaren": "McLaren",
    "Maybach": "Maybach",
    "Scion": "Scion",
    "Tata": "Tata",
    "Mahindra": "Mahindra",
    "Maruti": "Maruti",
    "Perodua": "Perodua",
    "BAIC": "BAIC",
    "Foton": "Foton",
    "GAC": "GAC",
    "JAC": "JAC",
    "Hino": "Hino",
    "SsangYong": "SsangYong",
    "Iran Khodro": "Iran Khodro",
    "Luxgen": "Luxgen",
    "Dodge": "Dodge",
    "Pontiac": "Pontiac",
    "Saturn": "Saturn",
    "Oldsmobile": "Oldsmobile",
    "Hummer": "Hummer",
    "Scania": "Scania",
    "MAN": "MAN",
    "Kenworth": "Kenworth",
    "Peterbilt": "Peterbilt",
    "Mack": "Mack",
    "IVECO": "IVECO",
    "Gaz": "Gaz",
    "UAZ": "UAZ",
    "Buggy": "Buggy",
    "Troller": "Troller",
    "Navistar": "Navistar",
    "DFSK": "DFSK",
    "Wuling": "Wuling"
}

car_models = {
    "Toyota": [
        "Camry", "Corolla", "RAV4", "Land Cruiser", "Hilux", "Yaris", "Prius", "Highlander", "Avensis", "C-HR"
    ],
    "Volkswagen": [
        "Golf", "Polo", "Passat", "Tiguan", "Jetta", "Touareg", "Arteon", "T-Roc", "Up!", "Caddy"
    ],
    "Ford": [
        "Focus", "Fiesta", "Explorer", "Kuga", "Mondeo", "Mustang", "Edge", "Ranger", "Ecosport", "Transit"
    ],
    "Honda": [
        "Civic", "Accord", "CR-V", "HR-V", "Fit", "Jazz", "Pilot", "Odyssey", "Insight", "Ridgeline"
    ],
    "Chevrolet": [
        "Camaro", "Tahoe", "Suburban", "Silverado", "Malibu", "Aveo", "Captiva", "Spark", "Traverse", "Equinox"
    ],
    "Mercedes-Benz": [
        "A-Class", "B-Class", "C-Class", "E-Class", "S-Class", "GLA", "GLC", "GLE", "GLS", "CLA", "V-Class"
    ],
    "BMW": [
        "1 Series", "2 Series", "3 Series", "4 Series", "5 Series", "6 Series", "7 Series", "X1", "X3", "X5", "X7", "Z4", "M3", "M5", "i3", "i8"
    ],
    "Nissan": [
        "Qashqai", "X-Trail", "Altima", "Juke", "Murano", "Note", "Sentra", "Tiida", "Leaf", "Pathfinder"
    ],
    "Hyundai": [
        "Solaris", "Elantra", "Sonata", "Tucson", "Santa Fe", "Creta", "Accent", "Kona", "Palisade", "ix35"
    ],
    "Kia": [
        "Rio", "Ceed", "Sportage", "Sorento", "Optima", "Seltos", "Stinger", "Picanto", "Cerato", "Soul"
    ],
    "Renault": [
        "Duster", "Logan", "Sandero", "Kaptur", "Arkana", "Megane", "Clio", "Koleos", "Talisman", "Scenic"
    ],
    "Peugeot": [
        "208", "308", "508", "2008", "3008", "5008", "Partner", "Traveller", "Rifter"
    ],
    "Audi": [
        "A3", "A4", "A6", "A8", "Q3", "Q5", "Q7", "Q8", "TT", "RS6", "e-Tron"
    ],
    "Suzuki": [
        "Swift", "Vitara", "Grand Vitara", "SX4", "Jimny", "Alto", "Ignis", "Baleno", "Celerio"
    ],
    "Fiat": [
        "500", "Panda", "Ducato", "Tipo", "Doblo", "Punto", "Fiorino", "Freemont"
    ],
    "Lexus": [
        "RX", "NX", "ES", "GX", "LX", "IS", "GS", "UX", "LC", "LS"
    ],
    "Mazda": [
        "Mazda3", "Mazda6", "CX-3", "CX-5", "CX-9", "MX-5", "CX-30", "BT-50"
    ],
    "Škoda": [
        "Octavia", "Rapid", "Superb", "Kodiaq", "Karoq", "Fabia", "Scala"
    ],
    "Mitsubishi": [
        "Outlander", "Lancer", "ASX", "Pajero", "Eclipse Cross", "Mirage", "Xpander"
    ],
    "Chery": [
        "Tiggo 3", "Tiggo 4", "Tiggo 7", "Tiggo 8", "Arrizo 7", "Arrizo 5"
    ],
    "Subaru": [
        "Forester", "Outback", "Impreza", "XV", "Legacy", "BRZ", "Levorg"
    ],
    "Jeep": [
        "Cherokee", "Grand Cherokee", "Compass", "Wrangler", "Renegade", "Gladiator"
    ],
    "Daihatsu": [
        "Terios", "Sirion", "Cuore", "Charade", "Mira"
    ],
    "Great Wall": [
        "Hover", "Haval H6", "Wingle", "Safe", "Deer"
    ],
    "Volvo": [
        "XC90", "XC60", "XC40", "S90", "S60", "V90", "V60", "V40"
    ],
    "Land Rover": [
        "Range Rover", "Range Rover Sport", "Range Rover Evoque", "Discovery", "Defender", "Freelander"
    ],
    "Citroën": [
        "C3", "C4", "C5", "Berlingo", "C4 Cactus", "SpaceTourer", "Jumper"
    ],
    "Jaguar": [
        "XE", "XF", "XJ", "F-Pace", "F-Type", "E-Pace", "I-Pace"
    ],
    "Opel": [
        "Astra", "Corsa", "Insignia", "Mokka", "Zafira", "Meriva", "Crossland"
    ],
    "Dacia": [
        "Logan", "Sandero", "Duster", "Dokker", "Lodgy"
    ],
    "Buick": [
        "Enclave", "Envision", "Encore", "LaCrosse", "Regal"
    ],
    "Cadillac": [
        "Escalade", "XT5", "CT6", "CTS", "XT4", "XT6"
    ],
    "Infiniti": [
        "Q50", "Q60", "QX50", "QX60", "QX80", "Q70"
    ],
    "Mini": [
        "Cooper", "Countryman", "Clubman", "Cabrio", "Paceman"
    ],
    "Porsche": [
        "911", "Cayenne", "Macan", "Panamera", "Taycan", "718"
    ],
    "Acura": [
        "MDX", "RDX", "TLX", "ILX", "NSX"
    ],
    "Seat": [
        "Ibiza", "Leon", "Ateca", "Arona", "Toledo", "Alhambra"
    ],
    "BYD": [
        "Tang", "Song", "Han", "Qin", "e5"
    ],
    "Geely": [
        "Atlas", "Coolray", "Emgrand", "Okavango", "Tugella"
    ],
    "Tesla": [
        "Model S", "Model 3", "Model X", "Model Y", "Cybertruck", "Roadster"
    ],
    "Saab": [
        "9-3", "9-5", "900", "9-7X", "9000"
    ],
    "Lada": [
        "Vesta", "Granta", "Largus", "X-Ray", "Niva", "Kalina", "Priora"
    ],
    "Haval": [
        "H6", "F7", "F7x", "H2", "H9"
    ],
    "Ram": [
        "1500", "2500", "3500", "Rebel"
    ],
    "Dongfeng": [],
    "Lincoln": [
        "Navigator", "Aviator", "Corsair", "Continental", "MKZ"
    ],
    "GMC": [
        "Sierra", "Acadia", "Yukon", "Canyon", "Terrain", "Savanna"
    ],
    "Alfa Romeo": [
        "Giulia", "Stelvio", "Giulietta", "Mito", "4C"
    ],
    "Chrysler": [
        "300C", "Pacifica", "Voyager", "Aspen"
    ],
    "Lotus": [
        "Elise", "Exige", "Evora", "Emira"
    ],
    "Isuzu": [
        "D-Max", "MU-X", "Trooper", "Axiom"
    ],
    "Smart": [
        "Fortwo", "Forfour", "Roadster"
    ],
    "FAW": [],
    "DS": [
        "DS 3", "DS 4", "DS 5", "DS 7 Crossback"
    ],
    "Rover": [
        "75", "200", "400", "800"
    ],
    "Proton": [
        "Saga", "Persona", "Exora", "Preve"
    ],
    "Genesis": [
        "G70", "G80", "G90", "GV70", "GV80"
    ],
    "Zotye": [],
    "Lancia": [
        "Ypsilon", "Delta", "Thema", "Voyager"
    ],
    "Bugatti": [
        "Veyron", "Chiron", "Divo", "Centodieci"
    ],
    "Bentley": [
        "Continental GT", "Flying Spur", "Bentayga", "Mulsanne"
    ],
    "Rolls-Royce": [
        "Phantom", "Ghost", "Wraith", "Cullinan", "Dawn"
    ],
    "Maserati": [
        "Ghibli", "Levante", "Quattroporte", "GranTurismo", "GranCabrio"
    ],
    "Aston Martin": [
        "DB11", "Vantage", "DBS Superleggera", "Rapide", "DBX"
    ],
    "Ferrari": [
        "488", "812 Superfast", "Portofino", "Roma", "SF90 Stradale", "F8 Tributo"
    ],
    "Lamborghini": [
        "Huracan", "Aventador", "Urus", "Gallardo", "Murcielago"
    ],
    "Pagani": [
        "Zonda", "Huayra"
    ],
    "McLaren": [
        "570S", "720S", "600LT", "GT", "Senna"
    ],
    "Maybach": [
        "57", "62", "S560", "S650"
    ],
    "Scion": [
        "tC", "xB", "FR-S", "xD", "iA", "iM"
    ],
    "Tata": [
        "Nano", "Tiago", "Safari", "Harrier", "Nexon"
    ],
    "Mahindra": [
        "Scorpio", "XUV500", "Bolero", "Thar"
    ],
    "Maruti": [
        "Baleno", "Alto", "Swift", "Dzire"
    ],
    "Perodua": [
        "Myvi", "Axia", "Bezza", "Aruz"
    ],
    "BAIC": [],
    "Foton": [],
    "GAC": [],
    "JAC": [],
    "Hino": [],
    "SsangYong": [
        "Rexton", "Tivoli", "Actyon", "Korando"
    ],
    "Iran Khodro": [],
    "Luxgen": [],
    "Dodge": [
        "Charger", "Challenger", "Durango", "Ram", "Journey"
    ],
    "Pontiac": [
        "G6", "G8", "Solstice", "Vibe"
    ],
    "Saturn": [
        "Aura", "Sky", "Outlook", "Vue"
    ],
    "Oldsmobile": [
        "Alero", "Bravada", "Silhouette"
    ],
    "Hummer": [
        "H2", "H3", "H1"
    ],
    "Scania": [],
    "MAN": [],
    "Kenworth": [],
    "Peterbilt": [],
    "Mack": [],
    "IVECO": [],
    "Gaz": [
        "ГАЗель", "Волга", "Соболь", "Садко"
    ],
    "UAZ": [
        "Патриот", "Хантер", "Буханка", "Профи"
    ],
    "Buggy": [],
    "Troller": [],
    "Navistar": [],
    "DFSK": [],
    "Wuling": []
}