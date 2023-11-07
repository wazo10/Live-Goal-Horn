import pip._vendor.requests as req
from bs4 import BeautifulSoup
import pygame as pg
import time


def play_team_horn(num):
    pg.init()
    if num == 0:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/TorontoMapleLeafs2024GoalHorn.mp3')  # 76 sec
    if num == 1:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/AnaheimDucks2024GoalHorn.mp3')  # 46 sec
    if num == 2:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/ArizonaCoyotes2024GoalHorn.mp3')  # 65 sec
    if num == 3:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/BuffaloSabres2024GoalHorn.mp3')  # 62 sec
    if num == 4:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/CalgaryFlames2024GoalHorn.mp3')  # 61 sec
    if num == 5:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/CarolinaHurricanes2024GoalHorn.mp3')  # 67 sec
    if num == 6:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/ChicagoBlackhawks2024GoalHorn.mp3')  # 67 sec
    if num == 7:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/ColoradoAvalanche2024GoalHorn.mp3')  # 91 sec
    if num == 8:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/ColumbusBlueJackets2024GoalHorn.mp3')  # 56 sec
    if num == 9:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/DallasStars2024GoalHorn.mp3')  # 70 sec
    if num == 10:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/DetroitRedWings2024GoalHorn.mp3')  # 62 sec
    if num == 11:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/EdmontonOilers2024GoalHorn.mp3')  # 81 sec
    if num == 12:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/FloridaPanthers2024GoalHorn.mp3')  # 44 sec
    if num == 13:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/LosAngelesKings2024GoalHorn.mp3')  # 48 sec
    if num == 14:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/MinnesotaWild2024GoalHorn.mp3')  # 63 sec
    if num == 15:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/MontrealCanadiens2024GoalHorn.mp3')  # 89 sec
    if num == 16:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/NashvillePredators2024GoalHorn.mp3')  # 62 sec
    if num == 17:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/NewJerseyDevils2024GoalHorn.mp3')  # 52 sec
    if num == 18:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/NewYorkIslanders2024GoalHorn.mp3')  # 49 sec
    if num == 19:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/NewYorkRangers2024GoalHorn.mp3')  # 91 sec
    if num == 20:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/OttawaSenators2024GoalHorn.mp3')  # 66 sec
    if num == 21:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/PhiladelphiaFlyers2024GoalHorn.mp3')  # 57 sec
    if num == 22:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/PittsburghPenguins2024GoalHorn.mp3')  # 65 sec
    if num == 23:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/SanJoseSharks2024GoalHorn.mp3')  # 46 sec
    if num == 24:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/SeattleKraken2024GoalHorn.mp3')  # 50 sec
    if num == 25:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/StLouisBlues2024GoalHorn.mp3')  # 97 sec
    if num == 26:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/TampaBayLightning2024GoalHorn.mp3')  # 59 sec
    if num == 27:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/VancouverCanucks2024GoalHorn.mp3')  # 49 sec
    if num == 28:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/VegasGoldenKnights2024GoalHorn.mp3')  # 70 sec
    if num == 29:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/WashingtonCapitals2024GoalHorn.mp3')  # 71 sec
    if num == 30:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns2024/WinnipegJets2024GoalHorn.mp3')  # 65 sec
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = req.get('https://www.espn.com/nhl/scoreboard', headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
game_scores = soup.find_all('ul', {'class': 'ScoreboardScoreCell__Competitors'})
games = []
for game in game_scores:
    scores = game.find_all('div', {'class': 'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'})
    teams = game.find_all('div', {'class': 'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'})
    teams = [x.text for x in teams]
    scores = [x.text for x in scores]
    games.append(dict(zip(teams, scores)))
tms = ['Maple Leafs', 'Ducks', 'Coyotes', 'Sabres', 'Flames', 'Hurricanes', 'Blackhawks', 'Avalanche', 'Blue Jackets', 'Stars', 'Red Wings', 'Oilers', 'Panthers', 'Kings', 'Wild', 'Canadiens', 'Predators', 'Devils', 'Islanders', 'Rangers', 'Senators', 'Flyers', 'Penguins', 'Sharks', 'Kraken', 'Blues', 'Lightning', 'Canucks', 'Golden Knights', 'Capitals', 'Jets']
scrs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
teams_ = ['TORONTO MAPLE LEAFS', 'ANAHEIM DUCKS', 'ARIZONA COYOTES', 'BUFFALO SABRES', 'CALGARY FLAMES', 'CAROLINA HURRICANES', 'CHICAGO BLACKHAWKS', 'COLORADO AVALANCHE', 'COLUMBUS BLUE JACKETS', 'DALLAS STARS', 'DETROIT RED WINGS', 'EDMONTON OILERS', 'FLORIDA PANTHERS', 'LOS ANGELES KINGS', 'MINNESOTA WILD', 'MONTREAL CANADIENS', 'NASHVILLE PREDATORS', 'NEW JERSEY DEVILS', 'NEW YORK ISLANDERS', 'NEW YORK RANGERS', 'OTTAWA SENATORS', 'PHILADELPHIA FLYERS', 'PITTSBURGH PENGUINS', 'SAN JOSE SHARKS', 'SEATTLE KRAKEN', 'ST LOUIS BLUES', 'TAMPA BAY LIGHTNING', 'VEGAS GOLDEN KNIGHTS', 'WASHINGTON CAPITALS', 'WINNIPEG JETS']
for g in games:
    for i in range(31):
        if g.get(tms[i]) is not None:
            if int(g.get(tms[i])) != scrs[i]:
                scrs[i] = int(g.get(tms[i]))
while True:
    print('--------------------------------------------------')
    page = req.get('https://www.espn.com/nhl/scoreboard', headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    game_scores = soup.find_all('ul', {'class': 'ScoreboardScoreCell__Competitors'})
    games = []
    for game in game_scores:
        scores = game.find_all('div', {'class': 'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'})
        teams = game.find_all('div', {'class': 'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'})
        teams = [x.text for x in teams]
        scores = [x.text for x in scores]
        games.append(dict(zip(teams, scores)))
    for g in games:
        print(g)
        for i in range(31):
            if g.get(tms[i]) is not None:
                if int(g.get(tms[i])) > scrs[i]:
                    scrs[i] = int(g.get(tms[i]))
                    print(teams_[i], 'GOOOAL!!!')
                    play_team_horn(i)
    time.sleep(3)
