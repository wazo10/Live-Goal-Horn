import pip._vendor.requests as req
from bs4 import BeautifulSoup
import pygame as pg
import time


def play_team_horn(num):
    pg.init()
    if num == 0:
        print('TORONTO MAPLE LEAFS GOOOAL!!!')  # 65 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Toronto_Maple_Leafs_2023_Goal_Horn.mp3')
    if num == 1:
        print('ANAHEIM DUCKS GOOOAL!!!')  # 67 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Anaheim_Ducks_2023_Goal_Horn.mp3')
    if num == 2:
        print('ARIZONA COYOTES GOOOAL!!!')  # 58 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Arizona_Coyotes_2023_Goal_Horn.mp3')
    if num == 3:
        print('BUFFALO SABRES GOOOAL!!!')  # 85 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Buffalo_Sabres_2023_Goal_Horn.mp3')
    if num == 4:
        print('CALGARY FLAMES GOOOAL!!!')  # 65 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Calgary_Flames_2023_Goal_Horn.mp3')
    if num == 5:
        print('CAROLINA HURRICANES GOOOAL!!!')  # 90 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Carolina_Hurricanes_2023_Goal_Horn.mp3')
    if num == 6:
        print('CHICAGO BLACKHAWKS GOOOAL!!!')  # 70 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Chicago_Blackhawks_2023_Goal_Horn.mp3')
    if num == 7:
        print('COLORADO AVALANCHE GOOOAL!!!')  # 104 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Colorado_Avalanche_2023_Goal_Horn.mp3')
    if num == 8:
        print('COLUMBUS BLUE JACKETS GOOOAL!!!')  # 57 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Columbus_Blue_Jackets_2023_Goal_Horn.mp3')
    if num == 9:
        print('DALLAS STARS GOOOAL!!!')  # 69 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Dallas_Stars_2023_Goal_Horn.mp3')
    if num == 10:
        print('DETROIT RED WINGS GOOOAL!!!')  # 69 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Detroit_Red_Wings_2023_Goal_Horn.mp3')
    if num == 11:
        print('EDMONTON OILERS GOOOAL!!!')  # 56 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Edmonton_Oilers_2023_Goal_Horn.mp3')
    if num == 12:
        print('FLORIDA PANTHERS GOOOAL!!!')  # 71 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Florida_Panthers_2023_Goal_Horn.mp3')
    if num == 13:
        print('LOS ANGELES KINGS GOOOAL!!!')  # 72 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Los_Angeles_Kings_2023_Goal_Horn.mp3')
    if num == 14:
        print('MINNESOTA WILD GOOOAL!!!')  # 61 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Minnesota_Wild_2023_Goal_Horn.mp3')
    if num == 15:
        print('MONTREAL CANADIENS GOOOAL!!!')  # 85 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Montreal_Canadiens_2023_Goal_Horn.mp3')
    if num == 16:
        print('NASHVILLE PREDATORS GOOOAL!!!')  # 60 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Nashville_Predators_2023_Goal_Horn.mp3')
    if num == 17:
        print('NEW JERSEY DEVILS GOOOAL!!!')  # 99 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/New_Jersey_Devils_2023_Goal_Horn.mp3')
    if num == 18:
        print('NEW YORK ISLANDERS GOOOAL!!!')  # 40 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/New_York_Islanders_2023_Goal_Horn.mp3')
    if num == 19:
        print('NEW YORK RANGERS GOOOAL!!!')  # 97 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/New_York_Rangers_2023_Goal_Horn.mp3')
    if num == 20:
        print('OTTAWA SENATORS GOOOAL!!!')  # 85 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Ottawa_Senators_2023_Goal_Horn.mp3')
    if num == 21:
        print('PHILADELPHIA FLYERS GOOOAL!!!')  # 59 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Philadelphia_Flyers_2023_Goal_Horn.mp3')
    if num == 22:
        print('PITTSBURGH PENGUINS GOOOAL!!!')  # 63 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Pittsburgh_Penguins_2023_Goal_Horn.mp3')
    if num == 23:
        print('SAN JOSE SHARKS GOOOAL!!!')  # 44 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/San_Jose_Sharks_2023_Goal_Horn.mp3')
    if num == 24:
        print('SEATTLE KRAKEN GOOOAL!!!')  # 49 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Seattle_Kraken_2023_Goal_Horn.mp3')
    if num == 25:
        print('ST LOUIS BLUES GOOOAL!!!')  # 95 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/St_Louis_Blues_2023_Goal_Horn.mp3')
    if num == 26:
        print('TAMPA BAY LIGHTNING GOOOAL!!!')  # 60 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Tampa_Bay_Lightning_2023_Goal_Horn.mp3')
    if num == 27:
        print('VANCOUVER CANUCKS GOOOAL!!!')  # 73 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Vancouver_Canucks_2023_Goal_Horn.mp3')
    if num == 28:
        print('VEGAS GOLDEN KNIGHTS GOOOAL!!!')  # 67 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Vegas_Golden_Knights_2023_Goal_Horn.mp3')
    if num == 29:
        print('WASHINGTON CAPITALS GOOOAL!!!')  # 109 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Washington_Capitals_2023_Goal_Horn.mp3')
    if num == 30:
        print("WINNIPEG JETS GOOOAL!!!")  # 80 sec
        pg.mixer.music.load('../LiveGoalHorn/GoalHorns/Winnipeg_Jets_2023_Goal_Horn.mp3')
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)


page = req.get("https://www.espn.com/nhl/scoreboard")
soup = BeautifulSoup(page.content, 'html.parser')
game_scores = soup.find_all("ul", {"class": "ScoreboardScoreCell__Competitors"})
games = []
for game in game_scores:
    scores = game.find_all("div", {"class": "ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"})
    teams = game.find_all("div", {"class": "ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"})
    teams = [x.text for x in teams]
    scores = [x.text for x in scores]
    games.append(dict(zip(teams, scores)))
tms = ["Maple Leafs", "Ducks", "Coyotes", "Sabres", "Flames", "Hurricanes", "Blackhawks", "Avalanche", "Blue Jackets", "Stars", "Red Wings", "Oilers", "Panthers", "Kings", "Wild", "Canadiens", "Predators", "Devils", "Islanders", "Rangers", "Senators", "Flyers", "Penguins", "Sharks", "Kraken", "Blues", "Lightning", "Canucks", "Golden Knights", "Capitals", "Jets"]
scrs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for g in games:
    for i in range(31):
        if g.get(tms[i]) is not None:
            if int(g.get(tms[i])) != scrs[i]:
                scrs[i] = int(g.get(tms[i]))
while True:
    print("--------------------------------------------------")
    page = req.get("https://www.espn.com/nhl/scoreboard")
    soup = BeautifulSoup(page.content, 'html.parser')
    game_scores = soup.find_all("ul", {"class": "ScoreboardScoreCell__Competitors"})
    games = []
    for game in game_scores:
        scores = game.find_all("div", {"class": "ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"})
        teams = game.find_all("div", {"class": "ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"})
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
