from enum import Enum

from .labels import Label
from .leagues import League, CapitalLeague, BuilderBaseLeague, WarLeague
from .location import Location


__all__ = (
    'ClanWarState',
    'ClanType',
    'Labels',
    'BuilderBaseLeagues',
    'CapitalLeagues',
    'ClanRole',
    'ClanWarLeagueGroupState',
    'ClanWarResult',
    'Languages',
    'Leagues',
    'Village',
    'Locations',
    'PlayerHouseElementType',
    'WarLeagues',
    'TokenStatus',
    'WarFrequency',
    'WarPreference',
)


class ClanType(Enum):
    CLOSED = "closed"
    INVITE_ONLY = "inviteOnly"
    OPEN = "open"


class WarFrequency(Enum):
    ALWAYS = "always"
    MORE_THAN_ONCE_PER_WEEK = "moreThanOncePerWeek"
    LESS_THAN_ONCE_PER_WEEK = "lessThanOncePerWeek"
    UNKNOWN = "unknown"
    ONCE_PER_WEEK = "oncePerWeek"
    NEVER = "never"


class Locations(Enum):
    EUROPE = Location({'id': 32000000, 'name': 'Europe', 'isCountry': False})
    NORTH_AMERICA = Location({'id': 32000001, 'name': 'North America', 'isCountry': False})
    SOUTH_AMERICA = Location({'id': 32000002, 'name': 'South America', 'isCountry': False})
    ASIA = Location({'id': 32000003, 'name': 'Asia', 'isCountry': False})
    AUSTRALIA_R = Location({'id': 32000004, 'name': 'Australia', 'isCountry': False})
    AFRICA = Location({'id': 32000005, 'name': 'Africa', 'isCountry': False})
    INTERNATIONAL = Location({'id': 32000006, 'name': 'International', 'isCountry': False})
    AFGHANISTAN = Location({'id': 32000007, 'name': 'Afghanistan', 'isCountry': True, 'countryCode': 'AF'})
    LAND_ISLANDS = Location({'id': 32000008, 'name': 'Åland Islands', 'isCountry': True, 'countryCode': 'AX'})
    ALBANIA = Location({'id': 32000009, 'name': 'Albania', 'isCountry': True, 'countryCode': 'AL'})
    ALGERIA = Location({'id': 32000010, 'name': 'Algeria', 'isCountry': True, 'countryCode': 'DZ'})
    AMERICAN_SAMOA = Location({'id': 32000011, 'name': 'American Samoa', 'isCountry': True, 'countryCode': 'AS'})
    ANDORRA = Location({'id': 32000012, 'name': 'Andorra', 'isCountry': True, 'countryCode': 'AD'})
    ANGOLA = Location({'id': 32000013, 'name': 'Angola', 'isCountry': True, 'countryCode': 'AO'})
    ANGUILLA = Location({'id': 32000014, 'name': 'Anguilla', 'isCountry': True, 'countryCode': 'AI'})
    ANTARCTICA = Location({'id': 32000015, 'name': 'Antarctica', 'isCountry': True, 'countryCode': 'AQ'})
    ANTIGUA_AND_BARBUDA = Location({'id': 32000016, 'name': 'Antigua and Barbuda', 'isCountry': True, 'countryCode': 'AG'})
    ARGENTINA = Location({'id': 32000017, 'name': 'Argentina', 'isCountry': True, 'countryCode': 'AR'})
    ARMENIA = Location({'id': 32000018, 'name': 'Armenia', 'isCountry': True, 'countryCode': 'AM'})
    ARUBA = Location({'id': 32000019, 'name': 'Aruba', 'isCountry': True, 'countryCode': 'AW'})
    ASCENSION_ISLAND = Location({'id': 32000020, 'name': 'Ascension Island', 'isCountry': True, 'countryCode': 'AC'})
    AUSTRALIA_C = Location({'id': 32000021, 'name': 'Australia', 'isCountry': True, 'countryCode': 'AU'})
    AUSTRIA = Location({'id': 32000022, 'name': 'Austria', 'isCountry': True, 'countryCode': 'AT'})
    AZERBAIJAN = Location({'id': 32000023, 'name': 'Azerbaijan', 'isCountry': True, 'countryCode': 'AZ'})
    BAHAMAS = Location({'id': 32000024, 'name': 'Bahamas', 'isCountry': True, 'countryCode': 'BS'})
    BAHRAIN = Location({'id': 32000025, 'name': 'Bahrain', 'isCountry': True, 'countryCode': 'BH'})
    BANGLADESH = Location({'id': 32000026, 'name': 'Bangladesh', 'isCountry': True, 'countryCode': 'BD'})
    BARBADOS = Location({'id': 32000027, 'name': 'Barbados', 'isCountry': True, 'countryCode': 'BB'})
    BELARUS = Location({'id': 32000028, 'name': 'Belarus', 'isCountry': True, 'countryCode': 'BY'})
    BELGIUM = Location({'id': 32000029, 'name': 'Belgium', 'isCountry': True, 'countryCode': 'BE'})
    BELIZE = Location({'id': 32000030, 'name': 'Belize', 'isCountry': True, 'countryCode': 'BZ'})
    BENIN = Location({'id': 32000031, 'name': 'Benin', 'isCountry': True, 'countryCode': 'BJ'})
    BERMUDA = Location({'id': 32000032, 'name': 'Bermuda', 'isCountry': True, 'countryCode': 'BM'})
    BHUTAN = Location({'id': 32000033, 'name': 'Bhutan', 'isCountry': True, 'countryCode': 'BT'})
    BOLIVIA = Location({'id': 32000034, 'name': 'Bolivia', 'isCountry': True, 'countryCode': 'BO'})
    BOSNIA_AND_HERZEGOVINA = Location({'id': 32000035, 'name': 'Bosnia and Herzegovina', 'isCountry': True, 'countryCode': 'BA'})
    BOTSWANA = Location({'id': 32000036, 'name': 'Botswana', 'isCountry': True, 'countryCode': 'BW'})
    BOUVET_ISLAND = Location({'id': 32000037, 'name': 'Bouvet Island', 'isCountry': True, 'countryCode': 'BV'})
    BRAZIL = Location({'id': 32000038, 'name': 'Brazil', 'isCountry': True, 'countryCode': 'BR'})
    BRITISH_INDIAN_OCEAN_TERRITORY = Location({'id': 32000039, 'name': 'British Indian Ocean Territory', 'isCountry': True, 'countryCode': 'IO'})
    BRITISH_VIRGIN_ISLANDS = Location({'id': 32000040, 'name': 'British Virgin Islands', 'isCountry': True, 'countryCode': 'VG'})
    BRUNEI = Location({'id': 32000041, 'name': 'Brunei', 'isCountry': True, 'countryCode': 'BN'})
    BULGARIA = Location({'id': 32000042, 'name': 'Bulgaria', 'isCountry': True, 'countryCode': 'BG'})
    BURKINA_FASO = Location({'id': 32000043, 'name': 'Burkina Faso', 'isCountry': True, 'countryCode': 'BF'})
    BURUNDI = Location({'id': 32000044, 'name': 'Burundi', 'isCountry': True, 'countryCode': 'BI'})
    CAMBODIA = Location({'id': 32000045, 'name': 'Cambodia', 'isCountry': True, 'countryCode': 'KH'})
    CAMEROON = Location({'id': 32000046, 'name': 'Cameroon', 'isCountry': True, 'countryCode': 'CM'})
    CANADA = Location({'id': 32000047, 'name': 'Canada', 'isCountry': True, 'countryCode': 'CA'})
    CANARY_ISLANDS = Location({'id': 32000048, 'name': 'Canary Islands', 'isCountry': True, 'countryCode': 'IC'})
    CAPE_VERDE = Location({'id': 32000049, 'name': 'Cape Verde', 'isCountry': True, 'countryCode': 'CV'})
    CARIBBEAN_NETHERLANDS = Location({'id': 32000050, 'name': 'Caribbean Netherlands', 'isCountry': True, 'countryCode': 'BQ'})
    CAYMAN_ISLANDS = Location({'id': 32000051, 'name': 'Cayman Islands', 'isCountry': True, 'countryCode': 'KY'})
    CENTRAL_AFRICAN_REPUBLIC = Location({'id': 32000052, 'name': 'Central African Republic', 'isCountry': True, 'countryCode': 'CF'})
    CEUTA_AND_MELILLA = Location({'id': 32000053, 'name': 'Ceuta and Melilla', 'isCountry': True, 'countryCode': 'EA'})
    CHAD = Location({'id': 32000054, 'name': 'Chad', 'isCountry': True, 'countryCode': 'TD'})
    CHILE = Location({'id': 32000055, 'name': 'Chile', 'isCountry': True, 'countryCode': 'CL'})
    CHINA = Location({'id': 32000056, 'name': 'China', 'isCountry': True, 'countryCode': 'CN'})
    CHRISTMAS_ISLAND = Location({'id': 32000057, 'name': 'Christmas Island', 'isCountry': True, 'countryCode': 'CX'})
    COCOS_KEELING_ISLANDS = Location({'id': 32000058, 'name': 'Cocos (Keeling) Islands', 'isCountry': True, 'countryCode': 'CC'})
    COLOMBIA = Location({'id': 32000059, 'name': 'Colombia', 'isCountry': True, 'countryCode': 'CO'})
    COMOROS = Location({'id': 32000060, 'name': 'Comoros', 'isCountry': True, 'countryCode': 'KM'})
    CONGO_DRC = Location({'id': 32000061, 'name': 'Congo (DRC)', 'isCountry': True, 'countryCode': 'CG'})
    CONGO_REPUBLIC = Location({'id': 32000062, 'name': 'Congo (Republic)', 'isCountry': True, 'countryCode': 'CD'})
    COOK_ISLANDS = Location({'id': 32000063, 'name': 'Cook Islands', 'isCountry': True, 'countryCode': 'CK'})
    COSTA_RICA = Location({'id': 32000064, 'name': 'Costa Rica', 'isCountry': True, 'countryCode': 'CR'})
    CTE_DIVOIRE = Location({'id': 32000065, 'name': 'Côte d’Ivoire', 'isCountry': True, 'countryCode': 'CI'})
    CROATIA = Location({'id': 32000066, 'name': 'Croatia', 'isCountry': True, 'countryCode': 'HR'})
    CUBA = Location({'id': 32000067, 'name': 'Cuba', 'isCountry': True, 'countryCode': 'CU'})
    CURAAO = Location({'id': 32000068, 'name': 'Curaçao', 'isCountry': True, 'countryCode': 'CW'})
    CYPRUS = Location({'id': 32000069, 'name': 'Cyprus', 'isCountry': True, 'countryCode': 'CY'})
    CZECH_REPUBLIC = Location({'id': 32000070, 'name': 'Czech Republic', 'isCountry': True, 'countryCode': 'CZ'})
    DENMARK = Location({'id': 32000071, 'name': 'Denmark', 'isCountry': True, 'countryCode': 'DK'})
    DIEGO_GARCIA = Location({'id': 32000072, 'name': 'Diego Garcia', 'isCountry': True, 'countryCode': 'DG'})
    DJIBOUTI = Location({'id': 32000073, 'name': 'Djibouti', 'isCountry': True, 'countryCode': 'DJ'})
    DOMINICA = Location({'id': 32000074, 'name': 'Dominica', 'isCountry': True, 'countryCode': 'DM'})
    DOMINICAN_REPUBLIC = Location({'id': 32000075, 'name': 'Dominican Republic', 'isCountry': True, 'countryCode': 'DO'})
    ECUADOR = Location({'id': 32000076, 'name': 'Ecuador', 'isCountry': True, 'countryCode': 'EC'})
    EGYPT = Location({'id': 32000077, 'name': 'Egypt', 'isCountry': True, 'countryCode': 'EG'})
    EL_SALVADOR = Location({'id': 32000078, 'name': 'El Salvador', 'isCountry': True, 'countryCode': 'SV'})
    EQUATORIAL_GUINEA = Location({'id': 32000079, 'name': 'Equatorial Guinea', 'isCountry': True, 'countryCode': 'GQ'})
    ERITREA = Location({'id': 32000080, 'name': 'Eritrea', 'isCountry': True, 'countryCode': 'ER'})
    ESTONIA = Location({'id': 32000081, 'name': 'Estonia', 'isCountry': True, 'countryCode': 'EE'})
    ETHIOPIA = Location({'id': 32000082, 'name': 'Ethiopia', 'isCountry': True, 'countryCode': 'ET'})
    FALKLAND_ISLANDS = Location({'id': 32000083, 'name': 'Falkland Islands', 'isCountry': True, 'countryCode': 'FK'})
    FAROE_ISLANDS = Location({'id': 32000084, 'name': 'Faroe Islands', 'isCountry': True, 'countryCode': 'FO'})
    FIJI = Location({'id': 32000085, 'name': 'Fiji', 'isCountry': True, 'countryCode': 'FJ'})
    FINLAND = Location({'id': 32000086, 'name': 'Finland', 'isCountry': True, 'countryCode': 'FI'})
    FRANCE = Location({'id': 32000087, 'name': 'France', 'isCountry': True, 'countryCode': 'FR'})
    FRENCH_GUIANA = Location({'id': 32000088, 'name': 'French Guiana', 'isCountry': True, 'countryCode': 'GF'})
    FRENCH_POLYNESIA = Location({'id': 32000089, 'name': 'French Polynesia', 'isCountry': True, 'countryCode': 'PF'})
    FRENCH_SOUTHERN_TERRITORIES = Location({'id': 32000090, 'name': 'French Southern Territories', 'isCountry': True, 'countryCode': 'TF'})
    GABON = Location({'id': 32000091, 'name': 'Gabon', 'isCountry': True, 'countryCode': 'GA'})
    GAMBIA = Location({'id': 32000092, 'name': 'Gambia', 'isCountry': True, 'countryCode': 'GM'})
    GEORGIA = Location({'id': 32000093, 'name': 'Georgia', 'isCountry': True, 'countryCode': 'GE'})
    GERMANY = Location({'id': 32000094, 'name': 'Germany', 'isCountry': True, 'countryCode': 'DE'})
    GHANA = Location({'id': 32000095, 'name': 'Ghana', 'isCountry': True, 'countryCode': 'GH'})
    GIBRALTAR = Location({'id': 32000096, 'name': 'Gibraltar', 'isCountry': True, 'countryCode': 'GI'})
    GREECE = Location({'id': 32000097, 'name': 'Greece', 'isCountry': True, 'countryCode': 'GR'})
    GREENLAND = Location({'id': 32000098, 'name': 'Greenland', 'isCountry': True, 'countryCode': 'GL'})
    GRENADA = Location({'id': 32000099, 'name': 'Grenada', 'isCountry': True, 'countryCode': 'GD'})
    GUADELOUPE = Location({'id': 32000100, 'name': 'Guadeloupe', 'isCountry': True, 'countryCode': 'GP'})
    GUAM = Location({'id': 32000101, 'name': 'Guam', 'isCountry': True, 'countryCode': 'GU'})
    GUATEMALA = Location({'id': 32000102, 'name': 'Guatemala', 'isCountry': True, 'countryCode': 'GT'})
    GUERNSEY = Location({'id': 32000103, 'name': 'Guernsey', 'isCountry': True, 'countryCode': 'GG'})
    GUINEA = Location({'id': 32000104, 'name': 'Guinea', 'isCountry': True, 'countryCode': 'GN'})
    GUINEA_BISSAU = Location({'id': 32000105, 'name': 'Guinea-Bissau', 'isCountry': True, 'countryCode': 'GW'})
    GUYANA = Location({'id': 32000106, 'name': 'Guyana', 'isCountry': True, 'countryCode': 'GY'})
    HAITI = Location({'id': 32000107, 'name': 'Haiti', 'isCountry': True, 'countryCode': 'HT'})
    HEARD_AND_MCDONALD_ISLANDS = Location({'id': 32000108, 'name': 'Heard & McDonald Islands', 'isCountry': True, 'countryCode': 'HM'})
    HONDURAS = Location({'id': 32000109, 'name': 'Honduras', 'isCountry': True, 'countryCode': 'HN'})
    HONG_KONG = Location({'id': 32000110, 'name': 'Hong Kong', 'isCountry': True, 'countryCode': 'HK'})
    HUNGARY = Location({'id': 32000111, 'name': 'Hungary', 'isCountry': True, 'countryCode': 'HU'})
    ICELAND = Location({'id': 32000112, 'name': 'Iceland', 'isCountry': True, 'countryCode': 'IS'})
    INDIA = Location({'id': 32000113, 'name': 'India', 'isCountry': True, 'countryCode': 'IN'})
    INDONESIA = Location({'id': 32000114, 'name': 'Indonesia', 'isCountry': True, 'countryCode': 'ID'})
    IRAN = Location({'id': 32000115, 'name': 'Iran', 'isCountry': True, 'countryCode': 'IR'})
    IRAQ = Location({'id': 32000116, 'name': 'Iraq', 'isCountry': True, 'countryCode': 'IQ'})
    IRELAND = Location({'id': 32000117, 'name': 'Ireland', 'isCountry': True, 'countryCode': 'IE'})
    ISLE_OF_MAN = Location({'id': 32000118, 'name': 'Isle of Man', 'isCountry': True, 'countryCode': 'IM'})
    ISRAEL = Location({'id': 32000119, 'name': 'Israel', 'isCountry': True, 'countryCode': 'IL'})
    ITALY = Location({'id': 32000120, 'name': 'Italy', 'isCountry': True, 'countryCode': 'IT'})
    JAMAICA = Location({'id': 32000121, 'name': 'Jamaica', 'isCountry': True, 'countryCode': 'JM'})
    JAPAN = Location({'id': 32000122, 'name': 'Japan', 'isCountry': True, 'countryCode': 'JP'})
    JERSEY = Location({'id': 32000123, 'name': 'Jersey', 'isCountry': True, 'countryCode': 'JE'})
    JORDAN = Location({'id': 32000124, 'name': 'Jordan', 'isCountry': True, 'countryCode': 'JO'})
    KAZAKHSTAN = Location({'id': 32000125, 'name': 'Kazakhstan', 'isCountry': True, 'countryCode': 'KZ'})
    KENYA = Location({'id': 32000126, 'name': 'Kenya', 'isCountry': True, 'countryCode': 'KE'})
    KIRIBATI = Location({'id': 32000127, 'name': 'Kiribati', 'isCountry': True, 'countryCode': 'KI'})
    KOSOVO = Location({'id': 32000128, 'name': 'Kosovo', 'isCountry': True, 'countryCode': 'XK'})
    KUWAIT = Location({'id': 32000129, 'name': 'Kuwait', 'isCountry': True, 'countryCode': 'KW'})
    KYRGYZSTAN = Location({'id': 32000130, 'name': 'Kyrgyzstan', 'isCountry': True, 'countryCode': 'KG'})
    LAOS = Location({'id': 32000131, 'name': 'Laos', 'isCountry': True, 'countryCode': 'LA'})
    LATVIA = Location({'id': 32000132, 'name': 'Latvia', 'isCountry': True, 'countryCode': 'LV'})
    LEBANON = Location({'id': 32000133, 'name': 'Lebanon', 'isCountry': True, 'countryCode': 'LB'})
    LESOTHO = Location({'id': 32000134, 'name': 'Lesotho', 'isCountry': True, 'countryCode': 'LS'})
    LIBERIA = Location({'id': 32000135, 'name': 'Liberia', 'isCountry': True, 'countryCode': 'LR'})
    LIBYA = Location({'id': 32000136, 'name': 'Libya', 'isCountry': True, 'countryCode': 'LY'})
    LIECHTENSTEIN = Location({'id': 32000137, 'name': 'Liechtenstein', 'isCountry': True, 'countryCode': 'LI'})
    LITHUANIA = Location({'id': 32000138, 'name': 'Lithuania', 'isCountry': True, 'countryCode': 'LT'})
    LUXEMBOURG = Location({'id': 32000139, 'name': 'Luxembourg', 'isCountry': True, 'countryCode': 'LU'})
    MACAU = Location({'id': 32000140, 'name': 'Macau', 'isCountry': True, 'countryCode': 'MO'})
    NORTH_MACEDONIA = Location({'id': 32000141, 'name': 'North Macedonia', 'isCountry': True, 'countryCode': 'MK'})
    MADAGASCAR = Location({'id': 32000142, 'name': 'Madagascar', 'isCountry': True, 'countryCode': 'MG'})
    MALAWI = Location({'id': 32000143, 'name': 'Malawi', 'isCountry': True, 'countryCode': 'MW'})
    MALAYSIA = Location({'id': 32000144, 'name': 'Malaysia', 'isCountry': True, 'countryCode': 'MY'})
    MALDIVES = Location({'id': 32000145, 'name': 'Maldives', 'isCountry': True, 'countryCode': 'MV'})
    MALI = Location({'id': 32000146, 'name': 'Mali', 'isCountry': True, 'countryCode': 'ML'})
    MALTA = Location({'id': 32000147, 'name': 'Malta', 'isCountry': True, 'countryCode': 'MT'})
    MARSHALL_ISLANDS = Location({'id': 32000148, 'name': 'Marshall Islands', 'isCountry': True, 'countryCode': 'MH'})
    MARTINIQUE = Location({'id': 32000149, 'name': 'Martinique', 'isCountry': True, 'countryCode': 'MQ'})
    MAURITANIA = Location({'id': 32000150, 'name': 'Mauritania', 'isCountry': True, 'countryCode': 'MR'})
    MAURITIUS = Location({'id': 32000151, 'name': 'Mauritius', 'isCountry': True, 'countryCode': 'MU'})
    MAYOTTE = Location({'id': 32000152, 'name': 'Mayotte', 'isCountry': True, 'countryCode': 'YT'})
    MEXICO = Location({'id': 32000153, 'name': 'Mexico', 'isCountry': True, 'countryCode': 'MX'})
    MICRONESIA = Location({'id': 32000154, 'name': 'Micronesia', 'isCountry': True, 'countryCode': 'FM'})
    MOLDOVA = Location({'id': 32000155, 'name': 'Moldova', 'isCountry': True, 'countryCode': 'MD'})
    MONACO = Location({'id': 32000156, 'name': 'Monaco', 'isCountry': True, 'countryCode': 'MC'})
    MONGOLIA = Location({'id': 32000157, 'name': 'Mongolia', 'isCountry': True, 'countryCode': 'MN'})
    MONTENEGRO = Location({'id': 32000158, 'name': 'Montenegro', 'isCountry': True, 'countryCode': 'ME'})
    MONTSERRAT = Location({'id': 32000159, 'name': 'Montserrat', 'isCountry': True, 'countryCode': 'MS'})
    MOROCCO = Location({'id': 32000160, 'name': 'Morocco', 'isCountry': True, 'countryCode': 'MA'})
    MOZAMBIQUE = Location({'id': 32000161, 'name': 'Mozambique', 'isCountry': True, 'countryCode': 'MZ'})
    MYANMAR_BURMA = Location({'id': 32000162, 'name': 'Myanmar (Burma)', 'isCountry': True, 'countryCode': 'MM'})
    NAMIBIA = Location({'id': 32000163, 'name': 'Namibia', 'isCountry': True, 'countryCode': 'NA'})
    NAURU = Location({'id': 32000164, 'name': 'Nauru', 'isCountry': True, 'countryCode': 'NR'})
    NEPAL = Location({'id': 32000165, 'name': 'Nepal', 'isCountry': True, 'countryCode': 'NP'})
    NETHERLANDS = Location({'id': 32000166, 'name': 'Netherlands', 'isCountry': True, 'countryCode': 'NL'})
    NEW_CALEDONIA = Location({'id': 32000167, 'name': 'New Caledonia', 'isCountry': True, 'countryCode': 'NC'})
    NEW_ZEALAND = Location({'id': 32000168, 'name': 'New Zealand', 'isCountry': True, 'countryCode': 'NZ'})
    NICARAGUA = Location({'id': 32000169, 'name': 'Nicaragua', 'isCountry': True, 'countryCode': 'NI'})
    NIGER = Location({'id': 32000170, 'name': 'Niger', 'isCountry': True, 'countryCode': 'NE'})
    NIGERIA = Location({'id': 32000171, 'name': 'Nigeria', 'isCountry': True, 'countryCode': 'NG'})
    NIUE = Location({'id': 32000172, 'name': 'Niue', 'isCountry': True, 'countryCode': 'NU'})
    NORFOLK_ISLAND = Location({'id': 32000173, 'name': 'Norfolk Island', 'isCountry': True, 'countryCode': 'NF'})
    NORTH_KOREA = Location({'id': 32000174, 'name': 'North Korea', 'isCountry': True, 'countryCode': 'KP'})
    NORTHERN_MARIANA_ISLANDS = Location({'id': 32000175, 'name': 'Northern Mariana Islands', 'isCountry': True, 'countryCode': 'MP'})
    NORWAY = Location({'id': 32000176, 'name': 'Norway', 'isCountry': True, 'countryCode': 'NO'})
    OMAN = Location({'id': 32000177, 'name': 'Oman', 'isCountry': True, 'countryCode': 'OM'})
    PAKISTAN = Location({'id': 32000178, 'name': 'Pakistan', 'isCountry': True, 'countryCode': 'PK'})
    PALAU = Location({'id': 32000179, 'name': 'Palau', 'isCountry': True, 'countryCode': 'PW'})
    PALESTINE = Location({'id': 32000180, 'name': 'Palestine', 'isCountry': True, 'countryCode': 'PS'})
    PANAMA = Location({'id': 32000181, 'name': 'Panama', 'isCountry': True, 'countryCode': 'PA'})
    PAPUA_NEW_GUINEA = Location({'id': 32000182, 'name': 'Papua New Guinea', 'isCountry': True, 'countryCode': 'PG'})
    PARAGUAY = Location({'id': 32000183, 'name': 'Paraguay', 'isCountry': True, 'countryCode': 'PY'})
    PERU = Location({'id': 32000184, 'name': 'Peru', 'isCountry': True, 'countryCode': 'PE'})
    PHILIPPINES = Location({'id': 32000185, 'name': 'Philippines', 'isCountry': True, 'countryCode': 'PH'})
    PITCAIRN_ISLANDS = Location({'id': 32000186, 'name': 'Pitcairn Islands', 'isCountry': True, 'countryCode': 'PN'})
    POLAND = Location({'id': 32000187, 'name': 'Poland', 'isCountry': True, 'countryCode': 'PL'})
    PORTUGAL = Location({'id': 32000188, 'name': 'Portugal', 'isCountry': True, 'countryCode': 'PT'})
    PUERTO_RICO = Location({'id': 32000189, 'name': 'Puerto Rico', 'isCountry': True, 'countryCode': 'PR'})
    QATAR = Location({'id': 32000190, 'name': 'Qatar', 'isCountry': True, 'countryCode': 'QA'})
    RUNION = Location({'id': 32000191, 'name': 'Réunion', 'isCountry': True, 'countryCode': 'RE'})
    ROMANIA = Location({'id': 32000192, 'name': 'Romania', 'isCountry': True, 'countryCode': 'RO'})
    RUSSIA = Location({'id': 32000193, 'name': 'Russia', 'isCountry': True, 'countryCode': 'RU'})
    RWANDA = Location({'id': 32000194, 'name': 'Rwanda', 'isCountry': True, 'countryCode': 'RW'})
    SAINT_BARTHLEMY = Location({'id': 32000195, 'name': 'Saint Barthélemy', 'isCountry': True, 'countryCode': 'BL'})
    SAINT_HELENA = Location({'id': 32000196, 'name': 'Saint Helena', 'isCountry': True, 'countryCode': 'SH'})
    SAINT_KITTS_AND_NEVIS = Location({'id': 32000197, 'name': 'Saint Kitts and Nevis', 'isCountry': True, 'countryCode': 'KN'})
    SAINT_LUCIA = Location({'id': 32000198, 'name': 'Saint Lucia', 'isCountry': True, 'countryCode': 'LC'})
    SAINT_MARTIN = Location({'id': 32000199, 'name': 'Saint Martin', 'isCountry': True, 'countryCode': 'MF'})
    SAINT_PIERRE_AND_MIQUELON = Location({'id': 32000200, 'name': 'Saint Pierre and Miquelon', 'isCountry': True, 'countryCode': 'PM'})
    SAMOA = Location({'id': 32000201, 'name': 'Samoa', 'isCountry': True, 'countryCode': 'WS'})
    SAN_MARINO = Location({'id': 32000202, 'name': 'San Marino', 'isCountry': True, 'countryCode': 'SM'})
    SO_TOM_AND_PRNCIPE = Location({'id': 32000203, 'name': 'São Tomé and Príncipe', 'isCountry': True, 'countryCode': 'ST'})
    SAUDI_ARABIA = Location({'id': 32000204, 'name': 'Saudi Arabia', 'isCountry': True, 'countryCode': 'SA'})
    SENEGAL = Location({'id': 32000205, 'name': 'Senegal', 'isCountry': True, 'countryCode': 'SN'})
    SERBIA = Location({'id': 32000206, 'name': 'Serbia', 'isCountry': True, 'countryCode': 'RS'})
    SEYCHELLES = Location({'id': 32000207, 'name': 'Seychelles', 'isCountry': True, 'countryCode': 'SC'})
    SIERRA_LEONE = Location({'id': 32000208, 'name': 'Sierra Leone', 'isCountry': True, 'countryCode': 'SL'})
    SINGAPORE = Location({'id': 32000209, 'name': 'Singapore', 'isCountry': True, 'countryCode': 'SG'})
    SINT_MAARTEN = Location({'id': 32000210, 'name': 'Sint Maarten', 'isCountry': True, 'countryCode': 'SX'})
    SLOVAKIA = Location({'id': 32000211, 'name': 'Slovakia', 'isCountry': True, 'countryCode': 'SK'})
    SLOVENIA = Location({'id': 32000212, 'name': 'Slovenia', 'isCountry': True, 'countryCode': 'SI'})
    SOLOMON_ISLANDS = Location({'id': 32000213, 'name': 'Solomon Islands', 'isCountry': True, 'countryCode': 'SB'})
    SOMALIA = Location({'id': 32000214, 'name': 'Somalia', 'isCountry': True, 'countryCode': 'SO'})
    SOUTH_AFRICA = Location({'id': 32000215, 'name': 'South Africa', 'isCountry': True, 'countryCode': 'ZA'})
    SOUTH_KOREA = Location({'id': 32000216, 'name': 'South Korea', 'isCountry': True, 'countryCode': 'KR'})
    SOUTH_SUDAN = Location({'id': 32000217, 'name': 'South Sudan', 'isCountry': True, 'countryCode': 'SS'})
    SPAIN = Location({'id': 32000218, 'name': 'Spain', 'isCountry': True, 'countryCode': 'ES'})
    SRI_LANKA = Location({'id': 32000219, 'name': 'Sri Lanka', 'isCountry': True, 'countryCode': 'LK'})
    ST_VINCENT_AND_GRENADINES = Location({'id': 32000220, 'name': 'St. Vincent & Grenadines', 'isCountry': True, 'countryCode': 'VC'})
    SUDAN = Location({'id': 32000221, 'name': 'Sudan', 'isCountry': True, 'countryCode': 'SD'})
    SURINAME = Location({'id': 32000222, 'name': 'Suriname', 'isCountry': True, 'countryCode': 'SR'})
    SVALBARD_AND_JAN_MAYEN = Location({'id': 32000223, 'name': 'Svalbard and Jan Mayen', 'isCountry': True, 'countryCode': 'SJ'})
    SWAZILAND = Location({'id': 32000224, 'name': 'Swaziland', 'isCountry': True, 'countryCode': 'SZ'})
    SWEDEN = Location({'id': 32000225, 'name': 'Sweden', 'isCountry': True, 'countryCode': 'SE'})
    SWITZERLAND = Location({'id': 32000226, 'name': 'Switzerland', 'isCountry': True, 'countryCode': 'CH'})
    SYRIA = Location({'id': 32000227, 'name': 'Syria', 'isCountry': True, 'countryCode': 'SY'})
    TAIWAN = Location({'id': 32000228, 'name': 'Taiwan', 'isCountry': True, 'countryCode': 'TW'})
    TAJIKISTAN = Location({'id': 32000229, 'name': 'Tajikistan', 'isCountry': True, 'countryCode': 'TJ'})
    TANZANIA = Location({'id': 32000230, 'name': 'Tanzania', 'isCountry': True, 'countryCode': 'TZ'})
    THAILAND = Location({'id': 32000231, 'name': 'Thailand', 'isCountry': True, 'countryCode': 'TH'})
    TIMOR_LESTE = Location({'id': 32000232, 'name': 'Timor-Leste', 'isCountry': True, 'countryCode': 'TL'})
    TOGO = Location({'id': 32000233, 'name': 'Togo', 'isCountry': True, 'countryCode': 'TG'})
    TOKELAU = Location({'id': 32000234, 'name': 'Tokelau', 'isCountry': True, 'countryCode': 'TK'})
    TONGA = Location({'id': 32000235, 'name': 'Tonga', 'isCountry': True, 'countryCode': 'TO'})
    TRINIDAD_AND_TOBAGO = Location({'id': 32000236, 'name': 'Trinidad and Tobago', 'isCountry': True, 'countryCode': 'TT'})
    TRISTAN_DA_CUNHA = Location({'id': 32000237, 'name': 'Tristan da Cunha', 'isCountry': True, 'countryCode': 'TA'})
    TUNISIA = Location({'id': 32000238, 'name': 'Tunisia', 'isCountry': True, 'countryCode': 'TN'})
    TRKIYE = Location({'id': 32000239, 'name': 'Türkiye', 'isCountry': True, 'countryCode': 'TR'})
    TURKMENISTAN = Location({'id': 32000240, 'name': 'Turkmenistan', 'isCountry': True, 'countryCode': 'TM'})
    TURKS_AND_CAICOS_ISLANDS = Location({'id': 32000241, 'name': 'Turks and Caicos Islands', 'isCountry': True, 'countryCode': 'TC'})
    TUVALU = Location({'id': 32000242, 'name': 'Tuvalu', 'isCountry': True, 'countryCode': 'TV'})
    US_OUTLYING_ISLANDS = Location({'id': 32000243, 'name': 'U.S. Outlying Islands', 'isCountry': True, 'countryCode': 'UM'})
    US_VIRGIN_ISLANDS = Location({'id': 32000244, 'name': 'U.S. Virgin Islands', 'isCountry': True, 'countryCode': 'VI'})
    UGANDA = Location({'id': 32000245, 'name': 'Uganda', 'isCountry': True, 'countryCode': 'UG'})
    UKRAINE = Location({'id': 32000246, 'name': 'Ukraine', 'isCountry': True, 'countryCode': 'UA'})
    UNITED_ARAB_EMIRATES = Location({'id': 32000247, 'name': 'United Arab Emirates', 'isCountry': True, 'countryCode': 'AE'})
    UNITED_KINGDOM = Location({'id': 32000248, 'name': 'United Kingdom', 'isCountry': True, 'countryCode': 'GB'})
    UNITED_STATES = Location({'id': 32000249, 'name': 'United States', 'isCountry': True, 'countryCode': 'US'})
    URUGUAY = Location({'id': 32000250, 'name': 'Uruguay', 'isCountry': True, 'countryCode': 'UY'})
    UZBEKISTAN = Location({'id': 32000251, 'name': 'Uzbekistan', 'isCountry': True, 'countryCode': 'UZ'})
    VANUATU = Location({'id': 32000252, 'name': 'Vanuatu', 'isCountry': True, 'countryCode': 'VU'})
    VATICAN_CITY = Location({'id': 32000253, 'name': 'Vatican City', 'isCountry': True, 'countryCode': 'VA'})
    VENEZUELA = Location({'id': 32000254, 'name': 'Venezuela', 'isCountry': True, 'countryCode': 'VE'})
    VIETNAM = Location({'id': 32000255, 'name': 'Vietnam', 'isCountry': True, 'countryCode': 'VN'})
    WALLIS_AND_FUTUNA = Location({'id': 32000256, 'name': 'Wallis and Futuna', 'isCountry': True, 'countryCode': 'WF'})
    WESTERN_SAHARA = Location({'id': 32000257, 'name': 'Western Sahara', 'isCountry': True, 'countryCode': 'EH'})
    YEMEN = Location({'id': 32000258, 'name': 'Yemen', 'isCountry': True, 'countryCode': 'YE'})
    ZAMBIA = Location({'id': 32000259, 'name': 'Zambia', 'isCountry': True, 'countryCode': 'ZM'})
    ZIMBABWE = Location({'id': 32000260, 'name': 'Zimbabwe', 'isCountry': True, 'countryCode': 'ZW'})
    MISSING32000261 = Location({'id': 32000261, 'name': '', 'isCountry': False})
    MISSING32000262 = Location({'id': 32000262, 'name': '', 'isCountry': False})
    MISSING32000263 = Location({'id': 32000263, 'name': '', 'isCountry': False})
    MISSING32000264 = Location({'id': 32000264, 'name': '', 'isCountry': False})
    MISSING32000265 = Location({'id': 32000265, 'name': '', 'isCountry': False})


