#!/usr/bin/env python

#THIS PROGRAM IS A MADLIB GAME
#AUTHOR: CRISTOBAL MITCHELL
#DATE MODIFIED: 02/16/2016
#VERSION: 0.1

#TODO

#DEBUG FLAG
debug = False

#IMPORTS


class MADLIBS():
	def __init__(self):
		pass

	def start(self):
		print
		print  "****     ****     **     *******         **       ** ******    ********"
		print  "/**/**   **/**    ****   /**////**       /**      /**/*////**  **////// "
		print  "/**//** ** /**   **//**  /**    /**      /**      /**/*   /** /**       "
		print  "/** //***  /**  **  //** /**    /**      /**      /**/******  /*********"
		print  "/**  //*   /** **********/**    /**      /**      /**/*//// **////////**"
		print  "/**   /    /**/**//////**/**    **       /**      /**/*    /**       /**"
		print  "/**        /**/**     /**/*******        /********/**/*******  ******** "
		print  "//         // //      // ///////         //////// // ///////  ////////  "
		print  
		print
		return self.player()
	 
	def player(self):
		name = raw_input("Player, what is your name? ")
		print 
		print "Hello %s, lets get started...\n" % name
		return self.game_select(name)

	def game_select(self, name):
		games = ["zoo", "weird day", "work"]
		print "The libs that are available...\n"
		for game in games:
			print game
		print
		selected = raw_input("Which game would you like to play? ").lower()
		if selected in games:
			if selected == "zoo":
				return self.game_zoo(name)

			elif selected == "work":
				return self.game_work(name)

			elif selected == "weird day":
				return self.ml_weird_day(name)

		else:
			print "I'm sorry that is not a valid selection"
			return self.game_select(name)

	def game_zoo(self, name):
		pass

	def game_work(self, name):
		pass

	def ml_weird_day(self, name):
		print "Please provide me with each of the follow...\n"

		noun = raw_input("A noun: ")
		adj1 = raw_input("An adjective: ")
		nouns = raw_input("A plural noun: ")
		famous = raw_input("The name of a famous person: ")
		place = raw_input("A place: ")
		verbing1 = raw_input("A verb ending in 'ing': ")
		adj2 = raw_input("Another adjective: ")
		song = raw_input("Your favorite song: ")
		verbed = raw_input("A verb ending in 'ed': ")
		adverb = raw_input("An adverb: ")
		verbing2 = raw_input("Another verb ending in 'ing': ")
		model = raw_input("The name of a supermodel: ")
		adj3 = raw_input("One final adjective: ")

		STORY = "Once upon a time there was a %s. It had %s %s! One day it met %s on the side of the %s they were %s. It was very %s; they both looked like hobos! All of the sudden they started singing %s really loudly. They %s really %s! %s started %s with %s. They looked really %s!"

		print
		print STORY % (noun, adj1, nouns, famous, place, verbing1, adj2, song, \
			verbed, adverb, famous, verbing2, model, adj3)



if __name__ == "__main__":
	ml = MADLIBS()
	ml.start()