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
    EUROPE = Location(...)
    NORTH_AMERICA = Location(...)
    SOUTH_AMERICA = Location(...)
    ASIA = Location(...)
    AUSTRALIA_R = Location(...)
    AFRICA = Location(...)
    INTERNATIONAL = Location(...)
    AFGHANISTAN = Location(...)
    LAND_ISLANDS = Location(...)
    ALBANIA = Location(...)
    ALGERIA = Location(...)
    AMERICAN_SAMOA = Location(...)
    ANDORRA = Location(...)
    ANGOLA = Location(...)
    ANGUILLA = Location(...)
    ANTARCTICA = Location(...)
    ANTIGUA_AND_BARBUDA = Location(...)
    ARGENTINA = Location(...)
    ARMENIA = Location(...)
    ARUBA = Location(...)
    ASCENSION_ISLAND = Location(...)
    AUSTRALIA_C = Location(...)
    AUSTRIA = Location(...)
    AZERBAIJAN = Location(...)
    BAHAMAS = Location(...)
    BAHRAIN = Location(...)
    BANGLADESH = Location(...)
    BARBADOS = Location(...)
    BELARUS = Location(...)
    BELGIUM = Location(...)
    BELIZE = Location(...)
    BENIN = Location(...)
    BERMUDA = Location(...)
    BHUTAN = Location(...)
    BOLIVIA = Location(...)
    BOSNIA_AND_HERZEGOVINA = Location(...)
    BOTSWANA = Location(...)
    BOUVET_ISLAND = Location(...)
    BRAZIL = Location(...)
    BRITISH_INDIAN_OCEAN_TERRITORY = Location(...)
    BRITISH_VIRGIN_ISLANDS = Location(...)
    BRUNEI = Location(...)
    BULGARIA = Location(...)
    BURKINA_FASO = Location(...)
    BURUNDI = Location(...)
    CAMBODIA = Location(...)
    CAMEROON = Location(...)
    CANADA = Location(...)
    CANARY_ISLANDS = Location(...)
    CAPE_VERDE = Location(...)
    CARIBBEAN_NETHERLANDS = Location(...)
    CAYMAN_ISLANDS = Location(...)
    CENTRAL_AFRICAN_REPUBLIC = Location(...)
    CEUTA_AND_MELILLA = Location(...)
    CHAD = Location(...)
    CHILE = Location(...)
    CHINA = Location(...)
    CHRISTMAS_ISLAND = Location(...)
    COCOS_KEELING_ISLANDS = Location(...)
    COLOMBIA = Location(...)
    COMOROS = Location(...)
    CONGO_DRC = Location(...)
    CONGO_REPUBLIC = Location(...)
    COOK_ISLANDS = Location(...)
    COSTA_RICA = Location(...)
    CTE_DIVOIRE = Location(...)
    CROATIA = Location(...)
    CUBA = Location(...)
    CURAAO = Location(...)
    CYPRUS = Location(...)
    CZECH_REPUBLIC = Location(...)
    DENMARK = Location(...)
    DIEGO_GARCIA = Location(...)
    DJIBOUTI = Location(...)
    DOMINICA = Location(...)
    DOMINICAN_REPUBLIC = Location(...)
    ECUADOR = Location(...)
    EGYPT = Location(...)
    EL_SALVADOR = Location(...)
    EQUATORIAL_GUINEA = Location(...)
    ERITREA = Location(...)
    ESTONIA = Location(...)
    ETHIOPIA = Location(...)
    FALKLAND_ISLANDS = Location(...)
    FAROE_ISLANDS = Location(...)
    FIJI = Location(...)
    FINLAND = Location(...)
    FRANCE = Location(...)
    FRENCH_GUIANA = Location(...)
    FRENCH_POLYNESIA = Location(...)
    FRENCH_SOUTHERN_TERRITORIES = Location(...)
    GABON = Location(...)
    GAMBIA = Location(...)
    GEORGIA = Location(...)
    GERMANY = Location(...)
    GHANA = Location(...)
    GIBRALTAR = Location(...)
    GREECE = Location(...)
    GREENLAND = Location(...)
    GRENADA = Location(...)
    GUADELOUPE = Location(...)
    GUAM = Location(...)
    GUATEMALA = Location(...)
    GUERNSEY = Location(...)
    GUINEA = Location(...)
    GUINEA_BISSAU = Location(...)
    GUYANA = Location(...)
    HAITI = Location(...)
    HEARD_AND_MCDONALD_ISLANDS = Location(...)
    HONDURAS = Location(...)
    HONG_KONG = Location(...)
    HUNGARY = Location(...)
    ICELAND = Location(...)
    INDIA = Location(...)
    INDONESIA = Location(...)
    IRAN = Location(...)
    IRAQ = Location(...)
    IRELAND = Location(...)
    ISLE_OF_MAN = Location(...)
    ISRAEL = Location(...)
    ITALY = Location(...)
    JAMAICA = Location(...)
    JAPAN = Location(...)
    JERSEY = Location(...)
    JORDAN = Location(...)
    KAZAKHSTAN = Location(...)
    KENYA = Location(...)
    KIRIBATI = Location(...)
    KOSOVO = Location(...)
    KUWAIT = Location(...)
    KYRGYZSTAN = Location(...)
    LAOS = Location(...)
    LATVIA = Location(...)
    LEBANON = Location(...)
    LESOTHO = Location(...)
    LIBERIA = Location(...)
    LIBYA = Location(...)
    LIECHTENSTEIN = Location(...)
    LITHUANIA = Location(...)
    LUXEMBOURG = Location(...)
    MACAU = Location(...)
    NORTH_MACEDONIA = Location(...)
    MADAGASCAR = Location(...)
    MALAWI = Location(...)
    MALAYSIA = Location(...)
    MALDIVES = Location(...)
    MALI = Location(...)
    MALTA = Location(...)
    MARSHALL_ISLANDS = Location(...)
    MARTINIQUE = Location(...)
    MAURITANIA = Location(...)
    MAURITIUS = Location(...)
    MAYOTTE = Location(...)
    MEXICO = Location(...)
    MICRONESIA = Location(...)
    MOLDOVA = Location(...)
    MONACO = Location(...)
    MONGOLIA = Location(...)
    MONTENEGRO = Location(...)
    MONTSERRAT = Location(...)
    MOROCCO = Location(...)
    MOZAMBIQUE = Location(...)
    MYANMAR_BURMA = Location(...)
    NAMIBIA = Location(...)
    NAURU = Location(...)
    NEPAL = Location(...)
    NETHERLANDS = Location(...)
    NEW_CALEDONIA = Location(...)
    NEW_ZEALAND = Location(...)
    NICARAGUA = Location(...)
    NIGER = Location(...)
    NIGERIA = Location(...)
    NIUE = Location(...)
    NORFOLK_ISLAND = Location(...)
    NORTH_KOREA = Location(...)
    NORTHERN_MARIANA_ISLANDS = Location(...)
    NORWAY = Location(...)
    OMAN = Location(...)
    PAKISTAN = Location(...)
    PALAU = Location(...)
    PALESTINE = Location(...)
    PANAMA = Location(...)
    PAPUA_NEW_GUINEA = Location(...)
    PARAGUAY = Location(...)
    PERU = Location(...)
    PHILIPPINES = Location(...)
    PITCAIRN_ISLANDS = Location(...)
    POLAND = Location(...)
    PORTUGAL = Location(...)
    PUERTO_RICO = Location(...)
    QATAR = Location(...)
    RUNION = Location(...)
    ROMANIA = Location(...)
    RUSSIA = Location(...)
    RWANDA = Location(...)
    SAINT_BARTHLEMY = Location(...)
    SAINT_HELENA = Location(...)
    SAINT_KITTS_AND_NEVIS = Location(...)
    SAINT_LUCIA = Location(...)
    SAINT_MARTIN = Location(...)
    SAINT_PIERRE_AND_MIQUELON = Location(...)
    SAMOA = Location(...)
    SAN_MARINO = Location(...)
    SO_TOM_AND_PRNCIPE = Location(...)
    SAUDI_ARABIA = Location(...)
    SENEGAL = Location(...)
    SERBIA = Location(...)
    SEYCHELLES = Location(...)
    SIERRA_LEONE = Location(...)
    SINGAPORE = Location(...)
    SINT_MAARTEN = Location(...)
    SLOVAKIA = Location(...)
    SLOVENIA = Location(...)
    SOLOMON_ISLANDS = Location(...)
    SOMALIA = Location(...)
    SOUTH_AFRICA = Location(...)
    SOUTH_KOREA = Location(...)
    SOUTH_SUDAN = Location(...)
    SPAIN = Location(...)
    SRI_LANKA = Location(...)
    ST_VINCENT_AND_GRENADINES = Location(...)
    SUDAN = Location(...)
    SURINAME = Location(...)
    SVALBARD_AND_JAN_MAYEN = Location(...)
    SWAZILAND = Location(...)
    SWEDEN = Location(...)
    SWITZERLAND = Location(...)
    SYRIA = Location(...)
    TAIWAN = Location(...)
    TAJIKISTAN = Location(...)
    TANZANIA = Location(...)
    THAILAND = Location(...)
    TIMOR_LESTE = Location(...)
    TOGO = Location(...)
    TOKELAU = Location(...)
    TONGA = Location(...)
    TRINIDAD_AND_TOBAGO = Location(...)
    TRISTAN_DA_CUNHA = Location(...)
    TUNISIA = Location(...)
    TRKIYE = Location(...)
    TURKMENISTAN = Location(...)
    TURKS_AND_CAICOS_ISLANDS = Location(...)
    TUVALU = Location(...)
    US_OUTLYING_ISLANDS = Location(...)
    US_VIRGIN_ISLANDS = Location(...)
    UGANDA = Location(...)
    UKRAINE = Location(...)
    UNITED_ARAB_EMIRATES = Location(...)
    UNITED_KINGDOM = Location(...)
    UNITED_STATES = Location(...)
    URUGUAY = Location(...)
    UZBEKISTAN = Location(...)
    VANUATU = Location(...)
    VATICAN_CITY = Location(...)
    VENEZUELA = Location(...)
    VIETNAM = Location(...)
    WALLIS_AND_FUTUNA = Location(...)
    WESTERN_SAHARA = Location(...)
    YEMEN = Location(...)
    ZAMBIA = Location(...)
    ZIMBABWE = Location(...)
    MISSING32000261 = Location(...)
    MISSING32000262 = Location(...)
    MISSING32000263 = Location(...)
    MISSING32000264 = Location(...)
    MISSING32000265 = Location(...)