class Leagues(Enum):
    UNRANKED = League({'id': 29000000, 'name': 'Unranked',
                       'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png',
                                    'tiny': 'https://api-assets.clashofclans.com/leagues/36/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png'}})
    BRONZE_LEAGUE_III = League({'id': 29000001, 'name': 'Bronze League III',
                                'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/uUJDLEdAh7Lwf6YOHmXfNM586ZlEvMju54bTlt2u6EE.png',
                                             'tiny': 'https://api-assets.clashofclans.com/leagues/36/uUJDLEdAh7Lwf6YOHmXfNM586ZlEvMju54bTlt2u6EE.png',
                                             'medium': 'https://api-assets.clashofclans.com/leagues/288/uUJDLEdAh7Lwf6YOHmXfNM586ZlEvMju54bTlt2u6EE.png'}})
    BRONZE_LEAGUE_II = League({'id': 29000002, 'name': 'Bronze League II',
                               'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/U2acNDRaR5rQDu4Z6pQKaGcjWm9dkSnHMAPZCXrHPB4.png',
                                            'tiny': 'https://api-assets.clashofclans.com/leagues/36/U2acNDRaR5rQDu4Z6pQKaGcjWm9dkSnHMAPZCXrHPB4.png',
                                            'medium': 'https://api-assets.clashofclans.com/leagues/288/U2acNDRaR5rQDu4Z6pQKaGcjWm9dkSnHMAPZCXrHPB4.png'}})
    BRONZE_LEAGUE_I = League({'id': 29000003, 'name': 'Bronze League I',
                              'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/SZIXZHZxfHTmgseKCH6T5hvMQ3JQM-Js2QfpC9A3ya0.png',
                                           'tiny': 'https://api-assets.clashofclans.com/leagues/36/SZIXZHZxfHTmgseKCH6T5hvMQ3JQM-Js2QfpC9A3ya0.png',
                                           'medium': 'https://api-assets.clashofclans.com/leagues/288/SZIXZHZxfHTmgseKCH6T5hvMQ3JQM-Js2QfpC9A3ya0.png'}})
    SILVER_LEAGUE_III = League({'id': 29000004, 'name': 'Silver League III',
                                'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/QcFBfoArnafaXCnB5OfI7vESpQEBuvWtzOyLq8gJzVc.png',
                                             'tiny': 'https://api-assets.clashofclans.com/leagues/36/QcFBfoArnafaXCnB5OfI7vESpQEBuvWtzOyLq8gJzVc.png',
                                             'medium': 'https://api-assets.clashofclans.com/leagues/288/QcFBfoArnafaXCnB5OfI7vESpQEBuvWtzOyLq8gJzVc.png'}})
    SILVER_LEAGUE_II = League({'id': 29000005, 'name': 'Silver League II',
                               'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/8OhXcwDJkenBH2kPH73eXftFOpHHRF-b32n0yrTqC44.png',
                                            'tiny': 'https://api-assets.clashofclans.com/leagues/36/8OhXcwDJkenBH2kPH73eXftFOpHHRF-b32n0yrTqC44.png',
                                            'medium': 'https://api-assets.clashofclans.com/leagues/288/8OhXcwDJkenBH2kPH73eXftFOpHHRF-b32n0yrTqC44.png'}})
    SILVER_LEAGUE_I = League({'id': 29000006, 'name': 'Silver League I',
                              'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/nvrBLvCK10elRHmD1g9w5UU1flDRMhYAojMB2UbYfPs.png',
                                           'tiny': 'https://api-assets.clashofclans.com/leagues/36/nvrBLvCK10elRHmD1g9w5UU1flDRMhYAojMB2UbYfPs.png',
                                           'medium': 'https://api-assets.clashofclans.com/leagues/288/nvrBLvCK10elRHmD1g9w5UU1flDRMhYAojMB2UbYfPs.png'}})
    GOLD_LEAGUE_III = League({'id': 29000007, 'name': 'Gold League III',
                              'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/vd4Lhz5b2I1P0cLH25B6q63JN3Wt1j2NTMhOYpMPQ4M.png',
                                           'tiny': 'https://api-assets.clashofclans.com/leagues/36/vd4Lhz5b2I1P0cLH25B6q63JN3Wt1j2NTMhOYpMPQ4M.png',
                                           'medium': 'https://api-assets.clashofclans.com/leagues/288/vd4Lhz5b2I1P0cLH25B6q63JN3Wt1j2NTMhOYpMPQ4M.png'}})
    GOLD_LEAGUE_II = League({'id': 29000008, 'name': 'Gold League II',
                             'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/Y6CveuHmPM_oiOic2Yet0rYL9AFRYW0WA0u2e44-YbM.png',
                                          'tiny': 'https://api-assets.clashofclans.com/leagues/36/Y6CveuHmPM_oiOic2Yet0rYL9AFRYW0WA0u2e44-YbM.png',
                                          'medium': 'https://api-assets.clashofclans.com/leagues/288/Y6CveuHmPM_oiOic2Yet0rYL9AFRYW0WA0u2e44-YbM.png'}})
    GOLD_LEAGUE_I = League({'id': 29000009, 'name': 'Gold League I',
                            'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/CorhMY9ZmQvqXTZ4VYVuUgPNGSHsO0cEXEL5WYRmB2Y.png',
                                         'tiny': 'https://api-assets.clashofclans.com/leagues/36/CorhMY9ZmQvqXTZ4VYVuUgPNGSHsO0cEXEL5WYRmB2Y.png',
                                         'medium': 'https://api-assets.clashofclans.com/leagues/288/CorhMY9ZmQvqXTZ4VYVuUgPNGSHsO0cEXEL5WYRmB2Y.png'}})
    CRYSTAL_LEAGUE_III = League({'id': 29000010, 'name': 'Crystal League III',
                                 'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/Hyqco7bHh0Q81xB8mSF_ZhjKnKcTmJ9QEq9QGlsxiKE.png',
                                              'tiny': 'https://api-assets.clashofclans.com/leagues/36/Hyqco7bHh0Q81xB8mSF_ZhjKnKcTmJ9QEq9QGlsxiKE.png',
                                              'medium': 'https://api-assets.clashofclans.com/leagues/288/Hyqco7bHh0Q81xB8mSF_ZhjKnKcTmJ9QEq9QGlsxiKE.png'}})
    CRYSTAL_LEAGUE_II = League({'id': 29000011, 'name': 'Crystal League II',
                                'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/jhP36EhAA9n1ADafdQtCP-ztEAQjoRpY7cT8sU7SW8A.png',
                                             'tiny': 'https://api-assets.clashofclans.com/leagues/36/jhP36EhAA9n1ADafdQtCP-ztEAQjoRpY7cT8sU7SW8A.png',
                                             'medium': 'https://api-assets.clashofclans.com/leagues/288/jhP36EhAA9n1ADafdQtCP-ztEAQjoRpY7cT8sU7SW8A.png'}})
    CRYSTAL_LEAGUE_I = League({'id': 29000012, 'name': 'Crystal League I',
                               'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/kSfTyNNVSvogX3dMvpFUTt72VW74w6vEsEFuuOV4osQ.png',
                                            'tiny': 'https://api-assets.clashofclans.com/leagues/36/kSfTyNNVSvogX3dMvpFUTt72VW74w6vEsEFuuOV4osQ.png',
                                            'medium': 'https://api-assets.clashofclans.com/leagues/288/kSfTyNNVSvogX3dMvpFUTt72VW74w6vEsEFuuOV4osQ.png'}})
    MASTER_LEAGUE_III = League({'id': 29000013, 'name': 'Master League III',
                                'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/pSXfKvBKSgtvfOY3xKkgFaRQi0WcE28s3X35ywbIluY.png',
                                             'tiny': 'https://api-assets.clashofclans.com/leagues/36/pSXfKvBKSgtvfOY3xKkgFaRQi0WcE28s3X35ywbIluY.png',
                                             'medium': 'https://api-assets.clashofclans.com/leagues/288/pSXfKvBKSgtvfOY3xKkgFaRQi0WcE28s3X35ywbIluY.png'}})
    MASTER_LEAGUE_II = League({'id': 29000014, 'name': 'Master League II',
                               'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/4wtS1stWZQ-1VJ5HaCuDPfdhTWjeZs_jPar_YPzK6Lg.png',
                                            'tiny': 'https://api-assets.clashofclans.com/leagues/36/4wtS1stWZQ-1VJ5HaCuDPfdhTWjeZs_jPar_YPzK6Lg.png',
                                            'medium': 'https://api-assets.clashofclans.com/leagues/288/4wtS1stWZQ-1VJ5HaCuDPfdhTWjeZs_jPar_YPzK6Lg.png'}})
    MASTER_LEAGUE_I = League({'id': 29000015, 'name': 'Master League I',
                              'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/olUfFb1wscIH8hqECAdWbdB6jPm9R8zzEyHIzyBgRXc.png',
                                           'tiny': 'https://api-assets.clashofclans.com/leagues/36/olUfFb1wscIH8hqECAdWbdB6jPm9R8zzEyHIzyBgRXc.png',
                                           'medium': 'https://api-assets.clashofclans.com/leagues/288/olUfFb1wscIH8hqECAdWbdB6jPm9R8zzEyHIzyBgRXc.png'}})
    CHAMPION_LEAGUE_III = League({'id': 29000016, 'name': 'Champion League III',
                                  'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/JmmTbspV86xBigM7OP5_SjsEDPuE7oXjZC9aOy8xO3s.png',
                                               'tiny': 'https://api-assets.clashofclans.com/leagues/36/JmmTbspV86xBigM7OP5_SjsEDPuE7oXjZC9aOy8xO3s.png',
                                               'medium': 'https://api-assets.clashofclans.com/leagues/288/JmmTbspV86xBigM7OP5_SjsEDPuE7oXjZC9aOy8xO3s.png'}})
    CHAMPION_LEAGUE_II = League({'id': 29000017, 'name': 'Champion League II',
                                 'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png',
                                              'tiny': 'https://api-assets.clashofclans.com/leagues/36/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png',
                                              'medium': 'https://api-assets.clashofclans.com/leagues/288/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png'}})
    CHAMPION_LEAGUE_I = League({'id': 29000018, 'name': 'Champion League I',
                                'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/9v_04LHmd1LWq7IoY45dAdGhrBkrc2ZFMZVhe23PdCE.png',
                                             'tiny': 'https://api-assets.clashofclans.com/leagues/36/9v_04LHmd1LWq7IoY45dAdGhrBkrc2ZFMZVhe23PdCE.png',
                                             'medium': 'https://api-assets.clashofclans.com/leagues/288/9v_04LHmd1LWq7IoY45dAdGhrBkrc2ZFMZVhe23PdCE.png'}})
    TITAN_LEAGUE_III = League({'id': 29000019, 'name': 'Titan League III',
                               'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/L-HrwYpFbDwWjdmhJQiZiTRa_zXPPOgUTdmbsaq4meo.png',
                                            'tiny': 'https://api-assets.clashofclans.com/leagues/36/L-HrwYpFbDwWjdmhJQiZiTRa_zXPPOgUTdmbsaq4meo.png',
                                            'medium': 'https://api-assets.clashofclans.com/leagues/288/L-HrwYpFbDwWjdmhJQiZiTRa_zXPPOgUTdmbsaq4meo.png'}})
    TITAN_LEAGUE_II = League({'id': 29000020, 'name': 'Titan League II',
                              'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/llpWocHlOoFliwyaEx5Z6dmoZG4u4NmxwpF-Jg7su7Q.png',
                                           'tiny': 'https://api-assets.clashofclans.com/leagues/36/llpWocHlOoFliwyaEx5Z6dmoZG4u4NmxwpF-Jg7su7Q.png',
                                           'medium': 'https://api-assets.clashofclans.com/leagues/288/llpWocHlOoFliwyaEx5Z6dmoZG4u4NmxwpF-Jg7su7Q.png'}})
    TITAN_LEAGUE_I = League({'id': 29000021, 'name': 'Titan League I',
                             'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/qVCZmeYH0lS7Gaa6YoB7LrNly7bfw7fV_d4Vp2CU-gk.png',
                                          'tiny': 'https://api-assets.clashofclans.com/leagues/36/qVCZmeYH0lS7Gaa6YoB7LrNly7bfw7fV_d4Vp2CU-gk.png',
                                          'medium': 'https://api-assets.clashofclans.com/leagues/288/qVCZmeYH0lS7Gaa6YoB7LrNly7bfw7fV_d4Vp2CU-gk.png'}})
    LEGEND_LEAGUE = League({'id': 29000022, 'name': 'Legend League',
                            'iconUrls': {'small': 'https://api-assets.clashofclans.com/leagues/72/R2zmhyqQ0_lKcDR5EyghXCxgyC9mm_mVMIjAbmGoZtw.png',
                                         'tiny': 'https://api-assets.clashofclans.com/leagues/36/R2zmhyqQ0_lKcDR5EyghXCxgyC9mm_mVMIjAbmGoZtw.png',
                                         'medium': 'https://api-assets.clashofclans.com/leagues/288/R2zmhyqQ0_lKcDR5EyghXCxgyC9mm_mVMIjAbmGoZtw.png'}})


