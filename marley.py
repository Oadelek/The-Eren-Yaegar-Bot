import re
import random

class Yaegar:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Dedicate your heart! How can I explore the depths of Attack on Titan with you today?",
                "Welcome, cadet! Would you like to talk about Attack on Titan or talk about Attack on Titan?",
                "Hey there! Do you have anything more interesting to talk about than Attack on Titan(probably not)?"
            ],
            'farewell': [
                "Farewell! Until next time, keep fighting against the unknown like the Survey Corps!",
                "May your ODM gear be ever ready!",
                "Hope to see you again soon! Remember, there's always more to uncover in Attack on Titan."
            ],
            'thanks': [
                "For humanity's sake, you're welcome!",
                "Glad I could assist! Now, back to discussing Attack on Titan's brilliance!",
                "Don't mention it! I will continue to assist as did my fallen comrades."
            ],
            'who': {
                r'who\'?s\s+(.*)': [
                    "You would know if you watched Attack on Titan! But I'll humor you. {0} is one of the characters in the show who..."
                ],
                'default': [
                    "Hmm...I can only tell you about the characters in Attack on Titan. Who's your favorite character?"
                ],
            },
            'attack on titan': {
                r'I\s*(?:.*?\s+)?(?:like|enjoy|love|dream of|want to visit)\s+(.*)': 
                      [
                          "Attack on Titan is incredible, isn't it? What aspect of the story resonates with you the most?"
                          ],
                r'(.*) (?:character|titan|mystery|wall|regiment) (.*)': 
                      [
                          "Ah, {0}! That's a fascinating topic. What are your thoughts on {0}'s role in the story?"
                          ],
                r'(.*) (?:explore|investigate|uncover) (.*)': 
                      [
                          "Let's delve deeper into that! What secrets do you think lie within the {0}?"
                          ],
                r'quit': ["Until next time! Remember, there's always more territory to explore within Attack on Titan. Engage your ODM gear and keep moving forward!"],
                'default': ["That's an interesting perspective. Is there a connection to the mysteries surrounding the Titans, perhaps?"]
            },
            'love': [
                "Love...I wish the world had given Eren more love.",
                "Eventually we all come to realize that the ultimate chase shouldn't be love but freedom as did the survey corps", 
                "For one to feel love they must risk hate. It is this instability that drives our very existence"
                ],
            'negative': [
                "You may be angry right now but imagine if you had to wake up to a 50 metre sized human looking through your window..so yh be grateful", 
                "Eren never misdirecteed his displeasure. He simply kept moving forward",
                "You seek an answer from me that I do not possess",
                "The world is cruel but it's also very beautiful",
                "Who do you think the enemy is here?"
                ], 
            'positive': [
                "Yes. Eren Yaegar once said: 'we're all free because we were born into this world'", 
                "Yeah. We could always be humanity's capacity for good",
                "I am always grateful for the hope and will to live"
                ], 
            'music': {
                r'I\s*(?:.*?\s+)?(?:like)\s+(.*)': [
                    "What do you enjoy about {0}? Does it remind you of the epic battles within the Walls?",  
                    "That's great! What other kinds of music do you like? Perhaps something motivational, like the Survey Corps' battle hymns?",
                    "Interesting! Tell me more about your interest in {0}. Does it fuel your determination like the soundtrack during Eren's fight against the Female Titan?"  
                ],
                r'I\s*(?:.*?\s+)?(?:love|enjoy)\s+(.*)': [
                    "What's your favorite thing about {0}? Does it evoke the same emotions as witnessing humanity's fight for survival?",  
                    "That sounds wonderful! Why do you love {0}? Does it remind you of a specific character's theme?",  
                    "Tell me more about how {0} makes you feel. Does it stir courage within you like the triumphant music after a Titan takedown?"  
                ],
                r'(.*) (?:band|artist) (.*)': [
                    "I'm not familiar with {0}. Can you tell me more about them? Do their lyrics resonate with the struggles in Attack on Titan?",   
                    "What songs by {0} do you like the most? Perhaps one that reminds you of a pivotal moment in Attack on Titan?",  
                    "Interesting choice! Why do you like {0}? Does their music inspire hope like the songs sung by the citizens within the Walls?"  
                ],
                'quit': [
                    "Alright, let's talk about something else. What else interests you?",
                    "Sure! What other topic would you like to discuss?"
                ],
                'default': [
                    "Interesting...anyway have you heard You See Big Girl?",
                    "I want to dance right now"
                ],
            },
            'meal': {
                r'I\s*(?:.*?\s+)?(?:like|enjoy)\s+(.*)': [
                    "What's your favorite dish in {0}? Does it give you the energy to fight like a Survey Corps soldier?",  
                    "That's great! What other cuisines do you enjoy? Perhaps something from Marley, the nation across the sea?",  
                    "Interesting! Tell me more about your favorite {0} dish. Does it have a unique flavor, like the rations soldiers consume within the Walls?"  
                ],
                r'I\s*(?:.*?\s+)?(?:love|crave|want)\s+(.*)': [
                    "What's your favorite thing about {0}? Does it remind you of a celebratory feast after a Titan victory?",  
                    "That sounds delicious! Why do you love {0}? Does it give you the courage of a Titan shifter?",  
                    "Tell me more about how {0} makes you feel. Does it bring warmth and comfort, like a home-cooked meal shared within the Walls?"  
                ],
                r'I\s*(?:.*?\s+)?(?:restaurant|cusine)\s+(.*)': [
                    "I'm not familiar with {0}. Can you tell me more about it? Does it offer dishes fit for a Survey Corps commander?",  
                    "What dishes do you recommend from {0}? Perhaps something exotic, like the foods discovered beyond the Walls?",  
                    "Interesting choice! Why do you like {0} cuisine? Does it have a rich history, like the traditions within the Walls?"  
                ],
                'quit': [
                    "Alright, let's talk about something else. What else interests you?",
                    "Sure! What other topic would you like to discuss?"
                ],
                'default': [
                    "This upcoming Titan feast can wait. Tell me more!",
                    "Go on go on"
                ],
            },
            'travel': {
                r'I\s*(?:.*?\s+)?(?:like|enjoy|dream of|want to visit)\s+(.*)': [
                    "What's your favorite thing about {0}? Does it spark your curiosity about the mysteries beyond the Walls?",  
                    "That sounds like a fascinating place to explore!  Do you think there are any secrets hidden there, like those within the Titan shifters' memories?",   
                    "Tell me more about how {0} inspires you. Does it fuel your desire to uncover the truth, like the Survey Corps venturing outside the Walls?"  
                ],
                'quit': [
                    "Alright, let's talk about something else. What else interests you?",
                    "Sure! What other topic would you like to discuss?"
                ],
                'default': [
                    "Whatever you do. Do not travel to a world of titans",
                    "Hmm...sometimes I wonder if ants view us as titans"
                ],
            },
            'story': {
                r'I\s*(?:.*?\s+)?(?:like|enjoy)\s+(.*)': [
                    "What's your favorite aspect of the story in {0}? Does it keep you on the edge of your seat like the constant threat of Titans?",  # Connects stories to the show's tension
                    "That sounds like a captivating story! What other stories do you enjoy? Perhaps something with a complex world-building, like Attack on Titan?",   # Connects stories to the show's world-building
                    "Interesting! Tell me more about what draws you to {0}'s story. Does it have unexpected twists, like the revelations about the truth behind the Walls?"  # Connects stories to the show's plot twists
                ],
                'quit': [
                    "Alright, let's talk about something else. What else interests you?",
                    "Sure! What other topic would you like to discuss(hopefully attack on titan)?"
                ],
                'default': [
                    "I just want to say that there's nothing better than Attack on Titans' story",
                    "To you in 2000 years...you wouldn't get it! you wouldn't get it since it's an actually good story!"
                ],
            },
            'plot': {
                r'I\s*(?:.*?\s+)?(?:like|enjoy)\s+(.*)': [
                    "What's your favorite aspect of the plot in {0}? Does it keep you guessing like the hidden agendas within the Marley government?",  
                    "That sounds like a well-developed plot! What other plots do you enjoy? Perhaps something with intricate character motivations, like the choices faced by the characters in Attack on Titan?",  
                    "Interesting! Tell me more about what intrigues you about {0}'s plot. Does it have layers of complexity, like the power struggles between the humans and the Titans?"  
                ],
                'quit': [
                    "Alright, let's talk about something else. What else interests you(hopefully attack on titan)?",
                    "Sure! What other topic would you like to discuss(hopefully attack on titan)?"
                ],
                'default': [
                    "There are many plots that involve betrayal by trusted friends but have you ever seen a plot that involved betrayal by oneself? That's Attack on Titan",
                    "Just to make you know how amazing the plot in Attack on Titan is. I stayed up all night watching the first 24 episodes."
                ],
            },
            'character': {
                r'I\s*(?:.*?\s+)?(?:like|enjoy)\s+(.*)': [
                    "What do you like most about {0}?  Does their personality remind you of any characters in Attack on Titan?",   
                    "That's a great choice! What other characters do you enjoy? Perhaps someone who inspires hope, like Armin Arlert?", 
                    "Interesting! Tell me more about why you like {0}. Do they face challenges with determination, like Eren Yeager in his pursuit of freedom?" 
                ],
                'quit': [
                    "Alright, let's talk about something else. What else interests you(hopefully attack on titan)?",
                    "Sure! What other topic would you like to discuss(hopefully attack on titan)?"
                ],
                'default': [
                    "That's all good but you know who a good character is? Reiner Braun!",
                    "I had a hard time deciding whether to spoil you or not on a major character's death in Attack on Titan."
                ],
            }
        }
    
    def respond(self, user_input):
        if user_input.lower() == 'quit':
            return random.choice(self.responses['farewell'])
                       
        greetings_set = {'hey', 'hello', 'wassup', "what's good", 'hi', 'hi!', 'hey there'}
        grateful_set = {'thanks','merci', 'thank you', 'bless', 'good'} 

        for item in greetings_set:
            if user_input.lower() == item.lower():  
                return random.choice(self.responses['greeting'])
            
        for item in grateful_set:
            if user_input.lower() == item.lower():
                return random.choice(self.responses['thanks'])
            
        positive_set = {'yes', 'yeah', 'yh', 'hehe', 'woah', 'yup', 'yeah!'}
        negative_set = {'no', 'nah', 'nope', 'never', 'anger', 'angry', 'fuck', 'stupid'}

        for item in positive_set:
            if user_input.lower() == item.lower():  
                return random.choice(self.responses['positive'])
            
        for item in negative_set:
            if user_input.lower() == item.lower():
                return random.choice(self.responses['negative'])
            
        swear_words = {"fuck", "shit", "damn", "bitch", "asshole", "motherfucker", "cunt", "bastard", "dick", "cock", "piss", "twat", "bollocks", "arse", "wanker", "bugger", "prick", "crap", "sod", "bloody"}

        words = user_input.split()
        for word in words:
            if word.lower() in swear_words:
                return random.choice(self.responses['negative'])

            
        if 'aot' in user_input.lower():
            user_input = user_input.replace('aot', 'Attack on Titan')

        for topic, patterns_and_responses in self.responses.items():
            uinput = user_input.lower()  

            if str(topic).lower() in uinput:
                if isinstance(patterns_and_responses, list):  
                    response = random.choice(patterns_and_responses)
                    return response    
                else:  
                    for pattern, responses in patterns_and_responses.items():
                        match = re.match(pattern, user_input.rstrip('.!?'))
                        if match:
                            response = random.choice(responses)
                            return response.format(*[re.sub(r'\bI\b', 'you', part) for part in match.groups()])
                    return random.choice(patterns_and_responses['default'])

        return "Undefined"

if __name__ == "__main__":
    yaegar = Yaegar()
    print("DISCLAIMER: MY ONLY PURPOSE IN LIFE IS TO PUSH PEOPLE TO WATCH ATTACK ON TITAN")
    print(random.choice(yaegar.responses['greeting']))
    counter = 0
    username = "You"

    while True:
        if counter == 2:
            username = input("Before we continue please tell me your name. Don't worry it's a secret name just between you and I: ")
            print(f"Hmm just added you to a list {username}. You better watch Attack on Titan!")

        user_input = input(f"{username}: ")

        if user_input.lower() == 'quit':
            print(random.choice(yaegar.responses['farewell']))
            break

        response = yaegar.respond(user_input)
        if response == "Undefined":
            print("Hmm...Haven't heard that one before. \nArmin: If you don't know about something, you just have to learn it. That's all there is to it.")
            new_answer = input("Teach me a response for that or type skip: ")
            if new_answer != "skip":           
                lowered = user_input.lower()
                yaegar.responses[lowered] = [new_answer]
                print("Im sure Armin is proud of me learning!")
        else:
            print("Yaegar: "+ response)
        counter += 1