class Leagues(Enum):
    UNRANKED = League(...)
    BRONZE_LEAGUE_III = League(...)
    BRONZE_LEAGUE_II = League(...)
    BRONZE_LEAGUE_I = League(...)
    SILVER_LEAGUE_III = League(...)
    SILVER_LEAGUE_II = League(...)
    SILVER_LEAGUE_I = League(...)
    GOLD_LEAGUE_III = League(...)
    GOLD_LEAGUE_II = League(...)
    GOLD_LEAGUE_I = League(...)
    CRYSTAL_LEAGUE_III = League(...)
    CRYSTAL_LEAGUE_II = League(...)
    CRYSTAL_LEAGUE_I = League(...)
    MASTER_LEAGUE_III = League(...)
    MASTER_LEAGUE_II = League(...)
    MASTER_LEAGUE_I = League(...)
    CHAMPION_LEAGUE_III = League(...)
    CHAMPION_LEAGUE_II = League(...)
    CHAMPION_LEAGUE_I = League(...)
    TITAN_LEAGUE_III = League(...)
    TITAN_LEAGUE_II = League(...)
    TITAN_LEAGUE_I = League(...)
    LEGEND_LEAGUE = League(...)


class CapitalLeagues(Enum):
    UNRANKED = CapitalLeague(...)
    BRONZE_LEAGUE_III = CapitalLeague(...)
    BRONZE_LEAGUE_II = CapitalLeague(...)
    BRONZE_LEAGUE_I = CapitalLeague(...)
    SILVER_LEAGUE_III = CapitalLeague(...)
    SILVER_LEAGUE_II = CapitalLeague(...)
    SILVER_LEAGUE_I = CapitalLeague(...)
    GOLD_LEAGUE_III = CapitalLeague(...)
    GOLD_LEAGUE_II = CapitalLeague(...)
    GOLD_LEAGUE_I = CapitalLeague(...)
    CRYSTAL_LEAGUE_III = CapitalLeague(...)
    CRYSTAL_LEAGUE_II = CapitalLeague(...)
    CRYSTAL_LEAGUE_I = CapitalLeague(...)
    MASTER_LEAGUE_III = CapitalLeague(...)
    MASTER_LEAGUE_II = CapitalLeague(...)
    MASTER_LEAGUE_I = CapitalLeague(...)
    CHAMPION_LEAGUE_III = CapitalLeague(...)
    CHAMPION_LEAGUE_II = CapitalLeague(...)
    CHAMPION_LEAGUE_I = CapitalLeague(...)
    TITAN_LEAGUE_III = CapitalLeague(...)
    TITAN_LEAGUE_II = CapitalLeague(...)
    TITAN_LEAGUE_I = CapitalLeague(...)
    LEGEND_LEAGUE = CapitalLeague(...)


