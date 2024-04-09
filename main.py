import requests
import random
from flask import Flask, render_template
app = Flask(__name__)

ip = requests.get('https://api.ipify.org').text
api_key = "at_TGFZTCVqhr6MAWoXTYTMcfJ99Md8c"


def geolocator(ip):
    try:
        response = requests.get(f"https://geo.ipify.org/api/v2/country,city?apiKey={api_key}&ipAddress={ip}")
        if response.status_code == 200:
            data = response.json() 
            location_info = data.get("location", {})
            Region = location_info.get("region")
            return Region
        else:
            print("An Error Occurred!")
    except Exception as e:
        print("An error occurred:", e)
        return None


def states():
    all_states = {}
    
    Alabama = {
        "What is the capital city of Alabama?": {
            "options": ["A) Birmingham", "B) Huntsville", "C) Montgomery", "D) Mobile"],
            "answer": "C) Montgomery"
        },
        "Which river forms the western boundary of Alabama?": {
            "options": ["A) Tennessee River", "B) Mississippi River", "C) Chattahoochee River", "D) Alabama River"],
            "answer": "B) Mississippi River"
        },
        "What is the nickname of Alabama?": {
            "options": ["A) The Sunshine State", "B) The Heart of Dixie", "C) The Yellowhammer State", "D) The Magnolia State"],
            "answer": "C) The Yellowhammer State"
        },
        "Who was the first female African-American astronaut from Alabama?": {
            "options": ["A) Sally Ride", "B) Mae Jemison", "C) Guion Bluford", "D) Ellen Ochoa"],
            "answer": "B) Mae Jemison"
        },
        "Which university is located in Tuscaloosa, Alabama, and is known for its football team?": {
            "options": ["A) Auburn University", "B) University of Alabama", "C) Alabama State University", "D) Troy University"],
            "answer": "B) University of Alabama"
        },
        "Which city in Alabama was the first capital of the Confederate States of America?": {
            "options": ["A) Birmingham", "B) Huntsville", "C) Montgomery", "D) Mobile"],
            "answer": "C) Montgomery"
        },
        "What is the official state bird of Alabama?": {
            "options": ["A) Robin", "B) Eagle", "C) Yellowhammer", "D) Cardinal"],
            "answer": "C) Yellowhammer"
        },
        "Which famous civil rights activist was born in Tuskegee, Alabama, and founded the Tuskegee Institute?": {
            "options": ["A) Martin Luther King Jr.", "B) Rosa Parks", "C) Malcolm X", "D) Booker T. Washington"],
            "answer": "D) Booker T. Washington"
        },
        "What is the highest point in Alabama?": {
            "options": ["A) Cheaha Mountain", "B) Lookout Mountain", "C) Mount Baldy", "D) Red Mountain"],
            "answer": "A) Cheaha Mountain"
        },
        "Which Alabama city was the site of the Montgomery Bus Boycott in 1955?": {
            "options": ["A) Birmingham", "B) Montgomery", "C) Selma", "D) Mobile"],
            "answer": "B) Montgomery"
        }
    }
    Alaska = {
        "What is the capital city of Alaska?": {
            "options": ["A) Anchorage", "B) Fairbanks", "C) Juneau", "D) Sitka"],
            "answer": "C) Juneau"
        },
        "Which U.S. state is the largest in terms of area?": {
            "options": ["A) Texas", "B) California", "C) Alaska", "D) Florida"],
            "answer": "C) Alaska"
        },
        "What is the highest peak in North America, located in Alaska?": {
            "options": ["A) Mount Everest", "B) Mount Kilimanjaro", "C) Denali", "D) Mount Rainier"],
            "answer": "C) Denali"
        },
        "Which Alaskan city is known as the 'gateway to Denali National Park'?": {
            "options": ["A) Anchorage", "B) Fairbanks", "C) Juneau", "D) Talkeetna"],
            "answer": "D) Talkeetna"
        },
        "What is the name of the indigenous people of Alaska?": {
            "options": ["A) Inuit", "B) Apache", "C) Sioux", "D) Cherokee"],
            "answer": "A) Inuit"
        },
        "Which month does the Iditarod Trail Sled Dog Race typically start in Alaska?": {
            "options": ["A) January", "B) February", "C) March", "D) April"],
            "answer": "B) February"
        },
        "What is the state flower of Alaska?": {
            "options": ["A) Forget-me-not", "B) Rose", "C) Lily", "D) Daisy"],
            "answer": "A) Forget-me-not"
        },
        "Which Alaskan city is the northernmost in the United States?": {
            "options": ["A) Barrow", "B) Anchorage", "C) Juneau", "D) Fairbanks"],
            "answer": "A) Barrow"
        },
        "What is the official state nickname of Alaska?": {
            "options": ["A) The Last Frontier", "B) The Golden State", "C) The Equality State", "D) The Beehive State"],
            "answer": "A) The Last Frontier"
        },
        "Which U.S. president famously purchased Alaska from Russia in 1867?": {
            "options": ["A) Abraham Lincoln", "B) Thomas Jefferson", "C) Andrew Johnson", "D) William Seward"],
            "answer": "D) William Seward"
        }
    }
    Arizona = {
            "What is the capital city of Arizona?": {
            "options": ["A) Phoenix", "B) Tucson", "C) Scottsdale", "D) Mesa"],
            "answer": "A) Phoenix"
        },
        "Which national park in Arizona is known for its grand canyon?": {
            "options": ["A) Grand Canyon National Park", "B) Zion National Park", "C) Yellowstone National Park", "D) Yosemite National Park"],
            "answer": "A) Grand Canyon National Park"
        },
        "What is the state bird of Arizona?": {
            "options": ["A) Bald Eagle", "B) Cactus Wren", "C) Roadrunner", "D) Cardinal"],
            "answer": "B) Cactus Wren"
        },
        "Which desert covers much of the southern and western parts of Arizona?": {
            "options": ["A) Mojave Desert", "B) Sahara Desert", "C) Gobi Desert", "D) Sonoran Desert"],
            "answer": "D) Sonoran Desert"
        },
        "What is the nickname of Arizona?": {
            "options": ["A) The Golden State", "B) The Grand Canyon State", "C) The Sunshine State", "D) The Lone Star State"],
            "answer": "B) The Grand Canyon State"
        },
        "Which city in Arizona is known for its annual Fiesta Bowl football game?": {
            "options": ["A) Phoenix", "B) Scottsdale", "C) Tucson", "D) Tempe"],
            "answer": "D) Tempe"
        },
        "What is the tallest mountain in Arizona?": {
            "options": ["A) Mount Lemmon", "B) Mount Baldy", "C) Humphreys Peak", "D) Mount Graham"],
            "answer": "C) Humphreys Peak"
        },
        "Which Native American tribe is known for their cliff dwellings at Montezuma Castle National Monument in Arizona?": {
            "options": ["A) Navajo", "B) Apache", "C) Hopi", "D) Sinagua"],
            "answer": "D) Sinagua"
        },
        "Which university in Arizona is known as the home of the Wildcats?": {
            "options": ["A) University of Arizona", "B) Arizona State University", "C) Northern Arizona University", "D) Grand Canyon University"],
            "answer": "A) University of Arizona"
        },
        "Which canyon in Arizona is known as the Grand Canyon of the Pacific?": {
            "options": ["A) Antelope Canyon", "B) Salt River Canyon", "C) Canyon de Chelly", "D) Waimea Canyon"],
            "answer": "D) Waimea Canyon"
        }
    }
    Arkansas = {
            "What is the capital city of Arkansas?": {
            "options": ["A) Little Rock", "B) Fayetteville", "C) Hot Springs", "D) Jonesboro"],
            "answer": "A) Little Rock"
        },
        "Which river forms much of the eastern border of Arkansas?": {
            "options": ["A) Mississippi River", "B) Colorado River", "C) Missouri River", "D) Ohio River"],
            "answer": "A) Mississippi River"
        },
        "What is the state bird of Arkansas?": {
            "options": ["A) Mockingbird", "B) Cardinal", "C) Blue jay", "D) Mockingjay"],
            "answer": "B) Cardinal"
        },
        "Which national park in Arkansas is known for its hot springs?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon National Park", "C) Hot Springs National Park", "D) Great Smoky Mountains National Park"],
            "answer": "C) Hot Springs National Park"
        },
        "What is the nickname of Arkansas?": {
            "options": ["A) The Natural State", "B) The Volunteer State", "C) The Sunshine State", "D) The Hoosier State"],
            "answer": "A) The Natural State"
        },
        "Which city in Arkansas is home to the University of Arkansas?": {
            "options": ["A) Little Rock", "B) Fayetteville", "C) Hot Springs", "D) Jonesboro"],
            "answer": "B) Fayetteville"
        },
        "What is the tallest mountain in Arkansas?": {
            "options": ["A) Mount Magazine", "B) Pinnacle Mountain", "C) Mount Nebo", "D) Mount Ida"],
            "answer": "A) Mount Magazine"
        },
        "Which U.S. president was born in Hope, Arkansas?": {
            "options": ["A) Bill Clinton", "B) George W. Bush", "C) Barack Obama", "D) Ronald Reagan"],
            "answer": "A) Bill Clinton"
        },
        "Which river flows through the Ozarks and the Mississippi Alluvial Plain in Arkansas?": {
            "options": ["A) Arkansas River", "B) Red River", "C) White River", "D) Ouachita River"],
            "answer": "C) White River"
        },
        "Which Arkansas city is known for its annual Duck Calling Contest?": {
            "options": ["A) Little Rock", "B) Fayetteville", "C) Stuttgart", "D) Pine Bluff"],
            "answer": "C) Stuttgart"
        }
    }
    California = {
        "What is the capital city of California?": {
            "options": ["A) Los Angeles", "B) San Francisco", "C) Sacramento", "D) San Diego"],
            "answer": "C) Sacramento"
        },
        "Which city in California is known as the 'City of Angels'?": {
            "options": ["A) Los Angeles", "B) San Francisco", "C) Sacramento", "D) San Diego"],
            "answer": "A) Los Angeles"
        },
        "What is the largest city in California by population?": {
            "options": ["A) Los Angeles", "B) San Francisco", "C) Sacramento", "D) San Diego"],
            "answer": "A) Los Angeles"
        },
        "Which national park in California is known for its giant sequoia trees?": {
            "options": ["A) Yosemite National Park", "B) Sequoia National Park", "C) Joshua Tree National Park", "D) Redwood National Park"],
            "answer": "B) Sequoia National Park"
        },
        "What is the state flower of California?": {
            "options": ["A) Poppy", "B) Rose", "C) Daisy", "D) Sunflower"],
            "answer": "A) Poppy"
        },
        "Which California university is known for its Silicon Valley location and computer science programs?": {
            "options": ["A) Stanford University", "B) University of California, Berkeley", "C) California Institute of Technology (Caltech)", "D) University of Southern California (USC)"],
            "answer": "A) Stanford University"
        },
        "What is the name of the famous bridge in San Francisco, California?": {
            "options": ["A) Golden Gate Bridge", "B) Brooklyn Bridge", "C) Bay Bridge", "D) London Bridge"],
            "answer": "A) Golden Gate Bridge"
        },
        "Which California city is known for its wine country and the Napa Valley region?": {
            "options": ["A) Los Angeles", "B) San Francisco", "C) Sacramento", "D) Santa Rosa"],
            "answer": "D) Santa Rosa"
        },
        "What is the nickname of California?": {
            "options": ["A) The Sunshine State", "B) The Golden State", "C) The Lone Star State", "D) The Evergreen State"],
            "answer": "B) The Golden State"
        },
        "Which California city is home to Disneyland Resort?": {
            "options": ["A) Anaheim", "B) San Diego", "C) Los Angeles", "D) San Francisco"],
            "answer": "A) Anaheim"
        }
    }
    Colorado = {
        "What is the capital city of Colorado?": {
            "options": ["A) Denver", "B) Colorado Springs", "C) Boulder", "D) Aspen"],
            "answer": "A) Denver"
        },
        "Which national park in Colorado is known for its Rocky Mountains?": {
            "options": ["A) Yellowstone National Park", "B) Grand Teton National Park", "C) Rocky Mountain National Park", "D) Yosemite National Park"],
            "answer": "C) Rocky Mountain National Park"
        },
        "What is the state bird of Colorado?": {
            "options": ["A) Blue Jay", "B) Lark Bunting", "C) Western Meadowlark", "D) Mountain Bluebird"],
            "answer": "B) Lark Bunting"
        },
        "Which city in Colorado is known for its Garden of the Gods rock formations?": {
            "options": ["A) Denver", "B) Colorado Springs", "C) Boulder", "D) Fort Collins"],
            "answer": "B) Colorado Springs"
        },
        "What is the nickname of Colorado?": {
            "options": ["A) The Golden State", "B) The Silver State", "C) The Centennial State", "D) The Sunshine State"],
            "answer": "C) The Centennial State"
        },
        "Which university in Colorado is known as the Buffaloes?": {
            "options": ["A) University of Colorado Boulder", "B) Colorado State University", "C) University of Denver", "D) Colorado College"],
            "answer": "A) University of Colorado Boulder"
        },
        "What is the tallest mountain in Colorado?": {
            "options": ["A) Mount Elbert", "B) Pikes Peak", "C) Longs Peak", "D) Mount Massive"],
            "answer": "A) Mount Elbert"
        },
        "Which river runs through the Grand Canyon in Colorado?": {
            "options": ["A) Colorado River", "B) Rio Grande", "C) Arkansas River", "D) Gunnison River"],
            "answer": "A) Colorado River"
        },
        "Which ski resort town in Colorado is known for its annual Aspen Food & Wine Classic event?": {
            "options": ["A) Vail", "B) Breckenridge", "C) Aspen", "D) Telluride"],
            "answer": "C) Aspen"
        },
        "Which Colorado city is home to the United States Air Force Academy?": {
            "options": ["A) Denver", "B) Colorado Springs", "C) Boulder", "D) Fort Collins"],
            "answer": "B) Colorado Springs"
        }
    }
    Connecticut = {
        "What is the capital city of Connecticut?": {
            "options": ["A) Bridgeport", "B) Hartford", "C) New Haven", "D) Stamford"],
            "answer": "B) Hartford"
        },
        "Which river forms the eastern boundary of Connecticut?": {
            "options": ["A) Connecticut River", "B) Hudson River", "C) Delaware River", "D) Potomac River"],
            "answer": "A) Connecticut River"
        },
        "What is the state bird of Connecticut?": {
            "options": ["A) American Robin", "B) Eastern Bluebird", "C) American Goldfinch", "D) American Bald Eagle"],
            "answer": "A) American Robin"
        },
        "Which Connecticut city is known for its Yale University?": {
            "options": ["A) Bridgeport", "B) Hartford", "C) New Haven", "D) Stamford"],
            "answer": "C) New Haven"
        },
        "What is the nickname of Connecticut?": {
            "options": ["A) The Constitution State", "B) The Green Mountain State", "C) The Empire State", "D) The Bay State"],
            "answer": "A) The Constitution State"
        },
        "Which famous inventor was born in Connecticut and is known for inventing the telephone?": {
            "options": ["A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) Benjamin Franklin"],
            "answer": "B) Alexander Graham Bell"
        },
        "What is the tallest mountain in Connecticut?": {
            "options": ["A) Mount Washington", "B) Mount Mansfield", "C) Bear Mountain", "D) Mount Frissell"],
            "answer": "C) Bear Mountain"
        },
        "Which Connecticut city is known for its annual International Festival of Arts & Ideas?": {
            "options": ["A) Bridgeport", "B) Hartford", "C) New Haven", "D) Stamford"],
            "answer": "C) New Haven"
        },
        "What is the name of the river that flows through Hartford, Connecticut?": {
            "options": ["A) Connecticut River", "B) Hudson River", "C) Delaware River", "D) Potomac River"],
            "answer": "A) Connecticut River"
        },
        "Which Connecticut city is known as the 'Insurance Capital of the World'?": {
            "options": ["A) Bridgeport", "B) Hartford", "C) New Haven", "D) Stamford"],
            "answer": "B) Hartford"
        }
    }
    Delaware = {
        "What is the capital city of Delaware?": {
            "options": ["A) Wilmington", "B) Dover", "C) Newark", "D) Lewes"],
            "answer": "B) Dover"
        },
        "Which river forms the western border of Delaware?": {
            "options": ["A) Delaware River", "B) Hudson River", "C) Susquehanna River", "D) Potomac River"],
            "answer": "A) Delaware River"
        },
        "What is the state bird of Delaware?": {
            "options": ["A) American Robin", "B) Eastern Bluebird", "C) American Goldfinch", "D) Delaware Blue Hen"],
            "answer": "D) Delaware Blue Hen"
        },
        "Which Delaware city is known as the 'First State's Capital'?": {
            "options": ["A) Wilmington", "B) Dover", "C) Newark", "D) Lewes"],
            "answer": "B) Dover"
        },
        "What is the nickname of Delaware?": {
            "options": ["A) The Diamond State", "B) The Garden State", "C) The Peach State", "D) The Bay State"],
            "answer": "A) The Diamond State"
        },
        "Which Delaware city is known for its tax-free shopping?": {
            "options": ["A) Wilmington", "B) Dover", "C) Newark", "D) Rehoboth Beach"],
            "answer": "D) Rehoboth Beach"
        },
        "What is the official state marine animal of Delaware?": {
            "options": ["A) Horseshoe Crab", "B) Dolphin", "C) Sea Turtle", "D) Blue Crab"],
            "answer": "A) Horseshoe Crab"
        },
        "Which Delaware city is known for its annual Firefly Music Festival?": {
            "options": ["A) Wilmington", "B) Dover", "C) Newark", "D) Rehoboth Beach"],
            "answer": "B) Dover"
        },
        "What is the name of the bay that borders Delaware to the east?": {
            "options": ["A) Chesapeake Bay", "B) Delaware Bay", "C) Long Island Sound", "D) Cape Cod Bay"],
            "answer": "B) Delaware Bay"
        },
        "Which Delaware city is known for its corporate headquarters and is often referred to as the 'Corporate Capital of the World'?": {
            "options": ["A) Wilmington", "B) Dover", "C) Newark", "D) Lewes"],
            "answer": "A) Wilmington"
        }
    }
    Florida = {
    "What is the capital city of Florida?": {
            "options": ["A) Miami", "B) Orlando", "C) Tallahassee", "D) Tampa"],
            "answer": "C) Tallahassee"
        },
        "Which city in Florida is known as the 'Theme Park Capital of the World'?": {
            "options": ["A) Miami", "B) Orlando", "C) Tampa", "D) Jacksonville"],
            "answer": "B) Orlando"
        },
        "What is the state bird of Florida?": {
            "options": ["A) Northern Mockingbird", "B) Bald Eagle", "C) American Robin", "D) Osprey"],
            "answer": "A) Northern Mockingbird"
        },
        "Which national park in Florida is known for its unique ecosystem of swamps and marshes?": {
            "options": ["A) Everglades National Park", "B) Yellowstone National Park", "C) Grand Canyon National Park", "D) Yosemite National Park"],
            "answer": "A) Everglades National Park"
        },
        "What is the nickname of Florida?": {
            "options": ["A) The Sunshine State", "B) The Golden State", "C) The Silver State", "D) The Lone Star State"],
            "answer": "A) The Sunshine State"
        },
        "Which Florida city is known for its world-famous South Beach?": {
            "options": ["A) Miami", "B) Orlando", "C) Tampa", "D) Jacksonville"],
            "answer": "A) Miami"
        },
        "What is the tallest mountain in Florida?": {
            "options": ["A) Mount Dora", "B) Sugarloaf Mountain", "C) Iron Mountain", "D) Britton Hill"],
            "answer": "D) Britton Hill"
        },
        "Which Florida city is known for its annual Gasparilla Pirate Festival?": {
            "options": ["A) Miami", "B) Orlando", "C) Tampa", "D) Jacksonville"],
            "answer": "C) Tampa"
        },
        "Which river forms part of the border between Florida and Georgia?": {
            "options": ["A) Mississippi River", "B) St. Johns River", "C) Apalachicola River", "D) Suwannee River"],
            "answer": "B) St. Johns River"
        },
        "Which Florida city is known for its NASA Kennedy Space Center?": {
            "options": ["A) Miami", "B) Orlando", "C) Cape Canaveral", "D) Tampa"],
            "answer": "C) Cape Canaveral"
        }
    }
    Georgia = {
    "What is the capital city of Georgia?": {
    "options": ["A) Atlanta", "B) Savannah", "C) Augusta", "D) Macon"],
    "answer": "A) Atlanta"
    },
    "Which river forms Georgia's eastern border?": {
    "options": ["A) Mississippi River", "B) Chattahoochee River", "C) Savannah River", "D) Altamaha River"],
    "answer": "C) Savannah River"
    },
    "What is the state bird of Georgia?": {
    "options": ["A) Brown Thrasher", "B) Northern Cardinal", "C) Mockingbird", "D) Bald Eagle"],
    "answer": "A) Brown Thrasher"
    },
    "What is Georgia's nickname?": {
    "options": ["A) The Peach State", "B) The Empire State", "C) The Sunshine State", "D) The Volunteer State"],
    "answer": "A) The Peach State"
    },
    "Which Georgia city is known for its historic district and oak-lined streets?": {
    "options": ["A) Atlanta", "B) Savannah", "C) Augusta", "D) Macon"],
    "answer": "B) Savannah"
    },
    "What is the highest peak in Georgia?": {
    "options": ["A) Brasstown Bald", "B) Stone Mountain", "C) Mount Oglethorpe", "D) Blood Mountain"],
    "answer": "A) Brasstown Bald"
    },
    "Which Georgia island is known for its wild horses?": {
    "options": ["A) Tybee Island", "B) Jekyll Island", "C) St. Simons Island", "D) Cumberland Island"],
    "answer": "D) Cumberland Island"
    },
    "Which university is located in Athens, Georgia?": {
    "options": ["A) Georgia State University", "B) Emory University", "C) University of Georgia", "D) Georgia Institute of Technology"],
    "answer": "C) University of Georgia"
    },
    "What is the name of the famous civil rights leader from Georgia?": {
    "options": ["A) Martin Luther King Jr.", "B) Malcolm X", "C) Rosa Parks", "D) Harriet Tubman"],
    "answer": "A) Martin Luther King Jr."
    },
    "Which Georgia city hosted the 1996 Summer Olympics?": {
    "options": ["A) Atlanta", "B) Savannah", "C) Augusta", "D) Macon"],
    "answer": "A) Atlanta"
    }
    }
    Hawaii = {
    "What is the capital city of Hawaii?": {
    "options": ["A) Honolulu", "B) Hilo", "C) Kailua", "D) Lahaina"],
    "answer": "A) Honolulu"
    },
    "Which Hawaiian island is known as the 'Garden Isle'?": {
    "options": ["A) Oahu", "B) Maui", "C) Kauai", "D) Hawaii (Big Island)"],
    "answer": "C) Kauai"
    },
    "What is the state bird of Hawaii?": {
    "options": ["A) Hawaiian Goose (Nene)", "B) Hawaiian Hawk ('Io)", "C) Hawaiian Coot ('Alae ke'oke'o)", "D) Hawaiian Petrel ('Ua'u)"],
    "answer": "A) Hawaiian Goose (Nene)"
    },
    "What is Hawaii's nickname?": {
    "options": ["A) The Aloha State", "B) The Rainbow State", "C) The Paradise State", "D) The Orchid Isle"],
    "answer": "A) The Aloha State"
    },
    "Which Hawaiian island is home to the famous Waikiki Beach?": {
    "options": ["A) Oahu", "B) Maui", "C) Kauai", "D) Hawaii (Big Island)"],
    "answer": "A) Oahu"
    },
    "What is the name of the active volcano located on Hawaii (Big Island)?": {
    "options": ["A) Mauna Loa", "B) Kilauea", "C) Mauna Kea", "D) Haleakala"],
    "answer": "B) Kilauea"
    },
    "Which Hawaiian king is known as the 'Merrie Monarch'?": {
    "options": ["A) King Kamehameha I", "B) King Kalakaua", "C) King Lunalilo", "D) King Kamehameha III"],
    "answer": "B) King Kalakaua"
    },
    "What is the traditional Hawaiian feast called?": {
    "options": ["A) Luau", "B) Paniolo", "C) Makahiki", "D) Ohana"],
    "answer": "A) Luau"
    },
    "Which Hawaiian island is known for its pineapple plantations?": {
    "options": ["A) Oahu", "B) Maui", "C) Kauai", "D) Lanai"],
    "answer": "D) Lanai"
    },
    "What is the name of the historic palace in Honolulu, once the residence of Hawaiian royalty?": {
    "options": ["A) Iolani Palace", "B) Hulihee Palace", "C) Queen Emma Summer Palace", "D) Pu'uhonua o Honaunau"],
    "answer": "A) Iolani Palace"
    }
    }
    Idaho = {
    "What is the capital city of Idaho?": {
    "options": ["A) Boise", "B) Idaho Falls", "C) Coeur d'Alene", "D) Pocatello"],
    "answer": "A) Boise"
    },
    "Which river forms Idaho's western border?": {
    "options": ["A) Columbia River", "B) Snake River", "C) Colorado River", "D) Salmon River"],
    "answer": "A) Columbia River"
    },
    "What is the state bird of Idaho?": {
    "options": ["A) Mountain Bluebird", "B) Western Meadowlark", "C) Peregrine Falcon", "D) American Goldfinch"],
    "answer": "A) Mountain Bluebird"
    },
    "What is Idaho's nickname?": {
    "options": ["A) The Gem State", "B) The Sunshine State", "C) The Treasure State", "D) The Potato State"],
    "answer": "A) The Gem State"
    },
    "Which Idaho city is known for its famous potatoes?": {
    "options": ["A) Boise", "B) Idaho Falls", "C) Coeur d'Alene", "D) Twin Falls"],
    "answer": "A) Boise"
    },
    "What is the highest peak in Idaho?": {
    "options": ["A) Mount Borah", "B) Bald Mountain", "C) Sawtooth Mountain", "D) Pioneer Mountain"],
    "answer": "A) Mount Borah"
    }
    }
    Illinois = {
    "What is the capital city of Illinois?": {
    "options": ["A) Chicago", "B) Springfield", "C) Peoria", "D) Rockford"],
    "answer": "B) Springfield"
    },
    "Which Great Lake does not border Illinois?": {
    "options": ["A) Lake Michigan", "B) Lake Superior", "C) Lake Erie", "D) Lake Huron"],
    "answer": "D) Lake Huron"
    },
    "What is the state bird of Illinois?": {
    "options": ["A) Cardinal", "B) Blue Jay", "C) Robin", "D) Goldfinch"],
    "answer": "A) Cardinal"
    },
    "What is Illinois's nickname?": {
    "options": ["A) The Prairie State", "B) The Land of Lincoln", "C) The Corn State", "D) The Garden State"],
    "answer": "A) The Prairie State"
    },
    "Which Illinois city is known as the 'Windy City'?": {
    "options": ["A) Chicago", "B) Springfield", "C) Peoria", "D) Aurora"],
    "answer": "A) Chicago"
    },
    "What is the tallest building in Illinois and the Western Hemisphere?": {
    "options": ["A) Willis Tower", "B) John Hancock Center", "C) Trump International Hotel and Tower", "D) Aon Center"],
    "answer": "A) Willis Tower"
    },
    "What is the name of the university located in Urbana-Champaign, Illinois?": {
    "options": ["A) University of Chicago", "B) Northwestern University", "C) University of Illinois", "D) Loyola University Chicago"],
    "answer": "C) University of Illinois"
    },
    "Which Illinois city is known for its annual Bean Blossom Blues Festival?": {
    "options": ["A) Chicago", "B) Springfield", "C) Peoria", "D) Bloomington"],
    "answer": "D) Bloomington"
    },
    "What is the name of the river that forms the western border of Illinois?": {
    "options": ["A) Mississippi River", "B) Ohio River", "C) Missouri River", "D) Illinois River"],
    "answer": "A) Mississippi River"
    },
    "Which Illinois city is famous for its architecture, including the Frank Lloyd Wright-designed Robie House?": {
    "options": ["A) Chicago", "B) Springfield", "C) Peoria", "D) Aurora"],
    "answer": "A) Chicago"
    }
    }
    Indiana = {
    "What is the capital city of Indiana?": {
    "options": ["A) Indianapolis", "B) Fort Wayne", "C) Evansville", "D) South Bend"],
    "answer": "A) Indianapolis"
    },
    "Which Great Lake does Indiana border?": {
    "options": ["A) Lake Michigan", "B) Lake Superior", "C) Lake Erie", "D) Lake Huron"],
    "answer": "A) Lake Michigan"
    },
    "What is the state bird of Indiana?": {
    "options": ["A) Cardinal", "B) Blue Jay", "C) Robin", "D) Woodpecker"],
    "answer": "A) Cardinal"
    },
    "What is Indiana's nickname?": {
    "options": ["A) The Hoosier State", "B) The Crossroads of America", "C) The Heart of America", "D) The Corn State"],
    "answer": "A) The Hoosier State"
    },
    "Which Indiana city is known for the Indianapolis Motor Speedway and the Indy 500?": {
    "options": ["A) Indianapolis", "B) Fort Wayne", "C) Evansville", "D) South Bend"],
    "answer": "A) Indianapolis"
    },
    "What is the largest university in Indiana by enrollment?": {
    "options": ["A) Purdue University", "B) Indiana University", "C) Ball State University", "D) Notre Dame University"],
    "answer": "B) Indiana University"
    },
    "Which Indiana city is known for its Amish population and traditional craftsmanship?": {
    "options": ["A) Shipshewana", "B) Carmel", "C) Bloomington", "D) Muncie"],
    "answer": "A) Shipshewana"
    },
    "What is the name of the river that forms part of Indiana's southern border?": {
    "options": ["A) Ohio River", "B) Mississippi River", "C) Wabash River", "D) White River"],
    "answer": "A) Ohio River"
    },
    "Which Indiana city is home to the University of Notre Dame?": {
    "options": ["A) Indianapolis", "B) Fort Wayne", "C) South Bend", "D) Bloomington"],
    "answer": "C) South Bend"
    },
    "What is the highest point in Indiana?": {
    "options": ["A) Hoosier Hill", "B) Mount Baldy", "C) Brown County High Point", "D) Weed Patch Hill"],
    "answer": "A) Hoosier Hill"
    }
    }
    Iowa = {
    "What is the capital city of Iowa?": {
    "options": ["A) Des Moines", "B) Cedar Rapids", "C) Davenport", "D) Iowa City"],
    "answer": "A) Des Moines"
    },
    "Which river forms Iowa's eastern border?": {
    "options": ["A) Missouri River", "B) Mississippi River", "C) Ohio River", "D) Iowa River"],
    "answer": "B) Mississippi River"
    },
    "What is the state bird of Iowa?": {
    "options": ["A) American Goldfinch", "B) Eastern Bluebird", "C) Eastern Meadowlark", "D) Bald Eagle"],
    "answer": "C) Eastern Meadowlark"
    },
    "What is Iowa's nickname?": {
    "options": ["A) The Hawkeye State", "B) The Corn State", "C) The Land of Enchantment", "D) The Gem State"],
    "answer": "A) The Hawkeye State"
    },
    "Which Iowa city is known for its annual Iowa State Fair, one of the largest state fairs in the United States?": {
    "options": ["A) Des Moines", "B) Cedar Rapids", "C) Davenport", "D) Ames"],
    "answer": "A) Des Moines"
    },
    "What is the tallest building in Iowa?": {
    "options": ["A) 801 Grand", "B) Principal Building", "C) Ruan Center", "D) Hub Tower"],
    "answer": "A) 801 Grand"
    }
    }
    Kansas = {
        "What is the capital city of Kansas?": {
            "options": ["A) Topeka", "B) Wichita", "C) Kansas City", "D) Lawrence"],
            "answer": "A) Topeka"
        },
        "Which river forms the eastern boundary of Kansas?": {
            "options": ["A) Mississippi River", "B) Missouri River", "C) Ohio River", "D) Arkansas River"],
            "answer": "B) Missouri River"
        },
        "What is the official state nickname of Kansas?": {
            "options": ["A) The Sunflower State", "B) The Jayhawk State", "C) The Heart of America", "D) The Wheat State"],
            "answer": "A) The Sunflower State"
        },
        "Which famous outlaw was shot and killed in 1882 in a shootout in Kansas?": {
            "options": ["A) Billy the Kid", "B) Jesse James", "C) Butch Cassidy", "D) John Dillinger"],
            "answer": "B) Jesse James"
        },
        "What is the highest point in Kansas?": {
            "options": ["A) Mount Sunflower", "B) Mount Magazine", "C) Mount Rushmore", "D) Mount Scott"],
            "answer": "A) Mount Sunflower"
        },
        "What is the state bird of Kansas?": {
            "options": ["A) Western Meadowlark", "B) American Robin", "C) Mourning Dove", "D) Northern Cardinal"],
            "answer": "A) Western Meadowlark"
        },
        "Which famous aviator was born in Atchison, Kansas?": {
            "options": ["A) Charles Lindbergh", "B) Amelia Earhart", "C) Howard Hughes", "D) Orville Wright"],
            "answer": "B) Amelia Earhart"
        },
        "What is the official state flower of Kansas?": {
            "options": ["A) Sunflower", "B) Tulip", "C) Daisy", "D) Rose"],
            "answer": "A) Sunflower"
        },
        "Which university in Kansas is known for its basketball program and is often called 'Rock Chalk Jayhawk'?": {
            "options": ["A) Kansas State University", "B) Wichita State University", "C) University of Kansas", "D) Emporia State University"],
            "answer": "C) University of Kansas"
        },
        "What is the name of the famous Supreme Court case decided in 1954 that originated in Kansas and led to desegregation in public schools?": {
            "options": ["A) Plessy v. Ferguson", "B) Brown v. Board of Education", "C) Roe v. Wade", "D) Miranda v. Arizona"],
            "answer": "B) Brown v. Board of Education"
        }
    }
    Kentucky = {
        "What is the capital city of Kentucky?": {
            "options": ["A) Lexington", "B) Louisville", "C) Frankfort", "D) Bowling Green"],
            "answer": "C) Frankfort"
        },
        "Which famous horse race takes place annually in Louisville, Kentucky?": {
            "options": ["A) Belmont Stakes", "B) Kentucky Derby", "C) Preakness Stakes", "D) Breeders' Cup"],
            "answer": "B) Kentucky Derby"
        },
        "What is the official state nickname of Kentucky?": {
            "options": ["A) The Bluegrass State", "B) The Derby State", "C) The Bourbon State", "D) The Horse State"],
            "answer": "A) The Bluegrass State"
        },
        "Which river forms Kentucky's northern border with Ohio?": {
            "options": ["A) Ohio River", "B) Mississippi River", "C) Tennessee River", "D) Cumberland River"],
            "answer": "A) Ohio River"
        },
        "What is the highest point in Kentucky?": {
            "options": ["A) Black Mountain", "B) Mount Ararat", "C) Pine Mountain", "D) Big Black Mountain"],
            "answer": "A) Black Mountain"
        },
        "What is the state bird of Kentucky?": {
            "options": ["A) Northern Cardinal", "B) American Robin", "C) Bald Eagle", "D) Eastern Bluebird"],
            "answer": "A) Northern Cardinal"
        },
        "Which famous frontiersman was born in Kentucky in 1734 and became a folk hero in American history?": {
            "options": ["A) Davy Crockett", "B) Daniel Boone", "C) Jim Bowie", "D) Kit Carson"],
            "answer": "B) Daniel Boone"
        },
        "What is the official state flower of Kentucky?": {
            "options": ["A) Goldenrod", "B) Tulip Poplar", "C) Rhododendron", "D) Bluegrass"],
            "answer": "B) Tulip Poplar"
        },
        "Which university in Kentucky is known for its basketball program and has won multiple NCAA championships?": {
            "options": ["A) University of Louisville", "B) University of Kentucky", "C) Murray State University", "D) Western Kentucky University"],
            "answer": "B) University of Kentucky"
        },
        "What is the name of the famous bourbon whiskey distillery located in Bardstown, Kentucky?": {
            "options": ["A) Jim Beam", "B) Maker's Mark", "C) Wild Turkey", "D) Buffalo Trace"],
            "answer": "B) Maker's Mark"
        }
    }
    Louisiana = {
        "What is the capital city of Louisiana?": {
            "options": ["A) Baton Rouge", "B) New Orleans", "C) Lafayette", "D) Shreveport"],
            "answer": "A) Baton Rouge"
        },
        "Which major river forms Louisiana's eastern border with Mississippi?": {
            "options": ["A) Mississippi River", "B) Red River", "C) Atchafalaya River", "D) Sabine River"],
            "answer": "A) Mississippi River"
        },
        "What is the official state nickname of Louisiana?": {
            "options": ["A) The Pelican State", "B) The Bayou State", "C) The Creole State", "D) The Jazz State"],
            "answer": "A) The Pelican State"
        },
        "Which iconic festival takes place annually in New Orleans, Louisiana, featuring parades, music, and masquerade balls?": {
            "options": ["A) Mardi Gras", "B) Jazz Fest", "C) French Quarter Festival", "D) Essence Festival"],
            "answer": "A) Mardi Gras"
        },
        "What is the highest point in Louisiana?": {
            "options": ["A) Driskill Mountain", "B) Mount Saint Mary", "C) Tallulah Mountain", "D) Red River Gorge"],
            "answer": "A) Driskill Mountain"
        },
        "Which bird is the official state bird of Louisiana?": {
            "options": ["A) Eastern Brown Pelican", "B) Northern Mockingbird", "C) Brown Thrasher", "D) Bald Eagle"],
            "answer": "A) Eastern Brown Pelican"
        },
        "What is the official state flower of Louisiana?": {
            "options": ["A) Magnolia", "B) Iris", "C) Rose", "D) Azalea"],
            "answer": "A) Magnolia"
        },
        "Louisiana is known for its unique cuisine. What traditional dish, originating from Louisiana, consists of rice, vegetables, meat, and spices?": {
            "options": ["A) Jambalaya", "B) Gumbo", "C) Étouffée", "D) Boudin"],
            "answer": "A) Jambalaya"
        },
        "Which famous music genre, characterized by its syncopated rhythm and improvisation, has deep roots in Louisiana, particularly in New Orleans?": {
            "options": ["A) Blues", "B) Jazz", "C) Country", "D) Rock and Roll"],
            "answer": "B) Jazz"
        },
        "What is the name of the famous swamp located in southern Louisiana, known for its unique ecosystem and alligator population?": {
            "options": ["A) Okefenokee Swamp", "B) Great Dismal Swamp", "C) Atchafalaya Basin", "D) Honey Island Swamp"],
            "answer": "C) Atchafalaya Basin"
        }
    }
    Maine = {
        "What is the capital city of Maine?": {
            "options": ["A) Portland", "B) Augusta", "C) Bangor", "D) Lewiston"],
            "answer": "B) Augusta"
        },
        "Which U.S. state borders Maine to the west?": {
            "options": ["A) New Hampshire", "B) Vermont", "C) Massachusetts", "D) Connecticut"],
            "answer": "A) New Hampshire"
        },
        "What is the nickname of Maine?": {
            "options": ["A) The Pine Tree State", "B) The Vacation State", "C) The Lighthouse State", "D) The Lobster State"],
            "answer": "A) The Pine Tree State"
        },
        "Which national park in Maine is known for its granite peaks, lakes, and forests?": {
            "options": ["A) Acadia National Park", "B) Yellowstone National Park", "C) Grand Canyon National Park", "D) Great Smoky Mountains National Park"],
            "answer": "A) Acadia National Park"
        },
        "What is the highest point in Maine?": {
            "options": ["A) Mount Katahdin", "B) Mount Washington", "C) Mount Mansfield", "D) Cadillac Mountain"],
            "answer": "A) Mount Katahdin"
        },
        "Which animal is the official state animal of Maine?": {
            "options": ["A) Moose", "B) Black Bear", "C) White-tailed Deer", "D) Bald Eagle"],
            "answer": "A) Moose"
        },
        "What is the official state flower of Maine?": {
            "options": ["A) White Pine Cone and Tassel", "B) Lupine", "C) Rose", "D) Lily"],
            "answer": "A) White Pine Cone and Tassel"
        },
        "Maine is known for its seafood. Which crustacean is a staple of Maine cuisine?": {
            "options": ["A) Crab", "B) Shrimp", "C) Lobster", "D) Crawfish"],
            "answer": "C) Lobster"
        },
        "Which famous author, known for his horror and suspense novels, was born in Maine and set many of his stories in the state?": {
            "options": ["A) Stephen King", "B) John Grisham", "C) J.K. Rowling", "D) Dan Brown"],
            "answer": "A) Stephen King"
        },
        "What is the name of the famous scenic highway that runs along the coast of Maine, known for its picturesque views?": {
            "options": ["A) Pacific Coast Highway", "B) Blue Ridge Parkway", "C) Great Ocean Road", "D) Acadia All-American Road"],
            "answer": "D) Acadia All-American Road"
        }
    }
    Maryland = {
        "What is the capital city of Maryland?": {
            "options": ["A) Baltimore", "B) Annapolis", "C) Frederick", "D) Rockville"],
            "answer": "B) Annapolis"
        },
        "Which U.S. state borders Maryland to the north?": {
            "options": ["A) Virginia", "B) Pennsylvania", "C) Delaware", "D) West Virginia"],
            "answer": "B) Pennsylvania"
        },
        "What is the nickname of Maryland?": {
            "options": ["A) The Old Line State", "B) The Free State", "C) The Monumental State", "D) The Chesapeake State"],
            "answer": "B) The Free State"
        },
        "Which major bay is located on the eastern coast of Maryland?": {
            "options": ["A) Chesapeake Bay", "B) San Francisco Bay", "C) Tampa Bay", "D) Puget Sound"],
            "answer": "A) Chesapeake Bay"
        },
        "Which American flag was flown during the Battle of Baltimore, inspiring the lyrics of the national anthem?": {
            "options": ["A) Stars and Bars", "B) Gadsden Flag", "C) Betsy Ross Flag", "D) Star-Spangled Banner"],
            "answer": "D) Star-Spangled Banner"
        },
        "What is the official state crustacean of Maryland?": {
            "options": ["A) Lobster", "B) Crab", "C) Shrimp", "D) Crawfish"],
            "answer": "B) Crab"
        },
        "Which famous historical figure and abolitionist was born into slavery in Maryland?": {
            "options": ["A) Harriet Tubman", "B) Frederick Douglass", "C) Sojourner Truth", "D) Booker T. Washington"],
            "answer": "B) Frederick Douglass"
        },
        "What is the official state sport of Maryland?": {
            "options": ["A) Football", "B) Soccer", "C) Lacrosse", "D) Baseball"],
            "answer": "C) Lacrosse"
        },
        "Maryland is home to which prestigious military academy located in Annapolis?": {
            "options": ["A) West Point", "B) Naval Academy", "C) Air Force Academy", "D) Coast Guard Academy"],
            "answer": "B) Naval Academy"
        },
        "Which amusement park, located near Baltimore, is known for its roller coasters and family-friendly attractions?": {
            "options": ["A) Disneyland", "B) Six Flags America", "C) Cedar Point", "D) Busch Gardens Williamsburg"],
            "answer": "B) Six Flags America"
        }
    }
    Massachusetts = {
        "What is the capital city of Massachusetts?": {
            "options": ["A) Boston", "B) Worcester", "C) Springfield", "D) Cambridge"],
            "answer": "A) Boston"
        },
        "Which of the following Ivy League universities is located in Massachusetts?": {
            "options": ["A) Harvard University", "B) Yale University", "C) Princeton University", "D) Columbia University"],
            "answer": "A) Harvard University"
        },
        "What is the nickname of Massachusetts?": {
            "options": ["A) The Empire State", "B) The Bay State", "C) The Sunshine State", "D) The Garden State"],
            "answer": "B) The Bay State"
        },
        "Which body of water separates Cape Cod from the mainland of Massachusetts?": {
            "options": ["A) Long Island Sound", "B) Cape Cod Bay", "C) Buzzards Bay", "D) Massachusetts Bay"],
            "answer": "C) Buzzards Bay"
        },
        "In which year did the Pilgrims establish the Plymouth Colony in Massachusetts?": {
            "options": ["A) 1620", "B) 1607", "C) 1630", "D) 1692"],
            "answer": "A) 1620"
        },
        "What is the official state dessert of Massachusetts?": {
            "options": ["A) Apple Pie", "B) Boston Cream Pie", "C) Key Lime Pie", "D) Pumpkin Pie"],
            "answer": "B) Boston Cream Pie"
        },
        "Which Massachusetts city is known for its annual marathon, held on Patriot's Day?": {
            "options": ["A) Worcester", "B) Salem", "C) Springfield", "D) Boston"],
            "answer": "D) Boston"
        },
        "What is the official state bird of Massachusetts?": {
            "options": ["A) Eastern Bluebird", "B) Black-capped Chickadee", "C) American Robin", "D) Baltimore Oriole"],
            "answer": "B) Black-capped Chickadee"
        },
        "Which famous American poet was born in Massachusetts and wrote extensively about nature and New England?": {
            "options": ["A) Robert Frost", "B) Emily Dickinson", "C) Walt Whitman", "D) Langston Hughes"],
            "answer": "A) Robert Frost"
        },
        "What is the official state cookie of Massachusetts?": {
            "options": ["A) Chocolate Chip Cookie", "B) Sugar Cookie", "C) Oatmeal Raisin Cookie", "D) Snickerdoodle"],
            "answer": "A) Chocolate Chip Cookie"
        }
    }
    Michigan = {
        "What is the capital city of Michigan?": {
            "options": ["A) Lansing", "B) Detroit", "C) Grand Rapids", "D) Ann Arbor"],
            "answer": "A) Lansing"
        },
        "Which of the Great Lakes does not border Michigan?": {
            "options": ["A) Lake Superior", "B) Lake Michigan", "C) Lake Huron", "D) Lake Erie"],
            "answer": "D) Lake Erie"
        },
        "What is Michigan's state nickname?": {
            "options": ["A) The Sunshine State", "B) The Land of Enchantment", "C) The Great Lakes State", "D) The Garden State"],
            "answer": "C) The Great Lakes State"
        },
        "What is the tallest building in Michigan?": {
            "options": ["A) Renaissance Center", "B) One Detroit Center", "C) Penobscot Building", "D) Guardian Building"],
            "answer": "A) Renaissance Center"
        },
        "Which automobile company is headquartered in Detroit, Michigan?": {
            "options": ["A) Ford", "B) General Motors", "C) Chrysler", "D) Tesla"],
            "answer": "B) General Motors"
        },
        "What is the official state bird of Michigan?": {
            "options": ["A) American Robin", "B) Common Loon", "C) Pileated Woodpecker", "D) American Goldfinch"],
            "answer": "B) Common Loon"
        },
        "What is the largest city in Michigan by population?": {
            "options": ["A) Detroit", "B) Grand Rapids", "C) Warren", "D) Sterling Heights"],
            "answer": "A) Detroit"
        },
        "Which river forms the border between Michigan and Ontario, Canada?": {
            "options": ["A) Detroit River", "B) St. Clair River", "C) Niagara River", "D) St. Lawrence River"],
            "answer": "A) Detroit River"
        },
        "What is Michigan's official state flower?": {
            "options": ["A) Rose", "B) Daisy", "C) Apple Blossom", "D) Trillium"],
            "answer": "D) Trillium"
        },
        "What is the name of the college football team representing the University of Michigan?": {
            "options": ["A) Spartans", "B) Wolverines", "C) Buckeyes", "D) Fighting Irish"],
            "answer": "B) Wolverines"
        }
    }
    Minnesota = {
        "What is the capital city of Minnesota?": {
            "options": ["A) Minneapolis", "B) Duluth", "C) St. Paul", "D) Rochester"],
            "answer": "C) St. Paul"
        },
        "Which of the following is known as the state bird of Minnesota?": {
            "options": ["A) Bald Eagle", "B) Common Loon", "C) American Goldfinch", "D) Northern Cardinal"],
            "answer": "B) Common Loon"
        },
        "What is the largest city in Minnesota by population?": {
            "options": ["A) Minneapolis", "B) Duluth", "C) St. Paul", "D) Rochester"],
            "answer": "A) Minneapolis"
        },
        "Which river forms part of the border between Minnesota and Wisconsin?": {
            "options": ["A) Mississippi River", "B) Missouri River", "C) Red River", "D) St. Croix River"],
            "answer": "D) St. Croix River"
        },
        "What is the state motto of Minnesota?": {
            "options": ["A) Land of 10,000 Lakes", "B) North Star State", "C) The Gopher State", "D) Land of Lincoln"],
            "answer": "B) North Star State"
        },
        "Which of the following is not a professional sports team in Minnesota?": {
            "options": ["A) Vikings", "B) Twins", "C) Wild", "D) Cardinals"],
            "answer": "D) Cardinals"
        },
        "What is Minnesota's official state fish?": {
            "options": ["A) Walleye", "B) Northern Pike", "C) Largemouth Bass", "D) Bluegill"],
            "answer": "A) Walleye"
        },
        "Which university is the largest in Minnesota based on student enrollment?": {
            "options": ["A) University of Minnesota", "B) Minnesota State University", "C) St. Cloud State University", "D) Winona State University"],
            "answer": "A) University of Minnesota"
        },
        "What is the highest point in Minnesota?": {
            "options": ["A) Eagle Mountain", "B) Mount Arvon", "C) Mount Curwood", "D) Mount Desor"],
            "answer": "A) Eagle Mountain"
        },
        "Which of the Great Lakes is the smallest in terms of surface area?": {
            "options": ["A) Lake Superior", "B) Lake Michigan", "C) Lake Huron", "D) Lake Ontario"],
            "answer": "D) Lake Ontario"
        }
    }
    Mississippi = {
        "What is the capital city of Mississippi?": {
            "options": ["A) Jackson", "B) Biloxi", "C) Gulfport", "D) Hattiesburg"],
            "answer": "A) Jackson"
        },
        "Which river forms the western boundary of Mississippi?": {
            "options": ["A) Mississippi River", "B) Missouri River", "C) Red River", "D) Ohio River"],
            "answer": "A) Mississippi River"
        },
        "What is the nickname of Mississippi?": {
            "options": ["A) The Sunshine State", "B) The Magnolia State", "C) The Lone Star State", "D) The Empire State"],
            "answer": "B) The Magnolia State"
        },
        "Which of the following is the largest city in Mississippi by population?": {
            "options": ["A) Jackson", "B) Biloxi", "C) Gulfport", "D) Southaven"],
            "answer": "C) Gulfport"
        },
        "Which U.S. state is to the north of Mississippi?": {
            "options": ["A) Louisiana", "B) Alabama", "C) Tennessee", "D) Arkansas"],
            "answer": "C) Tennessee"
        },
        "What is the highest point in Mississippi?": {
            "options": ["A) Woodall Mountain", "B) Cheaha Mountain", "C) Mount Davis", "D) Mount Magazine"],
            "answer": "A) Woodall Mountain"
        },
        "Which of the following is a famous riverboat casino city in Mississippi?": {
            "options": ["A) Vicksburg", "B) Natchez", "C) Tupelo", "D) Oxford"],
            "answer": "A) Vicksburg"
        },
        "Which of the following authors was born in Mississippi and wrote 'The Adventures of Huckleberry Finn'?": {
            "options": ["A) Mark Twain", "B) Ernest Hemingway", "C) F. Scott Fitzgerald", "D) William Faulkner"],
            "answer": "A) Mark Twain"
        },
        "What is the state flower of Mississippi?": {
            "options": ["A) Magnolia", "B) Iris", "C) Rose", "D) Daisy"],
            "answer": "A) Magnolia"
        },
        "Which of the following is not a neighboring state of Mississippi?": {
            "options": ["A) Tennessee", "B) Florida", "C) Georgia", "D) Kentucky"],
            "answer": "D) Kentucky"
        }
    }
    Missouri = {
        "What is the capital city of Missouri?": {
            "options": ["A) St. Louis", "B) Kansas City", "C) Jefferson City", "D) Springfield"],
            "answer": "C) Jefferson City"
        },
        "Which river forms part of the eastern border of Missouri?": {
            "options": ["A) Missouri River", "B) Mississippi River", "C) Ohio River", "D) Red River"],
            "answer": "B) Mississippi River"
        },
        "What is the nickname of Missouri?": {
            "options": ["A) The Grand Canyon State", "B) The Show-Me State", "C) The Silver State", "D) The Land of Enchantment"],
            "answer": "B) The Show-Me State"
        },
        "Which of the following is the largest city in Missouri by population?": {
            "options": ["A) St. Louis", "B) Kansas City", "C) Springfield", "D) Columbia"],
            "answer": "B) Kansas City"
        },
        "Which U.S. state is to the north of Missouri?": {
            "options": ["A) Iowa", "B) Nebraska", "C) Kansas", "D) Oklahoma"],
            "answer": "A) Iowa"
        },
        "What is the highest point in Missouri?": {
            "options": ["A) Taum Sauk Mountain", "B) Black Mountain", "C) White Butte", "D) Mount Rogers"],
            "answer": "A) Taum Sauk Mountain"
        },
        "Which of the following is known as the Gateway to the West and is located in Missouri?": {
            "options": ["A) Gateway Arch", "B) Statue of Liberty", "C) Mount Rushmore", "D) Golden Gate Bridge"],
            "answer": "A) Gateway Arch"
        },
        "Which of the following authors was born in Missouri and wrote 'The Adventures of Tom Sawyer'?": {
            "options": ["A) Mark Twain", "B) Ernest Hemingway", "C) F. Scott Fitzgerald", "D) William Faulkner"],
            "answer": "A) Mark Twain"
        },
        "What is the state flower of Missouri?": {
            "options": ["A) Hawthorn", "B) Sunflower", "C) White trillium", "D) Hawthorn"],
            "answer": "A) Hawthorn"
        },
        "Which of the following is not a neighboring state of Missouri?": {
            "options": ["A) Arkansas", "B) Oklahoma", "C) Kentucky", "D) Nebraska"],
            "answer": "D) Nebraska"
        }
    }
    Montana = {
        "What is the capital city of Montana?": {
            "options": ["A) Helena", "B) Billings", "C) Missoula", "D) Bozeman"],
            "answer": "A) Helena"
        },
        "Which national park is located in Montana?": {
            "options": ["A) Yellowstone National Park", "B) Yosemite National Park", "C) Grand Canyon National Park", "D) Glacier National Park"],
            "answer": "D) Glacier National Park"
        },
        "What is the nickname of Montana?": {
            "options": ["A) The Sunshine State", "B) The Treasure State", "C) The Mountain State", "D) The Garden State"],
            "answer": "B) The Treasure State"
        },
        "Which river is the longest in Montana?": {
            "options": ["A) Yellowstone River", "B) Missouri River", "C) Snake River", "D) Clark Fork River"],
            "answer": "B) Missouri River"
        },
        "Which of the following is not a neighboring state of Montana?": {
            "options": ["A) Wyoming", "B) Idaho", "C) Utah", "D) North Dakota"],
            "answer": "C) Utah"
        },
        "What is the highest peak in Montana?": {
            "options": ["A) Granite Peak", "B) Mount Rainier", "C) Mount Elbert", "D) Mount Whitney"],
            "answer": "A) Granite Peak"
        },
        "Which of the following animals is commonly found in Montana and is featured on the state flag?": {
            "options": ["A) Bald eagle", "B) Grizzly bear", "C) Bison", "D) Elk"],
            "answer": "C) Bison"
        },
        "What is the state flower of Montana?": {
            "options": ["A) Bitterroot", "B) Bluebonnet", "C) Indian Paintbrush", "D) Sunflower"],
            "answer": "A) Bitterroot"
        },
        "Montana is known for its vast expanses of which geographical feature?": {
            "options": ["A) Deserts", "B) Forests", "C) Prairies", "D) Mountains"],
            "answer": "D) Mountains"
        },
        "Which city in Montana is known as the Big Sky City?": {
            "options": ["A) Billings", "B) Missoula", "C) Great Falls", "D) Bozeman"],
            "answer": "B) Missoula"
        }
    }
    Nebraska = {
        "What is the capital city of Nebraska?": {
            "options": ["A) Lincoln", "B) Omaha", "C) Grand Island", "D) Kearney"],
            "answer": "A) Lincoln"
        },
        "Which river forms the eastern boundary of Nebraska?": {
            "options": ["A) Mississippi River", "B) Missouri River", "C) Platte River", "D) Niobrara River"],
            "answer": "B) Missouri River"
        },
        "What is the highest point in Nebraska?": {
            "options": ["A) Mount Laramie", "B) Scotts Bluff", "C) Panorama Point", "D) Pine Ridge"],
            "answer": "C) Panorama Point"
        },
        "What is the nickname of Nebraska?": {
            "options": ["A) The Grand Canyon State", "B) The Cornhusker State", "C) The Aloha State", "D) The Sunshine State"],
            "answer": "B) The Cornhusker State"
        },
        "Which of the following is Nebraska's state bird?": {
            "options": ["A) Bald Eagle", "B) Western Meadowlark", "C) American Robin", "D) Wild Turkey"],
            "answer": "B) Western Meadowlark"
        },
        "In which year did Nebraska become a state?": {
            "options": ["A) 1867", "B) 1872", "C) 1885", "D) 1901"],
            "answer": "A) 1867"
        },
        "Which university is located in Lincoln, Nebraska?": {
            "options": ["A) University of Nebraska-Lincoln", "B) Creighton University", "C) University of Nebraska-Omaha", "D) Nebraska Wesleyan University"],
            "answer": "A) University of Nebraska-Lincoln"
        },
        "What is the largest city in Nebraska by population?": {
            "options": ["A) Lincoln", "B) Omaha", "C) Bellevue", "D) Grand Island"],
            "answer": "B) Omaha"
        },
        "Which famous investor, philanthropist, and business tycoon was born in Omaha, Nebraska?": {
            "options": ["A) Jeff Bezos", "B) Warren Buffett", "C) Elon Musk", "D) Bill Gates"],
            "answer": "B) Warren Buffett"
        },
        "What is the state flower of Nebraska?": {
            "options": ["A) Sunflower", "B) Goldenrod", "C) Saguaro Cactus Blossom", "D) Prairie Goldenrod"],
            "answer": "A) Sunflower"
        }
    }
    Nevada = {
        "What is the capital city of Nevada?": {
            "options": ["A) Carson City", "B) Las Vegas", "C) Reno", "D) Henderson"],
            "answer": "A) Carson City"
        },
        "Which national park is located in Nevada and is known for its colorful rock formations?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon National Park", "C) Zion National Park", "D) Valley of Fire State Park"],
            "answer": "D) Valley of Fire State Park"
        },
        "What is the largest city in Nevada by population?": {
            "options": ["A) Carson City", "B) Las Vegas", "C) Reno", "D) Henderson"],
            "answer": "B) Las Vegas"
        },
        "Nevada is known as the Silver State.": {
            "options": ["A) True", "B) False"],
            "answer": "A) True"
        },
        "Which famous lake is located along the Nevada-California border?": {
            "options": ["A) Lake Tahoe", "B) Lake Mead", "C) Pyramid Lake", "D) Walker Lake"],
            "answer": "A) Lake Tahoe"
        },
        "What is the highest point in Nevada?": {
            "options": ["A) Boundary Peak", "B) Mount Charleston", "C) Wheeler Peak", "D) Ruby Dome"],
            "answer": "A) Boundary Peak"
        },
        "In which year did Nevada become a state?": {
            "options": ["A) 1854", "B) 1864", "C) 1876", "D) 1889"],
            "answer": "B) 1864"
        },
        "Which of the following is Nevada's state flower?": {
            "options": ["A) Sagebrush", "B) Desert Marigold", "C) Prickly Pear Cactus", "D) Sagebrush Mariposa Lily"],
            "answer": "A) Sagebrush"
        },
        "Which famous gambling destination is located in Nevada?": {
            "options": ["A) Atlantic City", "B) Macau", "C) Monte Carlo", "D) Las Vegas"],
            "answer": "D) Las Vegas"
        },
        "Which desert covers most of Nevada?": {
            "options": ["A) Mojave Desert", "B) Sonoran Desert", "C) Great Basin Desert", "D) Chihuahuan Desert"],
            "answer": "C) Great Basin Desert"
        }
    }
    New_Hampshire = {
        "What is the capital city of New Hampshire?": {
            "options": ["A) Concord", "B) Manchester", "C) Nashua", "D) Portsmouth"],
            "answer": "A) Concord"
        },
        "Which mountain range runs through the northern part of New Hampshire?": {
            "options": ["A) Appalachian Mountains", "B) Rocky Mountains", "C) Sierra Nevada", "D) Cascade Range"],
            "answer": "A) Appalachian Mountains"
        },
        "What is the nickname of New Hampshire?": {
            "options": ["A) The Granite State", "B) The Green Mountain State", "C) The Sunshine State", "D) The Silver State"],
            "answer": "A) The Granite State"
        },
        "Which river forms part of the border between New Hampshire and Vermont?": {
            "options": ["A) Connecticut River", "B) Hudson River", "C) Merrimack River", "D) Piscataqua River"],
            "answer": "A) Connecticut River"
        },
        "What is the highest point in New Hampshire?": {
            "options": ["A) Mount Adams", "B) Mount Washington", "C) Mount Lafayette", "D) Mount Monadnock"],
            "answer": "B) Mount Washington"
        },
        "In which year did New Hampshire become a state?": {
            "options": ["A) 1776", "B) 1789", "C) 1792", "D) 1788"],
            "answer": "D) 1788"
        },
        "Which of the following is the state bird of New Hampshire?": {
            "options": ["A) Purple Finch", "B) Northern Cardinal", "C) American Robin", "D) Eastern Bluebird"],
            "answer": "A) Purple Finch"
        },
        "What is the largest city in New Hampshire by population?": {
            "options": ["A) Concord", "B) Manchester", "C) Nashua", "D) Portsmouth"],
            "answer": "B) Manchester"
        },
        "Which famous motorcycle event takes place annually in New Hampshire?": {
            "options": ["A) Sturgis Motorcycle Rally", "B) Daytona Bike Week", "C) Laconia Motorcycle Week", "D) Rolling Thunder"],
            "answer": "C) Laconia Motorcycle Week"
        },
        "What is New Hampshire's state motto?": {
            "options": ["A) Live Free or Die", "B) Liberty and Union", "C) Eureka", "D) Freedom and Unity"],
            "answer": "A) Live Free or Die"
        }
    }
    New_Jersey = {
        "What is the capital city of New Jersey?": {
            "options": ["A) Trenton", "B) Newark", "C) Jersey City", "D) Atlantic City"],
            "answer": "A) Trenton"
        },
        "Which famous scientist conducted many of his early experiments in Menlo Park, New Jersey?": {
            "options": ["A) Albert Einstein", "B) Thomas Edison", "C) Isaac Newton", "D) Nikola Tesla"],
            "answer": "B) Thomas Edison"
        },
        "What is the nickname of New Jersey?": {
            "options": ["A) The Garden State", "B) The Empire State", "C) The Bay State", "D) The Keystone State"],
            "answer": "A) The Garden State"
        },
        "Which river forms part of the border between New Jersey and Pennsylvania?": {
            "options": ["A) Delaware River", "B) Hudson River", "C) Connecticut River", "D) Passaic River"],
            "answer": "A) Delaware River"
        },
        "Which of the following is the state bird of New Jersey?": {
            "options": ["A) American Goldfinch", "B) Eastern Bluebird", "C) Northern Cardinal", "D) Eastern Goldfinch"],
            "answer": "A) American Goldfinch"
        },
        "What is the highest point in New Jersey?": {
            "options": ["A) High Point", "B) Mount Mitchell", "C) Mount Marcy", "D) Mount Washington"],
            "answer": "A) High Point"
        },
        "In which year did New Jersey become a state?": {
            "options": ["A) 1776", "B) 1789", "C) 1787", "D) 1790"],
            "answer": "C) 1787"
        },
        "What is the largest city in New Jersey by population?": {
            "options": ["A) Trenton", "B) Newark", "C) Jersey City", "D) Paterson"],
            "answer": "B) Newark"
        },
        "Which famous boardwalk is located in New Jersey?": {
            "options": ["A) Coney Island Boardwalk", "B) Atlantic City Boardwalk", "C) Venice Beach Boardwalk", "D) Myrtle Beach Boardwalk"],
            "answer": "B) Atlantic City Boardwalk"
        },
        "What is New Jersey's state motto?": {
            "options": ["A) Liberty and Prosperity", "B) Excelsior", "C) Eureka", "D) Ad Astra Per Aspera"],
            "answer": "A) Liberty and Prosperity"
        }
    }
    New_Mexico = {
        "What is the capital city of New Mexico?": {
            "options": ["A) Santa Fe", "B) Albuquerque", "C) Las Cruces", "D) Roswell"],
            "answer": "A) Santa Fe"
        },
        "Which famous artist's museum is located in Santa Fe, New Mexico?": {
            "options": ["A) Pablo Picasso", "B) Georgia O'Keeffe", "C) Vincent van Gogh", "D) Salvador Dalí"],
            "answer": "B) Georgia O'Keeffe"
        },
        "What is the nickname of New Mexico?": {
            "options": ["A) The Land of Enchantment", "B) The Silver State", "C) The Sunshine State", "D) The Land of Opportunity"],
            "answer": "A) The Land of Enchantment"
        },
        "Which of the following is the state flower of New Mexico?": {
            "options": ["A) Saguaro Cactus Blossom", "B) Desert Marigold", "C) Yucca Flower", "D) Bluebonnet"],
            "answer": "C) Yucca Flower"
        },
        "What is the highest point in New Mexico?": {
            "options": ["A) Wheeler Peak", "B) Mount Elbert", "C) Mount Whitney", "D) Guadalupe Peak"],
            "answer": "A) Wheeler Peak"
        },
        "In which year did New Mexico become a state?": {
            "options": ["A) 1912", "B) 1907", "C) 1910", "D) 1916"],
            "answer": "A) 1912"
        },
        "What is the largest city in New Mexico by population?": {
            "options": ["A) Santa Fe", "B) Albuquerque", "C) Las Cruces", "D) Rio Rancho"],
            "answer": "B) Albuquerque"
        },
        "Which famous national park is located in New Mexico?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon National Park", "C) Great Smoky Mountains National Park", "D) Carlsbad Caverns National Park"],
            "answer": "D) Carlsbad Caverns National Park"
        },
        "What is New Mexico's state bird?": {
            "options": ["A) Roadrunner", "B) Western Meadowlark", "C) Greater Roadrunner", "D) American Robin"],
            "answer": "C) Greater Roadrunner"
        },
        "What is New Mexico's state cookie?": {
            "options": ["A) Chocolate Chip Cookie", "B) Biscochito", "C) Oatmeal Raisin Cookie", "D) Peanut Butter Cookie"],
            "answer": "B) Biscochito"
        }
    }
    New_York = {
        "What is the capital city of New York?": {
            "options": ["A) New York City", "B) Albany", "C) Buffalo", "D) Syracuse"],
            "answer": "B) Albany"
        },
        "Which waterfall is located on the border between New York and Canada?": {
            "options": ["A) Niagara Falls", "B) Victoria Falls", "C) Angel Falls", "D) Iguazu Falls"],
            "answer": "A) Niagara Falls"
        },
        "What is the nickname of New York?": {
            "options": ["A) The Empire State", "B) The Keystone State", "C) The Sunshine State", "D) The Land of Enchantment"],
            "answer": "A) The Empire State"
        },
        "Which of the following is the state tree of New York?": {
            "options": ["A) Oak", "B) Maple", "C) Pine", "D) Elm"],
            "answer": "B) Maple"
        },
        "What is the highest point in New York?": {
            "options": ["A) Mount Marcy", "B) Mount Washington", "C) Mount Mansfield", "D) Mount Katahdin"],
            "answer": "A) Mount Marcy"
        },
        "In which year did New York become a state?": {
            "options": ["A) 1776", "B) 1788", "C) 1792", "D) 1801"],
            "answer": "B) 1788"
        },
        "Which famous building is a prominent landmark in New York City?": {
            "options": ["A) Empire State Building", "B) Willis Tower", "C) One World Trade Center", "D) Chrysler Building"],
            "answer": "A) Empire State Building"
        },
        "Which river forms part of the border between New York and Canada?": {
            "options": ["A) Mississippi River", "B) Hudson River", "C) Colorado River", "D) St. Lawrence River"],
            "answer": "D) St. Lawrence River"
        },
        "What is New York's state bird?": {
            "options": ["A) Eastern Bluebird", "B) Eastern Goldfinch", "C) Eastern Bluebird", "D) Eastern Meadowlark"],
            "answer": "C) Eastern Bluebird"
        },
        "What is New York's state fruit?": {
            "options": ["A) Apple", "B) Grape", "C) Orange", "D) Peach"],
            "answer": "A) Apple"
        }
    }
    North_Carolina = {
        "What is the capital city of North Carolina?": {
            "options": ["A) Raleigh", "B) Charlotte", "C) Durham", "D) Asheville"],
            "answer": "A) Raleigh"
        },
        "Which of the following is known as the highest peak in North Carolina?": {
            "options": ["A) Mount Jefferson", "B) Mount Mitchell", "C) Grandfather Mountain", "D) Pilot Mountain"],
            "answer": "B) Mount Mitchell"
        },
        "What is the nickname of North Carolina?": {
            "options": ["A) The Grand Canyon State", "B) The Tar Heel State", "C) The Lone Star State", "D) The Garden State"],
            "answer": "B) The Tar Heel State"
        },
        "Which of these famous beaches is located in North Carolina?": {
            "options": ["A) Miami Beach", "B) Myrtle Beach", "C) Virginia Beach", "D) Outer Banks"],
            "answer": "D) Outer Banks"
        },
        "What is the state flower of North Carolina?": {
            "options": ["A) Dogwood", "B) Sunflower", "C) Daisy", "D) Rose"],
            "answer": "A) Dogwood"
        },
        "In which year did North Carolina become a state?": {
            "options": ["A) 1789", "B) 1795", "C) 1803", "D) 1812"],
            "answer": "A) 1789"
        },
        "Which university is located in Chapel Hill, North Carolina?": {
            "options": ["A) Duke University", "B) University of North Carolina", "C) North Carolina State University", "D) Wake Forest University"],
            "answer": "B) University of North Carolina"
        },
        "What river forms part of the border between North Carolina and South Carolina?": {
            "options": ["A) Mississippi River", "B) Hudson River", "C) Colorado River", "D) Catawba River"],
            "answer": "D) Catawba River"
        },
        "What is North Carolina's state bird?": {
            "options": ["A) Eastern Bluebird", "B) Northern Cardinal", "C) Northern Mockingbird", "D) Brown Thrasher"],
            "answer": "B) Northern Cardinal"
        },
        "Which of the following is North Carolina's state reptile?": {
            "options": ["A) Box Turtle", "B) Alligator", "C) Eastern Diamondback Rattlesnake", "D) Gopher Tortoise"],
            "answer": "A) Box Turtle"
        }
    }
    North_Dakota = {
        "What is the capital city of North Dakota?": {
            "options": ["A) Bismarck", "B) Fargo", "C) Grand Forks", "D) Minot"],
            "answer": "A) Bismarck"
        },
        "Which of the following is North Dakota's state nickname?": {
            "options": ["A) The Silver State", "B) The Peace Garden State", "C) The Green Mountain State", "D) The Sunflower State"],
            "answer": "B) The Peace Garden State"
        },
        "What is the largest city in North Dakota?": {
            "options": ["A) Bismarck", "B) Fargo", "C) Grand Forks", "D) Minot"],
            "answer": "B) Fargo"
        },
        "Which river forms most of North Dakota's eastern border?": {
            "options": ["A) Missouri River", "B) Mississippi River", "C) Red River", "D) Yellowstone River"],
            "answer": "C) Red River"
        },
        "What is the state bird of North Dakota?": {
            "options": ["A) Western Meadowlark", "B) American Robin", "C) Bald Eagle", "D) Pheasant"],
            "answer": "A) Western Meadowlark"
        },
        "When did North Dakota become a state?": {
            "options": ["A) 1889", "B) 1892", "C) 1901", "D) 1910"],
            "answer": "A) 1889"
        },
        "Which national park in North Dakota is known for its rugged Badlands?": {
            "options": ["A) Yellowstone National Park", "B) Theodore Roosevelt National Park", "C) Grand Canyon National Park", "D) Great Smoky Mountains National Park"],
            "answer": "B) Theodore Roosevelt National Park"
        },
        "What is North Dakota's state flower?": {
            "options": ["A) Sunflower", "B) Wild Prairie Rose", "C) Bluebonnet", "D) Daisy"],
            "answer": "B) Wild Prairie Rose"
        },
        "What is the state tree of North Dakota?": {
            "options": ["A) American Elm", "B) Cottonwood", "C) Eastern Redbud", "D) Northern Red Oak"],
            "answer": "A) American Elm"
        },
        "Which of these is a famous event held annually in North Dakota that involves hot air balloons?": {
            "options": ["A) Albuquerque International Balloon Fiesta", "B) Great Reno Balloon Race", "C) International Balloon Festival of Saint-Jean-sur-Richelieu", "D) Albuquerque International Balloon Festival"],
            "answer": "D) Albuquerque International Balloon Festival"
        }
    }
    Ohio = {
        "What is the capital city of Ohio?": {
            "options": ["A) Columbus", "B) Cleveland", "C) Cincinnati", "D) Dayton"],
            "answer": "A) Columbus"
        },
        "Which of the following is Ohio's state nickname?": {
            "options": ["A) The Silver State", "B) The Buckeye State", "C) The Peach State", "D) The Garden State"],
            "answer": "B) The Buckeye State"
        },
        "What is the largest city in Ohio?": {
            "options": ["A) Columbus", "B) Cleveland", "C) Cincinnati", "D) Dayton"],
            "answer": "B) Cleveland"
        },
        "Which Great Lake does not border Ohio?": {
            "options": ["A) Lake Erie", "B) Lake Huron", "C) Lake Michigan", "D) Lake Ontario"],
            "answer": "D) Lake Ontario"
        },
        "What is the state bird of Ohio?": {
            "options": ["A) Northern Cardinal", "B) American Robin", "C) Bald Eagle", "D) Eastern Bluebird"],
            "answer": "A) Northern Cardinal"
        },
        "When did Ohio become a state?": {
            "options": ["A) 1803", "B) 1812", "C) 1821", "D) 1836"],
            "answer": "A) 1803"
        },
        "Which amusement park in Ohio is known for its roller coasters, including the Millennium Force and the Top Thrill Dragster?": {
            "options": ["A) Six Flags Great Adventure", "B) Cedar Point", "C) Kings Island", "D) Disneyland"],
            "answer": "B) Cedar Point"
        },
        "What is Ohio's state flower?": {
            "options": ["A) Red Rose", "B) Scarlet Carnation", "C) White Lily", "D) Yellow Daisy"],
            "answer": "B) Scarlet Carnation"
        },
        "What is the state tree of Ohio?": {
            "options": ["A) White Oak", "B) Red Maple", "C) Buckeye", "D) Sycamore"],
            "answer": "C) Buckeye"
        },
        "Which of these is a famous river in Ohio known for its high pollution levels due to industrial contamination?": {
            "options": ["A) Ohio River", "B) Hudson River", "C) Mississippi River", "D) Colorado River"],
            "answer": "A) Ohio River"
        }
    }
    Oklahoma = {
        "What is the capital city of Oklahoma?": {
            "options": ["A) Oklahoma City", "B) Tulsa", "C) Norman", "D) Lawton"],
            "answer": "A) Oklahoma City"
        },
        "Which of the following is Oklahoma's state nickname?": {
            "options": ["A) The Sooner State", "B) The Hawkeye State", "C) The Volunteer State", "D) The Land of Enchantment"],
            "answer": "A) The Sooner State"
        },
        "What is the largest city in Oklahoma?": {
            "options": ["A) Oklahoma City", "B) Tulsa", "C) Norman", "D) Lawton"],
            "answer": "A) Oklahoma City"
        },
        "Which of these U.S. presidents was born in Oklahoma?": {
            "options": ["A) Abraham Lincoln", "B) George Washington", "C) Thomas Jefferson", "D) Dwight D. Eisenhower"],
            "answer": "D) Dwight D. Eisenhower"
        },
        "What is the state bird of Oklahoma?": {
            "options": ["A) Eastern Bluebird", "B) Northern Mockingbird", "C) Scissor-tailed Flycatcher", "D) Western Meadowlark"],
            "answer": "C) Scissor-tailed Flycatcher"
        },
        "When did Oklahoma become a state?": {
            "options": ["A) 1890", "B) 1907", "C) 1912", "D) 1923"],
            "answer": "B) 1907"
        },
        "Which of these is a famous natural landmark in Oklahoma known for its unusual rock formations?": {
            "options": ["A) Grand Canyon", "B) Mount Rushmore", "C) Monument Valley", "D) Gloss Mountains"],
            "answer": "D) Gloss Mountains"
        },
        "What is Oklahoma's state flower?": {
            "options": ["A) Indian Paintbrush", "B) Black-eyed Susan", "C) Rose", "D) Mistletoe"],
            "answer": "A) Indian Paintbrush"
        },
        "What is the state tree of Oklahoma?": {
            "options": ["A) Redbud", "B) Cottonwood", "C) Oak", "D) Pine"],
            "answer": "A) Redbud"
        },
        "Which of these rivers forms part of Oklahoma's southern border?": {
            "options": ["A) Mississippi River", "B) Rio Grande", "C) Arkansas River", "D) Red River"],
            "answer": "D) Red River"
        }
    }
    Oregon = {
        "What is the capital city of Oregon?": {
            "options": ["A) Portland", "B) Eugene", "C) Salem", "D) Bend"],
            "answer": "C) Salem"
        },
        "Which of the following is Oregon's state nickname?": {
            "options": ["A) The Beaver State", "B) The Sunshine State", "C) The Granite State", "D) The Equality State"],
            "answer": "A) The Beaver State"
        },
        "What is the largest city in Oregon?": {
            "options": ["A) Portland", "B) Eugene", "C) Salem", "D) Bend"],
            "answer": "A) Portland"
        },
        "Which of these national parks is located in Oregon?": {
            "options": ["A) Grand Canyon National Park", "B) Yellowstone National Park", "C) Crater Lake National Park", "D) Yosemite National Park"],
            "answer": "C) Crater Lake National Park"
        },
        "What is the state bird of Oregon?": {
            "options": ["A) Western Meadowlark", "B) American Robin", "C) Western Bluebird", "D) Western Meadowlark"],
            "answer": "B) American Robin"
        },
        "When did Oregon become a state?": {
            "options": ["A) 1859", "B) 1876", "C) 1890", "D) 1907"],
            "answer": "A) 1859"
        },
        "Which of these is a famous natural landmark in Oregon known for its unique rock formations and waterfalls?": {
            "options": ["A) Grand Canyon", "B) Mount Rushmore", "C) Yellowstone National Park", "D) Columbia River Gorge"],
            "answer": "D) Columbia River Gorge"
        },
        "What is Oregon's state flower?": {
            "options": ["A) Oregon Grape", "B) Camellia", "C) Bluebonnet", "D) Lily"],
            "answer": "A) Oregon Grape"
        },
        "What is the state tree of Oregon?": {
            "options": ["A) Douglas Fir", "B) Redwood", "C) Ponderosa Pine", "D) Sequoia"],
            "answer": "A) Douglas Fir"
        },
        "Which of these rivers flows through the city of Portland?": {
            "options": ["A) Colorado River", "B) Columbia River", "C) Mississippi River", "D) Ohio River"],
            "answer": "B) Columbia River"
        }
    }
    Pennsylvania = {
        "What is the capital city of Pennsylvania?": {
            "options": ["A) Philadelphia", "B) Pittsburgh", "C) Harrisburg", "D) Allentown"],
            "answer": "C) Harrisburg"
        },
        "Which of the following is Pennsylvania's state nickname?": {
            "options": ["A) The Bay State", "B) The Keystone State", "C) The Garden State", "D) The Empire State"],
            "answer": "B) The Keystone State"
        },
        "What is the largest city in Pennsylvania?": {
            "options": ["A) Philadelphia", "B) Pittsburgh", "C) Harrisburg", "D) Allentown"],
            "answer": "A) Philadelphia"
        },
        "Which of these historical documents was signed in Philadelphia, Pennsylvania in 1776?": {
            "options": ["A) The Magna Carta", "B) The Declaration of Independence", "C) The U.S. Constitution", "D) The Bill of Rights"],
            "answer": "B) The Declaration of Independence"
        },
        "What is the state bird of Pennsylvania?": {
            "options": ["A) Ruffed Grouse", "B) Eastern Bluebird", "C) American Goldfinch", "D) American Kestrel"],
            "answer": "A) Ruffed Grouse"
        },
        "When did Pennsylvania become a state?": {
            "options": ["A) 1787", "B) 1790", "C) 1800", "D) 1810"],
            "answer": "A) 1787"
        },
        "Which of these is a famous museum located in Pittsburgh, Pennsylvania?": {
            "options": ["A) The Louvre", "B) The Metropolitan Museum of Art", "C) The Smithsonian Institution", "D) The Andy Warhol Museum"],
            "answer": "D) The Andy Warhol Museum"
        },
        "What is Pennsylvania's state flower?": {
            "options": ["A) Mountain Laurel", "B) Rhododendron", "C) Dogwood", "D) Rose"],
            "answer": "A) Mountain Laurel"
        },
        "What is the state tree of Pennsylvania?": {
            "options": ["A) Eastern Hemlock", "B) Sugar Maple", "C) Eastern Redbud", "D) Eastern White Pine"],
            "answer": "A) Eastern Hemlock"
        },
        "Which of these sports teams is based in Philadelphia, Pennsylvania?": {
            "options": ["A) Pittsburgh Steelers", "B) Philadelphia Eagles", "C) Pittsburgh Penguins", "D) Pittsburgh Pirates"],
            "answer": "B) Philadelphia Eagles"
        }
    }
    Rhode_Island = {
        "What is the capital city of Rhode Island?": {
            "options": ["A) Providence", "B) Newport", "C) Warwick", "D) Cranston"],
            "answer": "A) Providence"
        },
        "Which of the following is Rhode Island's state nickname?": {
            "options": ["A) The Ocean State", "B) The Granite State", "C) The Green Mountain State", "D) The Silver State"],
            "answer": "A) The Ocean State"
        },
        "What is the largest city in Rhode Island?": {
            "options": ["A) Providence", "B) Newport", "C) Warwick", "D) Cranston"],
            "answer": "A) Providence"
        },
        "Which of these historical figures founded the colony of Rhode Island?": {
            "options": ["A) John Smith", "B) Roger Williams", "C) William Penn", "D) John Winthrop"],
            "answer": "B) Roger Williams"
        },
        "What is the state bird of Rhode Island?": {
            "options": ["A) American Goldfinch", "B) Rhode Island Red", "C) Northern Cardinal", "D) Common Loon"],
            "answer": "B) Rhode Island Red"
        },
        "When did Rhode Island become a state?": {
            "options": ["A) 1790", "B) 1776", "C) 1787", "D) 1791"],
            "answer": "D) 1791"
        },
        "Which of these is a famous mansion located in Newport, Rhode Island?": {
            "options": ["A) Biltmore Estate", "B) Hearst Castle", "C) The Breakers", "D) Graceland"],
            "answer": "C) The Breakers"
        },
        "What is Rhode Island's state flower?": {
            "options": ["A) Violet", "B) Mayflower", "C) White Pine Cone and Tassel", "D) Rhode Island Red"],
            "answer": "A) Violet"
        },
        "What is the state tree of Rhode Island?": {
            "options": ["A) Eastern Redbud", "B) Sugar Maple", "C) Red Oak", "D) White Ash"],
            "answer": "A) Eastern Redbud"
        },
        "Which of these universities is located in Providence, Rhode Island?": {
            "options": ["A) Harvard University", "B) Yale University", "C) Brown University", "D) Princeton University"],
            "answer": "C) Brown University"
        }
    }
    South_Carolina = {
        "What is the capital city of South Carolina?": {
            "options": ["A) Charleston", "B) Columbia", "C) Greenville", "D) Myrtle Beach"],
            "answer": "B) Columbia"
        },
        "Which of the following is South Carolina's state nickname?": {
            "options": ["A) The Palmetto State", "B) The Granite State", "C) The Hoosier State", "D) The Bay State"],
            "answer": "A) The Palmetto State"
        },
        "What is the largest city in South Carolina?": {
            "options": ["A) Charleston", "B) Columbia", "C) Greenville", "D) Myrtle Beach"],
            "answer": "A) Charleston"
        },
        "Which of these historical figures was a prominent leader during the Civil War and served as the Vice President of the Confederacy?": {
            "options": ["A) Thomas Jefferson", "B) Abraham Lincoln", "C) Jefferson Davis", "D) Ulysses S. Grant"],
            "answer": "C) Jefferson Davis"
        },
        "What is the state bird of South Carolina?": {
            "options": ["A) Wild Turkey", "B) Carolina Wren", "C) Northern Mockingbird", "D) Wood Duck"],
            "answer": "B) Carolina Wren"
        },
        "When did South Carolina become a state?": {
            "options": ["A) 1788", "B) 1776", "C) 1790", "D) 1791"],
            "answer": "A) 1788"
        },
        "Which of these is a famous plantation located near Charleston, South Carolina?": {
            "options": ["A) Monticello", "B) Magnolia Plantation and Gardens", "C) Mount Vernon", "D) The Hermitage"],
            "answer": "B) Magnolia Plantation and Gardens"
        },
        "What is South Carolina's state flower?": {
            "options": ["A) Yellow Jessamine", "B) Goldenrod", "C) American Beauty Rose", "D) Daisy"],
            "answer": "A) Yellow Jessamine"
        },
        "What is the state tree of South Carolina?": {
            "options": ["A) Longleaf Pine", "B) Bald Cypress", "C) American Elm", "D) Sabal Palmetto"],
            "answer": "D) Sabal Palmetto"
        },
        "Which of these famous golf tournaments is held annually in Augusta, Georgia, but is closely associated with South Carolina?": {
            "options": ["A) The Masters", "B) The U.S. Open", "C) The British Open", "D) The PGA Championship"],
            "answer": "A) The Masters"
        }
    }
    South_Dakota = {
        "What is the capital city of South Dakota?": {
            "options": ["A) Sioux Falls", "B) Rapid City", "C) Pierre", "D) Aberdeen"],
            "answer": "C) Pierre"
        },
        "Which of the following is South Dakota's state nickname?": {
            "options": ["A) The Mount Rushmore State", "B) The Sunshine State", "C) The Aloha State", "D) The Peach State"],
            "answer": "A) The Mount Rushmore State"
        },
        "What is the largest city in South Dakota?": {
            "options": ["A) Sioux Falls", "B) Rapid City", "C) Pierre", "D) Aberdeen"],
            "answer": "A) Sioux Falls"
        },
        "Which famous monument is located in the Black Hills of South Dakota?": {
            "options": ["A) Statue of Liberty", "B) Mount Rushmore", "C) Washington Monument", "D) Lincoln Memorial"],
            "answer": "B) Mount Rushmore"
        },
        "What is the state bird of South Dakota?": {
            "options": ["A) Ring-necked Pheasant", "B) Northern Mockingbird", "C) American Goldfinch", "D) Wild Turkey"],
            "answer": "A) Ring-necked Pheasant"
        },
        "When did South Dakota become a state?": {
            "options": ["A) 1889", "B) 1859", "C) 1901", "D) 1925"],
            "answer": "A) 1889"
        },
        "Which of these national parks is located in South Dakota?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon National Park", "C) Badlands National Park", "D) Great Smoky Mountains National Park"],
            "answer": "C) Badlands National Park"
        },
        "What is South Dakota's state flower?": {
            "options": ["A) Black-eyed Susan", "B) Pasque Flower", "C) Bluebonnet", "D) Indian Paintbrush"],
            "answer": "B) Pasque Flower"
        },
        "What is the state tree of South Dakota?": {
            "options": ["A) Black Hills Spruce", "B) Black Walnut", "C) White Oak", "D) Black Hills Cottonwood"],
            "answer": "A) Black Hills Spruce"
        },
        "Which of these Native American tribes is closely associated with South Dakota and has a reservation in the state?": {
            "options": ["A) Cherokee", "B) Navajo", "C) Lakota Sioux", "D) Apache"],
            "answer": "C) Lakota Sioux"
        }
    }
    Tennessee = {
        "What is the capital city of Tennessee?": {
            "options": ["A) Nashville", "B) Memphis", "C) Knoxville", "D) Chattanooga"],
            "answer": "A) Nashville"
        },
        "Which famous country music event takes place annually in Nashville, Tennessee?": {
            "options": ["A) CMA Awards", "B) Grammy Awards", "C) Coachella", "D) Lollapalooza"],
            "answer": "A) CMA Awards"
        },
        "What is Tennessee's state nickname?": {
            "options": ["A) The Volunteer State", "B) The Peach State", "C) The Golden State", "D) The Evergreen State"],
            "answer": "A) The Volunteer State"
        },
        "Which river forms part of the western border of Tennessee?": {
            "options": ["A) Mississippi River", "B) Colorado River", "C) Ohio River", "D) Tennessee River"],
            "answer": "A) Mississippi River"
        },
        "What is the largest city in Tennessee?": {
            "options": ["A) Nashville", "B) Memphis", "C) Knoxville", "D) Chattanooga"],
            "answer": "B) Memphis"
        },
        "Which of the following is a famous natural attraction in Tennessee known for its underground cave system?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon", "C) Great Smoky Mountains National Park", "D) Mammoth Cave National Park"],
            "answer": "D) Mammoth Cave National Park"
        },
        "When did Tennessee become a state?": {
            "options": ["A) 1796", "B) 1865", "C) 1900", "D) 1950"],
            "answer": "A) 1796"
        },
        "What is Tennessee's state flower?": {
            "options": ["A) Daisy", "B) Iris", "C) Sunflower", "D) Rose"],
            "answer": "B) Iris"
        },
        "What is the state tree of Tennessee?": {
            "options": ["A) Red Oak", "B) Tulip Poplar", "C) Maple", "D) Pine"],
            "answer": "B) Tulip Poplar"
        },
        "Which U.S. president was born in Tennessee?": {
            "options": ["A) Abraham Lincoln", "B) Andrew Jackson", "C) Thomas Jefferson", "D) George Washington"],
            "answer": "B) Andrew Jackson"
        }
    }
    Texas = {
        "What is the capital city of Texas?": {
            "options": ["A) Houston", "B) Dallas", "C) Austin", "D) San Antonio"],
            "answer": "C) Austin"
        },
        "Which famous festival in Texas is known for its music, film, and interactive media?": {
            "options": ["A) South by Southwest (SXSW)", "B) Coachella", "C) Burning Man", "D) Bonnaroo"],
            "answer": "A) South by Southwest (SXSW)"
        },
        "What is Texas's state nickname?": {
            "options": ["A) The Lone Star State", "B) The Sunshine State", "C) The Empire State", "D) The Golden State"],
            "answer": "A) The Lone Star State"
        },
        "Which river forms the border between Texas and Mexico?": {
            "options": ["A) Colorado River", "B) Rio Grande", "C) Mississippi River", "D) Missouri River"],
            "answer": "B) Rio Grande"
        },
        "What is the largest city in Texas?": {
            "options": ["A) Houston", "B) Dallas", "C) Austin", "D) San Antonio"],
            "answer": "A) Houston"
        },
        "Which of the following is a famous natural landmark in Texas known for its rock formations?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon", "C) Big Bend National Park", "D) Yosemite National Park"],
            "answer": "C) Big Bend National Park"
        },
        "When did Texas become a state?": {
            "options": ["A) 1820", "B) 1845", "C) 1876", "D) 1900"],
            "answer": "B) 1845"
        },
        "What is Texas's state flower?": {
            "options": ["A) Bluebonnet", "B) Rose", "C) Sunflower", "D) Daisy"],
            "answer": "A) Bluebonnet"
        },
        "What is the state tree of Texas?": {
            "options": ["A) Oak", "B) Pecan", "C) Pine", "D) Redwood"],
            "answer": "B) Pecan"
        },
        "Which U.S. president was born in Texas?": {
            "options": ["A) Abraham Lincoln", "B) George Washington", "C) Lyndon B. Johnson", "D) Thomas Jefferson"],
            "answer": "C) Lyndon B. Johnson"
        }
    }
    Utah = {
        "What is the capital city of Utah?": {
            "options": ["A) Salt Lake City", "B) Provo", "C) Ogden", "D) St. George"],
            "answer": "A) Salt Lake City"
        },
        "Which national park in Utah is known for its unique rock formations like hoodoos?": {
            "options": ["A) Yellowstone National Park", "B) Grand Canyon National Park", "C) Arches National Park", "D) Zion National Park"],
            "answer": "C) Arches National Park"
        },
        "What is Utah's state nickname?": {
            "options": ["A) The Beehive State", "B) The Granite State", "C) The Evergreen State", "D) The Garden State"],
            "answer": "A) The Beehive State"
        },
        "Which of the following is a famous ski resort in Utah?": {
            "options": ["A) Aspen", "B) Vail", "C) Park City", "D) Mammoth Mountain"],
            "answer": "C) Park City"
        },
        "What is the largest religious denomination in Utah?": {
            "options": ["A) Baptist", "B) Lutheran", "C) Mormon (Latter-day Saint)", "D) Catholic"],
            "answer": "C) Mormon (Latter-day Saint)"
        },
        "Which lake in Utah is known for its high salt content, making it easy for people to float on the surface?": {
            "options": ["A) Lake Superior", "B) Great Salt Lake", "C) Lake Michigan", "D) Lake Powell"],
            "answer": "B) Great Salt Lake"
        },
        "When did Utah become a state?": {
            "options": ["A) 1867", "B) 1896", "C) 1907", "D) 1912"],
            "answer": "B) 1896"
        },
        "What is Utah's state flower?": {
            "options": ["A) Sego Lily", "B) Sunflower", "C) Rose", "D) Bluebonnet"],
            "answer": "A) Sego Lily"
        },
        "What is the state tree of Utah?": {
            "options": ["A) Oak", "B) Pine", "C) Quaking Aspen", "D) Maple"],
            "answer": "C) Quaking Aspen"
        },
        "Which national monument in Utah is known for its natural bridges?": {
            "options": ["A) Mount Rushmore National Memorial", "B) White Sands National Monument", "C) Grand Staircase-Escalante National Monument", "D) Natural Bridges National Monument"],
            "answer": "D) Natural Bridges National Monument"
        }
    }
    Vermont = {
        "What is the capital city of Vermont?": {
            "options": ["A) Burlington", "B) Montpelier", "C) Rutland", "D) Brattleboro"],
            "answer": "B) Montpelier"
        },
        "Which famous ice cream company was founded in Vermont?": {
            "options": ["A) Ben & Jerry's", "B) Häagen-Dazs", "C) Baskin-Robbins", "D) Dairy Queen"],
            "answer": "A) Ben & Jerry's"
        },
        "What is Vermont's state motto?": {
            "options": ["A) Live Free or Die", "B) Freedom and Unity", "C) Eureka", "D) Peace and Justice"],
            "answer": "B) Freedom and Unity"
        },
        "Which of the following is a famous ski resort in Vermont?": {
            "options": ["A) Aspen", "B) Vail", "C) Stowe", "D) Mammoth Mountain"],
            "answer": "C) Stowe"
        },
        "What is Vermont's state bird?": {
            "options": ["A) American Robin", "B) Northern Cardinal", "C) Hermit Thrush", "D) Baltimore Oriole"],
            "answer": "C) Hermit Thrush"
        },
        "Which lake in Vermont is one of the largest freshwater lakes in the United States?": {
            "options": ["A) Lake Erie", "B) Lake Ontario", "C) Lake Champlain", "D) Lake Winnipesaukee"],
            "answer": "C) Lake Champlain"
        },
        "When did Vermont become a state?": {
            "options": ["A) 1776", "B) 1791", "C) 1803", "D) 1820"],
            "answer": "B) 1791"
        },
        "What is Vermont's state flower?": {
            "options": ["A) Red Clover", "B) Mountain Laurel", "C) Violet", "D) Rose"],
            "answer": "A) Red Clover"
        },
        "What is the state tree of Vermont?": {
            "options": ["A) Oak", "B) Maple", "C) Elm", "D) Pine"],
            "answer": "B) Maple"
        },
        "Which national park in Vermont is known for its scenic drive and fall foliage?": {
            "options": ["A) Acadia National Park", "B) Great Smoky Mountains National Park", "C) Shenandoah National Park", "D) none"],
            "answer": "D) none (Vermont does not have a national park)"
        }
    }
    Virginia = {
        "What is the capital city of Virginia?": {
            "options": ["A) Richmond", "B) Virginia Beach", "C) Norfolk", "D) Alexandria"],
            "answer": "A) Richmond"
        },
        "Which of the following presidents was born in Virginia?": {
            "options": ["A) John F. Kennedy", "B) Abraham Lincoln", "C) Thomas Jefferson", "D) Franklin D. Roosevelt"],
            "answer": "C) Thomas Jefferson"
        },
        "What is Virginia's state nickname?": {
            "options": ["A) The Sunshine State", "B) The Old Dominion", "C) The Golden State", "D) The Peach State"],
            "answer": "B) The Old Dominion"
        },
        "Which river forms part of the border between Virginia and Maryland?": {
            "options": ["A) Potomac River", "B) Mississippi River", "C) Ohio River", "D) Colorado River"],
            "answer": "A) Potomac River"
        },
        "What is Virginia's state flower?": {
            "options": ["A) Rose", "B) Dogwood", "C) Iris", "D) Sunflower"],
            "answer": "B) Dogwood"
        },
        "Which of the following is a historic site in Virginia related to the first English colony in America?": {
            "options": ["A) Jamestown Settlement", "B) Plymouth Rock", "C) Statue of Liberty", "D) Alamo Mission"],
            "answer": "A) Jamestown Settlement"
        },
        "When did Virginia become a state?": {
            "options": ["A) 1763", "B) 1776", "C) 1788", "D) 1791"],
            "answer": "C) 1788"
        },
        "What is Virginia's state bird?": {
            "options": ["A) Bald Eagle", "B) American Robin", "C) Northern Cardinal", "D) Wood Thrush"],
            "answer": "A) Cardinal"
        },
        "What is Virginia's state tree?": {
            "options": ["A) Oak", "B) Pine", "C) Dogwood", "D) Elm"],
            "answer": "C) Dogwood"
        },
        "Which university, founded by Thomas Jefferson, is located in Virginia?": {
            "options": ["A) Harvard University", "B) Yale University", "C) Stanford University", "D) University of Virginia"],
            "answer": "D) University of Virginia"
        }
    }
    Washington = {
    "What is the capital city of Washington?": {
    "options": ["A) Seattle", "B) Spokane", "C) Olympia", "D) Tacoma"],
    "answer": "C) Olympia"
    },
    "Which mountain range lies to the west of Washington state?": {
    "options": ["A) Rocky Mountains", "B) Sierra Nevada", "C) Cascade Range", "D) Appalachian Mountains"],
    "answer": "C) Cascade Range"
    },
    "What is the state bird of Washington?": {
    "options": ["A) American Goldfinch", "B) Willow Goldfinch", "C) Northern Mockingbird", "D) American Robin"],
    "answer": "B) Willow Goldfinch"
    },
    "What is Washington's nickname?": {
    "options": ["A) The Evergreen State", "B) The Sunshine State", "C) The Mountain State", "D) The Garden State"],
    "answer": "A) The Evergreen State"
    },
    "Which Washington city is known for its famous Space Needle?": {
    "options": ["A) Seattle", "B) Spokane", "C) Bellevue", "D) Everett"],
    "answer": "A) Seattle"
    },
    "What is the largest national park in Washington?": {
    "options": ["A) Olympic National Park", "B) North Cascades National Park", "C) Mount Rainier National Park", "D) Mount St. Helens National Volcanic Monument"],
    "answer": "A) Olympic National Park"
    },
    "Which Washington city is nicknamed the 'Apple Capital of the World'?": {
    "options": ["A) Wenatchee", "B) Yakima", "C) Walla Walla", "D) Spokane"],
    "answer": "A) Wenatchee"
    },
    "What is the name of the strait that separates Washington from Vancouver Island, Canada?": {
    "options": ["A) Puget Sound", "B) Strait of Georgia", "C) Strait of Juan de Fuca", "D) Rosario Strait"],
    "answer": "C) Strait of Juan de Fuca"
    },
    "Which Washington city is home to the University of Washington?": {
    "options": ["A) Seattle", "B) Spokane", "C) Tacoma", "D) Bellingham"],
    "answer": "A) Seattle"
    },
    "What is the highest peak in Washington?": {
    "options": ["A) Mount Adams", "B) Mount Rainier", "C) Mount Baker", "D) Mount St. Helens"],
    "answer": "B) Mount Rainier"
    }
    }
    West_Virginia = {
    "What is the capital city of West Virginia?": {
    "options": ["A) Charleston", "B) Morgantown", "C) Wheeling", "D) Huntington"],
    "answer": "A) Charleston"
    },
    "Which river forms part of the border between West Virginia and Ohio?": {
    "options": ["A) Ohio River", "B) Mississippi River", "C) Potomac River", "D) Kanawha River"],
    "answer": "A) Ohio River"
    },
    "What is the state bird of West Virginia?": {
    "options": ["A) Northern Cardinal", "B) American Robin", "C) Eastern Bluebird", "D) Peregrine Falcon"],
    "answer": "A) Northern Cardinal"
    },
    "What is West Virginia's nickname?": {
    "options": ["A) The Mountain State", "B) The Keystone State", "C) The Bluegrass State", "D) The Volunteer State"],
    "answer": "A) The Mountain State"
    },
    "Which West Virginia city is known for its annual Ramp Feast?": {
    "options": ["A) Charleston", "B) Morgantown", "C) Wheeling", "D) Huntington"],
    "answer": "B) Morgantown"
    },
    "What is the highest point in West Virginia?": {
    "options": ["A) Spruce Knob", "B) Black Mountain", "C) Backbone Mountain", "D) Cheat Mountain"],
    "answer": "A) Spruce Knob"
    },
    "Which West Virginia city is home to West Virginia University?": {
    "options": ["A) Charleston", "B) Morgantown", "C) Huntington", "D) Wheeling"],
    "answer": "B) Morgantown"
    },
    "What is the name of the historic river gorge in West Virginia known for its whitewater rafting?": {
    "options": ["A) New River Gorge", "B) Cheat River Gorge", "C) Gauley River Gorge", "D) Kanawha River Gorge"],
    "answer": "A) New River Gorge"
    },
    "Which national park in West Virginia is known for its extensive cave system?": {
    "options": ["A) Harpers Ferry National Historical Park", "B) New River Gorge National Park and Preserve", "C) Monongahela National Forest", "D) Lost World Caverns National Park"],
    "answer": "D) Lost World Caverns National Park"
    },
    "What is the state animal of West Virginia?": {
    "options": ["A) Black Bear", "B) White-tailed Deer", "C) Raccoon", "D) Opossum"],
    "answer": "A) Black Bear"
    }
    }
    Wisconsin = {
        "Focusing on a group of six teenagers’ lives in Point Place, Wisconsin 50 years ago, what’s the name of the groovy, FOX period sitcom that starred Ashton Kutcher and Mila Kunis?": {
            "options": ["Happy Days", "That '70s Show", "The Wonder Years", "Family Ties"],
            "answer": "That '70s Show"
        },
        "On Barbie’s refrigerator is a magnet from Kenosha’s Mars Cheese Castle. Tucked in her closet are a cheese helmet and Bart Starr and Brett Favre jerseys. These are mementoes from growing up in what dairy-loving Midwest state?": {
            "options": ["Illinois", "Ohio", "Michigan", "Wisconsin"],
            "answer": "Wisconsin"
        },
        "Hopefully they have good dental in Madison! More than 50 years before Bart Simpson made sure nobody laid a finger on his, Shirley Temple shilled for what crispety-crunchety candy bar that just topped Wisconsin’s most popular Halloween candy list for 2023?": {
            "options": ["Snickers", "Twix", "Butterfinger", "Kit Kat"],
            "answer": "Butterfinger"
        },
        "Delavan, Wisconsin—not South America—is the location of the factory that produces what brand of rectangular chocolate mint candies?": {
            "options": ["Junior Mints", "York Peppermint Patties", "Andes", "After Eight"],
            "answer": "Andes"
        },
        "What biome shares its name with a Toyota truck and appears in the moniker for a famous Wisconsin football stadium?": {
            "options": ["Desert", "Tundra", "Grassland", "Forest"],
            "answer": "Tundra"
        },
        "What tear-inducing satire news site was founded by two students at the University of Wisconsin, Madison in 1988?": {
            "options": ["The Daily Currant", "The Onion", "The Beaverton", "The Borowitz Report"],
            "answer": "The Onion"
        },
        "Usonian House and the Unitarian Meeting House are two Madison buildings that were designed by what architect? Monona Terrace was created by a student of this architect based off of one of the architect's designs.": {
            "options": ["Frank Gehry", "Zaha Hadid", "Frank Lloyd Wright", "I. M. Pei"],
            "answer": "Frank Lloyd Wright"
        },
        "Quintec Integration, Inc., a leader in conveyor systems integration, opened in the small-town Germantown, Wisconsin in what year?": {
            "options": ["1995", "1997", "1999", "2001"],
            "answer": "1999"
        },
        "In 2009, the City Council of Madison, Wisconsin declared what to be the official city bird? (It might be unique among official birds around the world by being the only one made of plastic.)": {
            "options": ["Plastic Flamingo", "Plastic Parrot", "Plastic Owl", "Plastic Penguin"],
            "answer": "Plastic Flamingo"
        },
        "The first cheesehead was not worn at a Green Bay Packers game but instead at a game for what baseball team?": {
            "options": ["Chicago Cubs", "St. Louis Cardinals", "Milwaukee Brewers", "Minnesota Twins"],
            "answer": "Milwaukee Brewers"
        }
    }
    Wyoming= {
        "Of all the states, Wyoming is the least what?": {
            "options": ["Populous", "Mountainous", "Industrialized", "Sunny"],
            "answer": "Populous"
        },
        "What is the Wyoming State tree?": {
            "options": ["Plains Cottonwood", "Ponderosa Pine", "Blue Spruce", "Redwood"],
            "answer": "Plains Cottonwood"
        },
        "What city is the capital of the state of Wyoming?": {
            "options": ["Cheyenne", "Jackson", "Laramie", "Casper"],
            "answer": "Cheyenne"
        },
        "What is the Wyoming State emblem?": {
            "options": ["Bucking Horse and Rider", "Cowboy Hat", "Bison", "Mountain"],
            "answer": "Bucking Horse and Rider"
        },
        "Wyoming has one public four-year institution, the University of Wyoming in Laramie, and how many two-year community colleges?": {
            "options": ["Seven", "Three", "Five", "Ten"],
            "answer": "Seven"
        },
        "Population wise, what is the largest city in Wyoming?": {
            "options": ["Cheyenne", "Casper", "Laramie", "Gillette"],
            "answer": "Cheyenne"
        },
        "Wyoming has borders along only straight latitudinal and longitudinal lines, rather than being defined by what?": {
            "options": ["Natural landmarks", "Rivers", "Mountains", "Political boundaries"],
            "answer": "Natural landmarks"
        },
        "The Wind River Indian Reservation is jointly owned by what two Indian Tribes?": {
            "options": ["Shoshone and Arapaho", "Navajo and Cherokee", "Sioux and Apache", "Chickasaw and Choctaw"],
            "answer": "Shoshone and Arapaho"
        },
        "What state borders Wyoming on the north?": {
            "options": ["Montana", "Idaho", "Utah", "Colorado"],
            "answer": "Montana"
        },
        "What is the Wyoming State sport?": {
            "options": ["Rodeo", "Ice Hockey", "Skiing", "Football"],
            "answer": "Rodeo"
        },
        "What is the name of the only other state besides Wyoming that is not served by Amtrak?": {
            "options": ["South Dakota", "Montana", "Alaska", "North Dakota"],
            "answer": "South Dakota"
        },
        "What is the Wyoming State song?": {
            "options": ["Wyoming", "My Wyoming Home", "Sagebrush Symphony", "Wyo, My Love"],
            "answer": "Wyoming"
        },
        "Which 2 US States border Wyoming on the east?": {
            "options": ["South Dakota and Nebraska", "Montana and Idaho", "Utah and Colorado", "Kansas and Oklahoma"],
            "answer": "South Dakota and Nebraska"
        },
        "What is the name of the biggest airport in the state of Wyoming?": {
            "options": ["The Jackson Hole Airport", "Casper/Natrona County International Airport", "Cheyenne Regional Airport", "Yellowstone Regional Airport"],
            "answer": "The Jackson Hole Airport"
        },
        "What is the Wyoming State soil?": {
            "options": ["Forkwood", "Silt", "Loam", "Peat"],
            "answer": "Forkwood"
        },
        "On the south, Wyoming is bordered by what state?": {
            "options": ["Colorado", "Utah", "Idaho", "Nebraska"],
            "answer": "Colorado"
        },
        "More federal tax dollars per capita in aid flows into Wyoming than any other state except which state?": {
            "options": ["Alaska", "Hawaii", "Montana", "New Mexico"],
            "answer": "Alaska"
        },
        "What is the Wyoming State seal?": {
            "options": ["Great Seal of the State of Wyoming", "Wyoming State Crest", "Bucking Horse Emblem", "Wyoming Star"],
            "answer": "Great Seal of the State of Wyoming"
        },
        "What state borders Wyoming on the southwest?": {
            "options": ["Utah", "Idaho", "Nevada", "Arizona"],
            "answer": "Utah"
        },
        "What is the Wyoming State dinosaur?": {
            "options": ["Triceratops", "Stegosaurus", "Tyrannosaurus Rex", "Brachiosaurus"],
            "answer": "Triceratops"
        },
        "Which U.S. State borders the State of Wyoming on the west?": {
            "options": ["Idaho", "Utah", "Montana", "Nevada"],
            "answer": "Idaho"
        },
        "What is the Wyoming State reptile?": {
            "options": ["Horned lizard", "Gopher snake", "Western painted turtle", "Prairie rattlesnake"],
            "answer": "Horned lizard"
        },
        "In area, Wyoming is the 10th biggest state with how many square miles of area?": {
            "options": ["97,814", "105,412", "122,902", "135,421"],
            "answer": "97,814"
        },
        "What is the Wyoming State fish?": {
            "options": ["Cutthroat trout", "Rainbow trout", "Brook trout", "Brown trout"],
            "answer": "Cutthroat trout"
        },
        "How many counties does Wyoming have?": {
            "options": ["23", "17", "30", "25"],
            "answer": "23"
        }
    }

    all_states["Alabama"] = Alabama
    all_states["Alaska"] = Alaska
    all_states["Arizona"] = Arizona
    all_states["Arkansas"] = Arkansas
    all_states["California"] = California
    all_states["Colorado"] = Colorado
    all_states["Connecticut"] = Connecticut
    all_states["Delaware"] = Delaware
    all_states["Florida"] = Florida
    all_states["Georgia"] = Georgia
    all_states["Hawaii"] = Hawaii
    all_states["Idaho"] = Idaho
    all_states["Illinois"] = Illinois
    all_states["Indiana"] = Indiana
    all_states["Iowa"] = Iowa
    all_states["Kansas"] = Kansas
    all_states["Kentucky"] = Kentucky
    all_states["Louisiana"] = Louisiana
    all_states["Maine"] = Maine
    all_states["Maryland"] = Maryland
    all_states["Massachusetts"] = Massachusetts
    all_states["Michigan"] = Michigan
    all_states["Minnesota"] = Minnesota
    all_states["Mississippi"] = Mississippi
    all_states["Missouri"] = Missouri
    all_states["Montana"] = Montana
    all_states["Nebraska"] = Nebraska
    all_states["Nevada"] = Nevada
    all_states["New Hampshire"] = New_Hampshire
    all_states["New Jersey"] = New_Jersey
    all_states["New Mexico"] = New_Mexico
    all_states["New York"] = New_York
    all_states["North Carolina"] = North_Carolina
    all_states["North Dakota"] = North_Dakota
    all_states["Ohio"] = Ohio
    all_states["Oklahoma"] = Oklahoma
    all_states["Oregon"] = Oregon
    all_states["Pennsylvania"] = Pennsylvania
    all_states["Rhode Island"] = Rhode_Island
    all_states["South Carolina"] = South_Carolina
    all_states["South Dakota"] = South_Dakota
    all_states["Tennessee"] = Tennessee
    all_states["Texas"] = Texas
    all_states["Utah"] = Utah
    all_states["Vermont"] = Vermont
    all_states["Virginia"] = Virginia
    all_states["Washington"] = Washington
    all_states["West Virginia"] = West_Virginia
    all_states["Wisconsin"] = Wisconsin
    all_states["Wyoming"] = Wyoming

    return all_states


def questions(question, options):
    print(question)
    for option in options:
        print(option)
    answer = input("Your answer (enter the letter corresponding to your choice): ")
    return answer.upper()


user_location = geolocator(ip)


def askquestion(user_location):

    all_states = states()

    state_questions = all_states[user_location]

    rand_questions = random.sample(list(state_questions.items()), 3)

    for question, data in rand_questions:
        answer = questions(question, data["options"])
        if answer == data["answer"][0]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", data["answer"])

@app.route('/')
def index():
    ip = requests.get('https://api.ipify.org').text
    user_location = geolocator(ip)
    all_states = states()
    state_questions = all_states[user_location]
    rand_questions = random.sample(list(state_questions.items()), 1)
    return render_template('index.html', questions=rand_questions)

if __name__ == "__main__":
    app.run(debug=True)


askquestion(user_location)