class CapitalLeagues(Enum):
    UNRANKED = CapitalLeague({'id': 85000000, 'name': 'Unranked'})
    BRONZE_LEAGUE_III = CapitalLeague({'id': 85000001, 'name': 'Bronze League III'})
    BRONZE_LEAGUE_II = CapitalLeague({'id': 85000002, 'name': 'Bronze League II'})
    BRONZE_LEAGUE_I = CapitalLeague({'id': 85000003, 'name': 'Bronze League I'})
    SILVER_LEAGUE_III = CapitalLeague({'id': 85000004, 'name': 'Silver League III'})
    SILVER_LEAGUE_II = CapitalLeague({'id': 85000005, 'name': 'Silver League II'})
    SILVER_LEAGUE_I = CapitalLeague({'id': 85000006, 'name': 'Silver League I'})
    GOLD_LEAGUE_III = CapitalLeague({'id': 85000007, 'name': 'Gold League III'})
    GOLD_LEAGUE_II = CapitalLeague({'id': 85000008, 'name': 'Gold League II'})
    GOLD_LEAGUE_I = CapitalLeague({'id': 85000009, 'name': 'Gold League I'})
    CRYSTAL_LEAGUE_III = CapitalLeague({'id': 85000010, 'name': 'Crystal League III'})
    CRYSTAL_LEAGUE_II = CapitalLeague({'id': 85000011, 'name': 'Crystal League II'})
    CRYSTAL_LEAGUE_I = CapitalLeague({'id': 85000012, 'name': 'Crystal League I'})
    MASTER_LEAGUE_III = CapitalLeague({'id': 85000013, 'name': 'Master League III'})
    MASTER_LEAGUE_II = CapitalLeague({'id': 85000014, 'name': 'Master League II'})
    MASTER_LEAGUE_I = CapitalLeague({'id': 85000015, 'name': 'Master League I'})
    CHAMPION_LEAGUE_III = CapitalLeague({'id': 85000016, 'name': 'Champion League III'})
    CHAMPION_LEAGUE_II = CapitalLeague({'id': 85000017, 'name': 'Champion League II'})
    CHAMPION_LEAGUE_I = CapitalLeague({'id': 85000018, 'name': 'Champion League I'})
    TITAN_LEAGUE_III = CapitalLeague({'id': 85000019, 'name': 'Titan League III'})
    TITAN_LEAGUE_II = CapitalLeague({'id': 85000020, 'name': 'Titan League II'})
    TITAN_LEAGUE_I = CapitalLeague({'id': 85000021, 'name': 'Titan League I'})
    LEGEND_LEAGUE = CapitalLeague({'id': 85000022, 'name': 'Legend League'})