class BuilderBaseLeagues(Enum):
    WOOD_LEAGUE_V = BuilderBaseLeague(...)
    WOOD_LEAGUE_IV = BuilderBaseLeague(...)
    WOOD_LEAGUE_III = BuilderBaseLeague(...)
    WOOD_LEAGUE_II = BuilderBaseLeague(...)
    WOOD_LEAGUE_I = BuilderBaseLeague(...)
    CLAY_LEAGUE_V = BuilderBaseLeague(...)
    CLAY_LEAGUE_IV = BuilderBaseLeague(...)
    CLAY_LEAGUE_III = BuilderBaseLeague(...)
    CLAY_LEAGUE_II = BuilderBaseLeague(...)
    CLAY_LEAGUE_I = BuilderBaseLeague(...)
    STONE_LEAGUE_V = BuilderBaseLeague(...)
    STONE_LEAGUE_IV = BuilderBaseLeague(...)
    STONE_LEAGUE_III = BuilderBaseLeague(...)
    STONE_LEAGUE_II = BuilderBaseLeague(...)
    STONE_LEAGUE_I = BuilderBaseLeague(...)
    COPPER_LEAGUE_V = BuilderBaseLeague(...)
    COPPER_LEAGUE_IV = BuilderBaseLeague(...)
    COPPER_LEAGUE_III = BuilderBaseLeague(...)
    COPPER_LEAGUE_II = BuilderBaseLeague(...)
    COPPER_LEAGUE_I = BuilderBaseLeague(...)
    BRASS_LEAGUE_III = BuilderBaseLeague(...)
    BRASS_LEAGUE_II = BuilderBaseLeague(...)
    BRASS_LEAGUE_I = BuilderBaseLeague(...)
    IRON_LEAGUE_III = BuilderBaseLeague(...)
    IRON_LEAGUE_II = BuilderBaseLeague(...)
    IRON_LEAGUE_I = BuilderBaseLeague(...)
    STEEL_LEAGUE_III = BuilderBaseLeague(...)
    STEEL_LEAGUE_II = BuilderBaseLeague(...)
    STEEL_LEAGUE_I = BuilderBaseLeague(...)
    TITANIUM_LEAGUE_III = BuilderBaseLeague(...)
    TITANIUM_LEAGUE_II = BuilderBaseLeague(...)
    TITANIUM_LEAGUE_I = BuilderBaseLeague(...)
    PLATINUM_LEAGUE_III = BuilderBaseLeague(...)
    PLATINUM_LEAGUE_II = BuilderBaseLeague(...)
    PLATINUM_LEAGUE_I = BuilderBaseLeague(...)
    EMERALD_LEAGUE_III = BuilderBaseLeague(...)
    EMERALD_LEAGUE_II = BuilderBaseLeague(...)
    EMERALD_LEAGUE_I = BuilderBaseLeague(...)
    RUBY_LEAGUE_III = BuilderBaseLeague(...)
    RUBY_LEAGUE_II = BuilderBaseLeague(...)
    RUBY_LEAGUE_I = BuilderBaseLeague(...)
    DIAMOND_LEAGUE = BuilderBaseLeague(...)


