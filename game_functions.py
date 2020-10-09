from random import *
import numpy as np
import random

def game_status(game, x):

  #check row score
  row_scores = []
  for i in range(len(game)):
    row_scr = 0
    for j in range(len(game[i])):
      if game[i][j] == x:
        row_scr += 1
    row_scores.append(row_scr)

  #check column score
  col_scores = []
  row_0 = 0
  row_1 = 0
  row_2 = 0
  for i in range(len(game)):
    if game[i][0] == x:
      row_0 += 1
    if game[i][1] == x:
      row_1 += 1 
    if game[i][2] == x:
      row_2 += 1 
  col_scores.append(row_0)
  col_scores.append(row_1)
  col_scores.append(row_2)

  #check diagonal score
  def get_diagonals(game):

    diag1_to_row = []
    diag2_to_row = []
    for i in range(len(game)):
      diag1_to_row.append(game[i][i])

    diag2_to_row.append(game[0][2])
    diag2_to_row.append(game[1][1])
    diag2_to_row.append(game[2][0])

    diagonals = [np.asarray(diag1_to_row), np.asarray(diag2_to_row)]

    return np.asarray(diagonals)

  diag_scores = []
  daig = get_diagonals(game)
  for i in range(len(daig)):

    count = 0
    for j in range(len(daig[i])):
      if daig[i][j] == x:
        count += 1

    diag_scores.append(count)

  scores = [row_scores, col_scores, diag_scores]

  return scores



def score_ideces(scores):

  indecesy3 = []
  indecesx3 = []
  indecesx2 = []
  indecesx1 = []
  indecesy2 = []
  indecesy1 = []
  for i in range(len(scores[0])):

    for j in range(len(scores[0][i])):
      
      if scores[0][i][j] == 2:
        index = (i, j)
        if scores[1][i][j] == 0:
          indecesx2.append(index)
        else:
          continue

      elif scores[0][i][j] == 1:
        index = (i, j)
        if scores[1][i][j] == 0:
          indecesx1.append(index)
        else:
          continue

      elif scores[1][i][j] == 2:
        index = (i, j)
        if scores[0][i][j] == 0:
          indecesy2.append(index)
        else:
          continue

      elif scores[1][i][j] == 1:
        index = (i, j)
        if scores[0][i][j] == 0:
          indecesy1.append(index)
        else:
          continue

      elif scores[0][i][j] == 0:
        index = (i, j)
        if scores[1][i][j] == 0:
          indecesx3.append(index)
        else:
          continue

      elif scores[1][i][j] == 0:
        index = (i, j)
        if scores[0][i][j] == 0:
          indecesy3.append(index)
        else:
          continue
  
  
    scoresx = {'1': indecesx1, '2': indecesx2, '0': indecesx3}
    scoresy = {'1': indecesy1, '2': indecesy2, '0': indecesy3}
    
  return scoresx, scoresy


def find_bias_option_to_move(game, index_to_win):
  index = []
  if index_to_win[0] == 0:
    for i in range(len(game[index_to_win[1]])):
      if game[index_to_win[1]][i] == 0:
        index.append((index_to_win[1], i))

  if index_to_win[0] == 1:
    for i in range(len(game)):
      if game[i][index_to_win[1]] == 0:
        index.append((i, index_to_win[1]))

  if index_to_win[0] == 2:
    if index_to_win[1] == 0:
      diag = [game[0][0], game[1][1], game[2][2]]
      idx = []
      for i in range(len(diag)):
        if diag[i] == 0:
          idx.append(i)
      idx = random.choice(idx)
      index.append((idx, idx))

    elif index_to_win[1] == 1:
      diag = [game[0][2], game[1][1], game[2][0]]
      for i in range(len(diag)):
        if diag[i] == 0:
          if i == 0:
            index.append((0, 2))
          if i == 1:
            index.append((1, 1))
          if i == 2:
            index.append((2, 0))
  return index[0], game

def best_next_move(game, scores):

  if scores[0]['2'] != []:
    index_to_win = random.choice(scores[0]['2'])

  elif scores[1]['2'] != []:
    index_to_win = random.choice(scores[1]['2'])

  elif scores[0]['1'] != []:
    index_to_win = random.choice(scores[0]['1'])

  elif scores[1]['1'] != []:
    index_to_win = random.choice(scores[1]['1'])

  elif scores[0]['0'] != []:
    index_to_win = random.choice(scores[0]['0'])

  else:
    index_to_win = random.choice(scores[1]['0'])

  index_to_win, game = find_bias_option_to_move(game, index_to_win)

  return index_to_win, game

def check_for_winners(game):
  old_game = game.copy()

  empty_slots = 0
  for i in range(len(game)):
    for j in range(len(game[i])):
      if game[i][j] == 0:
        empty_slots += 1

  if empty_slots == 0:
    game = game

  else:
    for i in range(len(game_status(game, 1))):
      for j in range(len(game_status(game, 1)[i])):
        if game_status(game, 1)[i][j] == 3:
          print('I win!')
          print(game)
          print('new game:')
          game = np.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0] ).reshape( (3,3) )
        

        elif game_status(game, 2)[i][j] == 3:
          print('You win!')
          print(game)
          print('new game:')
          game = np.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0] ).reshape( (3,3) )

        
  return game, old_game


def play(game, number):

  if number == 0:
    if game[0][0] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[0][0] = 2
  if number == 1:
    if game[0][1] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[0][1] = 2
  if number == 2:
    if game[0][2] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[0][2] = 2
  if number == 3:
    if game[1][0] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[1][0] = 2
  if number == 4:
    if game[1][1] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[1][1] = 2
  if number == 5:
    if game[1][2] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[1][2] = 2
  if number == 6:
    if game[2][0] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[2][0] = 2
  if number == 7:
    if game[2][1] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[2][1] = 2
  if number == 8:
    if game[2][2] != 0:
      print('ocupied, play different move:')
      print(game)
      return game
    else:
      game[2][2] = 2


  scores = [game_status(game, 1), game_status(game, 2)]
  scores = score_ideces(scores)
  res0 = not scores[0]['0']
  res1 = not scores[0]['1']
  res2 = not scores[0]['2']
  res3 = not scores[1]['0']
  res4 = not scores[1]['1']
  res5 = not scores[1]['2']

  if res0 == True and res1== True and res2 == True and res3 == True and res4== True and res5 == True:
    game, old_game = check_for_winners(game)
    print('tie!')
    print(game)
    print('new game:')
    game = np.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0] ).reshape( (3,3) )

  else:
    print('my turn:')
    move, game = best_next_move(game, scores)
    game[move[0], move[1]] = 1
    game, old_game = check_for_winners(game)
  
  print(game)

  return game