class BuilderBaseLeagues(Enum):
    WOOD_LEAGUE_V = BuilderBaseLeague({'id': 44000000, 'name': 'Wood League V'})
    WOOD_LEAGUE_IV = BuilderBaseLeague({'id': 44000001, 'name': 'Wood League IV'})
    WOOD_LEAGUE_III = BuilderBaseLeague({'id': 44000002, 'name': 'Wood League III'})
    WOOD_LEAGUE_II = BuilderBaseLeague({'id': 44000003, 'name': 'Wood League II'})
    WOOD_LEAGUE_I = BuilderBaseLeague({'id': 44000004, 'name': 'Wood League I'})
    CLAY_LEAGUE_V = BuilderBaseLeague({'id': 44000005, 'name': 'Clay League V'})
    CLAY_LEAGUE_IV = BuilderBaseLeague({'id': 44000006, 'name': 'Clay League IV'})
    CLAY_LEAGUE_III = BuilderBaseLeague({'id': 44000007, 'name': 'Clay League III'})
    CLAY_LEAGUE_II = BuilderBaseLeague({'id': 44000008, 'name': 'Clay League II'})
    CLAY_LEAGUE_I = BuilderBaseLeague({'id': 44000009, 'name': 'Clay League I'})
    STONE_LEAGUE_V = BuilderBaseLeague({'id': 44000010, 'name': 'Stone League V'})
    STONE_LEAGUE_IV = BuilderBaseLeague({'id': 44000011, 'name': 'Stone League IV'})
    STONE_LEAGUE_III = BuilderBaseLeague({'id': 44000012, 'name': 'Stone League III'})
    STONE_LEAGUE_II = BuilderBaseLeague({'id': 44000013, 'name': 'Stone League II'})
    STONE_LEAGUE_I = BuilderBaseLeague({'id': 44000014, 'name': 'Stone League I'})
    COPPER_LEAGUE_V = BuilderBaseLeague({'id': 44000015, 'name': 'Copper League V'})
    COPPER_LEAGUE_IV = BuilderBaseLeague({'id': 44000016, 'name': 'Copper League IV'})
    COPPER_LEAGUE_III = BuilderBaseLeague({'id': 44000017, 'name': 'Copper League III'})
    COPPER_LEAGUE_II = BuilderBaseLeague({'id': 44000018, 'name': 'Copper League II'})
    COPPER_LEAGUE_I = BuilderBaseLeague({'id': 44000019, 'name': 'Copper League I'})
    BRASS_LEAGUE_III = BuilderBaseLeague({'id': 44000020, 'name': 'Brass League III'})
    BRASS_LEAGUE_II = BuilderBaseLeague({'id': 44000021, 'name': 'Brass League II'})
    BRASS_LEAGUE_I = BuilderBaseLeague({'id': 44000022, 'name': 'Brass League I'})
    IRON_LEAGUE_III = BuilderBaseLeague({'id': 44000023, 'name': 'Iron League III'})
    IRON_LEAGUE_II = BuilderBaseLeague({'id': 44000024, 'name': 'Iron League II'})
    IRON_LEAGUE_I = BuilderBaseLeague({'id': 44000025, 'name': 'Iron League I'})
    STEEL_LEAGUE_III = BuilderBaseLeague({'id': 44000026, 'name': 'Steel League III'})
    STEEL_LEAGUE_II = BuilderBaseLeague({'id': 44000027, 'name': 'Steel League II'})
    STEEL_LEAGUE_I = BuilderBaseLeague({'id': 44000028, 'name': 'Steel League I'})
    TITANIUM_LEAGUE_III = BuilderBaseLeague({'id': 44000029, 'name': 'Titanium League III'})
    TITANIUM_LEAGUE_II = BuilderBaseLeague({'id': 44000030, 'name': 'Titanium League II'})
    TITANIUM_LEAGUE_I = BuilderBaseLeague({'id': 44000031, 'name': 'Titanium League I'})
    PLATINUM_LEAGUE_III = BuilderBaseLeague({'id': 44000032, 'name': 'Platinum League III'})
    PLATINUM_LEAGUE_II = BuilderBaseLeague({'id': 44000033, 'name': 'Platinum League II'})
    PLATINUM_LEAGUE_I = BuilderBaseLeague({'id': 44000034, 'name': 'Platinum League I'})
    EMERALD_LEAGUE_III = BuilderBaseLeague({'id': 44000035, 'name': 'Emerald League III'})
    EMERALD_LEAGUE_II = BuilderBaseLeague({'id': 44000036, 'name': 'Emerald League II'})
    EMERALD_LEAGUE_I = BuilderBaseLeague({'id': 44000037, 'name': 'Emerald League I'})
    RUBY_LEAGUE_III = BuilderBaseLeague({'id': 44000038, 'name': 'Ruby League III'})
    RUBY_LEAGUE_II = BuilderBaseLeague({'id': 44000039, 'name': 'Ruby League II'})
    RUBY_LEAGUE_I = BuilderBaseLeague({'id': 44000040, 'name': 'Ruby League I'})
    DIAMOND_LEAGUE = BuilderBaseLeague({'id': 44000041, 'name': 'Diamond League'})


