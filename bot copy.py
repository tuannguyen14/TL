import requests
from requests.structures import CaseInsensitiveDict
import json
import string
import random
from termcolor import colored
import os
import time
from random import randint, shuffle
from tqdm import tqdm
import math
import urllib.request
from datetime import datetime


skills =   ["Skill Id: 1 Combo", "Skill Id: 2 Crippling Strike", "Skill Id: 3 Weakness", "Skill Id: 4 Battle trance", "Skill Id: 5 Vulnerability", "Skill Id: 10 Elemental disbalance", "Skill Id: 9 Cold Rush", "Skill Id: 6 Flaming Blade", "Skill Id: 7 Acid Burn", "Skill Id: 8 Flesh Erosion","Skill Id: 11 Open Wounds","Skill Id: 12 Sucker Punch","Skill Id: 13 Wildfire", "Skill Id: 14 Vampirism", "Skill Id: 15 Tranquility", "Skill Id: 17 Soul prism", "Skill Id: 16 Enchanted Weapon", "Skill Id: 18 Inner Fire", "Skill Id: 21 Accumulation", "Skill Id: 22 Ionization", "Skill Id: 23 Arms lore", "Skill Id: 24 Fencing", "Skill Id: 25 Critical strike", "Skill Id: 26 Perfect Vessel", "Skill Id: 27 Harmony", "Skill Id: 19 Electric charge", "Skill Id: 20 Lightning burst"]
shuffle(skills)

