import os
from math import ceil
from random import random as rand


class DoubleOrNothing:
	def __init__(self, start, reward, rounds):
		self.start = start
		self.balance = 1000
		self.stake = start
		self.reward = reward
		self.rounds = rounds
		self.losses = 0
		self.wins = 0

	def run(self):
		for i in range(self.rounds):
			print(f"round : #{i+1}, balance : ${self.balance}, stake : ${self.stake} ")
			self.balance -= self.stake
			if rand() <= 1 / self.reward:
				print(f"Won! : reward ${self.stake * self.reward}")
				self.wins += 1
				self.balance += self.stake * self.reward
				self.stake = self.start
			else:
				print(f"Loss! : loss -${self.stake}")
				self.losses += 1
				# self.stake +=  self.stake + self.stake * int( 1 / self.reward)
				self.stake += self.stake # + int(  self.stake / self.reward)


		print(f"wins={self.wins} ; losses: {self.losses} ; balance: ${self.balance}")
		return self.balance


rounds = 10000
total = 0
for i in range(1000):
	total += DoubleOrNothing(1, 4, rounds).run()
print(f"Average balance: {total/rounds}")