class WarLeagues(Enum):
    UNRANKED = WarLeague({'id': 48000000, 'name': 'Unranked'})
    BRONZE_LEAGUE_III = WarLeague({'id': 48000001, 'name': 'Bronze League III'})
    BRONZE_LEAGUE_II = WarLeague({'id': 48000002, 'name': 'Bronze League II'})
    BRONZE_LEAGUE_I = WarLeague({'id': 48000003, 'name': 'Bronze League I'})
    SILVER_LEAGUE_III = WarLeague({'id': 48000004, 'name': 'Silver League III'})
    SILVER_LEAGUE_II = WarLeague({'id': 48000005, 'name': 'Silver League II'})
    SILVER_LEAGUE_I = WarLeague({'id': 48000006, 'name': 'Silver League I'})
    GOLD_LEAGUE_III = WarLeague({'id': 48000007, 'name': 'Gold League III'})
    GOLD_LEAGUE_II = WarLeague({'id': 48000008, 'name': 'Gold League II'})
    GOLD_LEAGUE_I = WarLeague({'id': 48000009, 'name': 'Gold League I'})
    CRYSTAL_LEAGUE_III = WarLeague({'id': 48000010, 'name': 'Crystal League III'})
    CRYSTAL_LEAGUE_II = WarLeague({'id': 48000011, 'name': 'Crystal League II'})
    CRYSTAL_LEAGUE_I = WarLeague({'id': 48000012, 'name': 'Crystal League I'})
    MASTER_LEAGUE_III = WarLeague({'id': 48000013, 'name': 'Master League III'})
    MASTER_LEAGUE_II = WarLeague({'id': 48000014, 'name': 'Master League II'})
    MASTER_LEAGUE_I = WarLeague({'id': 48000015, 'name': 'Master League I'})
    CHAMPION_LEAGUE_III = WarLeague({'id': 48000016, 'name': 'Champion League III'})
    CHAMPION_LEAGUE_II = WarLeague({'id': 48000017, 'name': 'Champion League II'})
    CHAMPION_LEAGUE_I = WarLeague({'id': 48000018, 'name': 'Champion League I'})