class WarLeagues(Enum):
    UNRANKED = WarLeague(...)
    BRONZE_LEAGUE_III = WarLeague(...)
    BRONZE_LEAGUE_II = WarLeague(...)
    BRONZE_LEAGUE_I = WarLeague(...)
    SILVER_LEAGUE_III = WarLeague(...)
    SILVER_LEAGUE_II = WarLeague(...)
    SILVER_LEAGUE_I = WarLeague(...)
    GOLD_LEAGUE_III = WarLeague(...)
    GOLD_LEAGUE_II = WarLeague(...)
    GOLD_LEAGUE_I = WarLeague(...)
    CRYSTAL_LEAGUE_III = WarLeague(...)
    CRYSTAL_LEAGUE_II = WarLeague(...)
    CRYSTAL_LEAGUE_I = WarLeague(...)
    MASTER_LEAGUE_III = WarLeague(...)
    MASTER_LEAGUE_II = WarLeague(...)
    MASTER_LEAGUE_I = WarLeague(...)
    CHAMPION_LEAGUE_III = WarLeague(...)
    CHAMPION_LEAGUE_II = WarLeague(...)
    CHAMPION_LEAGUE_I = WarLeague(...)


class Labels(Enum):
    ACTIVE_DAILY = Label(...)
    ACTIVE_DONATOR = Label(...)
    AMATEUR_ATTACKER = Label(...)
    BASE_DESIGNING = Label(...)
    BUILDER_BASE = Label(...)
    CLAN_CAPITAL = Label(...)
    CLAN_GAMES = Label(...)
    CLAN_WAR_LEAGUE = Label(...)
    CLAN_WARS = Label(...)
    COMPETITIVE = Label(...)
    DONATIONS = Label(...)
    FARMING = Label(...)
    FRIENDLY = Label(...)
    FRIENDLY_WARS = Label(...)
    HUNGRY_LEARNER = Label(...)
    INTERNATIONAL = Label(...)
    NEWBIE = Label(...)
    NEWBIE_FRIENDLY = Label(...)
    RELAXED = Label(...)
    TROPHY_PUSHING = Label(...)
    TALKATIVE = Label(...)
    TEACHER = Label(...)
    UNDERDOG = Label(...)
    VETERAN = Label(...)


class Languages(Enum):
    """
    not implemented yet
    """

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
    WAR_ENDED = "warEnded"


class ClanWarLeagueGroupState(Enum):
    GROUP_NOT_FOUND = "groupNotFound"
    NOT_IN_WAR = "notInWar"
    PREPARATION = "preparation"
    WAR = "war"
    ENDED = "ended"


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
