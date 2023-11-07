# Live Goal Horn

**TLDR:**

Plays NHL team specific goal horn when goal is scored live

**Intro:**

Tired of scoreboard watching the NHL? Well give your eyes a rest and let your ears bleed with Live Goal Horn. Before every evening's slate of NHL games, run this program and you will be pleasantly surprised every time a team scores a goal (except for one team which I have excluded due to their rivalry with my team, but you are welcome to add them on your own).

**How it works:**

Initially I attempted to use APIs to get live scores, but that did not work. Instead, I used requests and BeautifulSoup4 to fetch the scores from espn.com/nhl/scoreboard. All teams scores are stored and if the newly fetched data is greater than the previous scores, that means a goal was scored and that team's goal horn is played. Pygame was used to play the goal horns.

**Dependencies:**

Coming soon...

**Run Instructions:**

Coming soon...

**2023 Goal Horns courtesy of Elite Goal Horns (https://www.youtube.com/@EliteGoalHorns)**

**2024 Goal Horns courtesy of Dr. Goal Horn (https://www.youtube.com/@dr.goalhorn)**

**HAVE FUN!!!**
