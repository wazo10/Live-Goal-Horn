import pip._vendor.requests as req
from bs4 import BeautifulSoup
import pygame as pg
import time
teams_ = ['TORONTO MAPLE LEAFS', 'ANAHEIM DUCKS', 'ARIZONA COYOTES', 'BUFFALO SABRES', 'CALGARY FLAMES', 'CAROLINA HURRICANES', 'CHICAGO BLACKHAWKS', 'COLORADO AVALANCHE', 'COLUMBUS BLUE JACKETS', 'DALLAS STARS', 'DETROIT RED WINGS', 'EDMONTON OILERS', 'FLORIDA PANTHERS', 'LOS ANGELES KINGS', 'MINNESOTA WILD', 'MONTREAL CANADIENS', 'NASHVILLE PREDATORS', 'NEW JERSEY DEVILS', 'NEW YORK ISLANDERS', 'NEW YORK RANGERS', 'OTTAWA SENATORS', 'PHILADELPHIA FLYERS', 'PITTSBURGH PENGUINS', 'SAN JOSE SHARKS', 'SEATTLE KRAKEN', 'ST LOUIS BLUES', 'TAMPA BAY LIGHTNING', 'VEGAS GOLDEN KNIGHTS', 'WASHINGTON CAPITALS', 'WINNIPEG JETS']


def play_team_horn(num):
    print(teams_[num], 'GOOOAL!!!')
    pg.init()
    if num == 0:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Toronto_Maple_Leafs_2023_Goal_Horn.mp3')  # 65 sec
    if num == 1:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Anaheim_Ducks_2023_Goal_Horn.mp3')  # 67 sec
    if num == 2:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Arizona_Coyotes_2023_Goal_Horn.mp3')  # 58 sec
    if num == 3:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Buffalo_Sabres_2023_Goal_Horn.mp3')  # 85 sec
    if num == 4:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Calgary_Flames_2023_Goal_Horn.mp3')  # 65 sec
    if num == 5:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Carolina_Hurricanes_2023_Goal_Horn.mp3')  # 90 sec
    if num == 6:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Chicago_Blackhawks_2023_Goal_Horn.mp3')  # 70 sec
    if num == 7:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Colorado_Avalanche_2023_Goal_Horn.mp3')  # 104 sec
    if num == 8:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Columbus_Blue_Jackets_2023_Goal_Horn.mp3')  # 57 sec
    if num == 9:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Dallas_Stars_2023_Goal_Horn.mp3')  # 69 sec
    if num == 10:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Detroit_Red_Wings_2023_Goal_Horn.mp3')  # 69 sec
    if num == 11:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Edmonton_Oilers_2023_Goal_Horn.mp3')  # 56 sec
    if num == 12:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Florida_Panthers_2023_Goal_Horn.mp3')  # 71 sec
    if num == 13:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Los_Angeles_Kings_2023_Goal_Horn.mp3')  # 72 sec
    if num == 14:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Minnesota_Wild_2023_Goal_Horn.mp3')  # 61 sec
    if num == 15:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Montreal_Canadiens_2023_Goal_Horn.mp3')  # 85 sec
    if num == 16:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Nashville_Predators_2023_Goal_Horn.mp3')  # 60 sec
    if num == 17:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/New_Jersey_Devils_2023_Goal_Horn.mp3')  # 99 sec
    if num == 18:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/New_York_Islanders_2023_Goal_Horn.mp3')  # 40 sec
    if num == 19:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/New_York_Rangers_2023_Goal_Horn.mp3')  # 97 sec
    if num == 20:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Ottawa_Senators_2023_Goal_Horn.mp3')  # 85 sec
    if num == 21:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Philadelphia_Flyers_2023_Goal_Horn.mp3')  # 59 sec
    if num == 22:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Pittsburgh_Penguins_2023_Goal_Horn.mp3')  # 63 sec
    if num == 23:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/San_Jose_Sharks_2023_Goal_Horn.mp3')  # 44 sec
    if num == 24:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Seattle_Kraken_2023_Goal_Horn.mp3')  # 49 sec
    if num == 25:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/St_Louis_Blues_2023_Goal_Horn.mp3')  # 95 sec
    if num == 26:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Tampa_Bay_Lightning_2023_Goal_Horn.mp3')  # 60 sec
    if num == 27:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Vancouver_Canucks_2023_Goal_Horn.mp3')  # 73 sec
    if num == 28:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Vegas_Golden_Knights_2023_Goal_Horn.mp3')  # 67 sec
    if num == 29:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Washington_Capitals_2023_Goal_Horn.mp3')  # 109 sec
    if num == 30:
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Winnipeg_Jets_2023_Goal_Horn.mp3')  # 80 sec
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
                    play_team_horn(i)
    time.sleep(3)
