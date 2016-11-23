from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestword = None

    # For each word in the wordList
    for word in wordList:
#        print 'DEBUG: testing word: %s' % word
#        if word == 'zzz':
#            print 'DEBUG: hit end of wordlist: %s' % word
        wordscore = 0
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            wordscore = getWordScore(word, n)
            if wordscore > score:
            # Find out how much making that word is worth
                score = wordscore
                bestword = word
#                print "better word: %s" % bestword
#            else:
#                print 'DEBUG: word: %s is not bette than score %d' % (wordscore, word)
#        else:
#            print 'DEBUG: word %s cannot be made with hand: %r' % (word, hand)
#
#    print 'DEBUG: found best word: %s' % bestword
    return bestword


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    # displayhand
    # while hand > 0 words are not exhausted
        # computerchooses word (it won't choose bad words, so no checking needed)
    # 
    # Keep track of the total score.
    score = 0
    exhausted = False
    
    while calculateHandlen(hand) > 0 and not exhausted:
        wordscore = 0
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
#        print 'DEBUG: word chosen: %s' % word
        if word:
            wordscore += getWordScore(word, n)
            score += wordscore
            print "\"%s\" earned %d points.  Total: %d points" % (word, wordscore, score)
            hand = updateHand(hand, word) 
#            print "DEBUG: hand length: %d exhausted: %r" % (calculateHandlen(hand), exhausted) 
        else:
            exhausted = True              
    print "Run out of letters.  Total score: %d" % score

'''
wordList = loadWords()
hand = dealHand(HAND_SIZE)
compPlayHand(hand, wordList, HAND_SIZE)
'''

#
# Problem #8: Playing a game
#
#

def pickPlayer():
    playerstate = None
    while playerstate not in ['u','c']: 
        playerstate = raw_input("Enter u to have yourself play, c to have the computer play: ")
        if playerstate not in ['u','c']:
            print "Invalid command."
    return playerstate

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    gamestate = None
    playerstate = None
    hand = None

    while gamestate not in ['e']:
        gamestate = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if gamestate not in ['e','n','r']:
            print "Invalid command."
        elif gamestate == 'e':
            break
        elif gamestate == 'n':
            playerstate = pickPlayer()
            if playerstate == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
            elif playerstate == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
        elif gamestate == 'r' and not hand:
            print "You have not played a hand yet. Please play a new hand first!"
        elif gamestate == 'r':
            playerstate = pickPlayer()
            if playerstate == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif playerstate == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)

        playerstate = '' # reset playerstate to allow a new choice each time.
 

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


