from dashboard.models import Brand, CarModel

mydict = {
    "Toyota": ["Camry", "Corolla", "Rav4", "Prius", "Highlander", "Land Cruiser", "Hilux", "Tacoma", "Sienna", "4Runner"],  # noqa: E501
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Odyssey", "Fit", "HR-V", "Ridgeline", "Passport"],  # noqa: E501
    "Ford": ["F-150", "Mustang", "Explorer", "Focus", "Escape", "Ranger", "Edge", "Bronco", "Fiesta", "Expedition"],  # noqa: E501
    "Chevrolet": ["Silverado", "Camaro", "Equinox", "Malibu", "Tahoe", "Suburban", "Traverse", "Colorado", "Impala"],  # noqa: E501
    "Volkswagen": ["Golf", "Passat", "Tiguan", "Jetta", "Atlas", "Arteon", "ID.4", "Polo", "Touareg"],  # noqa: E501
    "BMW": ["3 Series", "5 Series", "X5", "X3", "7 Series", "X1", "X7", "M3", "M5"],
    "Mercedes-Benz": ["C-Class", "E-Class", "S-Class", "GLC", "GLE", "A-Class", "GLA", "GLS", "AMG GT"],  # noqa: E501
    "Audi": ["A4", "A6", "Q5", "Q7", "A3", "Q3", "A5", "A7", "e-tron"],
    "Nissan": ["Altima", "Rogue", "Sentra", "Maxima", "Pathfinder", "Murano", "Frontier", "Titan", "Leaf"],  # noqa: E501
    "Hyundai": ["Elantra", "Tucson", "Santa Fe", "Sonata", "Kona", "Palisade", "Venue", "Accent"],  # noqa: E501
    "Kia": ["Sorento", "Sportage", "Forte", "Telluride", "Rio", "Seltos", "Optima", "Soul", "Carnival"],  # noqa: E501
    "Volvo": ["XC60", "XC90", "S60", "S90", "V60", "V90", "XC40", "Polestar 2"],
    "Subaru": ["Outback", "Forester", "Impreza", "Crosstrek", "Legacy", "Ascent", "WRX", "BRZ"],  # noqa: E501
    "Mazda": ["CX-5", "Mazda3", "CX-9", "Mazda6", "CX-30", "MX-5 Miata", "CX-3"],
    "Lexus": ["RX", "NX", "ES", "GX", "LS", "UX", "IS", "LC"],
    "Jeep": ["Wrangler", "Grand Cherokee", "Cherokee", "Compass", "Renegade", "Gladiator", "Wagoneer"],  # noqa: E501
    "Tesla": ["Model 3", "Model S", "Model Y", "Model X", "Cybertruck", "Roadster"],
    "Porsche": ["911", "Cayenne", "Macan", "Taycan", "Panamera", "Cayman", "Boxster"],
    "Land Rover": ["Range Rover", "Range Rover Sport", "Discovery", "Defender", "Range Rover Evoque", "Velar"],  # noqa: E501
    "Fiat": ["500", "Panda", "Tipo", "500X", "500L", "Ducato"],
    "Renault": ["Clio", "Megane", "Captur", "Kadjar", "Duster", "Zoe", "Talisman"],
    "Peugeot": ["208", "308", "3008", "5008", "2008", "508", "Rifter"],
    "Citroen": ["C3", "C4", "C5 Aircross", "Berlingo", "Cactus", "Spacetourer"],
    "Skoda": ["Octavia", "Superb", "Kodiaq", "Karoq", "Fabia", "Scala", "Kamiq"],
    "Seat": ["Leon", "Ibiza", "Arona", "Ateca", "Tarraco", "Cupra Formentor"],
    "Dacia": ["Sandero", "Duster", "Logan", "Spring", "Jogger", "Lodgy"],
    "Suzuki": ["Swift", "Vitara", "Jimny", "Ignis", "S-Cross", "Baleno"],
    "Mitsubishi": ["Outlander", "ASX", "Eclipse Cross", "Pajero", "L200", "Mirage"],
    "Alfa Romeo": ["Giulia", "Stelvio", "Tonale", "4C", "Giulietta"],
    "Ferrari": ["488", "F8 Tributo", "SF90 Stradale", "Roma", "Portofino", "812 Superfast"],  # noqa: E501
    "Lamborghini": ["Aventador", "Huracan", "Urus", "Sian", "Countach"],
    "Bugatti": ["Chiron", "Veyron", "Divo", "Centodieci"],
    "McLaren": ["720S", "570S", "Artura", "P1", "GT"],
    "Aston Martin": ["DB11", "Vantage", "DBS Superleggera", "Valhalla", "Rapide"],
    "Bentley": ["Continental GT", "Bentayga", "Flying Spur", "Mulsanne"],
    "Rolls-Royce": ["Phantom", "Ghost", "Cullinan", "Wraith", "Dawn"],
    "Maserati": ["Ghibli", "Quattroporte", "Levante", "GranTurismo", "MC20"],
    "Jaguar": ["F-Pace", "XE", "XF", "E-Pace", "I-Pace", "F-Type"],
    "Infiniti": ["Q50", "Q60", "QX50", "QX60", "QX80"],
    "Acura": ["MDX", "RDX", "TLX", "NSX", "ILX"],
    "Genesis": ["G70", "G80", "G90", "GV70", "GV80"],
    "Mini": ["Cooper", "Countryman", "Clubman", "Paceman", "Electric"],
    "Smart": ["Fortwo", "Forfour", "EQ Fortwo"],
    "Lada": ["Granta", "Vesta", "Niva", "XRAY", "Largus"],
    "UAZ": ["Patriot", "Hunter", "Pickup", "Bukhanka"],
    "GAZ": ["Volga", "Gazelle", "Sobol", "Tigr"],
    "Chrysler": ["300", "Pacifica", "Voyager"],
    "Dodge": ["Challenger", "Charger", "Durango", "Journey"],
    "Ram": ["1500", "2500", "3500", "Promaster"],
    "Buick": ["Encore", "Enclave", "Regal"],
    "Cadillac": ["Escalade", "XT5", "CT5", "XT4"],
    "Lincoln": ["Navigator", "Aviator", "Corsair", "Nautilus"],
    "GMC": ["Sierra", "Yukon", "Acadia", "Canyon"],
    "Hummer": ["H2", "H3", "EV"],
    "Pontiac": ["GTO", "Firebird", "Trans Am", "Solstice"],
    "Saab": ["9-3", "9-5", "900", "93X"],
    "Opel": ["Astra", "Corsa", "Insignia", "Mokka", "Grandland"],
    "Daihatsu": ["Terios", "Mira", "Move", "Cast"],
    "Isuzu": ["D-Max", "MU-X", "Trooper", "Rodeo"],
    "Proton": ["Saga", "Persona", "X70", "Iriz"],
    "Geely": ["Coolray", "Atlas", "Emgrand", "Tugella"],
    "Great Wall": ["Haval H6", "Wingle", "Poer", "Tank 300"],
    "BYD": ["Han", "Tang", "Song", "Yuan"],
    "Chery": ["Tiggo", "Arrizo", "QQ", "Exeed"],
    "ZAZ": ["Sens", "Forza", "Tavria", "Vida"],
    "Lifan": ["Solano", "X60", "Myway", "Smily"],
    "Haval": ["H6", "H9", "Jolion", "F7"],
    "FAW": ["Bestune", "Oley", "Vita", "X40"],
    "Brilliance": ["V5", "V7", "H530"],
    "Changan": ["CS75", "Eado", "Alsvin", "UNI-K"],
    "Datsun": ["on-Do", "mi-Do", "redi-GO"],
    "Tata": ["Nexon", "Harrier", "Safari", "Tiago"],
    "Mahindra": ["Scorpio", "Thar", "XUV500", "Bolero"],
    "Maruti Suzuki": ["Swift", "Baleno", "Dzire", "Vitara Brezza"],
    "SsangYong": ["Rexton", "Tivoli", "Korando", "Musso"],
    "Lancia": ["Ypsilon", "Delta", "Thema"],
    "Maybach": ["S-Class", "GLS"],
    "Wuling": ["Hongguang", "Almaz", "Cortez"],
    "Hongqi": ["H9", "HS7", "E-HS9"],
    "Koenigsegg": ["Jesko", "Gemera", "Regera"],
    "Rimac": ["Nevera", "Concept One"],
    "Lucid": ["Air", "Gravity"],
    "Rivian": ["R1T", "R1S"],
    "Polestar": ["1", "2", "3"],
    "NIO": ["ET7", "ES8", "EC6"],
    "XPeng": ["P7", "G3", "P5"],
    "Li Auto": ["One", "L9", "L8"],
    "Fisker": ["Ocean", "Karma"],
    "Borgward": ["BX7", "BX5"],
    "Morris": ["Mini", "Marina"],
    "Austin": ["Mini", "Allegro"],
    "Trabant": ["601", "P50"],
    "Wartburg": ["353", "311"],
    "Zastava": ["Yugo", "Florida"],
    "Moskvich": ["412", "2140"],
    "Volga": ["GAZ-24", "GAZ-21"]
}

from workspace import mydict  # noqa: E402, F811

for key in mydict:
    new_brand = Brand(name=key)
    new_brand.save()
    for val in mydict.get(key):
        new_model = CarModel(brand=new_brand, name=val)
        new_model.save()