data1 = [
      "Version: 0.9.2.20221226",
      "Point:1; Monster:1;  ClickCount:" + str(randint(20, 30)) + "; KillTime:" + str(randint(1, 10)) + "; isBoss:false",
      "Point:1; Monster:2;  ClickCount:" + str(randint(20, 30)) + "; KillTime:" + str(randint(1, 10)) + "; isBoss:false",

      "Point:2; Monster:1;  ClickCount:" + str(randint(40, 50)) + "; KillTime:" + str(randint(5, 10)) + "; isBoss:false",
      "Point:2; Monster:2;  ClickCount:" + str(randint(40, 50)) + "; KillTime:" + str(randint(5, 10)) + "; isBoss:false",

      "Point:3; Monster:1;  ClickCount:" + str(randint(60, 70)) + "; KillTime:" + str(randint(10, 15)) + "; isBoss:false",
      "Point:3; Monster:2;  ClickCount:" + str(randint(60, 70)) + "; KillTime:" + str(randint(10, 15)) + "; isBoss:false",

      "Point:4; Monster:1;  ClickCount:" + str(randint(80, 90)) + "; KillTime:" + str(randint(15, 20)) + "; isBoss:false",
      "Point:4; Monster:2;  ClickCount:" + str(randint(80, 90)) + "; KillTime:" + str(randint(15, 20)) + "; isBoss:false",
      "Point:4; Monster:3;  ClickCount:" + str(randint(80, 90)) + "; KillTime:" + str(randint(15, 20)) + "; isBoss:false",

      "Point:5; Monster:1;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:2;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:3;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",

      "Point:6; Monster:1;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:2;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:3;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:7; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:8; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:8; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:8; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:9; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:9; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:9; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      
      "Point:10; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:10; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:10; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:10; Monster:4;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:11; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(30, 35)) + "; isBoss:false",
      "Point:11; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(30, 35)) + "; isBoss:false",
      "Point:11; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(30, 35)) + "; isBoss:false",
      "Point:11; Monster:4;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(30, 35)) + "; isBoss:false",

      "Point:12; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(35, 40)) + "; isBoss:false",
      "Point:12; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(35, 40)) + "; isBoss:false",
      "Point:12; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(35, 40)) + "; isBoss:false",
      "Point:12; Monster:4;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(35, 40)) + "; isBoss:false",
      "Point:12; Monster:5;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(35, 40)) + "; isBoss:false",

      "Point:13; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      "Point:13; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      "Point:13; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      "Point:13; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      "Point:13; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      "Point:13; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      "Point:13; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(40, 50)) + "; isBoss:false",
      
      "Point:14; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:15; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",
      "Point:15; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",
      "Point:15; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",
      "Point:15; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",
      "Point:15; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",
      "Point:15; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",
      "Point:15; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(55, 60)) + "; isBoss:false",

      "Point:16; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",
      "Point:16; Monster:8;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(60, 65)) + "; isBoss:false",

      "Point:17; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:8;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:9;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:10;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:11;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:12;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",
      "Point:17; Monster:13;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(65, 70)) + "; isBoss:false",

      "Point:18; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:8;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:9;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:10;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:11;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:12;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:13;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",
      "Point:18; Monster:14;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(70, 75)) + "; isBoss:false",

      "Point:19; Monster:1;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:2;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:3;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:4;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:5;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:6;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:7;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:8;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:9;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:10;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:11;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:12;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:13;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:14;  ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",
      "Point:19; Monster:15; ClickCount:" + str(randint(1000, 3000)) + "; KillTime:" + str(randint(80, 85)) + "; isBoss:false",

      "Point:20; Monster:0; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:true",
      
      skills[0] + " Time: " + str(randint(1, 3)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[1] + " Time: " +  str(randint(3, 5)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[2] + " Time: " +  str(randint(4, 6)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[3] + " Time: " +  str(randint(6, 8)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[4] + " Time: " +  str(randint(8, 10)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[5] + " Time: " +  str(randint(10, 12)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[6] + " Time: " +  str(randint(12, 14)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[7] + " Time: " +  str(randint(14, 16)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[8] + " Time: " +  str(randint(16, 18)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[9] + " Time: " +  str(randint(18, 20)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[10] + " Time: " +  str(randint(20, 22)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[11] + " Time: " +  str(randint(22, 24)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[12] + " Time: " +  str(randint(24, 26)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[13] + " Time: " +  str(randint(26, 27)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[14] + " Time: " +  str(randint(27, 28)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[15] + " Time: " +  str(randint(28, 29)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[16] + " Time: " +  str(randint(29, 30)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[17] + " Time: " +  str(randint(30, 31)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[18] + " Time: " +  str(randint(31, 32)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[19] + " Time: " +  str(randint(32, 33)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[20] + " Time: " +  str(randint(33, 34)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[21] + " Time: " +  str(randint(34, 35)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[22] + " Time: " +  str(randint(35, 36)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[23] + " Time: " +  str(randint(36, 37)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[24] + " Time: " +  str(randint(37, 38)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[25] + " Time: " +  str(randint(38, 39)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[26] + " Time: " +  str(randint(39, 40)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60))
]


data2 = [
      "Version: 0.9.2.20221226",
       "Point:1; Monster:1;  ClickCount:" + str(randint(20, 30)) + "; KillTime:" + str(randint(1, 10)) + "; isBoss:false",
      "Point:1; Monster:2;  ClickCount:" + str(randint(20, 30)) + "; KillTime:" + str(randint(1, 10)) + "; isBoss:false",

      "Point:2; Monster:1;  ClickCount:" + str(randint(40, 50)) + "; KillTime:" + str(randint(5, 10)) + "; isBoss:false",
      "Point:2; Monster:2;  ClickCount:" + str(randint(40, 50)) + "; KillTime:" + str(randint(5, 10)) + "; isBoss:false",

      "Point:3; Monster:1;  ClickCount:" + str(randint(60, 70)) + "; KillTime:" + str(randint(10, 15)) + "; isBoss:false",
      "Point:3; Monster:2;  ClickCount:" + str(randint(60, 70)) + "; KillTime:" + str(randint(10, 15)) + "; isBoss:false",
      "Point:3; Monster:2;  ClickCount:" + str(randint(60, 70)) + "; KillTime:" + str(randint(10, 15)) + "; isBoss:false",
      
      "Point:4; Monster:3;  ClickCount:" + str(randint(80, 90)) + "; KillTime:" + str(randint(15, 20)) + "; isBoss:false",
      "Point:4; Monster:3;  ClickCount:" + str(randint(80, 90)) + "; KillTime:" + str(randint(15, 20)) + "; isBoss:false",
      "Point:4; Monster:3;  ClickCount:" + str(randint(80, 90)) + "; KillTime:" + str(randint(15, 20)) + "; isBoss:false",

      "Point:5; Monster:1;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:2;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:3;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:3;  ClickCount:" + str(randint(100, 110)) + "; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      
      "Point:6; Monster:1;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:2;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:1;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:2;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:3;  ClickCount:" + str(randint(110, 120)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:7; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:1;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:2;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:3;  ClickCount:" + str(randint(100, 300)) + "; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:8; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:8; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      
      "Point:9; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:9; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",

      "Point:10; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:9; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:10; Monster:10; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      
      "Point:11; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:9; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:11; Monster:10; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",

      "Point:12; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:9; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:10; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:11; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:12; Monster:12; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",

      "Point:13; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:9; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:10; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:11; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:13; Monster:12; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",

      "Point:14; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:9; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:10; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:11; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:12; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:13; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:14; Monster:14; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",

      "Point:15; Monster:1; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:2; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:3; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:4; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:5; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:6; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:7; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:8; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:9; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:10; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:11; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:12; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:13; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:14; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:15; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",
      "Point:15; Monster:16; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:false",

      "Point:16; Monster:0; ClickCount:" + str(randint(3000, 5000)) + "; KillTime:" + str(randint(90, 100)) + "; isBoss:true",
      
      skills[0] + " Time: " + str(randint(1, 3)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[1] + " Time: " +  str(randint(3, 5)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[2] + " Time: " +  str(randint(4, 6)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[3] + " Time: " +  str(randint(6, 8)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[4] + " Time: " +  str(randint(8, 10)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[5] + " Time: " +  str(randint(10, 12)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[6] + " Time: " +  str(randint(12, 14)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[7] + " Time: " +  str(randint(14, 16)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[8] + " Time: " +  str(randint(16, 18)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[9] + " Time: " +  str(randint(18, 20)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[10] + " Time: " +  str(randint(20, 22)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[11] + " Time: " +  str(randint(22, 24)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[12] + " Time: " +  str(randint(24, 26)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[13] + " Time: " +  str(randint(26, 27)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[14] + " Time: " +  str(randint(27, 28)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[15] + " Time: " +  str(randint(28, 29)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[16] + " Time: " +  str(randint(29, 30)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[17] + " Time: " +  str(randint(30, 31)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[18] + " Time: " +  str(randint(31, 32)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[19] + " Time: " +  str(randint(32, 33)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60)),
      skills[20] + " Time: " +  str(randint(33, 34)) + " : " + str(randint(1, 60)) + " : " + str(randint(1, 60))
   ]

    # "21": "zanglam192929",
emailObjectNumber = {}

def isConnect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

with open('emails.json', 'r') as openfile:
    emailObjectNumber = json.load(openfile)

password = "AdMiN123"

numberInput = int(input())
currentNumber = 0
pointLeft = 20
gameData = []
accessToken = []
maintoken = ""
timer = 1
dataEnd = None
randomEndData = None

headers = CaseInsensitiveDict()
headers["Host"] = "game-api.tl.games"
headers["Accept"] = "*/*"
headers["Content-Type"] = "application/json"
headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"
headers["Accept-Encoding"] = "gzip, deflate"

def isConnect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def onPrint(text, color):
  print(colored(" " + str(text), color))

def loading(timeLoop):
  timeLoop = math.floor(timeLoop)
  for i in tqdm(range(timeLoop)):
    time.sleep(1)

def onLogin(email):
    url = "https://game-api.tl.games/auth/login"

    headersLogin = CaseInsensitiveDict()
    headersLogin["Host"] = "game-api.tl.games"
    headersLogin["Connection"] = "keep-alive"
    headersLogin["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"
    headersLogin["Content-Type"] = "application/json"
    headersLogin["Accept"] = "*/*"
    headersLogin["Origin"] = "app://"
    headersLogin["Sec-Fetch-Site"] = "cross-site"
    headersLogin["Sec-Fetch-Mode"] = "cors"
    headersLogin["Sec-Fetch-Dest"] = "empty"
    headersLogin["Accept-Language"] = "en-US"
    headersLogin["Accept-Encoding"] = "gzip, deflate"

    data = {
        "email": email + '@gmail.com',
        "password": email
    }

    onPrint(email, "green")

    respLogin = requests.post(url, headers=headersLogin, data=json.dumps(data))
    
    if (respLogin.status_code == 200):
        global accessToken
        loginResult = json.loads(respLogin.content)
        print(loginResult)
        accessToken.append(loginResult['accessToken'])
        onPrintCurrentAccount()
        onPrint("   Login success!", "green")


        # onChangeGender(loginResult['accessToken'])
        # onChangeNickname(loginResult['accessToken'], email)
        
    else:
        onPrint("   Login failed!", "red")
        # print(loginResult)

def onChangeGender(accessToken1):
    url = "https://game-api.tl.games/game/player/gender?authToken=" + accessToken1

    data = {
        "gender" : "male"
    }

    resp = requests.post(url, headers=headers, data=json.dumps(data))

    if (resp.status_code == 200):
        result = json.loads(resp.content)
        onPrint("   Change gender success!", "green")
    else:
        onPrint("   Change gender failed!", "red")
        #print(result)

def onChangeNickname(accessToken1, email):
    url = "https://game-api.tl.games/game/player/nickname?authToken=" + accessToken1

    data = {
        "nickname": email 
    }

    resp = requests.post(url, headers=headers, data=json.dumps(data))

    if (resp.status_code == 200):
        result = json.loads(resp.content)
        #print(result)
        onPrint("   Change nickname success!", "green")
    else:
        onPrint("   Change nickname failed!", "red")
        #print(result)

def onStartGame(currentNumber):
    url = "https://game-api.tl.games/game/start?auto=0"

    data = {
        "mine" : "common",
        "authToken" : accessToken[currentNumber],
        "client_data" : [ "Platform: Windows", "DeviceID: ", "Version: 0.9.2.20221226" ]
    }
    try:
        resp = requests.post(url, headers=headers, data=json.dumps(data))

        if (resp.status_code == 200):
            result = json.loads(resp.content)
            global gameData
            gameData.append(result)
            onPrintCurrentAccount()
            #print(result)
            onPrint("   Start game success!", "green")
        else:
            onPrint("   Start game failed!", "red")
            #print(result)
    except:
        onStartGame(currentNumber)

def onUpdateBalance(currentNumber):
    url = "https://game-api.tl.games/game-account/gold-balance"

    data = {
        "authToken" : accessToken[currentNumber],
        "goldBalance" : randint(1, 17),
        "operation" : "increase"
    }
    try:
        respLogin = requests.post(url, headers=headers, data=json.dumps(data))
        

        if (respLogin.status_code == 200):
            onPrintCurrentAccount()
            # result = json.loads(respLogin.content)
            #print(result)
            onPrint("   Update balance success!", "green")
        else:
            onPrint("   Update balance failed!", "red")
            #print(result)
    except:
        onUpdateBalance(currentNumber)

def onUpdateResouce(currentNumber):
    url = "https://game-api.tl.games/clicker/lobby/event?authToken=" + accessToken[currentNumber]

    data = {
        "event" : "MonsterCommonSpawn",
        "lobbyId" : gameData[currentNumber]['lobbyId']
    }
    try:
        respLogin = requests.post(url, headers=headers, data=json.dumps(data))

        if (respLogin.status_code == 200):
            onPrintCurrentAccount()
            # result = json.loads(respLogin.content)
            #print(result)
            onPrint("   Update Resouce success!", "green")
        else:
            onPrint("   Update Resouce failed!", "red")
            #print(result)
    except:
        onUpdateResouce(currentNumber)

def onUpdateTime(currentNumber):
    url = "https://game-api.tl.games/clicker/lobby/timeSpent?authToken=" + accessToken[currentNumber]

    data = {
        "lobbyId" : gameData[currentNumber]['lobbyId'],
        "time" : 300
    }
    try:
        respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    
        if (respLogin.status_code == 200):
            onPrintCurrentAccount()
            # result = json.loads(respLogin.content)
            #print(result)
            onPrint("   Update time success!", "green")
        else:
            onPrint("   Update time failed!", "red")
            #print(result)
    except:
        onUpdateTime(currentNumber)


def onGetStatGame(currentNumber):
    url = "https://game-api.tl.games/game/stats"

    data = {
        "lobbyId" : gameData[currentNumber]['lobbyId'],
        "stats" : dataEnd[randomEndData]
    }
    try:
        resp = requests.post(url, headers=headers, data=json.dumps(data))

        if (resp.status_code == 200):
            # result = json.loads(resp.content)
            onPrintCurrentAccount()
            onPrint("   Get Stat game sucess!", "green")
        else:
            onPrint("   Get Stat game failed!", "red")
            #print(result)
    except:
        onGetStatGame(currentNumber)


def onEndGame(currentNumber):
    url = "https://game-api.tl.games/game/end"

    data = {
        "client_data" : [ "Platform: Windows", "DeviceID: ", "Version: 0.9.2.20221226" ],
        "lobbyId" : gameData[currentNumber]['lobbyId'],
        "result" : "true",
        "secretKey" : gameData[currentNumber]['secretKey']
    }

    try:
        resp = requests.post(url, headers=headers, data=json.dumps(data))
        

        if (resp.status_code == 200):
            onPrintCurrentAccount()
            result = json.loads(resp.content)
            onPrint("   End game success!", "green")
            return result

        else:
            onPrint("   End game failed!", "red")
            #print(result)
    except:
        onEndGame(currentNumber)

def onPrintTime():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    # print("Time: ", current_time)
    return "Time: " + current_time

def onHireMonster(token):
    url = "https://game-api.tl.games/minigame/squad/hire?authToken=" + token

    data = {}

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        onPrint("   Hire monster success!", "green")

    else:
        onPrint("   Hire monster failed!", "red")

def onGetMonster(token):
    url = "https://game-api.tl.games/game-inventory/items?authToken=" + token + "&itemType=monster"

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get monster success!", "green")
        return result

    else:
        onPrint("   Get monster failed!", "red")

def onGetLastLobby(token):
    url = "https://game-api.tl.games/clicker/currentLobbyInfo?authToken=" + token

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get Last Lobby success!", "green")
        return result

    else:
        onPrint("   Get Last Lobby failed!", "red")
        #print(result)

def onCancelLastLobby(token, id):
    url = "https://game-api.tl.games/clicker/lobby/cancel?authToken=" + token

    data = {
        "lobbyId" : id
    }

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Cancel Last Lobby success!", "green")
        return result

    else:
        onPrint("   Cancel Last Lobby failed!", "red")
        #print(result)

def onEquiptMonster(token, id):
    url = "https://game-api.tl.games/game-inventory/equip?authToken=" + token

    data = {
        "itemId" : id
    }

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Equipt item success!", "green")
        return result

    else:
        onPrint("   Equipt item failed!", "red")

def onGetSpy(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    url = "https://game-api.tl.games/minigame/spy?authToken=" + accessToken[currentNumber]

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get spy success!", "green")
        return result

    else:
        onPrint("   Get spy failed!", "red")
        #print(result)

def onSendSpy(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    dataSpy = onGetSpy(currentNumber)
    onUpgradeSpy(dataSpy, currentNumber)
    if dataSpy['spy']['cooldownSeconds'] == 0:
        enemies = onGetEnemies(currentNumber)
        url = "https://game-api.tl.games/minigame/spy/spying?authToken=" + accessToken[currentNumber]

        if len(enemies['journal']) > 0:
            for enemy in enemies['journal']:
                
                print(enemy)
                if not enemies['journal'][enemy]['spiedOn']:
                    data = {
                        "enemyId" : enemy
                    }

                    resp = requests.post(url, headers=headers, data=json.dumps(data))

                    if (resp.status_code == 200):
                        onPrintCurrentAccount()
                        result = json.loads(resp.content)
                        print(result)
                        onPrint("   Send spy success!", "green")
                        # return result
                    else:
                        onPrint("   Send spy failed!", "red")
                        time.sleep(500)
                    return

def onUpgradeSpy(dataSpy, currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    if dataSpy['spy']['exp'] == dataSpy['spy']['maxExp']:
        url = "https://game-api.tl.games/minigame/spy/upgrade?authToken=" + accessToken[currentNumber]

        data = {}

        resp = requests.post(url, headers=headers, data=json.dumps(data))
        
        if (resp.status_code == 200):
            onPrintCurrentAccount()
            result = json.loads(resp.content)
            onPrint("   Upgrade spy success!", "green")
            return result

        else:
            onPrint("   Upgrade spy failed!", "red")
            #print(result)

def onSendScout(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    dataScrout = onGetScrout(currentNumber)
    onUpgradeScout(dataScrout, currentNumber)
    if dataScrout['scout']['cooldownSeconds'] == 0:
        url = "https://game-api.tl.games/minigame/scout/scouting?authToken=" + accessToken[currentNumber]

        data = {}

        resp = requests.post(url, headers=headers, data=json.dumps(data))
        
        if (resp.status_code == 200):
            onPrintCurrentAccount()
            result = json.loads(resp.content)
            onPrint("   Hire monster success!", "green")
            return result

        else:
            onPrint("   Hire monster failed!", "red")
            #print(result)

def onUpgradeScout(dataScrout, currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    if dataScrout['scout']['exp'] == dataScrout['scout']['maxExp']:
        url = "https://game-api.tl.games/minigame/scout/upgrade?authToken=" + accessToken[currentNumber]

        data = {}

        resp = requests.post(url, headers=headers, data=json.dumps(data))
        
        if (resp.status_code == 200):
            onPrintCurrentAccount()
            result = json.loads(resp.content)
            onPrint("   Upgrade scout success!", "green")
            return result

        else:
            onPrint("   Upgrade scout failed!", "red")
            #print(result)

def onGetScrout(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    url = "https://game-api.tl.games/minigame/scout?authToken=" + accessToken[currentNumber]

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get spy success!", "green")
        return result

    else:
        onPrint("   Get spy failed!", "red")
        #print(result)

def onGetEnemies(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    url = "https://game-api.tl.games/minigame/journal?authToken=" + accessToken[currentNumber]

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get enemies success!", "green")
        return result

    else:
        onPrint("   Get enemies failed!", "red")
        #print(result)

def onGetAttack(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    url = "https://game-api.tl.games/minigame/squad?authToken=" + accessToken[currentNumber]

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get attack success!", "green")
        return result

    else:
        onPrint("   Get attack failed!", "red")
        #print(result)

def onConfirmSqual(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    url = "https://game-api.tl.games/minigame/squad/confirm?authToken=" + accessToken[currentNumber]

    data = {}

    resp = requests.post(url, headers=headers, data=json.dumps(data))
        
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Confirm attack success!", "green")
        return result

    else:
        onPrint("   Confirm attack failed!", "red")
        #print(result)
    

def onAttackEnemy(currentNumber):
    headers["Authorization"] = accessToken[currentNumber]
    dataAttack = onGetAttack(currentNumber)
    if dataAttack['canAttack']:
        enemies = onGetEnemies(currentNumber)
        url = "https://game-api.tl.games/minigame/squad/attack?authToken=" + accessToken[currentNumber]

        if len(enemies['journal']) > 0:
            target = {'id': None, 'squad': 0, 'crystal': -1}
            for enemy in enemies['journal']:
                if  enemies['journal'][enemy]['spiedOn'] and enemies['journal'][enemy]['resources']['squad'] > -1 and enemies['journal'][enemy]['resources']['squad'] <= target['squad'] and enemies['journal'][enemy]['resources']['crystal'] > target['crystal']:
                    target['id'] = enemy
                    target['squad'] = enemies['journal'][enemy]['resources']['squad']
            
            if target['id'] != None:
                data = {
                    "enemyId" : target['id']
                }

                resp = requests.post(url, headers=headers, data=json.dumps(data))
                        
                if (resp.status_code == 200):
                    onPrintCurrentAccount()
                    result = json.loads(resp.content)
                    onPrint("   Attack player success!", "green")
                    return result
                else:
                    onPrint("   Attack player failed!", "red")
                    #print(result)

def onRentAndEquiptMosnter(currentNumber):
    monsters = onGetMonster(accessToken[currentNumber])
    for m in range(0, 9 - len(monsters['items'])):
        onHireMonster(accessToken[currentNumber])

    lastLobbdy = onGetLastLobby(accessToken[currentNumber])
    if lastLobbdy['mode'] != 'idle':
        onCancelLastLobby(accessToken[currentNumber], lastLobbdy['lobbyId'])

    monsters = onGetMonster(accessToken[currentNumber])
    for monster in monsters['items']:
        if not monster['isEquip']:
            onEquiptMonster(accessToken[currentNumber], monster['_id'])

def onGetItems(currentNumber, type):
    url = "https://game-api.tl.games/game-inventory/items?authToken=" + accessToken[currentNumber] + "&itemType=" + type

    resp = requests.get(url, headers=headers)
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Get items success!", "green")
        return result

    else:
        onPrint("   Get items failed!", "red")

def onEquiptItems(currentNumber, id):
    url = "https://game-api.tl.games/game-inventory/equip?authToken=" + accessToken[currentNumber]

    data = {
        "itemId": id
    }

    print(data)

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Equipt items success!", "green")
        return result

    else:
        onPrint("   Equipt items failed!", "red")

def onUnequiptItems(currentNumber, id):
    url = "https://game-api.tl.games/game-inventory/unequip?authToken=" + accessToken[currentNumber]

    data = {
        "itemId": id
    }

    print(data)

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    
    if (resp.status_code == 200):
        onPrintCurrentAccount()
        result = json.loads(resp.content)
        onPrint("   Equipt items success!", "green")
        return result

    else:
        onPrint("   Equipt items failed!", "red")

totalAccount = 1

def onPrintCurrentAccount():
    os.system('cls||clear')

    onPrint(str(int(numberInput) + 1) + '-' + str(int(numberInput) + totalAccount), 'yellow')
    onPrint(str(int(currentNumber) + int(numberInput) + 1), 'white')
    onPrint(str(pointLeft) + " left", 'white')
    # onPrintTime()

def main():
    try:
        emails = {}
        for number in emailObjectNumber:
            if (int(number) > numberInput):
                emails[number] = emailObjectNumber[number]
            if (int(number) == numberInput + totalAccount):
                break
        
        lastTimeAttack = 0
        isFirstTime = True

        while (True):
            begin = time.time() + 2100
            global currentNumber
            global accessToken
            global gameData
            global pointLeft
            global dataEnd
            global randomEndData

            currentNumber = 0
            pointLeft = 20
            gameData = []
            accessToken = []

            dataEnd = [data1, data2]
            randomEndData = randint(0, 1)
            roundEnd = 20
            timeNextPoint = 72
            if randomEndData == 1:
                roundEnd = 16
                timeNextPoint = 90

            os.system('cls||clear')

            for number in emails:
                email = emails[number]
                onLogin(email)
            
            # return

# Cancel Lobby
            if isFirstTime:
                for number in emails:
                    lastLobbdy = onGetLastLobby(accessToken[int(number) - 1 - numberInput])
                    if lastLobbdy['mode'] != 'idle':
                        onCancelLastLobby(accessToken[int(number) - 1 - numberInput], lastLobbdy['lobbyId'])
                isFirstTime = False

            # for number in emails:
            #     swords = onGetItems(int(number) - 1 - numberInput, 'sword')
            #     for sword in swords['items']:
            #         if sword['isEquip']:
            #             onUnequiptItems(int(number) - 1 - numberInput, sword['_id'])
            #     armors = onGetItems(int(number) - 1 - numberInput, 'armor')
            #     for armor in armors['items']:
            #         if armor['isEquip']:
            #             onUnequiptItems(int(number) - 1 - numberInput, armor['_id'])
            # ##########################################################################################

# #PvP
            # now = time.time()
    
            # for number in emails:
            #     onRentAndEquiptMosnter(int(number) - 1 - numberInput)
            # if int(now) - int(lastTimeAttack) > 0:
            #     for number in emails:
            #             currentNumber = str(int(number) - 1 - numberInput)
            #             onConfirmSqual(int(number) - 1 - numberInput)
            #             onSendSpy(int(number) - 1 - numberInput)
            #             onSendScout(int(number) - 1 - numberInput)
            #             onAttackEnemy(int(number) - 1 - numberInput)
            #             lastTimeAttack = time.time() + 10,800
            ##########################################################################################


# Play Game
            for number in emails:
                currentNumber = str(int(number) - 1 - numberInput)
                onStartGame(int(number) - 1 - numberInput)

            lastTimeUpdateTime = time.time() + 300
            lastTimeUpdateResource = time.time() + randint(30, 60)
            lastTimeNextPoint = time.time() + timeNextPoint

            roundCounter = 1

            while True:
                now = time.time()

                if now - lastTimeUpdateTime > 0:
                    for number in emails:
                        currentNumber = str(int(number) - 1 - numberInput)
                        onUpdateTime(int(number) - 1 - numberInput)
                    lastTimeUpdateTime = time.time() + 300
                
                if now - lastTimeUpdateResource > 0:
                    for number in emails:
                        currentNumber = str(int(number) - 1 - numberInput)
                        onUpdateResouce(int(number) - 1 - numberInput)
                    lastTimeUpdateResource = time.time() + randint(30, 60)
                
                if now - lastTimeNextPoint > 0:
                    for number in emails:
                        currentNumber = str(int(number) - 1 - numberInput)
                        onUpdateBalance(int(number) - 1 - numberInput)
                    roundCounter = roundCounter + 1
                    pointLeft = roundEnd - roundCounter + 1
                    lastTimeNextPoint = time.time() + timeNextPoint
                
                remainTime = begin - time.time() 
                if remainTime <= 0:
                   lastTimeNextPoint = time.time()
                   
                if roundCounter > roundEnd:
                    break

                time.sleep(0.5)

            remainTime = begin - time.time() + 300
            if remainTime <= 0:
                for number in emails:
                    currentNumber = str(int(number) - 1 - numberInput)
                    onGetStatGame(int(number) - 1 - numberInput)
                    result = onEndGame(int(number) - 1 - numberInput)
                    onPrint(result, "green")
                    if (not result['status']):
                        onPrint(result, "red")

            else:
                loading(remainTime + 70)
                for number in emails:
                    currentNumber = str(int(number) - 1 - numberInput)
                    onGetStatGame(int(number) - 1 - numberInput)
                    result = onEndGame(int(number) - 1 - numberInput)
                    onPrint(result, "green")
                    if (not result['status']):
                        onPrint(result, "red")

    except Exception as e:
        onPrint(e, 'red')
        loading(78)
        main()
        
main()  