class Labels(Enum):
    ACTIVE_DAILY = Label({'id': 57000009, 'name': 'Active Daily',
                          'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/mcWhk0ii7CyjiiHOidhRofrSulpVrxjDu24cQtGCQbE.png',
                                       'medium': 'https://api-assets.clashofclans.com/labels/128/mcWhk0ii7CyjiiHOidhRofrSulpVrxjDu24cQtGCQbE.png'}})
    ACTIVE_DONATOR = Label({'id': 57000008, 'name': 'Active Donator',
                            'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/MvL0LDt0yv9AI-Vevpu8yE5NAJUIV05Ofpsr4IfGRxQ.png',
                                         'medium': 'https://api-assets.clashofclans.com/labels/128/MvL0LDt0yv9AI-Vevpu8yE5NAJUIV05Ofpsr4IfGRxQ.png'}})
    AMATEUR_ATTACKER = Label({'id': 57000017, 'name': 'Amateur Attacker',
                              'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/8Q08M2dj1xz1Zx-sAre6QO14hOX2aiEvg-FaGGSX-7M.png',
                                           'medium': 'https://api-assets.clashofclans.com/labels/128/8Q08M2dj1xz1Zx-sAre6QO14hOX2aiEvg-FaGGSX-7M.png'}})
    BASE_DESIGNING = Label({'id': 56000006, 'name': 'Base Designing',
                            'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/LG966XuC6YoEJsPthcgtyJ8uS46LqYDAeiHJNQKR3YQ.png',
                                         'medium': 'https://api-assets.clashofclans.com/labels/128/LG966XuC6YoEJsPthcgtyJ8uS46LqYDAeiHJNQKR3YQ.png'}})
    BUILDER_BASE = Label({'id': 56000005, 'name': 'Builder Base',
                          'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/kyuaiAWdnD9v3ReYPS3_x6QP3V3e0nNAPyDroOIDFZQ.png',
                                       'medium': 'https://api-assets.clashofclans.com/labels/128/kyuaiAWdnD9v3ReYPS3_x6QP3V3e0nNAPyDroOIDFZQ.png'}})
    CLAN_CAPITAL = Label({'id': 56000016, 'name': 'Clan Capital',
                          'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/Odg2DaLfhMgQOci4QvHovdoYq4SDiBrocWS2Bjm8Ah8.png',
                                       'medium': 'https://api-assets.clashofclans.com/labels/128/Odg2DaLfhMgQOci4QvHovdoYq4SDiBrocWS2Bjm8Ah8.png'}})
    CLAN_GAMES = Label({'id': 56000004, 'name': 'Clan Games',
                        'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/7qU7tQGERiVITVG0CPFov1-BnFldu4bMN2gXML5bLIU.png',
                                     'medium': 'https://api-assets.clashofclans.com/labels/128/7qU7tQGERiVITVG0CPFov1-BnFldu4bMN2gXML5bLIU.png'}})
    CLAN_WAR_LEAGUE = Label({'id': 56000001, 'name': 'Clan War League',
                             'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/5w60_3bdtYUe9SM6rkxBRyV_8VvWw_jTlDS5ieU3IsI.png',
                                          'medium': 'https://api-assets.clashofclans.com/labels/128/5w60_3bdtYUe9SM6rkxBRyV_8VvWw_jTlDS5ieU3IsI.png'}})
    CLAN_WARS = Label({'id': 56000000, 'name': 'Clan Wars',
                       'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/lXaIuoTlfoNOY5fKcQGeT57apz1KFWkN9-raxqIlMbE.png',
                                    'medium': 'https://api-assets.clashofclans.com/labels/128/lXaIuoTlfoNOY5fKcQGeT57apz1KFWkN9-raxqIlMbE.png'}})
    COMPETITIVE = Label({'id': 56000014, 'name': 'Competitive',
                         'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/DhBE-1SSnrZQtsfjVHyNW-BTBWMc8Zoo34MNRCNiRsA.png',
                                      'medium': 'https://api-assets.clashofclans.com/labels/128/DhBE-1SSnrZQtsfjVHyNW-BTBWMc8Zoo34MNRCNiRsA.png'}})
    DONATIONS = Label({'id': 56000009, 'name': 'Donations',
                       'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/RauzS-02tv4vWm1edZ-q3gPQGWKGANLZ-85HCw_NVP0.png',
                                    'medium': 'https://api-assets.clashofclans.com/labels/128/RauzS-02tv4vWm1edZ-q3gPQGWKGANLZ-85HCw_NVP0.png'}})
    FARMING = Label({'id': 56000008, 'name': 'Farming',
                     'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/iLWz6AiaIHg_DqfG6s9vAxUJKb-RsPbSYl_S0ii9GAM.png',
                                  'medium': 'https://api-assets.clashofclans.com/labels/128/iLWz6AiaIHg_DqfG6s9vAxUJKb-RsPbSYl_S0ii9GAM.png'}})
    FRIENDLY = Label({'id': 56000010, 'name': 'Friendly',
                      'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/hM7SHnN0x7syFa-s6fE7LzeO5yWG2sfFpZUHuzgMwQg.png',
                                   'medium': 'https://api-assets.clashofclans.com/labels/128/hM7SHnN0x7syFa-s6fE7LzeO5yWG2sfFpZUHuzgMwQg.png'}})
    FRIENDLY_WARS = Label({'id': 56000003, 'name': 'Friendly Wars',
                           'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/6NxZMDn9ryFw8-FHJJimcEkKwnXZHMVUp_0cCVT6onY.png',
                                        'medium': 'https://api-assets.clashofclans.com/labels/128/6NxZMDn9ryFw8-FHJJimcEkKwnXZHMVUp_0cCVT6onY.png'}})
    HUNGRY_LEARNER = Label({'id': 57000010, 'name': 'Hungry Learner',
                            'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/jEvZf9PnfPaqYh2PMLBoJfB1BoBpomerqmsYWDYisKY.png',
                                         'medium': 'https://api-assets.clashofclans.com/labels/128/jEvZf9PnfPaqYh2PMLBoJfB1BoBpomerqmsYWDYisKY.png'}})
    INTERNATIONAL = Label({'id': 56000007, 'name': 'International',
                           'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/zyaTKuJXrsPiU3DvjgdqaSA6B1qvcQ0cjD6ktRah4xs.png',
                                        'medium': 'https://api-assets.clashofclans.com/labels/128/zyaTKuJXrsPiU3DvjgdqaSA6B1qvcQ0cjD6ktRah4xs.png'}})
    NEWBIE = Label({'id': 57000016, 'name': 'Newbie',
                    'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/PcgplBTQo2W_PXYqMi0i6g6nrNMjzCM8Ipd_umSnuHw.png',
                                 'medium': 'https://api-assets.clashofclans.com/labels/128/PcgplBTQo2W_PXYqMi0i6g6nrNMjzCM8Ipd_umSnuHw.png'}})
    NEWBIE_FRIENDLY = Label({'id': 56000015, 'name': 'Newbie Friendly',
                             'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/3oOuYkPdkjWVrBUITgByz9Ur0nmJ4GsERXc-1NUrjKg.png',
                                          'medium': 'https://api-assets.clashofclans.com/labels/128/3oOuYkPdkjWVrBUITgByz9Ur0nmJ4GsERXc-1NUrjKg.png'}})
    RELAXED = Label({'id': 56000013, 'name': 'Relaxed',
                     'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/Kv1MZQfd5A7DLwf1Zw3tOaUiwQHGMwmRpjZqOalu_hI.png',
                                  'medium': 'https://api-assets.clashofclans.com/labels/128/Kv1MZQfd5A7DLwf1Zw3tOaUiwQHGMwmRpjZqOalu_hI.png'}})
    TROPHY_PUSHING = Label({'id': 56000002, 'name': 'Trophy Pushing',
                            'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/hNtigjuwJjs6PWhVtVt5HvJgAp4ZOMO8e2nyjHX29sA.png',
                                         'medium': 'https://api-assets.clashofclans.com/labels/128/hNtigjuwJjs6PWhVtVt5HvJgAp4ZOMO8e2nyjHX29sA.png'}})
    TALKATIVE = Label({'id': 56000011, 'name': 'Talkative',
                       'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/T1c8AYalTn_RruVkY0mRPwNYF5n802thTBEEnOtNTMw.png',
                                    'medium': 'https://api-assets.clashofclans.com/labels/128/T1c8AYalTn_RruVkY0mRPwNYF5n802thTBEEnOtNTMw.png'}})
    TEACHER = Label({'id': 57000013, 'name': 'Teacher',
                     'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/sy5nJmT4BFjS4iT4_iILE02rfrO8VjgpGKFE0rLmot4.png',
                                  'medium': 'https://api-assets.clashofclans.com/labels/128/sy5nJmT4BFjS4iT4_iILE02rfrO8VjgpGKFE0rLmot4.png'}})
    UNDERDOG = Label({'id': 56000012, 'name': 'Underdog',
                      'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/ImSgCg88EEl80mwzFZMIiJTqa33bJmJPcl4v2eT6O04.png',
                                   'medium': 'https://api-assets.clashofclans.com/labels/128/ImSgCg88EEl80mwzFZMIiJTqa33bJmJPcl4v2eT6O04.png'}})
    VETERAN = Label({'id': 57000015, 'name': 'Veteran',
                     'iconUrls': {'small': 'https://api-assets.clashofclans.com/labels/64/u-VKK5y0hj0U8B1xdawjxNcXciv-fwMK3VqEBWCn1oM.png',
                                  'medium': 'https://api-assets.clashofclans.com/labels/128/u-VKK5y0hj0U8B1xdawjxNcXciv-fwMK3VqEBWCn1oM.png'}})


class Languages(Enum):
    pass


class ClanWarState(Enum):
    CLAN_NOT_FOUND = "clanNotFound"
    ACCESS_DENIED = "accessDenied"
    NOT_IN_WAR = "notInWar"
    IN_MATCHMAKING = "inMatchmaking"
    ENTER_WAR = "enterWar"
    MATCHED = "matched"
    PREPARATION = "preparation"
    WAR = "war"
    IN_WAR = "inWar"
    ENDED = "ended"
    WAR_ENDEN = "warEnded"


class ClanWarLeagueGroupState(Enum):
    GROUP_NOT_FOUND = "groupNotFound"
    NOT_IN_WAR = "notInWar"
    PREPARATION = "preparation"
    WAR = "war"
    ENDED = "ended"
    InWar = "inWar"


class ClanWarResult(Enum):
    LOSE = "lose"
    WIN = "win"
    TIE = "tie"
    NONE = None


class ClanRole(Enum):
    NOT_MEMBER = "notMember"
    MEMBER = "member"
    LEADER = "leader"
    ADMIN = "admin"
    COLEADER = "coLeader"


class WarPreference(Enum):
    OUT = "out"
    IN = "in"


class PlayerHouseElementType(Enum):
    GROUND = "ground"
    ROOF = "roof"
    FOOT = "foot"
    DECO = "deco"


class Village(Enum):
    HOME_VILLAGE = "homeVillage"
    BUILDER_BASE = "builderBase"


class TokenStatus(Enum):
    OK = "ok"
    INVALID = "invalid"
